import netCDF4 as n
import numpy as np

from matplotlib import cm, pyplot as plt
import pylab
from mpl_toolkits.basemap import Basemap, maskoceans

from metadata import cwd

cwd()

data = n.Dataset('AWAP_1900-2014_monthly_precip_v1.nc','r')

lat = data.variables['AWAP_precipitation']
lat_units = data.variables['latitude'].units
lon = data.variables['AWAP_precipitation']
lon_units = data.variables['longitude'].units

var_time = data.variables['AWAP_precipitation'][0,:,:]
var_units = data.variables['AWAP_precipitation'].units

m = Basemap(projection='cyl', resolution='c',\
    llcrnrlat=-50,urcrnrlat=0,\
    llcrnrlon=110,urcrnrlon=160)
m.drawcoastlines()

[lonall,latall] = np.meshgrid(lon,lat)
x,y = m(lonall,latall)

cs = m.pcolor(x,y,var_time)
cbar = m.colorbar(cs, location='right', pad="10%")

plt.show()

"""
data = n.Dataset('AWAP_1900-2014_monthly_precip_v1.nc','r')

lat = data.variables['latitude'][:]
lat_units = data.variables['latitude'].units
lon = data.variables['longitude'][:]
lon_units = data.variables['longitude'].units

var_time = data.variables['AWAP_precipitation'][0,:,:]
var_units = data.variables['AWAP_precipitation'].units

m = Basemap(projection='cyl', resolution='c',\
    llcrnrlat=-50,urcrnrlat=0,\
    llcrnrlon=110,urcrnrlon=160)
m.drawcoastlines()

[lonall,latall] = np.meshgrid(lon,lat)
x,y = m(lonall,latall)

cs = m.pcolor(x,y,var_time)
cbar = m.colorbar(cs, location='right', pad="10%")

plt.show()
"""


