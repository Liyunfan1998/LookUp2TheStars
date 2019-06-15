# FileName : main.py
# Author   : Adil
# DateTime : 2018/8/13 10:18
# SoftWare : PyCharm

import mainwindow3
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import time


class MyWindow(QtWidgets.QPushButton):

    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("关闭窗口")
        self.clicked.connect(QtWidgets.qApp.quit)

    def load_data(self, sp):
        for i in range(1, 11):  # 模拟主程序加载过程
            time.sleep(0.1)  # 加载数据
            sp.showMessage("加载... {0}%\nBy: 李云帆，南山牧野，赵玥".format(i * 10), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom,
                           QtCore.Qt.white)
            QtWidgets.qApp.processEvents()  # 允许主进程处理事件


class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("./data/icon.jpg"))
    splash.showMessage("加载... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
    splash.show()  # 显示启动界面
    QtWidgets.qApp.processEvents()  # 处理主进程事件
    window = MyWindow()
    window.setWindowTitle("QSplashScreen类使用")
    window.resize(300, 30)
    window.load_data(splash)  # 加载数据
    window.show()
    splash.finish(window)  # 隐藏启动界面
    window.close()

    # app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('./data/icon.jpg'))
    styleFile = './data/QSS/Ubuntu.qss'
    # styleFile = './data/QssUI/StyleSheets/MetroUI.qss'
    # styleFile = './data/qss-dracula/dracula.css'

    qssStyle = CommonHelper.readQss(styleFile)
    MainWindow.setStyleSheet(qssStyle)
    ui = mainwindow3.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
