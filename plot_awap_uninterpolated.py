"""
Program to plot AWAP uninterpolated data.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 7 November 2015.
"""

import netCDF4 as n
import numpy as np
from matplotlib import cm, pyplot as plt

from maps_sub import m
from data import awap

from cwd import *
cwdInFunction()


data = n.Dataset(awap,'a')
awap_dat = data.variables['AWAP_precipitation']
awap_dat1 = np.ma.masked_less_equal(awap_dat,0.0)
awap_data = np.ma.multiply(awap_dat1,1000.0)

def lat():
    """
    A function to replace empty latitudinal values in the resampled
    AWAP dataset with actual latitudinal values.
    """
    start = -43.575
    newlist = []
    for i in range(0,670):
        i = start
        newlist.append(i)
        start += 0.05
    data.variables['latitude'][:] = newlist[:]
    return data.variables['latitude'][:]

def lon():
    """
    A function to replace empty longitudinal values in the resampled
    AWAP dataset with actual longitudinal values.
    """
    start_lon = 112.925
    newlist_lon = []
    for i in range(0,813):
        i = start_lon
        newlist_lon.append(i)
        start_lon += 0.05
    data.variables['longitude'][:] = newlist_lon[:]
    return data.variables['longitude'][:]

dict1 = {}
dict1['var_units'] = "Precipitation (mm/day)"
dict1['lat'] = lat()
dict1['lon'] = lon()
dict1['vmin'] = 0.0 # mm/day
dict1['vmax'] = 3.0 # mm/day


[lonall,latall] = np.meshgrid((dict1['lon']),(dict1['lat']))
x,y = m(lonall,latall)

cs = m.pcolor(x,y,awap_data[0,:,:],vmin=dict1['vmin'],vmax=dict1['vmax'])
cbar = m.colorbar(cs, location='right', pad="1%")
cbarLabel = "%s" %(dict1['var_units'])
cbar.set_label(cbarLabel)
plt.show()
