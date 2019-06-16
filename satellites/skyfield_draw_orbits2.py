from skyfield.api import Topos, load
from skyfield.api import Loader
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.basemap import Basemap
from matplotlib import cm


def makecubelimits(axis, centers=None, hw=None):
    lims = ax.get_xlim(), ax.get_ylim(), ax.get_zlim()
    if centers == None:
        centers = [0.5*sum(pair) for pair in lims] 

    if hw == None:
        widths  = [pair[1] - pair[0] for pair in lims]
        hw      = 0.5*max(widths)
        ax.set_xlim(centers[0]-hw, centers[0]+hw)
        ax.set_ylim(centers[1]-hw, centers[1]+hw)
        ax.set_zlim(centers[2]-hw, centers[2]+hw)
        print("hw was None so set to:", hw)
    else:
        try:
            hwx, hwy, hwz = hw
            print("ok hw requested: ", hwx, hwy, hwz)

            ax.set_xlim(centers[0]-hwx, centers[0]+hwx)
            ax.set_ylim(centers[1]-hwy, centers[1]+hwy)
            ax.set_zlim(centers[2]-hwz, centers[2]+hwz)
        except:
            print("nope hw requested: ", hw)
            ax.set_xlim(centers[0]-hw, centers[0]+hw)
            ax.set_ylim(centers[1]-hw, centers[1]+hw)
            ax.set_zlim(centers[2]-hw, centers[2]+hw)

    return centers, hw



## 从网络导入空间站数据
# stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
# satellites = load.tle(stations_url)
# satellite = satellites['ISS (ZARYA)']
# all_satellites_names = list(satellites.keys())
# all_satellites = list(satellites.values())
tle_path = "Full_Catalog-20190613T0000.tle"

satellites = load.tle(tle_path)
MAX_NUMBER = 100
all_satellites_names = np.array(list(satellites.keys()))[:MAX_NUMBER]
all_satellites = np.array(list(satellites.values()))[:MAX_NUMBER]


load = Loader(directory='.', expire=False)
# expire=False: use local files
ts = load.timescale() 


from skyfield.api import Loader, EarthSatellite
from skyfield.timelib import Time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


halfpi, pi, twopi = [f*np.pi for f in (0.5, 1, 2)]
degs, rads = 180/pi, pi/180




hours = np.arange(0, 3, 0.01)
time = ts.utc(2018, 2, 7, hours)


all_Rpos = [sate.at(time).position.km for sate in all_satellites]
all_Rposecl = [sate.at(time).ecliptic_position().km for sate in all_satellites]




all_ele = [sate.at(time).subpoint().elevation.m for sate in all_satellites]

MAX_ELE = np.nanmax(np.array(all_ele))
MIN_ELE = np.nanmin(np.array(all_ele))

color_ref = (np.array(all_ele) - MIN_ELE) / (MAX_ELE - MIN_ELE)
cmap = cm.get_cmap('Oranges')




re = 6378.   # earth radius

theta = np.linspace(0, twopi, 201)
cth, sth, zth = [f(theta) for f in (np.cos, np.sin, np.zeros_like)]
lon0 = re*np.vstack((cth, zth, sth))
lons = []
for phi in rads*np.arange(0, 180, 15):
    cph, sph = [f(phi) for f in (np.cos, np.sin)]
    lon = np.vstack((lon0[0]*cph - lon0[1]*sph,
                     lon0[1]*cph + lon0[0]*sph,
                     lon0[2]) )
    lons.append(lon)

lat0 = re*np.vstack((cth, sth, zth))
lats = []
for phi in rads*np.arange(-75, 90, 15):
    cph, sph = [f(phi) for f in (np.cos, np.sin)]
    lat = re*np.vstack((cth*cph, sth*cph, zth+sph))
    lats.append(lat)




if True:    
    fig = plt.figure(figsize=[10, 8])  # [12, 10]

    ax  = fig.add_subplot(1, 1, 1, projection='3d')

    for i in range(len(all_Rpos)):
        Rpos = all_Rpos[i]
        x, y, z = Rpos
        ax.plot(x, y, z, alpha=0.3, color=cmap(color_ref[i].mean()))
        for x, y, z in lons:
            ax.plot(x, y, z, '-k', linewidth=0.3)
        for x, y, z in lats:
            ax.plot(x, y, z, '-k', linewidth=0.3)

    centers, hw = makecubelimits(ax)

    print("centers are: ", centers)
    print("hw is:       ", hw)

    plt.show()

# r_Roadster = np.sqrt((Rpos**2).sum(axis=0))
# alt_roadster = r_Roadster - re

# if True:
#     plt.figure()
#     plt.plot(hours, r_Roadster)
#     plt.plot(hours, alt_roadster)
#     plt.xlabel('hours', fontsize=14)
#     plt.ylabel('Geocenter radius or altitude (km)', fontsize=14)
#     plt.show()

