from skyfield.api import Topos, load
from skyfield.api import Loader
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.basemap import Basemap
from matplotlib import cm




def draw_satellite_map(basemap_params, colored_attribute='orient'):
    '''
    Input:
    basemap_params: <dict> 'basemap parameter': value
    colored_attribute: 'orient''elevation', which attributes to be used in colormap
    '''
    llcrnrlon = basemap_params.get('llcrnrlon')
    llcrnrlat = basemap_params.get('llcrnrlat')
    urcrnrlon = basemap_params.get('urcrnrlon')
    urcrnrlat = basemap_params.get('urcrnrlat')
    projection = basemap_params.get('projection', 'cyl')
    lat_0 = basemap_params.get('lat_0')
    lon_0 = basemap_params.get('lon_0')

    if colored_attribute == 'orient':
        cmap = cm.get_cmap('hsv')  # cyclic colormap for angles
    elif colored_attribute == 'elevation':
        cmap = cm.get_cmap('Oranges')



    ## 从网络导入空间站数据
    from skyfield.api import Topos, load
    stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
    satellites = load.tle(stations_url)
    satellite = satellites['ISS (ZARYA)']


    load = Loader(directory='.', expire=False)
    # expire=False: use local files
    ts = load.timescale() 

    all_stations_names = list(satellites.keys())
    all_stations = list(satellites.values())

    # 获取卫星的当前位置
    t = ts.now()

    all_geocentric = [sate.at(t) for sate in all_stations] 


    # 避免不停地写list的向量运算np.vectorize一切, 我们
    vecfun_subpoint = np.vectorize(lambda x: x.subpoint())
    vecfun_lon = np.vectorize(lambda x: x.longitude.degrees)
    vecfun_lat = np.vectorize(lambda x: x.latitude.degrees)
    vecfun_ele = np.vectorize(lambda x: x.elevation.m)


    all_subpoint = vecfun_subpoint(all_geocentric)
    all_lon = vecfun_lon(all_subpoint)
    all_lat = vecfun_lat(all_subpoint)
    all_ele = vecfun_ele(all_subpoint)


    # 初始化画布
    fig, ax = plt.subplots(figsize=(8,8))

    m = Basemap(llcrnrlon=llcrnrlon, llcrnrlat=llcrnrlat, urcrnrlon=urcrnrlon, urcrnrlat=urcrnrlat,
                lat_0=lat_0, lon_0=lon_0, projection=projection)
    m.bluemarble()

    # 初始画图
    x, y = m(all_lon, all_lat)
    scat = []
    for i in range(len(x)):
        satellite_velocity = all_stations[i].ITRF_position_velocity_error(t)[1]
        satellite_orient = np.mod(np.rad2deg(np.angle(satellite_velocity[0] + satellite_velocity[1]*1j)) - 90, 360)
        scat.append(m.scatter(x[i], y[i], marker=(3, 0, satellite_orient), color=cmap(satellite_orient/360)))


    '''内嵌的函数init, update 用于动画'''
    def init():
        # return scat,
        # return scat,sate_text
        return scat


    def update(frame):
        t = ts.now()
        all_geocentric = [sate.at(t) for sate in all_stations]

        all_subpoint = vecfun_subpoint(all_geocentric)

        all_subpoint = vecfun_subpoint(all_geocentric)
        all_lon = vecfun_lon(all_subpoint)
        all_lat = vecfun_lat(all_subpoint)
        all_ele = vecfun_ele(all_subpoint)

        x, y = m(all_lon, all_lat)

        scat = []
        for i in range(len(x)):
            satellite_velocity = all_stations[i].ITRF_position_velocity_error(t)[1]
            satellite_orient = np.mod(np.rad2deg(np.angle(satellite_velocity[0] + satellite_velocity[1]*1j)) - 90, 360)
            scat.append(m.scatter(x[i], y[i], marker=(3, 0, satellite_orient), color=cmap(satellite_orient/360)))

        # scat = m.scatter(x, y, marker=(3, 0, 40), zorder=10, color=[0.2,0.2,0.9])
        # sate_text = plt.text(x+8, y-8, all_stations_names, color=[0.9,0.2,0.2])

        # return scat,
        # return scat,sate_text
        return scat


    ani = FuncAnimation(fig, update, frames=np.linspace(0, 50),
                    init_func=init, blit=True, interval=2000)
    plt.show()


if __name__ == '__main__':

    basemap_params = {
        'llcrnrlon': None,
        'llcrnrlat': None,
        'urcrnrlon': None,
        'urcrnrlat': None,
        'projection': 'cyl',
        'lat_0': None,
        'lon_0': None
    }

    draw_satellite_map(basemap_params)

