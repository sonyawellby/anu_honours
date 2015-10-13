"""
Routines to plot HadISST, ACCESS and AWAP datasets. 

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 12 October 2015.
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
Import the metadata about the data to be plotted:
"""

from awap_prepare import latitude,longitude,awap_lon_units,awap_lat_units
from access_prepare_pr import latACCESS, lonACCESS, latACCESS_units, \
     latACCESS_tr, lonACCESS_tr, lonACCESS_units
from hadisst_prepare import latHad, lonHad, latHad_units, lonHad_units

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
    dict3['vmin'] = 0.0 # mm/day
    dict3['vmax'] = vmax(dataset) # mm/day
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

def mapCorr():
    """
    A function to call variables needed to plot correlations between index and
    precipitation data.
    """
    dict6 = {}
    dict6['lat'] = latACCESS_tr
    dict6['lon'] = lonACCESS_tr
    dict6['lat_units'] = latACCESS_units
    dict6['lon_units'] = lonACCESS_units
    dict6['var_units'] = 'Correlation coefficient'
    dict6['vmin'] = -1.0 # deg Celsius
    dict6['vmax'] = 1.0 # deg Celsius
    return dict6

def mapComposite(dataset):
    """
    A function to call variables needed to plot AWAP data
    (can also be used for ACCESS data).

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as
            defined in 'awap_prepare.py'.
    """
    dict7 = {}
    dict7['lat'] = latitude
    dict7['lon'] = longitude
    dict7['lat_units'] = awap_lat_units
    dict7['lon_units'] = awap_lon_units
    dict7['var_units'] = "Precipitation (mm/day)"
    dict7['vmin'] = 0.0 # mm/day
    dict7['vmax'] = 10.0 # mm/day.
    return dict7

def mapCompositeAnom(dataset):
    """
    A function to call variables needed to plot rainfall
    anomalies for AWAP data (can also be used for ACCESS data).

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as
            defined in 'awap_prepare.py'.
    """
    dict8 = {}
    dict8['lat'] = latitude
    dict8['lon'] = longitude
    dict8['lat_units'] = awap_lat_units
    dict8['lon_units'] = awap_lon_units
    dict8['var_units'] = "Precipitation anomalies (mm/day)"
    dict8['vmin'] = -3.0 # mm/day
    dict8['vmax'] = 3.0 # mm/day.
    return dict8

def mapDifference(dataset):
    """
    A function to call variables needed to plot rainfall
    differences between phases of indices for AWAP data
    (can also be used for ACCESS data).

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted.
    """
    dict9 = {}
    dict9['lat'] = latitude
    dict9['lon'] = longitude
    dict9['lat_units'] = awap_lat_units
    dict9['lon_units'] = awap_lon_units
    dict9['var_units'] = "Mean precipitation difference (mm/day)"
    dict9['vmin'] = -3.0 # mm/day
    dict9['vmax'] = 3.0 # mm/day.
    return dict9

def mapStandardised(dataset):
    """
    A function to call variables needed to plot rainfall
    differences between phases of indices for AWAP data
    (can also be used for ACCESS data).

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted.
    """
    dict10 = {}
    dict10['lat'] = latitude
    dict10['lon'] = longitude
    dict10['lat_units'] = awap_lat_units
    dict10['lon_units'] = awap_lon_units
    dict10['var_units'] = r'Standardised rainfall ($\sigma$)'
    dict10['vmin'] = -3.0 # standard deviations
    dict10['vmax'] = 3.0 # standard deviations
    return dict10


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

    if grid == True:
        gridWhole(-47.5,-7.5,1.25,112.5,157.5,1.875)
        gridLabels(-47.5,-7.5,2.5,112.5,159.375,7.5)
    elif grid == 'Simple':
        gridLabels(-40.0,0.0,10.0,110.0,160.0,10.0)
    elif grid == 'Ticks':
        gridLabels(-40.0,0.0,10.0,110.0,160.0,10.0)
    else:
        pass

    if labels == True and grid==True:
        plt.xlabel("Longitude ($^\circ$E)",labelpad=25)
        plt.ylabel("Latitude ($^\circ$S)",labelpad=50)
    elif labels == True and not grid==True:
        plt.xlabel("Longitude ($^\circ$E)",labelpad=25)
        plt.ylabel("Latitude ($^\circ$S)",labelpad=30)
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

def multi(directory,nrow,ncol,title=''):
    """
    A file to plot nine pre-plotted images in a three-by-three image.
    Parameters:
    -----------
    directory : The directory (str; with wildcards and extension) of the
                images to be plotted.
                E.g. 'my_coding_routines/images/test/*.png'
    nrow : The number of rows of images in the file.
    ncol : The number of columns of images in the file.
    title : (default = '')
            The title of the graph (str).  By default, none is added.
    """
    fig = plt.figure(facecolor='white') # removing 'facecolor' sets it to 'None'

    mainTitle = title
    plt.suptitle(mainTitle,fontsize = 18)
    
    fileList = sorted(glob.glob(directory))
    
    for i in range(1,(nrow*ncol)+1):
        a = fig.add_subplot(nrow,ncol,i)
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
    return fig


def multiScatter(directory,nrow,ncol,title=''):
    """
    A file to plot nine pre-plotted images in a three-by-three image.
    Parameters:
    -----------
    directory : The directory (str; with wildcards and extension) of the
                images to be plotted.
                E.g. 'my_coding_routines/images/test/*.png'
    nrow : The number of rows of images in the file.
    ncol : The number of columns of images in the file.
    title : (default = '')
            The title of the graph (str).  By default, none is added.
    """
    fig = plt.figure(facecolor='white') # removing 'facecolor' sets it to 'None'

    mainTitle = title
    plt.suptitle(mainTitle,fontsize = 18)
    
    fileList = glob.glob(directory)
    
    for i in range(1,(nrow*ncol)+1):
        a = fig.add_subplot(nrow,ncol,i)
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
            a.set_title('HadISST1')
            a.set_ylabel('TPI',fontsize=10)
            a.set_xlabel('ENSO',fontsize=10)
        elif i == 2:
            a.set_title('ACCESS1.3 R1')
            a.set_ylabel('TPI',fontsize=10)
            a.set_xlabel('ENSO',fontsize=10)
        elif i == 3:
            a.set_title('ACCESS1.3 R2')
            a.set_ylabel('TPI',fontsize=10)
            a.set_xlabel('ENSO',fontsize=10)
        elif i == 4:
            a.set_title('ACCESS1.3 R3')
            a.set_ylabel('TPI',fontsize=10)
            a.set_xlabel('ENSO',fontsize=10)
        else:
            pass

    return fig

def multiGeneral(directory,nrow,ncol,title=''):
    """
    A file to plot nine pre-plotted images in a three-by-three image.
    Parameters:
    -----------
    directory : The directory (str; with wildcards and extension) of the
                images to be plotted.
                E.g. 'my_coding_routines/images/test/*.png'
    nrow : The number of rows of images in the file.
    ncol : The number of columns of images in the file.
    title : (default = '')
            The title of the graph (str).  By default, none is added.
    """
    fig = plt.figure(facecolor='white') # removing 'facecolor' sets it to 'None'

    mainTitle = title
    plt.suptitle(mainTitle,fontsize = 18)
    
    fileList = glob.glob(directory)
    
    for i in range(1,(nrow*ncol)+1):
        a = fig.add_subplot(nrow,ncol,i)
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
    return fig


"""
#Plot AWAP annual data
from awap_prepare import awap_Annual
dict1 = mapAWAP(awap_Annual)
plot(awap_Annual[0,0],dict1)
plt.show(plot)
"""

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

