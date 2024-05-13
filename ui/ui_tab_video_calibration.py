# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_video_calibration.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabVideoCalibration(object):
    def setupUi(self, TabVideoCalibration):
        TabVideoCalibration.setObjectName("TabVideoCalibration")
        TabVideoCalibration.resize(950, 511)
        TabVideoCalibration.setMaximumSize(QtCore.QSize(1920, 1048))
        self.verticalLayout = QtWidgets.QVBoxLayout(TabVideoCalibration)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(TabVideoCalibration)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_rx5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rx5.setObjectName("horizontalLayout_rx5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_video_left = QtWidgets.QLabel(self.groupBox)
        self.label_video_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video_left.setObjectName("label_video_left")
        self.verticalLayout_5.addWidget(self.label_video_left)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_img_left = QtWidgets.QLabel(self.groupBox)
        self.label_img_left.setMinimumSize(QtCore.QSize(72, 48))
        self.label_img_left.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_left.setObjectName("label_img_left")
        self.horizontalLayout_6.addWidget(self.label_img_left)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.setStretch(0, 1)
        self.horizontalLayout_rx5.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_video_middle = QtWidgets.QLabel(self.groupBox)
        self.label_video_middle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video_middle.setObjectName("label_video_middle")
        self.verticalLayout_2.addWidget(self.label_video_middle)
        self.horizontalLayout_middle = QtWidgets.QHBoxLayout()
        self.horizontalLayout_middle.setObjectName("horizontalLayout_middle")
        self.label_img_middle = QtWidgets.QLabel(self.groupBox)
        self.label_img_middle.setMinimumSize(QtCore.QSize(72, 48))
        self.label_img_middle.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_middle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_middle.setObjectName("label_img_middle")
        self.horizontalLayout_middle.addWidget(self.label_img_middle)
        self.label_img_spacer = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_img_spacer.sizePolicy().hasHeightForWidth())
        self.label_img_spacer.setSizePolicy(sizePolicy)
        self.label_img_spacer.setText("")
        self.label_img_spacer.setObjectName("label_img_spacer")
        self.horizontalLayout_middle.addWidget(self.label_img_spacer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_middle)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_rx5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_video_right = QtWidgets.QLabel(self.groupBox)
        self.label_video_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video_right.setObjectName("label_video_right")
        self.verticalLayout_3.addWidget(self.label_video_right)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_img_right = QtWidgets.QLabel(self.groupBox)
        self.label_img_right.setMinimumSize(QtCore.QSize(72, 48))
        self.label_img_right.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_right.setObjectName("label_img_right")
        self.horizontalLayout_8.addWidget(self.label_img_right)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.setStretch(0, 1)
        self.horizontalLayout_rx5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_rx5.setStretch(0, 1)
        self.horizontalLayout_rx5.setStretch(1, 1)
        self.horizontalLayout_rx5.setStretch(2, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_rx5)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(TabVideoCalibration)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_left_play = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_left_play.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_left_play.setFont(font)
        self.pushButton_left_play.setObjectName("pushButton_left_play")
        self.horizontalLayout.addWidget(self.pushButton_left_play)
        self.pushButton_middle_play = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_middle_play.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_middle_play.setFont(font)
        self.pushButton_middle_play.setObjectName("pushButton_middle_play")
        self.horizontalLayout.addWidget(self.pushButton_middle_play)
        self.pushButton_right_play = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_right_play.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_right_play.setFont(font)
        self.pushButton_right_play.setObjectName("pushButton_right_play")
        self.horizontalLayout.addWidget(self.pushButton_right_play)
        spacerItem2 = QtWidgets.QSpacerItem(591, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_img_left_middle = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_img_left_middle.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_img_left_middle.setFont(font)
        self.pushButton_img_left_middle.setObjectName("pushButton_img_left_middle")
        self.horizontalLayout.addWidget(self.pushButton_img_left_middle)
        self.pushButton_img_middle_right = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_img_middle_right.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_img_middle_right.setFont(font)
        self.pushButton_img_middle_right.setObjectName("pushButton_img_middle_right")
        self.horizontalLayout.addWidget(self.pushButton_img_middle_right)
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_start.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(TabVideoCalibration)
        QtCore.QMetaObject.connectSlotsByName(TabVideoCalibration)

    def retranslateUi(self, TabVideoCalibration):
        _translate = QtCore.QCoreApplication.translate
        TabVideoCalibration.setWindowTitle(_translate("TabVideoCalibration", "标定拼接Tab"))
        self.groupBox.setTitle(_translate("TabVideoCalibration", "显示"))
        self.label_video_left.setText(_translate("TabVideoCalibration", "左视频"))
        self.label_img_left.setText(_translate("TabVideoCalibration", "左截图"))
        self.label_video_middle.setText(_translate("TabVideoCalibration", "中视频"))
        self.label_img_middle.setText(_translate("TabVideoCalibration", "中截图"))
        self.label_video_right.setText(_translate("TabVideoCalibration", "右视频"))
        self.label_img_right.setText(_translate("TabVideoCalibration", "右截图"))
        self.groupBox_2.setTitle(_translate("TabVideoCalibration", "操作"))
        self.pushButton_left_play.setText(_translate("TabVideoCalibration", "左"))
        self.pushButton_middle_play.setText(_translate("TabVideoCalibration", "中"))
        self.pushButton_right_play.setText(_translate("TabVideoCalibration", "右"))
        self.pushButton_img_left_middle.setText(_translate("TabVideoCalibration", "截图左中"))
        self.pushButton_img_middle_right.setText(_translate("TabVideoCalibration", "截图中右"))
        self.pushButton_start.setText(_translate("TabVideoCalibration", "开始标定"))
