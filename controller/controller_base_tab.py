#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import threading
import time
from functools import partial

import cv2
from PyQt5.QtCore import QTimer, QObject, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel
from utils.m_global import m_connect_local

from controller.controller_base import BaseController
from model.app import app_model
from model.video import Video
from server.web.web_server import server


class BaseControllerTab(BaseController):
    tab_index = 0
    current_tab_index = -1
    video_map = {}

    show_message_signal = None
    reboot_finish_signal = None
    current_direction = 'left'

    # 绑定配置文件中的相机与去显示的lable
    def bind_label_and_timer(self, direction: str, label: QLabel, rotate):
        video = Video()
        video.label = label
        video.rotate = rotate
        self.video_map[direction] = video

    # 切换界面
    def on_tab_changed(self, index):
        self.current_tab_index = index
        # 切换界面非本界面则暂停一切显示
        if self.tab_index != index:
            self.parse_video()
            return
        # 切换界面为本界面则开始播放视频
        video_server = app_model.video_server
        if video_server is None:
            return
        cameras = app_model.video_server.get_cameras()
        if cameras is None:
            return
        if app_model.is_connected:
            app_model.video_server.pause_all()
            # print(f"{index} pause_all")
            self.start_video(cameras)

    # 连接设备
    def on_connect_device(self, connect_state):
        if self.current_tab_index != self.tab_index:
            return
        if connect_state:
            app_model.video_server.pause_all()
            cameras = app_model.video_server.get_cameras()
            self.start_video(cameras)
        else:
            self.parse_video()

    # 播放视频
    # cameras是要播放的相机，其属于video_server，可以读到相机不断变换的帧
    # video_map中记录了相机与对应的定时器
    def start_video(self, cameras):
        if cameras is None:
            return
        for key, video in self.video_map.items():
            camera = cameras.get(key)
            if camera is None:
                continue
            app_model.video_server.resume(key)
            video.timer = QTimer(self)
            ret_a = video.timer.timeout.connect(partial(self.update_frame, camera, video))
            video.timer.start(100)
            print("Timer is active:", video.timer.isActive())
            print("start_timer")


    # 暂停播放视频
    def parse_video(self):
        for key, video in self.video_map.items():
            # app_model.video_server.pause(key)
            if video.timer:
                video.timer.stop()

    # 暂停播放视频，并只播放指定视频
    def start_video_unique(self, direction: str, label: QLabel, rotate):
    # def start_video_unique(self, direction: str):
        self.parse_video()
        for key, video in self.video_map.items():
            app_model.video_server.pause(key)

        self.video_map = {}
        self.bind_label_and_timer(direction, label, rotate)
        cameras = app_model.video_server.get_cameras()
        if cameras is None:
            return
        if app_model.is_connected:
            self.start_video(cameras)
        print("start_video_unique\n")
        # app_model.video_server.resume_uniq(direction)

    # 更新视频帧到lable上
    # camera中可以读到相机当前时刻的帧
    # video中包含了相机对lable的对应关系
    def update_frame(self, camera, video):
        # print(f"{camera.rtsp_url} update_frame\n")
        if camera is None or camera.frame is None:
            # self.log.log_err(f"Tab({self.tab_index}), Invalid camera or frame")
            return
        frame = camera.frame

        if video is None or video.label is None:
            self.log.log_err(f"Tab({self.tab_index}), Invalid video or label")
            return
        label = video.label

        frame_rotated = None
        rotate = video.rotate
        label_size = label.size()
        if rotate == 0:
            frame_resized = cv2.resize(frame, (label_size.width(), label_size.height() - 1))
            frame_rotated = frame_resized
        else:
            frame_resized = cv2.resize(frame, (label_size.height() - 1, label_size.width()))
            # print("update_frame, frame_resized", frame_resized.shape)
            if rotate == 90:
                frame_rotated = cv2.rotate(frame_resized, cv2.ROTATE_90_CLOCKWISE)
            elif rotate == 180:
                frame_rotated = cv2.rotate(frame_resized, cv2.ROTATE_180)
            elif rotate == 270:
                frame_rotated = cv2.rotate(frame_resized, cv2.ROTATE_90_COUNTERCLOCKWISE)

        if frame_rotated is None:
            return
        frame_rgb = cv2.cvtColor(frame_rotated, cv2.COLOR_BGR2RGB)
        h, w, ch = frame_rgb.shape
        bytes_per_line = ch * w
        q_image = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        # new_pixmap = pixmap.scaled(2960, 1664)
        # print(f"before label.size:{label.size()}")
        label.setPixmap(pixmap)
        # print(f"after label.size:{label.size()}")

    # 设置工厂模式
    # 尝试连接设备并设置工厂模式，如果设置工厂模式失败，则等待设备重启，再次尝试设置工厂模式，直到成功设置或达到最大重试次数
    def check_device_factory_mode(self):
        need_wait_device_restart = False
        # 连接设备设置工厂模式
        for time_index in range(app_model.login_retry_max_count):
            if not server.login(app_model.device_model.ip):
                time.sleep(1)
                continue

            if m_connect_local:
                result = 1
            else:
                result = self.set_factory_mode()
            if result == 0:
                need_wait_device_restart = True
            elif result == 1:
                need_wait_device_restart = False
            break

        if need_wait_device_restart:
            # 等待设备重启
            for time_index in range(app_model.login_retry_max_count):
                if not server.login(app_model.device_model.ip):
                    time.sleep(1)
                    continue

                if m_connect_local:
                    result = 1
                else:
                    result = self.set_factory_mode()
                if result == 1:
                    self.show_message_signal.emit(True, "设置工厂模式成功")
                    return True
                else:
                    self.show_message_signal.emit(False, "设置工厂模式失败")
                    return False
        self.show_message_signal.emit(True, "设置工厂模式成功")
        return True

    # 重新设置工厂模式
    def reset_factory_mode(self):
        reset_factory_mode_result = server.set_factory_mode(mode=0)
        self.log.log_debug(f"reset_factory_mode_result: {reset_factory_mode_result}")

    # 设置工厂模式
    def set_factory_mode(self):
        factory_mode_result = server.set_factory_mode(mode=1)
        self.log.log_debug(f"factory_mode_result: {factory_mode_result}")
        if not factory_mode_result:
            return -1
        try:
            factory_mode_json = json.loads(factory_mode_result)
            if factory_mode_json.get("state") == 200:
                return 0
            elif factory_mode_json.get("state") == 406:
                self.show_message_signal.emit(True, "设备已处于工厂模式")
                return 1
            else:
                return -3
        except Exception as e:
            return -2

    # 重启设备按钮槽函数
    def on_reboot_device(self):
        self.parse_video()
        if self.current_tab_index != self.tab_index:
            return
        threading.Thread(target=self.reboot_device, daemon=True).start()

    # 重启设备
    def reboot_device(self):
        for time_index in range(app_model.login_retry_max_count):
            if not server.login(app_model.device_model.ip):
                time.sleep(1)
                continue

            self.show_message_signal.emit(True, "设备重启中")
            server.reboot()
            time.sleep(1)
            break

        for time_index in range(app_model.login_retry_max_count):
            if not server.login(app_model.device_model.ip):
                time.sleep(1)
                continue

            self.show_message_signal.emit(True, "设备重启完成")
            server.logout()
            self.reboot_finish_signal.emit(1)
            return
        self.show_message_signal.emit(False, "重新连接设备失败")
