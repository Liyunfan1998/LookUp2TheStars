# FileName : main.py
# Author   : Adil
# DateTime : 2018/8/13 10:18
# SoftWare : PyCharm

import mainwindow3
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('./data/icon.jpg'))

    ui = mainwindow3.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
