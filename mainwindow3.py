# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import Utils
import cv2
from fullscreenwindow2D import *
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkDemo import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.backgroundColor = 'Natural'
        self.alignment = False
        self.coordinate = 'Equatorial'
        self.axis = 'off'
        self.mag = 4
        self.x = 0
        self.y = 0
        self.dataset = 'BSC'
        self.picFormat = 'png'
        self.url = './data/BSC_Equatorial_4_off.jpg'

        self.render = vtk.vtkRenderer()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.vtkWidget = QVTKRenderWindowInteractor(self.centralwidget)
        actor, sphere_Actor, c_b = celestial_sphere(mag=4)
        self.render.SetBackground(c_b[0], c_b[1], c_b[2])

        self.actor = actor
        self.sphere_Actor = sphere_Actor
        self.render.AddActor(actor)
        self.render.AddActor(sphere_Actor)
        # Sign up to receive TimerEvent
        self.cb = vtkTimerCallback()
        self.cb.actor = actor
        self.vtkWidget.AddObserver('TimerEvent', self.cb.execute)
        self.vtkWidget.CreateRepeatingTimer(100)
        self.render.ResetCamera()
        self.render.GetActiveCamera().Zoom(2)
        self.vtkWidget.GetRenderWindow().AddRenderer(self.render)
        self.vtkWidget.GetRenderWindow().SetSize(1600, 1600)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
        self.iren.SetRenderWindow(self.vtkWidget.GetRenderWindow())
        self.vtkWidget.GetRenderWindow().Render()
        self.iren.Initialize()
        self.iren.Start()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1231, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tools2D = QtWidgets.QGroupBox(self.centralwidget)
        self.tools2D.setGeometry(QtCore.QRect(10, 207, 251, 241))
        self.tools2D.setObjectName("tools2D")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tools2D)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fullScreenBtn = QtWidgets.QPushButton(self.tools2D)
        self.fullScreenBtn.setObjectName("fullScreenBtn")
        self.verticalLayout.addWidget(self.fullScreenBtn)
        self.alignmentLinesCheckBox = QtWidgets.QCheckBox(self.tools2D)
        self.alignmentLinesCheckBox.setObjectName("alignmentLinesCheckBox")
        self.verticalLayout.addWidget(self.alignmentLinesCheckBox)
        self.axisCheckBox = QtWidgets.QCheckBox(self.tools2D)
        self.axisCheckBox.setObjectName("axisCheckBox")
        self.verticalLayout.addWidget(self.axisCheckBox)
        self.preview2D = QtWidgets.QGraphicsView(self.centralwidget)
        self.preview2D.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.preview2D.setObjectName("preview2D")
        self.showPic()
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 10, 861, 531))
        self.preview3D = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.preview3D.setContentsMargins(0, 0, 0, 0)
        self.preview3D.setObjectName("preview3D")
        self.tools3D = QtWidgets.QGroupBox(self.centralwidget)
        self.tools3D.setGeometry(QtCore.QRect(280, 550, 871, 151))
        self.tools3D.setObjectName("tools3D")
        self.mouseXYTextEdit = QtWidgets.QTextEdit(self.tools3D)
        self.mouseXYTextEdit.setGeometry(QtCore.QRect(10, 40, 191, 31))
        self.mouseXYTextEdit.setObjectName("mouseXYTextEdit")
        self.label_3 = QtWidgets.QLabel(self.tools3D)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_3.setObjectName("label_3")
        self.findStarBtn = QtWidgets.QPushButton(self.tools3D)
        self.findStarBtn.setGeometry(QtCore.QRect(10, 80, 113, 32))
        self.findStarBtn.setObjectName("findStarBtn")
        self.closestStarTextBrowser = QtWidgets.QTextBrowser(self.tools3D)
        self.closestStarTextBrowser.setGeometry(QtCore.QRect(235, 30, 621, 111))
        self.closestStarTextBrowser.setObjectName("closestStarTextBrowser")
        self.addEarthCheckBox = QtWidgets.QCheckBox(self.tools3D)
        self.addEarthCheckBox.setGeometry(QtCore.QRect(20, 120, 86, 20))
        self.addEarthCheckBox.setObjectName("addEarthCheckBox")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(10, 450, 251, 32))
        self.resetBtn.setObjectName("resetBtn")
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
        self.actionNatural.setObjectName("actionNatrual")
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
        self.findStarBtn.clicked.connect(lambda: self.searchStar(self.mouseXYTextEdit.toPlainText(), self.dataset))

        self.fullScreenBtn.clicked.connect(self.fullScreenBtnClicked)
        self.addEarthCheckBox.stateChanged.connect(self.addEarth2Globe)

        self.axisCheckBox.stateChanged.connect(self.setAxis)
        self.alignmentLinesCheckBox.stateChanged.connect(self.setCoordinate)

        self.preview3D.mousePressEvent = self.previewXY
        self.preview2D.mousePressEvent = self.previewXY

        self.preview3D.addWidget(self.vtkWidget)
        # self.vtkWidget.resize(200, 100)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "仰望 V1.0"))
        self.tools2D.setTitle(_translate("MainWindow", "二维图选项"))
        self.fullScreenBtn.setText(_translate("MainWindow", "全屏展示二维图"))
        self.alignmentLinesCheckBox.setText(_translate("MainWindow", "银河坐标系"))
        self.axisCheckBox.setText(_translate("MainWindow", "有坐标"))
        self.tools3D.setTitle(_translate("MainWindow", "输入星体编号，获得详细信息"))
        self.label_3.setText(_translate("MainWindow", "你查询的星体是："))
        self.findStarBtn.setText(_translate("MainWindow", "查询"))
        self.addEarthCheckBox.setText(_translate("MainWindow", " 显示地球"))
        self.resetBtn.setText(_translate("MainWindow", "清空结果"))
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

    def fullScreenBtnClicked(self):
        prams = {'backgroundColor': self.backgroundColor,
                 'alignment': self.alignment,
                 'coordinate': self.coordinate,
                 'axis': self.axis,
                 'mag': self.mag,
                 'dataset': self.dataset,
                 'picFormat': self.picFormat,
                 'url': self.url}

        self.secondWindow = SecondWindow(self.MainWindow)
        self.ui2 = Ui_MainWindow2D(prams)
        # ui.setupUi(self.MainWindow)
        self.ui2.setupUi(self.secondWindow)
        self.statusbar.showMessage("Switched to 2-D")
        self.secondWindow.show()
        # self.close()

    def setCoordinate(self):
        self.coordinate = 'Galactic' if self.alignmentLinesCheckBox.isChecked() else 'Equatorial'
        self.superChange2D()

    def setAxis(self):
        self.axis = self.axisCheckBox.isChecked()
        self.axis = 'on' if self.axis else 'off'
        self.superChange2D()

    def changeDataset(self, dataset):
        self.dataset = dataset
        self.superChange3D()
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
        self.zoomscale = 0.2  # 图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.item.setScale(self.zoomscale)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.preview2D.setScene(self.scene)  # 将场景添加至视图

    def superChange3D(self):
        bc = self.backgroundColor
        data = self.dataset
        mag = self.mag
        self.render.RemoveActor(self.actor)
        self.render.RemoveActor(self.sphere_Actor)
        self.actor, self.sphere_Actor, c_b = celestial_sphere(colortype=bc, file_name=data, mag=mag)
        # print(c_b)
        self.render.SetBackground(c_b[0], c_b[1], c_b[2])  # 背景颜色（0-1)

        self.render.AddActor(self.actor)
        self.render.AddActor(self.sphere_Actor)

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
        self.superChange3D()

    def saveAs(self, type):
        pass

    def changeMag(self, mag):
        self.mag = mag
        self.superChange3D()
        self.superChange2D()

    def searchStar(self, starIndex, database):
        description = Utils.searchStarByName(starIndex, database)
        if description is not None:
            res = ''
            dic = description
            if dic is not None:
                for k in dic:
                    res += k + ': ' + dic[k] + '\n'
            self.closestStarTextBrowser.setText(res)
        else:
            self.closestStarTextBrowser.setText('Sorry, no starts can be found due to unknown reasons.')
        # self.closestStarTextBrowser.moveCursor(self.closestStarTextBrowser.textCursor().End)

    def addEarth2Globe(self):
        if self.addEarthCheckBox.isChecked():
            self.earthActor = addEarth()
            self.render.AddActor(self.earthActor)
            self.sphere_Actor.GetProperty().SetOpacity(0.1)
        else:
            self.render.RemoveActor(self.earthActor)
            self.sphere_Actor.GetProperty().SetOpacity(1)

    def changeStarColor(self, starColor):
        pass

    def previewXY(self, event):
        self.x = event.x()
        self.y = event.y()
        print(self.x, self.y)


class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
