from skyfield.api import Topos, load
from skyfield.api import Loader
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import cm
cmap = cm.get_cmap('Oranges')


# 本地数据
# tle_path = "Full_Catalog-20190613T0000.tle"
# satellites = load.tle(tle_path)
# 联网数据
stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle(stations_url)

'''设定画的轨道数量'''
MAX_NUMBER = 100


all_satellites_names = np.array(list(satellites.keys()))
all_satellites = np.array(list(satellites.values()))

# SAMPLE_IDX = [1]
SAMPLE_IDX = np.random.randint(0, len(all_satellites_names)-1, MAX_NUMBER)
all_satellites_names = np.array(all_satellites_names)[SAMPLE_IDX]
all_satellites = np.array(all_satellites)[SAMPLE_IDX]
# all_satellites_names = all_satellites_names[:MAX_NUMBER]
# all_satellites = all_satellites[:MAX_NUMBER]
print('all_satellites_names', all_satellites_names)

load = Loader(directory='.', expire=False)
# expire=False: use local files
ts = load.timescale()


# hours = np.arange(0, 24, 0.1)
hours = np.arange(0, 3, 0.1)  '''设定画的时间范围，hours跨度越大，对应时间越长，轨迹越长'''
time = ts.utc(2018, 2, 7, hours)


fig, ax = plt.subplots(figsize=(8,8))
ax.set_position([0.0,0.0,1.0,1.0])


# add axis for space background effect
galaxy_image = plt.imread('galaxy_image.png')
ax.imshow(galaxy_image)
ax.set_axis_off()
ax1 = fig.add_axes([0.25,0.2,0.5,0.5])


# m = Basemap(projection="ortho", lon_0=110, lat_0=90)
m = Basemap()
m.bluemarble()
# m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
# m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
# m.drawcoastlines(linewidth=0.1, color=[0.4,0.4,1])
# m.drawcountries(linewidth=0.07, color="white")


all_ele = [sate.at(time).subpoint().elevation.m for sate in all_satellites]

MAX_ELE = np.nanmax(np.array(all_ele))
MIN_ELE = np.nanmin(np.array(all_ele))

color_ref = (np.array(all_ele) - MIN_ELE) / (MAX_ELE - MIN_ELE)
cmap = cm.get_cmap('Oranges')


for i in range(len(all_satellites)):
    satellite = all_satellites[i]
    for h in range(1, len(hours)):
        t1 = time[h-1]
        t2 = time[h]

        subpoint1 = satellite.at(t1).subpoint()
        subpoint2 = satellite.at(t2).subpoint()

        lon1 = subpoint1.longitude.degrees
        lat1 = subpoint1.latitude.degrees
        lon2 = subpoint2.longitude.degrees
        lat2 = subpoint2.latitude.degrees


        m.drawgreatcircle(lon1, lat1, lon2, lat2, color=cmap(color_ref[i][h-1]**0.5), linewidth=0.5)



plt.show()