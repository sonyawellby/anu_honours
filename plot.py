"""
Routines to plot HadISST, ACCESS and AWAP datasets. 

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 18 August 2015.
"""

import netCDF4 as n
import numpy as np

from matplotlib import cm, pyplot as plt
import pylab
import glob
import matplotlib.image as mpimg
from mpl_toolkits.basemap import Basemap, maskoceans

from maps_sub import m, saveFig, gridWhole, gridLabels

from cwd import *
cwdInFunction()

"""
Import the data to be plotted:
"""

from awap_prepare import latitude,longitude,awap_lon_units,awap_lat_units
from access_prepare_pr import latACCESS, lonACCESS, latACCESS_units, \
     latACCESS_tr, lonACCESS_tr, lonACCESS_units
from hadisst_prepare import latHad, lonHad, latHad_units, lonHad_units

#Note that access_prepare_pr.py may be changed to raw_input to allow for comparison of
#datasets of interest

#Note that access_prepare_ts.py may be changed to raw_input to allow for
#comparison of datasets of interest

def vmax(dataset):
    """
    A function to define the maximum value of data to be displayed on
    the plot, where 'vmax' = 3 standard deviations above the dataset's
    mean.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as imported from
    access_prepare_ts, hadisst_prepare, awap_prepare, access_prepare_pr
    or access_trimmed.
    """
    mean = np.mean(dataset)
    sd = np.std(dataset)
    vmax = mean + 2.0*sd
    return vmax

def mapAWAP(dataset):
    """
    A function to call variables needed to plot AWAP data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as
            defined in 'awap_prepare.py'.
    """
    dict1 = {}
    dict1['lat'] = latitude
    dict1['lon'] = longitude
    dict1['lat_units'] = awap_lat_units
    dict1['lon_units'] = awap_lon_units
    dict1['var_units'] = "Precipitation (mm/day)"
    dict1['vmin'] = 0.0 # mm/day
    dict1['vmax'] = vmax(dataset) # mm/day.
    return dict1

def mapACCESSpr(dataset):
    """
    A function to call variables needed to plot ACCESS precipitation
    data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as
            defined in 'access_prepare.py'.
    """
    dict2 = {}
    dict2['lat'] = latACCESS
    dict2['lon'] = lonACCESS
    dict2['lat_units'] = latACCESS_units
    dict2['lon_units'] = lonACCESS_units
    dict2['var_units'] = "Precipitation (mm/day)"
    dict2['vmin'] = 0.0 # mm/day
    dict2['vmax'] = vmax(dataset) # mm/day.
    return dict2

def mapACCESSpr_tr(dataset):
    """
    A function to call variables needed to plot trimmed ACCESS
    precipitation data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as
            defined in 'access_prepare.py'.
    """
    dict3 = {}
    dict3['lat'] = latACCESS_tr
    dict3['lon'] = lonACCESS_tr
    dict3['lat_units'] = latACCESS_units
    dict3['lon_units'] = lonACCESS_units
    dict3['var_units'] = 'Precipitation (mm/day)'
    dict3['vmin'] = 0.0 # deg Celsius
    dict3['vmax'] = vmax(dataset) # deg Celsius
    return dict3

def mapACCESSts(dataset):
    """
    A function to call variables needed to plot ACCESS SST data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as
            defined in 'access_prepare.py'.
    """
    dict4 = {}
    dict4['lat'] = latACCESS
    dict4['lon'] = lonACCESS
    dict4['lat_units'] = latACCESS_units
    dict4['lon_units'] = lonACCESS_units
    dict4['var_units'] = 'Temperature ($^\circ$C)'
    dict4['vmin'] = -2.0 # deg Celsius
    dict4['vmax'] = vmax(dataset) # deg Celsius
    return dict4

def mapHadisst(dataset):
    """
    A function to call variables needed to plot HadISST SST data.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as
            defined in 'access_prepare.py'.
    """
    dict5 = {}
    dict5['lat'] = latHad
    dict5['lon'] = lonHad
    dict5['lat_units'] = latHad_units
    dict5['lon_units'] = lonHad_units
    dict5['var_units'] = 'Temperature ($^\circ$C)'
    dict5['vmin'] = -2.0 # deg Celsius
    dict5['vmax'] = vmax(dataset) # deg Celsius
    return dict5

def plot(var_time,Dict,labels=False,grid=False,oceans=False,cbar=True):
    """
    A function to plot and display a basic plot of ACCESS,
    AWAP, or HadISST datasets.

    Parameters:
    -----------
    var_time : The variable to be plotted.  Use the imported
            data from access_prepare_ts, hadisst_prepare,
            awap_prepare, access_prepare_pr or access_trimmed.
    Dict :  a dictionary defining various
            variables needed for the dataset to be plotted.
            The dictionaries are defined above in the
            mapAWAP(), mapACCESSpr(), mapACCESSts(), mapACCESSpr_tr() and
            mapHadisst() functions.
    labels : (default = False)
            Adds axis labels for longitude/latitude if "True".
    grid : (default = False)
            If set to "True", the a grid is superimposed over
            the map at the 1.25 (lat) by 1.875 (lon) degree
            resolution.  If set to "False", only the latitudes/
            longitudes that show the dimensions of the box are
            plotted.
            If set to "Simple", only the boundary lat/lon
            values for the map are shown (no grid-lines).
    oceans : (default = False)
            If set to "True", ocean regions remain unmaskeded
            and are plotted; if set to "False", the oceans are
            not plotted.
    cbar : (default = True)
            Plots a colour-bar if set to "True".
    """
    m
    
    [lonall,latall] = np.meshgrid((Dict['lon']),(Dict['lat']))
    x,y = m(lonall,latall)

    #Check to see if gridLabels correct; check wholeGrid spacing if using
    if grid == False:
        pass
    elif grid == 'Simple':
        gridLabels(-43.75,-11.25,31.25,114.375,153.75,37.5)
    else:
        gridWhole(-43.75,-11.25,1.25,114.375,153.75,1.875)
        gridLabels(-43.75,-11.25,31.25,114.375,153.75,37.5)

    if labels == True:
        plt.xlabel("Longitude ($^\circ$E)",labelpad=25)
        plt.ylabel("Latitude ($^\circ$S)",labelpad=25)
        
    else:
        pass

    if oceans == False:
        var_time_land = maskoceans(lonall,latall,var_time)
        cs = m.pcolor(x,y,var_time_land,vmin=Dict['vmin'],vmax=Dict['vmax'],cmap=plt.cm.get_cmap('RdBu'))
    else:
        cs = m.pcolor(x,y,var_time,vmin=Dict['vmin'],vmax=Dict['vmax'])

    if cbar == True:
        cbar = m.colorbar(cs, location='right', pad="10%")
        cbarLabel = "%s" %(Dict['var_units'])
        cbar.set_label(cbarLabel)
    else:
        pass

    return plt

#def plot(dict, compdict) - add a comparison dictionary if necessary
#When making comparisions, remember vmax - especially if plotting afterwards

def multi(directory,title=''):
    """
    A file to plot nine pre-plotted images in a three-by-three image.
    Parameters:
    -----------
    directory : The directory (str; with wildcards and extension) of the
                images to be plotted.
                E.g. 'my_coding_routines/images/test/*.png'
    title : (default = '')
            The title of the graph (str).  By default, none is added.
    """
    fig = plt.figure(facecolor='white') # removing 'facecolor' sets it to 'None'

    mainTitle = title
    plt.suptitle(mainTitle,fontsize = 18)
    
    fileList = glob.glob(directory)
    
    for i in range(10):
        a = fig.add_subplot(3,3,i)
        img = mpimg.imread(fileList[i-1])
        imgplot = plt.imshow(img)
        plt.tick_params(
            axis='both',        # Apply to both x- and y-axes
            which='both',       # Turns major and minor ticks off
            left = 'off',       # Turns axis ticks off
            right = 'off',
            bottom='off',      
            top='off',         
            labelbottom='off',  # Turns axis labels off
            labelleft='off')
        if i == 1:
            a.set_title('ENSO Positive')
            a.set_ylabel('IPO Positive',fontsize=15)
        elif i == 2:
            a.set_title('ENSO Neutral')
        elif i == 3:
            a.set_title('ENSO Negative')
        elif i == 4:
            a.set_ylabel('IPO Neutral',fontsize=15)
        elif i == 7:
            a.set_ylabel('IPO Negative',fontsize=15)
        else:
            pass
    """
    #Code for colorbar - but will only go between 0 and 1.
    #If include, will need to add "units" to function arguments.
    #Will also need to make sure it is the right colour scheme.
    pylab.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    cax = pylab.axes([0.85, 0.1, 0.04, 0.8])
    pylab.colorbar(cax=cax,ticks=[0, 0.5, 1.5],label=units)
    """
    plt.show(fig)
    

"""
#Make sure to check vmax!

#Plot AWAP annual data
from awap_prepare import awap_Annual
dict1 = mapAWAP(awap_Annual)
plot(awap_Annual[0,0],dict1)
plt.show(plot)

#Plot ACCESS annual pr data
from access_prepare_pr import pr_Annual
dict2 = mapACCESSpr(pr_Annual)
plot(pr_Annual[0,0],dict2)
plt.show(plot)

#Plot ACCESS annual pr data, trimmed
from access_trimmed import trim_Annual
dict3 = mapACCESSpr_tr(trim_Annual)
plot(trim_Annual[0,0],dict3)
plt.show(plot)

#Plot ACCESS annual sst data
from access_prepare_ts import ts_Annual
dict4 = mapACCESSts(ts_Annual)
plot(ts_Annual[0,0],dict4,oceans=True)
plt.show(plot)

#Plot HadISST April data
from hadisst_prepare import sst_April
dict5 = mapHadisst(sst_April)
plot(sst_April[0],dict5,oceans=True)
plt.show(plot)
"""

