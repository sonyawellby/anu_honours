"""
File to plot monthly data from the trimmed 105 year HadISST dataset

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 7 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

from matplotlib import cm, pyplot as plt
import pylab
import Image
from mpl_toolkits.basemap import Basemap

from hadisst_prepare import *

#Import the base map
m = Basemap(projection='cyl', resolution='c',\
    llcrnrlat=-80,urcrnrlat=80,\
    llcrnrlon=0,urcrnrlon=179)

#Import SST data from hadisst_prepare
sst_Annual
sst_June
sst_July
sst_August
sst_September
sst_October
sst_November
sst_December
sst_January
sst_February
sst_March
sst_April
sst_May
sst_JJA
sst_SON
sst_DJF
sst_MAM

data = n.Dataset('HadISST_sst.nc','r')
#data.variables['sst'][365][90][180] (time,latitude,longitude)
#shows June 1900 at lat [90] (-0.5 N) and lon 180 (0.5 E)

lat = data.variables['latitude'][:]
lat_units = data.variables['latitude'].units
lon = data.variables['longitude'][:]
lon_units = data.variables['longitude'].units
#Change this time period accordingly.  Currently shows December 1900-1901.
#var_time = data.variables['sst'][0,0,:,:] #This uses the original hadISST dataset - time not trimmed
#var_time = sst_Annual[0,0,:,:]
#var_time = sst_June[0,:,:]
var_time = sst_DJF[0,:,:]
var_units = data.variables['sst'].units
data.close()

lonall,latall = np.meshgrid(lon,lat)
x,y = m(lonall,latall)

cs = m.pcolor(x,y,var_time,vmin=-10,vmax=40)
cbar = m.colorbar(cs, location='right', pad="10%")
cbarLabel = "%s %s" %("Degrees",var_units)
cbar.set_label(cbarLabel)

plt.show()