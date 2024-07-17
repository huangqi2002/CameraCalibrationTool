# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_internal_calibration.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabInternalCalibration(object):
    def setupUi(self, TabInternalCalibration):
        TabInternalCalibration.setObjectName("TabInternalCalibration")
        TabInternalCalibration.resize(880, 515)
        TabInternalCalibration.setMaximumSize(QtCore.QSize(1920, 1048))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(TabInternalCalibration)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(TabInternalCalibration)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_fg = QtWidgets.QHBoxLayout()
        self.horizontalLayout_fg.setObjectName("horizontalLayout_fg")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.label_video_fg = QtWidgets.QLabel(self.groupBox_3)
        self.label_video_fg.setMaximumSize(QtCore.QSize(16777215, 640))
        self.label_video_fg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video_fg.setObjectName("label_video_fg")
        self.verticalLayout_1.addWidget(self.label_video_fg)
        self.horizontalLayout_middle_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_middle_2.setObjectName("horizontalLayout_middle_2")
        self.label_img_1 = QtWidgets.QLabel(self.groupBox_3)
        self.label_img_1.setMinimumSize(QtCore.QSize(72, 48))
        self.label_img_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_1.setObjectName("label_img_1")
        self.horizontalLayout_middle_2.addWidget(self.label_img_1)
        self.clarity_label_ML = QtWidgets.QLabel(self.groupBox_3)
        self.clarity_label_ML.setText("")
        self.clarity_label_ML.setObjectName("clarity_label_ML")
        self.horizontalLayout_middle_2.addWidget(self.clarity_label_ML)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_middle_2.addItem(spacerItem)
        self.label_img_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_img_2.setMinimumSize(QtCore.QSize(72, 48))
        self.label_img_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_2.setObjectName("label_img_2")
        self.horizontalLayout_middle_2.addWidget(self.label_img_2)
        self.clarity_label_L = QtWidgets.QLabel(self.groupBox_3)
        self.clarity_label_L.setText("")
        self.clarity_label_L.setObjectName("clarity_label_L")
        self.horizontalLayout_middle_2.addWidget(self.clarity_label_L)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_middle_2.addItem(spacerItem1)
        self.label_img_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_img_3.setMinimumSize(QtCore.QSize(72, 48))
        self.label_img_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_3.setObjectName("label_img_3")
        self.horizontalLayout_middle_2.addWidget(self.label_img_3)
        self.clarity_label_R = QtWidgets.QLabel(self.groupBox_3)
        self.clarity_label_R.setText("")
        self.clarity_label_R.setObjectName("clarity_label_R")
        self.horizontalLayout_middle_2.addWidget(self.clarity_label_R)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_middle_2.addItem(spacerItem2)
        self.label_img_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_img_4.setMinimumSize(QtCore.QSize(72, 48))
        self.label_img_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_4.setObjectName("label_img_4")
        self.horizontalLayout_middle_2.addWidget(self.label_img_4)
        self.clarity_label_MR = QtWidgets.QLabel(self.groupBox_3)
        self.clarity_label_MR.setText("")
        self.clarity_label_MR.setObjectName("clarity_label_MR")
        self.horizontalLayout_middle_2.addWidget(self.clarity_label_MR)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_middle_2.addItem(spacerItem3)
        self.verticalLayout_1.addLayout(self.horizontalLayout_middle_2)
        self.verticalLayout_1.setStretch(0, 8)
        self.verticalLayout_1.setStretch(1, 1)
        self.horizontalLayout_fg.addLayout(self.verticalLayout_1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_fg)
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setObjectName("widget")
        self.verticalLayout_7.addWidget(self.widget)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(TabInternalCalibration)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_play_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_play_1.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_play_1.setFont(font)
        self.pushButton_play_1.setObjectName("pushButton_play_1")
        self.horizontalLayout_2.addWidget(self.pushButton_play_1)
        self.pushButton_play_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_play_2.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_play_2.setFont(font)
        self.pushButton_play_2.setObjectName("pushButton_play_2")
        self.horizontalLayout_2.addWidget(self.pushButton_play_2)
        self.pushButton_play_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_play_3.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_play_3.setFont(font)
        self.pushButton_play_3.setObjectName("pushButton_play_3")
        self.horizontalLayout_2.addWidget(self.pushButton_play_3)
        self.pushButton_play_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_play_4.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_play_4.setFont(font)
        self.pushButton_play_4.setObjectName("pushButton_play_4")
        self.horizontalLayout_2.addWidget(self.pushButton_play_4)
        self.pushButton_play_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_play_5.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_play_5.setFont(font)
        self.pushButton_play_5.setObjectName("pushButton_play_5")
        self.horizontalLayout_2.addWidget(self.pushButton_play_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.undistorted_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.undistorted_checkBox.setFont(font)
        self.undistorted_checkBox.setObjectName("undistorted_checkBox")
        self.horizontalLayout_2.addWidget(self.undistorted_checkBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.clarity_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clarity_checkBox.setFont(font)
        self.clarity_checkBox.setObjectName("clarity_checkBox")
        self.horizontalLayout_2.addWidget(self.clarity_checkBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_start.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.verticalLayout_4.setStretch(0, 1)

        self.retranslateUi(TabInternalCalibration)
        QtCore.QMetaObject.connectSlotsByName(TabInternalCalibration)

    def retranslateUi(self, TabInternalCalibration):
        _translate = QtCore.QCoreApplication.translate
        TabInternalCalibration.setWindowTitle(_translate("TabInternalCalibration", "内参标定Tab"))
        self.groupBox_3.setTitle(_translate("TabInternalCalibration", "显示"))
        self.label_video_fg.setText(_translate("TabInternalCalibration", "FG视频"))
        self.label_img_1.setText(_translate("TabInternalCalibration", "最左截图"))
        self.label_img_2.setText(_translate("TabInternalCalibration", "左截图"))
        self.label_img_3.setText(_translate("TabInternalCalibration", "右截图"))
        self.label_img_4.setText(_translate("TabInternalCalibration", "最右截图"))
        self.groupBox_2.setTitle(_translate("TabInternalCalibration", "操作"))
        self.pushButton_play_1.setText(_translate("TabInternalCalibration", "最左"))
        self.pushButton_play_2.setText(_translate("TabInternalCalibration", "左"))
        self.pushButton_play_3.setText(_translate("TabInternalCalibration", "右"))
        self.pushButton_play_4.setText(_translate("TabInternalCalibration", "最右"))
        self.pushButton_play_5.setText(_translate("TabInternalCalibration", "全视野"))
        self.undistorted_checkBox.setText(_translate("TabInternalCalibration", "去畸变"))
        self.clarity_checkBox.setText(_translate("TabInternalCalibration", "清晰度"))
        self.pushButton_start.setText(_translate("TabInternalCalibration", "开始标定"))
