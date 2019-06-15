# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2dfullscreenwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2
import Utils


class Ui_MainWindow2D(object):

    def __init__(self, prams):
        print("switch to 2D full screen" + str(prams))
        self.backgroundColor = prams['backgroundColor']
        self.alignment = prams['alignment']
        self.coordinate = prams['coordinate']
        self.axis = prams['axis']
        self.mag = prams['mag']
        self.dataset = prams['dataset']
        self.url = prams['url']
        self.picFormat = prams['picFormat']
        self.zoomscale = 0.5

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 897)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(210, 10, 831, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.preview2D = QtWidgets.QGraphicsView(self.frame)
        self.preview2D.setGeometry(QtCore.QRect(0, 0, 841, 421))
        self.preview2D.setObjectName("graphicsView")
        self.tools2D = QtWidgets.QGroupBox(self.centralwidget)
        self.tools2D.setGeometry(QtCore.QRect(10, 0, 191, 141))
        self.tools2D.setObjectName("tools2D")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tools2D)
        self.verticalLayout.setObjectName("verticalLayout")
        self.allScreenBtn = QtWidgets.QPushButton(self.tools2D)
        self.allScreenBtn.setObjectName("allScreenBtn")
        self.verticalLayout.addWidget(self.allScreenBtn)
        self.alignmentLinesCheckBox = QtWidgets.QCheckBox(self.tools2D)
        self.alignmentLinesCheckBox.setObjectName("alignmentLinesCheckBox")
        self.verticalLayout.addWidget(self.alignmentLinesCheckBox)
        self.axisCheckBox = QtWidgets.QCheckBox(self.tools2D)
        self.axisCheckBox.setObjectName("coordinatesCheckBox")
        self.verticalLayout.addWidget(self.axisCheckBox)
        self.tools3D = QtWidgets.QGroupBox(self.centralwidget)
        self.tools3D.setGeometry(QtCore.QRect(10, 140, 191, 341))
        self.tools3D.setObjectName("tools3D")
        self.mouseXYTextEdit = QtWidgets.QTextEdit(self.tools3D)
        self.mouseXYTextEdit.setGeometry(QtCore.QRect(10, 40, 171, 21))
        self.mouseXYTextEdit.setObjectName("mouseXYTextEdit")
        self.label_3 = QtWidgets.QLabel(self.tools3D)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_3.setObjectName("label_3")
        # self.findStarBtn = QtWidgets.QPushButton(self.tools3D)
        # self.findStarBtn.setGeometry(QtCore.QRect(10, 60, 171, 32))
        # self.findStarBtn.setObjectName("findStarBtn")
        self.closestStarTextBrowser = QtWidgets.QTextBrowser(self.tools3D)
        self.closestStarTextBrowser.setGeometry(QtCore.QRect(10, 90, 171, 191))
        self.closestStarTextBrowser.setObjectName("closestStarTextBrowser")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(220, 430, 331, 51))
        self.groupBox.setObjectName("groupBox")
        self.zoomBtn = QtWidgets.QPushButton(self.groupBox)
        self.zoomBtn.setGeometry(QtCore.QRect(0, 20, 91, 32))
        self.zoomBtn.setObjectName("zoomBtn")
        self.deZoomBtn = QtWidgets.QPushButton(self.groupBox)
        self.deZoomBtn.setGeometry(QtCore.QRect(90, 20, 81, 32))
        self.deZoomBtn.setObjectName("deZoomBtn")
        self.zoomLabel = QtWidgets.QLabel(self.groupBox)
        self.zoomLabel.setGeometry(QtCore.QRect(180, 19, 141, 31))
        self.zoomLabel.setObjectName("zoomLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1231, 22))
        self.menubar.setObjectName("menubar")
        self.menuSaveAs = QtWidgets.QMenu(self.menubar)
        self.menuSaveAs.setObjectName("menuSaveAs")
        self.menuStarStandard = QtWidgets.QMenu(self.menubar)
        self.menuStarStandard.setObjectName("menuStarStandard")
        self.menuDataset = QtWidgets.QMenu(self.menubar)
        self.menuDataset.setObjectName("menuDataset")
        self.backgroundMenu = QtWidgets.QMenu(self.menubar)
        self.backgroundMenu.setObjectName("backgroundMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionpng = QtWidgets.QAction(MainWindow)
        self.actionpng.setObjectName("actionpng")
        self.actionjpeg = QtWidgets.QAction(MainWindow)
        self.actionjpeg.setObjectName("actionjpeg")
        self.actionsvg = QtWidgets.QAction(MainWindow)
        self.actionsvg.setObjectName("actionsvg")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.actionBSC = QtWidgets.QAction(MainWindow)
        self.actionBSC.setObjectName("actionBSC")
        self.actionHipparcos = QtWidgets.QAction(MainWindow)
        self.actionHipparcos.setObjectName("actionHipparcos")
        self.actionNatural = QtWidgets.QAction(MainWindow)
        self.actionNatural.setObjectName("actionNatural")
        self.actionPurple_sky = QtWidgets.QAction(MainWindow)
        self.actionPurple_sky.setObjectName("actionPurple_sky")
        self.actionGreyscale = QtWidgets.QAction(MainWindow)
        self.actionGreyscale.setObjectName("actionGreyscale")
        self.actionPrinter_friendly = QtWidgets.QAction(MainWindow)
        self.actionPrinter_friendly.setObjectName("actionPrinter_friendly")
        self.actionPrinter_greyscale = QtWidgets.QAction(MainWindow)
        self.actionPrinter_greyscale.setObjectName("actionPrinter_greyscale")
        self.menuSaveAs.addAction(self.actionpng)
        self.menuSaveAs.addAction(self.actionjpeg)
        self.menuSaveAs.addAction(self.actionsvg)
        self.menuStarStandard.addAction(self.action1)
        self.menuStarStandard.addAction(self.action2)
        self.menuStarStandard.addAction(self.action3)
        self.menuStarStandard.addAction(self.action4)
        self.menuDataset.addAction(self.actionBSC)
        self.menuDataset.addAction(self.actionHipparcos)
        self.backgroundMenu.addAction(self.actionNatural)
        self.backgroundMenu.addAction(self.actionPurple_sky)
        self.backgroundMenu.addAction(self.actionGreyscale)
        self.backgroundMenu.addAction(self.actionPrinter_friendly)
        self.backgroundMenu.addAction(self.actionPrinter_greyscale)
        self.menubar.addAction(self.menuDataset.menuAction())
        self.menubar.addAction(self.menuStarStandard.menuAction())
        self.menubar.addAction(self.menuSaveAs.menuAction())
        self.menubar.addAction(self.backgroundMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "仰望 V1.0 -全屏二维图"))
        self.tools2D.setTitle(_translate("MainWindow", "二维图选项"))
        self.allScreenBtn.setText(_translate("MainWindow", "回到主界面"))
        self.alignmentLinesCheckBox.setText(_translate("MainWindow", "银河坐标系"))
        self.axisCheckBox.setText(_translate("MainWindow", "有坐标"))
        self.tools3D.setTitle(_translate("MainWindow", "鼠标点击，找到附近的星星"))
        self.label_3.setText(_translate("MainWindow", "你点击的位置是："))
        # self.findStarBtn.setText(_translate("MainWindow", "最近的星体"))
        self.menuSaveAs.setTitle(_translate("MainWindow", "2D预览另存为"))
        self.menuStarStandard.setTitle(_translate("MainWindow", "星等"))
        self.menuDataset.setTitle(_translate("MainWindow", " 导入数据集"))
        self.backgroundMenu.setTitle(_translate("MainWindow", "背景颜色"))
        self.actionpng.setText(_translate("MainWindow", "png"))
        self.actionjpeg.setText(_translate("MainWindow", "jpeg"))
        self.actionsvg.setText(_translate("MainWindow", "svg"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action3.setText(_translate("MainWindow", "3"))
        self.action4.setText(_translate("MainWindow", "4"))
        self.actionBSC.setText(_translate("MainWindow", "BSC"))
        self.actionBSC.setIconText(_translate("MainWindow", "BSC"))
        self.actionHipparcos.setText(_translate("MainWindow", "Hipparcos"))
        self.actionNatural.setText(_translate("MainWindow", "Natural"))
        self.actionPurple_sky.setText(_translate("MainWindow", "Purple sky"))
        self.actionGreyscale.setText(_translate("MainWindow", "Greyscale"))
        self.actionPrinter_friendly.setText(_translate("MainWindow", "Printer friendly"))
        self.actionPrinter_greyscale.setText(_translate("MainWindow", "Printer greyscale"))

        self.groupBox.setTitle(_translate("MainWindow", " 缩放"))
        self.zoomBtn.setText(_translate("MainWindow", "放大"))
        self.deZoomBtn.setText(_translate("MainWindow", "缩小"))
        self.zoomLabel.setText(_translate("MainWindow", "当前比例：0.5"))

        # 菜单栏点击事件
        self.actionBSC.triggered.connect(lambda: self.changeDataset('BSC'))
        self.actionHipparcos.triggered.connect(lambda: self.changeDataset('Hipparcos'))
        self.action1.triggered.connect(lambda: self.changeMag(1))
        self.action2.triggered.connect(lambda: self.changeMag(2))
        self.action3.triggered.connect(lambda: self.changeMag(3))
        self.action4.triggered.connect(lambda: self.changeMag(4))
        self.actionGreyscale.triggered.connect(lambda: self.changeBackGroundColor('Greyscale'))
        self.actionNatural.triggered.connect(lambda: self.changeBackGroundColor('Natural'))
        self.actionPrinter_friendly.triggered.connect(lambda: self.changeBackGroundColor('Printer_friendly'))
        self.actionPrinter_greyscale.triggered.connect(lambda: self.changeBackGroundColor('Printer_greyscale'))
        self.actionPurple_sky.triggered.connect(lambda: self.changeBackGroundColor('Purple_sky'))
        self.actionjpeg.triggered.connect(lambda: self.saveAs('jpeg'))
        self.actionpng.triggered.connect(lambda: self.saveAs('png'))
        self.actionsvg.triggered.connect(lambda: self.saveAs('svg'))
        # self.findStarBtn.clicked.connect(lambda: Utils.searchCloestStar(self.x, self.y, self.zoomscale, self.dataset))

        self.axisCheckBox.stateChanged.connect(self.setAxis)
        self.alignmentLinesCheckBox.stateChanged.connect(self.setCoordinate)

        # self.preview3D.mousePressEvent = self.previewXY
        self.preview2D.mousePressEvent = self.previewXY
        self.preview2D.grabShortcut(QtGui.QKeySequence.mnemonic("&S"))
        self.preview2D.grabShortcut(QtGui.QKeySequence.mnemonic("&L"))

        self.shc_s = QtWidgets.QShortcut(QtGui.QKeySequence.mnemonic("&S"), MainWindow)
        self.shc_s.setContext(QtCore.Qt.WindowShortcut)
        self.shc_s.activated.connect(self.deZoomPic)
        self.shc_l = QtWidgets.QShortcut(QtGui.QKeySequence.mnemonic("&L"), MainWindow)
        self.shc_l.setContext(QtCore.Qt.WindowShortcut)
        self.shc_l.activated.connect(self.zoomPic)

        self.zoomBtn.clicked.connect(self.zoomPic)
        self.deZoomBtn.clicked.connect(self.deZoomPic)

        self.allScreenBtn.clicked.connect(self.closeWindow)

        self.superChange2D()

    def setCoordinate(self):
        self.coordinate = 'Galactic' if self.alignmentLinesCheckBox.isChecked() else 'Equatorial'
        self.superChange2D()

    def setAxis(self):
        self.axis = self.axisCheckBox.isChecked()
        self.axis = 'on' if self.axis else 'off'
        self.superChange2D()

    def changeDataset(self, dataset):
        self.dataset = dataset
        self.superChange2D()

    def superChange2D(self):
        # bc = self.backgroundColor
        database = self.dataset
        mag = self.mag
        coordinate = self.coordinate
        axis = self.axis
        self.url = './data/' + database + '_' + coordinate + '_' + str(mag) + '_' + axis + '.jpg'
        self.showPic()

    def showPic(self):
        img = cv2.imread(self.url)  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        self.picW = x
        self.picH = y
        # self.zoomscale = 0.5  # 图片放缩尺度
        self.zoomLabel.setText("当前比例：" + str(round(self.zoomscale, 2)))
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.item.setScale(self.zoomscale)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.preview2D.setScene(self.scene)  # 将场景添加至视图

    def resetBtnClicked(self):
        self.alignment = False
        self.axis = 'off'
        self.backgroundColor = 'Natural'
        self.mag = 1
        self.x = 0
        self.y = 0
        self.dataset = 'BSC'
        self.picFormat = 'png'
        self.closestStarTextBrowser.setText('')
        self.mouseXYTextEdit.setText('')
        # TODO
        # wipe out 2-D and 3-D figures

    def changeBackGroundColor(self, backGroundColor):
        self.backgroundColor = backGroundColor

    def saveAs(self, type):
        pass

    def changeMag(self, mag):
        self.mag = mag
        self.superChange2D()

    def previewXY(self, event):
        self.x = event.x()
        self.y = event.y()
        """
        print(self.x, self.y)
        # print(self.item.width(), self.item.height())
        print(self.preview2D.size().width(), self.preview2D.size().height())
        # print(self.item.x(), self.item.y())
        # print(self.preview2D.x(), self.preview2D.y())
        print(self.picW * self.zoomscale, self.picH * self.zoomscale)
        # Utils.searchCloestStar(x * 2, y * 2, 0, self.dataset)
        """
        self.x, self.y = self.changeXY(self.x, self.y)
        self.mouseXYTextEdit.setText(str(round(self.x,2)) + ', ' + str(round(self.y,2)))
        # self.x, self.y = Utils.calcLongLatByXY(self.x, self.y, self.zoomscale)
        dic = Utils.searchCloestStar(self.x, self.y, self.zoomscale, self.dataset)
        # self.closestStarTextBrowser.setText(str(dic))

        res = ''
        if dic is not None:
            for k in dic:
                res += k + ': ' + dic[k] + '\n'
        else:
            res = 'Sorry, no starts can be found due to unknown reasons.'
        self.closestStarTextBrowser.setText(res)

    def shortCuts(self):
        self.shc_s = QtWidgets.QShortcut(QtGui.QKeySequence.mnemonic("&S"), self)
        self.shc_s.setContext(QtCore.Qt.WindowShortcut)
        self.shc_s.activated.connect(self.deZoomPic)
        self.shc_l = QtWidgets.QShortcut(QtGui.QKeySequence.mnemonic("&L"), self)
        self.shc_l.setContext(QtCore.Qt.WindowShortcut)
        self.shc_l.activated.connect(self.zoomPic)
        self.showPic()
        pass

    def zoomPic(self):
        print('Zoom')
        if self.zoomscale <= 3:
            self.zoomscale += 0.1
        self.superChange2D()

    def deZoomPic(self):
        print('Dezoom')
        if self.zoomscale >= 0.2:
            self.zoomscale -= 0.1
        self.superChange2D()

    def keyPressEvent(self, event):
        # 按键事件对大小写不敏感
        if (event.key() == Qt.Key_S):
            print('测试：S')
            if self.zoomscale >= 0.2:
                self.zoomscale -= 0.1
        if (event.key() == Qt.Key_L):
            print('测试：L')
            if self.zoomscale <= 3:
                self.zoomscale += 0.1
        if (event.key() == Qt.Key_Enter):
            print('测试：Enter')
            self.axis = not self.axisCheckBox.isChecked()
            self.axis = 'on' if self.axis else 'off'
        if (event.key() == Qt.Key_Space):
            print('测试：Space')
            self.coordinate = not self.alignmentLinesCheckBox.isChecked()
            self.coordinate = 'Galactic' if self.coordinate else 'Equatorial'
        self.showPic()

    def closeWindow(self):
        self.MainWindow.close()

    def changeXY(self, x, y):
        a = x / 150 * 36
        b = 90 - 18 * y / 80
        return a, b

"""
        # # 当需要组合键时，要很多种方式，这里举例为“shift+单个按键”，也可以采用shortcut、或者pressSequence的方法。
        # if (event.key() == Qt.Key_P):
        #     if QApplication.keyboardModifiers() == Qt.ShiftModifier:
        #         print("shift + p")
        #     else:
        #         print("p")
        # if (event.key() == Qt.Key_O) and QApplication.keyboardModifiers() == Qt.ShiftModifier:
        #     print("shift + o")
"""
