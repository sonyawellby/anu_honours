"""
Routines to plot HadISST, ACCESS and AWAP datasets. 

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 14 August 2015.
"""

import netCDF4 as n
import numpy as np

from matplotlib import cm, pyplot as plt
import pylab
from mpl_toolkits.basemap import Basemap, maskoceans
from maps_sub import m, saveFig

from cwd import *
cwdInFunction()

from awap_prepare import latitude,longitude,awap_units,awap_lon_units,awap_lat_units

from awap_prepare import awap_Annual, awap_June,awap_July,awap_August, \
     awap_September,awap_October,awap_November,awap_December,awap_January,\
     awap_February,awap_March,awap_April,awap_May,awap_JJA,awap_SON,\
     awap_DJF,awap_MAM

#Note that access_prepare_pr.py may be changed to raw_input to allow for comparison of
#datasets of interest
from access_prepare_pr import pr_Annual, pr_June,pr_July,pr_August, \
     pr_September,pr_October,pr_November,pr_December,pr_January,\
     pr_February,pr_March,pr_April,pr_May,pr_JJA,pr_SON,pr_DJF,pr_MAM

"""
from access_trimmed import trim_Annual, trim_June,trim_July,trim_August, \
     trim_September,trim_October,trim_November,trim_December,trim_January,\
     trim_February,trim_March,trim_April,trim_May,trim_JJA,trim_SON,\
     trim_DJF,pr_MAM
"""

#Note that access_prepare_ts.py may be changed to raw_input to allow for
#comparison of datasets of interest
from access_prepare_ts import ts_Annual, ts_June,ts_July,ts_August, \
     ts_September,ts_October,ts_November,ts_December,ts_January,\
     ts_February,ts_March,ts_April,ts_May,ts_JJA,ts_SON,ts_DJF,ts_MAM
"""
from hadisst_prepare import sst_Annual, sst_June,sst_July,sst_August, \
     sst_September,sst_October,sst_November,sst_December,sst_January,\
     sst_February,sst_March,sst_April,sst_May,sst_JJA,sst_SON,sst_DJF,sst_MAM
"""


"""
A function that sets up the map background for the Australian region.
"""

def mapAWAP():
    """
    A function to plot AWAP data
    """
    lat = latitude
    lon = longitude
    lat_units = awap_lat_units
    lon_units = awap_lon_units
    var_units = awap_units
    #Change this according to what want

    data = n.Dataset('AWAP_1900-2014_monthly_precip_swACCESSgrid_v4.nc','a')
    var_time = data.variables['AWAP_precipitation'][104,:,:]
    #var_time = awap_Annual[104,:,:]

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
[lonall,latall] = np.meshgrid(lon,lat)
    x,y = m(lonall,latall)
    var_time_land = maskoceans(lonall,latall,var_time)

    cs = m.pcolor(x,y,var_time_land,vmin=0) #vmax = (for colourbar upper limit)
    cbar = m.colorbar(cs, location='right', pad="10%")
    cbarLabel = "%s %s%s%s" %(units_name,"(",var_units,")")
    cbar.set_label(cbarLabel)

    if raw_input("Do you want to save this image? y/n ") == 'y':
        mapBasic(grid=True,save=True)
    else:
        mapBasic(title=False,save=False)
"""
