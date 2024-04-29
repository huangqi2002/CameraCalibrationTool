import copy
import json
import random

import numpy as np
import cv2

from server.aruco_vz import aruco_tool


class ExternalCalibrator:
    def __init__(self, objectPoints=None, imgPoints=None, intrinsic_params=None):
        self.objectPoints = objectPoints
        self.imgPoints = imgPoints
        self.intrinsic_params = intrinsic_params
        self.show_img = np.zeros((3000, 2960, 3))

    def set_intrinsic_params(self, internal_cfg):
        self.intrinsic_params = internal_cfg
        # with open(internal_cfg_path, 'r') as file:
        #     self.intrinsic_params = json.load(file)

    def get_corners(self, img, dic_size=5, dic_num=1000, board_width=11, board_height=8, board_spacer=1,
                    threshold_min=0,
                    threshold_max=87, square_size=25, board_num=10, save_path=None):
        aruco_tool.set_aruco_dictionary(dic_size, dic_num)
        aruco_tool.set_charuco_board((board_width + 1, (board_height + 1) * board_num + board_spacer * (board_num - 1)))

        objPoints, imgPoints, charucoIds, ret_img = aruco_tool.charuco_detect(img, False)
        threshold = board_width * (board_height + 1 + board_spacer)

        # 初始化一个列表来存储十个组
        temp_obj_point_list = [np.empty((0, 1, 3)) for _ in range(board_num)]
        temp_img_point_list = [np.empty((0, 1, 2)) for _ in range(board_num)]

        # 将 objPoints 和 charucoIds 进行 zip，得到每个点对应的 charucoId
        points_with_charuco_ids = zip(objPoints, imgPoints, charucoIds)

        # 分组并筛选出满足条件的非空组
        for obj_point, img_point, ids in points_with_charuco_ids:
            if ids is not None and threshold_min <= ids[0] <= threshold_max:
                temp_ids = ids[0] // threshold
                temp_obj_point_list[temp_ids] = np.vstack(
                    [temp_obj_point_list[temp_ids], (obj_point[0].reshape(1, 1, -1) / 0.25 * square_size)])
                temp_img_point_list[temp_ids] = np.vstack(
                    [temp_img_point_list[temp_ids], img_point[0].reshape(1, 1, -1)])

        # 过滤掉为空的组
        self.objectPoints = [arr.astype(np.float32) for arr in temp_obj_point_list if arr.size > 0]
        # for group in self.objectPoints:
        #     first_element_points = group[0].copy()  # 获取第一个元素的值
        #     for i in range(0, len(group)):  # 遍历除第一个元素外的其他元素
        #         points = group[i]
        #         group[i] = points - first_element_points

        self.imgPoints = [arr.astype(np.float32) for arr in temp_img_point_list if arr.size > 0]

        if save_path is not None:
            aruco_tool.draw_charuco_corners(ret_img, self.imgPoints)
            # temp_img = cv2.resize(ret_img, (800, 600))
            # cv2.imshow("ret_img", temp_img)
            # cv2.waitKey(0)
            cv2.imwrite(save_path, ret_img)

        ok = False
        if len(self.objectPoints) > 0:
            ok = True
        return ok

    def calibrate(self, dirct, img, dic_size=5, dic_num=1000, board_width=11, board_height=8, board_spacer=1,
                  threshold_min=0,
                  threshold_max=87, square_size=25, board_num=10, save_path=None):
        ret, rvecs, tvecs = False, None, None
        if dirct is None or self.intrinsic_params is None:
            return ret, rvecs, tvecs
        dirct_calib = dirct + "_calib"
        if dirct_calib not in self.intrinsic_params:
            return ret, rvecs, tvecs

        intrinsic_params_dirct = self.intrinsic_params[dirct_calib]
        # 内参
        mtx = np.array(intrinsic_params_dirct[2:11]).reshape(3, 3)
        dist = np.array(intrinsic_params_dirct[11:])
        dist_e = np.zeros_like(dist)

        ok = self.get_corners(img, dic_size, dic_num, board_width, board_height, board_spacer, threshold_min,
                            threshold_max, square_size, board_num, save_path)
        # 亚像素级别的角点优化
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        color = (0, 0.5, 0)
        img = cv2.imread("../m_data/hqtest/690/ex_R_ss.jpg")
        if dirct == "left":
            color = (0, 0, 0.5)
            img = cv2.imread("../m_data/hqtest/690/ex_L_ss.jpg")

        # ok, self.imgPoints = cv2.findChessboardCorners(img, (11, 8),
        #                                                flags=cv2.CALIB_CB_ADAPTIVE_THRESH | cv2.CALIB_CB_NORMALIZE_IMAGE)
        # self.imgPoints = [self.imgPoints.astype(np.float32)]
        # self.objectPoints = [np.array([[(j * 25, i * 25, 0.)]
        #                               for i in range(8)
        #                               for j in range(11)], dtype=np.float32)]

        if ok:
            temp_imgPoints = copy.deepcopy(self.imgPoints)
            for i in range(len(self.imgPoints)):
                PointsNdarray = self.imgPoints[i]
                # 亚像素级别的角点优化
                PointsNdarray = cv2.cornerSubPix(gray, PointsNdarray, (11, 11), (-1, -1), criteria)
                if dirct == "left" or dirct == "right":
                    cv2.fisheye.undistortPoints(PointsNdarray, mtx, dist, PointsNdarray)
                else:
                    cv2.undistortPoints(PointsNdarray, mtx, dist, PointsNdarray)

                for j in range(PointsNdarray.shape[0]):
                    points = PointsNdarray[j][0]
                    points[0] = points[0] * mtx[0][0] + mtx[0][2]
                    points[1] = points[1] * mtx[1][1] + mtx[1][2]

                    if j == 0:
                        cv2.circle(self.show_img, (int(points[0]), int(points[1])), 5, (1, 1, 1), -1)
                    else:
                        cv2.circle(self.show_img, (int(points[0]), int(points[1])), 5, color, -1)

            color = [i * 2 for i in color]
            rvecs = tvecs = np.zeros((3, 1))
            for i in range(len(self.objectPoints)):
                # if i == 0:
                #     continue
                ret, temp_rvecs, temp_tvecs = cv2.solvePnP(self.objectPoints[i], self.imgPoints[i], mtx, dist_e)
                # rvecs += temp_rvecs
                print(temp_rvecs)
                if i == 0:
                    tvecs = temp_tvecs
                    rvecs = temp_rvecs
            # rvecs /= 2

            rvecs_mat, _ = cv2.Rodrigues(rvecs)
            cv2.invert(rvecs_mat, rvecs_mat)
            tvecs_1 = np.dot(rvecs_mat, tvecs)

            for i in range(len(temp_imgPoints)):
                PointsNdarray = temp_imgPoints[i]

                if dirct == "left" or dirct == "right":
                    cv2.fisheye.undistortPoints(PointsNdarray, mtx, dist, PointsNdarray, rvecs_mat)
                else:
                    cv2.undistortPoints(PointsNdarray, mtx, dist, PointsNdarray, rvecs_mat)

                for j in range(PointsNdarray.shape[0]):
                    points = PointsNdarray[j][0]
                    points[0] = (points[0] - 0 * tvecs_1[0] / 1000) * mtx[0][0] + mtx[0][2]
                    points[1] = (points[1] - 0 * tvecs_1[1] / 1000) * mtx[1][1] + mtx[1][2]
                    print(points)
                    if j == 0:
                        cv2.circle(self.show_img, (int(points[0]), int(points[1])), 5, (1, 1, 1), -1)
                    else:
                        cv2.circle(self.show_img, (int(points[0]), int(points[1])), 5, color, -1)
            show_img = cv2.resize(self.show_img, (600, 400))
            cv2.imshow("show_img_1", show_img)
            cv2.waitKey(1)

        # 返回结果
        return ret, rvecs, tvecs

    def calibrate_src(self, dirct, img, dic_size=5, dic_num=1000, board_width=11, board_height=8, board_spacer=1,
                       threshold_min=0,
                       threshold_max=87, square_size=25, board_num=10, save_path=None):
        ret, rvecs, tvecs = False, None, None
        if dirct is None or self.intrinsic_params is None:
            return ret, rvecs, tvecs
        dirct_calib = dirct + "_calib"
        if dirct_calib not in self.intrinsic_params:
            return ret, rvecs, tvecs

        intrinsic_params_dirct = self.intrinsic_params[dirct_calib]
        # 内参
        mtx = np.array(intrinsic_params_dirct[2:11]).reshape(3, 3)
        dist = np.array(intrinsic_params_dirct[11:])
        dist_e = np.zeros_like(dist)

        # 寻找角点
        if self.get_corners(img, dic_size, dic_num, board_width, board_height, board_spacer, threshold_min,
                              threshold_max, square_size, board_num, save_path):
            # 亚像素级别的角点优化
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            for i in range(len(self.imgPoints)):
                PointsNdarray = self.imgPoints[i]
                # 亚像素级别的角点优化
                PointsNdarray = cv2.cornerSubPix(gray, PointsNdarray, (11, 11), (-1, -1), criteria)
                if dirct == "left" or dirct == "right":
                    cv2.fisheye.undistortPoints(PointsNdarray, mtx, dist, PointsNdarray)
                else:
                    cv2.undistortPoints(PointsNdarray, mtx, dist, PointsNdarray)

                for j in range(PointsNdarray.shape[0]):
                    points = PointsNdarray[j][0]
                    points[0] = points[0] * mtx[0][0] + mtx[0][2]
                    points[1] = points[1] * mtx[1][1] + mtx[1][2]

            rvecs = tvecs = np.zeros((3, 1))
            for i in range(len(self.objectPoints)):
                ret, temp_rvecs, temp_tvecs = cv2.solvePnP(self.objectPoints[i], self.imgPoints[i], mtx, dist_e)
                # rvecs += temp_rvecs
                print(temp_rvecs)
                if i == 0:
                    tvecs = temp_tvecs
                    rvecs = temp_rvecs
            # rvecs /= 2

        # 返回结果
        return ret, rvecs, tvecs


ex_calib = ExternalCalibrator()
