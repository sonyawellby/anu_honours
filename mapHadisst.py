"""
File to plot monthly data from the trimmed 105 year HadISST dataset

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 6 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

from matplotlib import cm, pyplot as plt
import pylab
import Image
from mpl_toolkits.basemap import Basemap

from hadISST_prepare import *

#Import the base map
m = Basemap(projection='cyl', resolution='c',\
    llcrnrlat=-80,urcrnrlat=80,\
    llcrnrlon=0,urcrnrlon=179)

data = hadisstData
data = n.Dataset('HadISST_sst.nc','r')

lat = data.variables['latitude'][:]
lat_units = data.variables['latitude'].units
lon = data.variables['longitude'][:]
lon_units = data.variables['longitude'].units
#Change this time period accordingly.  Currently shows June 1900.
var_time = hadisstData[0,:,:]
var_units = data.variables['sst'].units
data.close()

lonall,latall = np.meshgrid(lon,lat)
x,y = m(lonall,latall)

cs = m.pcolor(x,y,var_time,vmin=-10,vmax=40)
cbar = m.colorbar(cs, location='right', pad="10%")
cbarLabel = "%s %s" %("Degrees",var_units)
cbar.set_label(cbarLabel)

plt.show()
