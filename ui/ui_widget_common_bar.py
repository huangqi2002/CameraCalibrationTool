# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_common_bar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetCommonBar(object):
    def setupUi(self, WidgetCommonBar):
        WidgetCommonBar.setObjectName("WidgetCommonBar")
        WidgetCommonBar.resize(1100, 94)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(WidgetCommonBar)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(WidgetCommonBar)
        self.groupBox_2.setMinimumSize(QtCore.QSize(350, 80))
        self.groupBox_2.setMaximumSize(QtCore.QSize(350, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_choise_device_type = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_choise_device_type.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_choise_device_type.setFont(font)
        self.comboBox_choise_device_type.setObjectName("comboBox_choise_device_type")
        self.horizontalLayout_2.addWidget(self.comboBox_choise_device_type)
        self.pushButton_show_log_view = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_show_log_view.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_show_log_view.setFont(font)
        self.pushButton_show_log_view.setObjectName("pushButton_show_log_view")
        self.horizontalLayout_2.addWidget(self.pushButton_show_log_view)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(WidgetCommonBar)
        self.groupBox_3.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_time_status = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_time_status.sizePolicy().hasHeightForWidth())
        self.label_time_status.setSizePolicy(sizePolicy)
        self.label_time_status.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_time_status.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_time_status.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        self.label_time_status.setFont(font)
        self.label_time_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_status.setObjectName("label_time_status")
        self.horizontalLayout_3.addWidget(self.label_time_status)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(WidgetCommonBar)
        self.groupBox.setMinimumSize(QtCore.QSize(500, 70))
        self.groupBox.setMaximumSize(QtCore.QSize(500, 70))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_device_ip = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_device_ip.setFont(font)
        self.lineEdit_device_ip.setObjectName("lineEdit_device_ip")
        self.horizontalLayout.addWidget(self.lineEdit_device_ip)
        self.pushButton_connect_device = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_connect_device.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_connect_device.setFont(font)
        self.pushButton_connect_device.setObjectName("pushButton_connect_device")
        self.horizontalLayout.addWidget(self.pushButton_connect_device)
        self.pushButton_reboot_device = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_reboot_device.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_reboot_device.setFont(font)
        self.pushButton_reboot_device.setObjectName("pushButton_reboot_device")
        self.horizontalLayout.addWidget(self.pushButton_reboot_device)
        self.horizontalLayout_4.addWidget(self.groupBox)

        self.retranslateUi(WidgetCommonBar)
        QtCore.QMetaObject.connectSlotsByName(WidgetCommonBar)

    def retranslateUi(self, WidgetCommonBar):
        _translate = QtCore.QCoreApplication.translate
        WidgetCommonBar.setWindowTitle(_translate("WidgetCommonBar", "通用栏"))
        self.groupBox_2.setTitle(_translate("WidgetCommonBar", "软件控制"))
        self.label_2.setText(_translate("WidgetCommonBar", "设备类型"))
        self.pushButton_show_log_view.setText(_translate("WidgetCommonBar", "显示日志"))
        self.groupBox_3.setTitle(_translate("WidgetCommonBar", "流程/结果"))
        self.label_time_status.setText(_translate("WidgetCommonBar", "00:00 当前步骤"))
        self.groupBox.setTitle(_translate("WidgetCommonBar", "设备"))
        self.label.setText(_translate("WidgetCommonBar", "设备IP"))
        self.lineEdit_device_ip.setText(_translate("WidgetCommonBar", "192.168.1.100"))
        self.pushButton_connect_device.setText(_translate("WidgetCommonBar", "连接设备"))
        self.pushButton_reboot_device.setText(_translate("WidgetCommonBar", "重启设备"))
