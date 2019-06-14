import pandas as pd
import numpy as np
import random


def searchCloestStar(x, y, zoom, database):
    # zoom 放大倍数
    # x0 = 44  ###
    # y0 = 10  ###
    # a = 36 / 14 * (x - 360 * 9 / 114 - x0)
    # b = 90 + 18 / 31 * (y - 180 / 310 * 48 - y0)
    # a = 180 - (180 - a) / zoom * 2
    # b = b / zoom * 2
    a, b = x, y
    file_name_dict = {'BSC': "./data/BSC.csv", 'Hipparcos': './data/hip_small.csv'}
    file_name = file_name_dict[database]
    df = pd.read_csv(file_name)
    select = df[(df['J2000_a'] <= (np.round(a, 2) + 10)) & (df['J2000_a'] > (np.round(a, 2)))
                & (df['J2000_d'] <= (np.round(b, 2) + 10)) & (df['J2000_d'] > (np.round(b, 2)))]
    if len(select) == 0:
        return None
    select = select[select.Vmag == max(select.Vmag)]
    d = {}
    if database == 'BSC':
        d['Number'] = 'SAO ' + str(select['SAO'].tolist()[0])
        d['Name'] = str(select['name'].tolist()[0])
    elif database == 'Hipparcos':
        d['HIP CODE'] = str(select['Hcode'].tolist()[0])
    d['B-V'] = str(round(select['BV'].tolist()[0], 4))
    d['SPtype'] = str(select['SPtype'].tolist()[0])
    d['RAhms'] = str(select['RAhms'].tolist()[0])
    d['DEdms'] = str(select['DEdms'].tolist()[0])
    d['GLON'] = str(select['l'].tolist()[0])
    d['GLAT'] = str(select['b'].tolist()[0])
    return d


def searchStarByName(name, database):
    file_name_dict = {'BSC': "./data/BSC.csv", 'Hipparcos': './data/hip_small.csv'}
    file_name = file_name_dict[database]
    df = pd.read_csv(file_name)
    if database == 'BSC':
        try:
            name = int(name)
        except:
            return None
        if name in df.SAO.unique():
            select = df[df.SAO == name]
        else:
            return None
    elif database == 'Hipparcos':
        if name in df.Hcode.unique():
            select = df[df.Hcode == name]
        else:
            return None
    select = select[select.Vmag == max(select.Vmag)]
    d = {}
    if database == 'BSC':
        d['Number'] = 'SAO ' + str(select['SAO'].tolist()[0])
        d['Name'] = str(select['name'].tolist()[0])
    elif database == 'Hipparcos':
        d['HIP CODE'] = str(select['Hcode'].tolist()[0])
    d['B-V'] = str(round(select['BV'].tolist()[0], 4))
    d['SPtype'] = str(select['SPtype'].tolist()[0])
    d['RAhms'] = str(select['RAhms'].tolist()[0])
    d['DEdms'] = str(select['DEdms'].tolist()[0])
    d['GLON'] = str(select['l'].tolist()[0])
    d['GLAT'] = str(select['b'].tolist()[0])
    return d


def calcLongLatByXY(x, y, zoom):
    a = random.randint(0, 90)
    b = random.randint(-90, 90)
    return a, b
