# -*-coding:UTF-8 -*-
import matplotlib
import pandas as pd
import numpy as np

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout, QFileDialog
import sys
import pylab as pl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

pl.mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
def bv2rgb(bv):
    if bv < -0.40: bv = -0.40
    if bv > 2.00: bv = 2.00

    r = 0.0
    g = 0.0
    b = 0.0

    if  -0.40 <= bv<0.00:
        t=(bv+0.40)/(0.00+0.40)
        r=0.61+(0.11*t)+(0.1*t*t)
    elif 0.00 <= bv<0.40:
        t=(bv-0.00)/(0.40-0.00)
        r=0.83+(0.17*t)
    elif 0.40 <= bv<2.10:
        t=(bv-0.40)/(2.10-0.40)
        r=1.00
    if  -0.40 <= bv<0.00:
        t=(bv+0.40)/(0.00+0.40)
        g=0.70+(0.07*t)+(0.1*t*t)
    elif 0.00 <= bv<0.40:
        t=(bv-0.00)/(0.40-0.00)
        g=0.87+(0.11*t)
    elif 0.40 <= bv<1.60:
        t=(bv-0.40)/(1.60-0.40)
        g=0.98-(0.16*t)
    elif 1.60 <= bv<2.00:
        t=(bv-1.60)/(2.00-1.60)
        g=0.82-(0.5*t*t)
    if  -0.40 <= bv<0.40:
        t=(bv+0.40)/(0.40+0.40)
        b=1.00
    elif 0.40 <= bv<1.50:
        t=(bv-0.40)/(1.50-0.40)
        b=1.00-(0.47*t)+(0.1*t*t)
    elif 1.50 <= bv<1.94:
        t=(bv-1.50)/(1.94-1.50)
        b=0.63-(0.6*t*t)

    return (r, g, b)


class ShowWindow(QWidget):
    def __init__(self):
        super(ShowWindow, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建控件对象
        self.inputLabel = QLabel("请输入文件路径:")
        self.editLine = QLineEdit()
        self.selectButton = QPushButton("...")

        self.selectButton.clicked.connect(self.selectFile)

        inputLayout = QHBoxLayout()  # 水平
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.editLine)
        inputLayout.addWidget(self.selectButton)

        # a figure instance to plot on
        self.figure = plt.figure()
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plotText)
        plotLayout = QVBoxLayout()  # 垂直
        plotLayout.addWidget(self.canvas)
        plotLayout.addWidget(self.button)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(plotLayout)
        self.setLayout(mainLayout)
        self.show()

    # 选择图形数据文件存放地址
    def selectFile(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                          "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)
        self.editLine.setText(fileName1)

    # 画图
    def plotText(self):
        X = []
        Y = []
        input_file = self.editLine.text()
        # input_file = r'E:\pyqt\1.txt'
        df=pd.read_csv(input_file)
        data = df[df.Vmag <= 3]



        Ax = self.figure.add_subplot(111)  # Create a `axes' instance in the figure
        Ax.clear()
        Ax.set_ylabel('角度')
        Ax.set_xlabel('时间')
        for x, y, a, c in zip(data['l'], data['b'], data['Vmag'], data['BV']):
            a = 0.8 - a / 10
            c = bv2rgb(c)
            Ax.scatter(x, y, s=a * 10, c=c, alpha=a)
        self.canvas.draw()  # 更新画布


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowWindow()
    sys.exit(app.exec_())
