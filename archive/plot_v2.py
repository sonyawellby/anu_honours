"""
Routines to plot HadISST, ACCESS and AWAP datasets. 

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 17 August 2015.
"""

import netCDF4 as n
import numpy as np

from matplotlib import cm, pyplot as plt
import pylab
from mpl_toolkits.basemap import Basemap, maskoceans
from maps_sub import m, saveFig

from cwd import *
cwdInFunction()

"""
Import the data to be plotted:
"""

from awap_prepare import latitude,longitude,awap_lon_units,awap_lat_units
from access_prepare_pr import latACCESS, lonACCESS, latACCESS_units, \
     latACCESS_tr, lonACCESS_tr, lonACCESS_units
from hadisst_prepare import latHad, lonHad, latHad_units, lonHad_units

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
     trim_DJF,trim_MAM

#Note that access_prepare_ts.py may be changed to raw_input to allow for
#comparison of datasets of interest
from access_prepare_ts import ts_Annual, ts_June,ts_July,ts_August, \
     ts_September,ts_October,ts_November,ts_December,ts_January,\
     ts_February,ts_March,ts_April,ts_May,ts_JJA,ts_SON,ts_DJF,ts_MAM

from hadisst_prepare import sst_Annual, sst_June,sst_July,sst_August, \
     sst_September,sst_October,sst_November,sst_December,sst_January,\
     sst_February,sst_March,sst_April,sst_May,sst_JJA,sst_SON,sst_DJF,sst_MAM
"""

def vmax(dataset):
    """
    A function to define the maximum value of data to be displayed on
    the plot, where 'vmax' = 3 standard deviations above the dataset's
    mean.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as imported above.
    """
    mean = np.mean(dataset)
    sd = np.std(dataset)
    vmax = mean + 3.0*sd
    return vmax

def mapAWAP(dataset):
    """
    A function to call variables needed to plot AWAP data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as imported above,
            and as defined in 'awap_prepare.py'.
    """
    dict1 = {}
    dict1['lat'] = latitude
    dict1['lon'] = longitude
    dict1['lat_units'] = awap_lat_units
    dict1['lon_units'] = awap_lon_units
    dict1['var_units'] = "mm/day"
    dict1['vmin'] = 0.0 # mm/day
    dict1['vmax'] = vmax # mm/day.
    return dict1

def mapACCESSpr(dataset):
    """
    A function to call variables needed to plot ACCESS precipitation
    data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as imported above,
            and as defined in 'access_prepare.py'.
    """
    dict2 = {}
    dict2['lat'] = latACCESS
    dict2['lon'] = lonACCESS
    dict2['lat_units'] = latACCESS_units
    dict2['lon_units'] = lonACCESS_units
    dict2['var_units'] = "mm/day"
    dict2['vmin'] = 0.0 # mm/day
    dict2['vmax'] = vmax # mm/day.
    return dict2

def mapACCESSpr_tr(dataset):
    """
    A function to call variables needed to plot trimmed ACCESS
    precipitation data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as imported above,
            and as defined in 'access_prepare.py'.
    """
    dict3 = {}
    dict3['lat'] = latACCESS_tr
    dict3['lon'] = lonACCESS_tr
    dict3['lat_units'] = latACCESS_units
    dict3['lon_units'] = lonACCESS_units
    dict3['var_units'] = 'mm/day'
    dict3['vmin'] = 0.0 # deg Celsius
    dict3['vmax'] = vmax # deg Celsius
    return dict3

def mapACCESSts(dataset):
    """
    A function to call variables needed to plot ACCESS SST data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as imported above,
            and as defined in 'access_prepare.py'.
    """
    dict4 = {}
    dict4['lat'] = latACCESS
    dict4['lon'] = lonACCESS
    dict4['lat_units'] = latACCESS_units
    dict4['lon_units'] = lonACCESS_units
    dict4['var_units'] = '$^\circ$C'
    dict4['vmin'] = -2.0 # deg Celsius
    dict4['vmax'] = vmax # deg Celsius
    return dict4

def mapHadisst(dataset):
    """
    A function to call variables needed to plot HadISST SST data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as imported above,
            and as defined in 'access_prepare.py'.
    """
    dict5 = {}
    dict5['lat'] = latHad
    dict5['lon'] = lonHad
    dict5['lat_units'] = latHad_units
    dict5['lon_units'] = lonHad_units
    dict5['var_units'] = '$^\circ$C'
    dict5['vmin'] = -2.0 # deg Celsius
    dict5['vmax'] = vmax # deg Celsius
    return dict5


#def testPlot(dic={}, compdic={})
#def plot(Dict={}):

def plot(var_time,Dict): #grid=False,labels=True,save=False,states=False):
    """
    A function to plot and display a basic plot of ACCESS,
    AWAP, or HadISST datasets.

    Parameters:
    -----------
    var_time: The variable to be plotted.  Use the imported
            data above.
    Dict :  a dictionary defining various
            variables needed for the dataset to be plotted.
            The dictionaries are defined above in the
            mapAWAP(), mapACCESSpr(), mapACCESSts(), and
            mapHadisst() functions.
    """
    m
    
    [lonall,latall] = np.meshgrid((Dict['lon']),(Dict['lat']))
    x,y = m(lonall,latall)

    cs = m.pcolor(x,y,var_time,vmin=Dict['vmin'],vmax=Dict['vmax'])
    cbarLabel = "%s" %(Dict['var_units']) #not working
    cbar = m.colorbar(cs, location='right', pad="10%")

    plt.show()

def save():

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

"""
#Plot AWAP annual data
vmax = vmax(awap_Annual)
dict1 = mapAWAP(awap_Annual)
plot(awap_Annual[0,0],mapAWAP(dict1))
"""
#Plot ACCESS annual pr data
vmax = vmax(pr_Annual)
dict2 = mapACCESSpr(pr_Annual)
plot(pr_Annual[0,0],mapACCESSpr(dict2))
"""
#Plot ACCESS annual pr data, trimmed
vmax = vmax(trim_Annual)
dict3 = mapACCESSpr_tr(trim_Annual)
plot(trim_Annual[0,0],mapACCESSpr_tr(dict3))

#Plot ACCESS annual sst data
vmax = vmax(ts_Annual)
dict4 = mapACCESSts(ts_Annual)
plot(ts_Annual[0,0],mapACCESSts(dict4))

#Plot HadISST annual data
vmax = vmax(sst_Annual)
dict5 = mapACCESSpr(sst_Annual)
plot(sst_Annual[0,0],mapHadisst(dict5))
"""

