# FileName : main.py
# Author   : Adil
# DateTime : 2018/8/13 10:18
# SoftWare : PyCharm

import mainwindow
import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
