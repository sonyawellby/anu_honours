import netCDF4 as n
import numpy as np

from matplotlib import cm, pyplot as plt
import pylab
from mpl_toolkits.basemap import Basemap, maskoceans

from maps import saveFig
from cwd import *

cwdInFunction()


data = n.Dataset('AWAP_1900-2014_monthly_precip_swACCESSgrid_v4.nc','a')
#AWAP_1900-2014_monthly_precip_swACCESSgrid_v1.nc
#AWAP_1900-2013_annual_precip_v1.nc
#ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc
#data/AWAP_1900-2013_annual_precip_v2_latlon.nc
#AWAP_1900-2014_monthly_precip_swACCESSgrid_v3.nc



"""
Fill in correct longitude and latitude values for dataset (originally
all values of both latitude and longitude were set to 0.0).
"""
#awapTime()

#'start' formerly = -43.125 (for grid that does not match ACCESS)
start = -43.75
newlist = []
for i in range(0,27):
    i = start
    newlist.append(i)
    start += 1.25
print newlist    

data.variables['latitude'][:] = newlist[:]


start_lon = 114.375
newlist_lon = []
for i in range(0,22):
    i = start_lon
    newlist_lon.append(i)
    start_lon += 1.875
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

"""
Trim AWAP to right time period

"""
#def awapTime():
"""
A function to trim and reshape AWAP data from January 1900-December 2005
to June 1900-May 2004.

Note:
data.variables['AWAP_precipitation'][1370:1371] #December 2005
data.variables['AWAP_precipitation'][0:1] # January 1900
"""
"""
data_new = data.variables['AWAP_precipitation'][5:1253]
print len(data_new)
data = np.array(data_new)
data = np.reshape(data,(104,12,27,22))
#return data
"""
