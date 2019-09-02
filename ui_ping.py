# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QEventLoop, QTimer
import select_ip

from PyQt5.QtWidgets import QFileDialog
import sys
import os, re
from datetime import datetime
import time
from PyQt5.QtGui import QTextCursor
# import text1


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(559, 391)
        MainWindow.setMinimumSize(QtCore.QSize(200, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 547, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(20, 30))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setEnabled(False)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)

        # ip地址输入
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setInputMask('000.000.000.000; ')

        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)

        # ping 次数输入
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.lineEdit_4.setPlaceholderText('')

        # ping 开始键
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.pushButton_6)
        self.pushButton_6.clicked.connect(self.ping_start)
        # ping 停止键
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ping_stop)

        self.horizontalLayout_7.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(20, 30))
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        # 导入EXCEL
        self.label_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.label_9.clicked.connect(self.open_file)

        self.horizontalLayout_8.addWidget(self.label_9)
        # 显示excel 表
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        # self.lineEdit_2.setInputMask('1.1.1.1;#')
        self.horizontalLayout_8.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        # 批量开始键
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.batch_start)
        self.horizontalLayout_9.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        # 清除键
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.clear_message)
        self.horizontalLayout_10.addWidget(self.pushButton_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        #时间输入
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.layoutWidget)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.horizontalLayout_2.addWidget(self.timeEdit_2)
        #定时开始
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.timing)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        # 电话号码输入
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        # 短信确认键
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())

        # 输出界面显示
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_4.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        sys.stdout = EmittingStream(textWritten=self.out_message)
        sys.stderr = EmittingStream(textWritten=self.out_message)
        self.timer = QTimer()
        self.timer.timeout.connect(self.start_auto)  # 到达设定的时间后，执行槽函数代码
        self.flag = 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", " 单 独 检 测"))
        self.label_6.setText(_translate("MainWindow", " ping"))
        self.label_7.setText(_translate("MainWindow", " 次数"))
        self.pushButton_6.setText(_translate("MainWindow", "开始"))
        self.pushButton.setText(_translate("MainWindow", "停止"))
        self.label.setText(_translate("MainWindow", " 批 量 检 测"))
        self.label_9.setText(_translate("MainWindow", " 导入excel表"))
        self.pushButton_4.setText(_translate("MainWindow", "开始"))
        self.pushButton_5.setText(_translate("MainWindow", "数据清除"))
        self.label_2.setText(_translate("MainWindow", " 设置每日检测"))
        self.label_4.setText(_translate("MainWindow", " 开始时间"))
        self.pushButton_2.setText(_translate("MainWindow", "开始"))
        self.label_3.setText(_translate("MainWindow", " 设置短信通知"))
        self.label_5.setText(_translate("MainWindow", " 输入号码"))
        self.pushButton_3.setText(_translate("MainWindow", "确定"))
        self.menu.setTitle(_translate("MainWindow", "开始"))

    def ping_start(self):
        self.flag = 1
        x = self.lineEdit.text()
        if self.lineEdit_4.text() == '':
            y = 99999999

        else:
            y = int(self.lineEdit_4.text())
        self.ip_ping(x, y)

    def ip_ping(self, ip, count):
        self.ip = str(ip)
        self.fai = 0
        self.suc = 0

        for i in range(count):
            # 寻找成功的信息
            ping = os.popen('ping {} -n 1'.format(self.ip)).read()
            select = re.compile(r'来自..+', re.M).findall(ping)
            if self.flag == 1:
                # select2 = re.compile(r'请求超时+', re.M).findall(ping)
                if select == []:
                    self.fai += 1
                    print('丢失 = {}信息 : {}'.format(self.fai, ping))
                    self.cache_out()

                else:
                    self.suc += 1
                    self.cache_out()
                    print('成功 = {}'.format(self.suc))
                    print('失败 = {}'.format(self.fai))
                    print(datetime.now())

            else:
                break

    def ping_stop(self):
        self.flag = 2

    def open_file(self):
        # 实例化QFileDialog
        dig = QFileDialog()
        # 设置可以打开任何文件
        dig.setFileMode(QFileDialog.AnyFile)
        # 文件过滤
        # dig.setFilter(QDir.Files)

        if dig.exec_():
            # 接受选中文件的路径，默认为列表
            filenames = dig.selectedFiles()
            map = ''.join(filenames)
            self.lineEdit_2.setText(map)

    def cache_out(self):
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec_()

    def batch_start(self):
        select_ip.Select().NotifyAdmin('{}'.format(self.lineEdit_2.text()))

    def out_message(self, mess):
        out_mess = str(mess)
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(out_mess)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def clear_message(self):
        self.textEdit.clear()

    def timing(self):
        x =self.timeEdit_2.text()
        y=time.strftime("%H:%M")
        time_x = self.time_change(x)
        time_y = self.time_change(y)
        # print('{} {}'.format(time_x,time_y))
        # if time_x>time_y:
        time_c=time_x - time_y
        self.start_time(time_c)
        # else:
        #     time_c = time_y - time_x
        #     self.start_time(time_c)

    def time_change(self,time_in):
        h,m = time_in.strip().split(':')
        return int(h)*360000 + int(m)*6000
    def start_time(self,time_c):
        self.timer.start(time_c)
        print('开始')

    def start_auto(self):
        self.batch_start()
        time.sleep(30)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    my_ui = Ui_MainWindow()
    my_ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())