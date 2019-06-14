import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

df = pd.read_csv("./catalog.csv")


def bv2rgb(bv):
    if bv < -0.40: bv = -0.40
    if bv > 2.00: bv = 2.00

    r = 0.0
    g = 0.0
    b = 0.0

    if -0.40 <= bv < 0.00:
        t = (bv + 0.40) / (0.00 + 0.40)
        r = 0.61 + (0.11 * t) + (0.1 * t * t)
    elif 0.00 <= bv < 0.40:
        t = (bv - 0.00) / (0.40 - 0.00)
        r = 0.83 + (0.17 * t)
    elif 0.40 <= bv < 2.10:
        t = (bv - 0.40) / (2.10 - 0.40)
        r = 1.00
    if -0.40 <= bv < 0.00:
        t = (bv + 0.40) / (0.00 + 0.40)
        g = 0.70 + (0.07 * t) + (0.1 * t * t)
    elif 0.00 <= bv < 0.40:
        t = (bv - 0.00) / (0.40 - 0.00)
        g = 0.87 + (0.11 * t)
    elif 0.40 <= bv < 1.60:
        t = (bv - 0.40) / (1.60 - 0.40)
        g = 0.98 - (0.16 * t)
    elif 1.60 <= bv < 2.00:
        t = (bv - 1.60) / (2.00 - 1.60)
        g = 0.82 - (0.5 * t * t)
    if -0.40 <= bv < 0.40:
        t = (bv + 0.40) / (0.40 + 0.40)
        b = 1.00
    elif 0.40 <= bv < 1.50:
        t = (bv - 0.40) / (1.50 - 0.40)
        b = 1.00 - (0.47 * t) + (0.1 * t * t)
    elif 1.50 <= bv < 1.94:
        t = (bv - 1.50) / (1.94 - 1.50)
        b = 0.63 - (0.6 * t * t)

    return (r, g, b)


def DrawStar2D(database='BSC', color=None, coordinate='Equatorial', mag=4):
    file_name_dict = {'BSC': "./BSC.csv", 'Hipparcos': './hip_small.csv'}
    df = pd.read_csv(file_name_dict[database])
    if mag:
        df = df[df.Vmag <= mag]

    plt.figure(figsize=(15, 8))
    plt.xlim((0, 360))
    plt.ylim((-90, 90))
    plt.ion()  # 开启interactive模式

    if coordinate == 'Equatorial':
        list1 = df['J2000_a']
        list2 = df['J2000_d']

    elif coordinate == 'Galactic':
        list1 = df['l']
        list2 = df['b']

    for x, y, a, c in zip(list1, list2, df['Vmag'], df['BV']):
        a = 0.8 - a / 10
        c = bv2rgb(c)
        plt.scatter(x, y, s=a * 10, c=c, alpha=a)
        plt.pause(0.1)

    name1 = './' + database + '_' + coordinate + '_' + str(mag) + '_' + 'on' + '.jpg'
    plt.savefig(name1)
    plt.ioff()  # 关闭interactive模式，否则后面的plt.show()也会一闪而过
    plt.axis('off')
    name2 = './' + database + '_' + coordinate + '_' + str(mag) + '_' + 'off' + '.jpg'
    plt.savefig(name2)
    plt.show()


DrawStar2D(database='BSC', color=None, coordinate='Equatorial', mag=1)
