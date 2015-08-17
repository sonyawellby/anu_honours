import netCDF4 as n
import numpy as np

from matplotlib import cm, pyplot as plt
import pylab
from mpl_toolkits.basemap import Basemap, maskoceans

from maps import saveFig
from cwd import *

cwdInFunction()

data = n.Dataset('data/AWAP_1900-2013_annual_precip_v2_latlon.nc','a')
#AWAP_1900-2014_monthly_precip_swACCESSgrid_v1.nc
#AWAP_1900-2013_annual_precip_v1.nc
#ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc
#data/AWAP_1900-2013_annual_precip_v2_latlon.nc

start = -43.575
newlist = []
for i in range(0,670):
    i = start
    newlist.append(i)
    start += 0.05
print newlist    

data.variables['latitude'][:] = newlist[:]


start_lon = 112.925
newlist_lon = []
for i in range(0,813):
    i = start_lon
    newlist_lon.append(i)
    start_lon += 0.05
print newlist_lon    

data.variables['longitude'][:] = newlist_lon[:]
    

#lat = data.variables['AWAP_precipitation'][0,:,0]
lat = data.variables['latitude']
lat_units = data.variables['latitude'].units
#lon = data.variables['AWAP_precipitation'][0,0,:]
lon = data.variables['longitude']
lon_units = data.variables['longitude'].units

var_time = data.variables['AWAP_precipitation'][0,:,:]
var_units = data.variables['AWAP_precipitation'].units

m = Basemap(projection='cyl', resolution='c',\
    llcrnrlat=-50,urcrnrlat=0,\
    llcrnrlon=110,urcrnrlon=160)
m.drawcoastlines()
#data.variables['latitude']

[lonall,latall] = np.meshgrid(lon,lat)
x,y = m(lonall,latall)

cs = m.pcolor(x,y,var_time,vmin=0,vmax=0.02) #
cbarLabel = "%s" %(var_units) #not working
cbar = m.colorbar(cs, location='right', pad="10%")

titleName = raw_input("Enter the graph title (don't forget units): ")
plt.title(titleName,fontsize=18)
saveFig()

plt.show()

