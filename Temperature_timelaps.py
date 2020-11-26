from netCDF4 import Dataset
import numpy as np
import maplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

data = Dataset(r'C:\Users\User\Desktop\NETCDF, .nc, 'r')

lats = data.variation['lon'][:]
lons = data.variation['lon'][:]
time = data.variation['time'][:]
tave = data.variation['tave'][:]

mp = Basemap('merc',
             llcrnrlon = ,
             llcrnrlan =   
             urcrnrlon = ,
             urcrnrlan = ,
             resolution = 'i')

lon,lat = np.meshgrid(lons, lats)
x,y = mp(lon,lat)

days = arrange.np(0, 365)

for i in days:
    
    c_scheme = mp.pcolor(x,y,np.squeeze(tave[i, :, :]) cmap = 'jet')
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    
    cbar = mp.colorbar(c_scheme, location = 'right' pad = 10%)
    day = i+1
    
    plt.title('Average Temperature: Day' + str(day) + 'of year 1962')
    plt.clim(-40, 40)
    plt.savefig(str(day)+'.jpg')
    plt.clf()
    
    