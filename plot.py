"""
Routines to plot HadISST, ACCESS and AWAP datasets. 

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 9 November 2015.
"""

import netCDF4 as n
import numpy as np
import numpy.ma

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
    the plot, where 'vmax' = 3 (2?) standard deviations above the dataset's
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

def vmax_masked(dataset):
    """
    A function to define the maximum value of data to be displayed on
    the plot, where 'vmax' = 0.5 standard deviations above the dataset's
    mean.  Handles masked arrays.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as imported from
    access_prepare_ts, hadisst_prepare, awap_prepare, access_prepare_pr
    or access_trimmed.
    """
    mean = np.ma.mean(dataset)
    sd = np.ma.std(dataset)
    vmax = mean + 0.5*sd
    return vmax

def vmin_masked(dataset):
    """
    A function to define the maximum value of data to be displayed on
    the plot, where 'vmax' = 0.5 standard deviations above the dataset's
    mean.  Handles masked arrays.

    Parameters:
    -----------
    dataset : the name of the dataset to be plotted, as imported from
    access_prepare_ts, hadisst_prepare, awap_prepare, access_prepare_pr
    or access_trimmed.
    """
    mean = np.ma.mean(dataset)
    sd = np.ma.std(dataset)
    vmin = mean - 0.5*sd
    return vmin


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

def mapCorrStratified(correlation_array):
    """
    A function to call variables needed to plot correlations between
    one index and stratified (according to a second index) precipitation data.
    """
    dict11 = {}
    dict11['lat'] = latACCESS_tr
    dict11['lon'] = lonACCESS_tr
    dict11['lat_units'] = latACCESS_units
    dict11['lon_units'] = lonACCESS_units
    dict11['var_units'] = 'Correlation coefficient'
    dict11['vmin'] = vmin_masked(correlation_array) #Correlation coefficient
    dict11['vmax'] = vmax_masked(correlation_array) #Correlation coefficient
    return dict11

def mapAWAPinterpolated(dataset):
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
    dict1['vmax'] = 3.0 # mm/day.
    return dict1

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
        cbar = m.colorbar(cs, location='right', pad="1%")
        cbarLabel = "%s" %(Dict['var_units'])
        cbar.set_label(cbarLabel)
    else:
        pass

    return plt


def plotAWAP_original(var_time,Dict):
    """
    Plot uninterpolated AWAP data.
    """
    m

    [lonall,latall] = np.meshgrid((Dict['lon']),(Dict['lat']))
    x,y = m(lonall,latall)

    cs = m.pcolor(x,y,var_time,vmin=Dict['vmin'],vmax=Dict['vmax'])

    cbar = m.colorbar(cs, location='right', pad="1%")
    cbarLabel = "%s" %(Dict['var_units'])
    cbar.set_label(cbarLabel)

    return plt

def plotKoppen(Dict):
    """
    Plot a map of the Koppen climate zones used in the correlation analysis.
    """
    m

    empty = np.zeros((27,22))

    empty[23:,14:] = 1.0 #equatorial
    empty[19:23,14:] = 2.0 #tropical
    empty[10:19,16:] = 3.0 #subtropical
    empty[9:17,14:15] = 4.0 #desert

    empty[17:19,14:15] = 5.0#grass1
    empty[17:19,15:16] = 5.0 #grass2
    empty[4:17,15:16] = 5.0 #grass3
    empty[4:9,14:15] = 5.0 #grass4

    empty[4:10,16:] = 6.0 #temperate1
    empty[:4,14:20] = 6.0 #temperate2

    [lonall,latall] = np.meshgrid((Dict['lon']),(Dict['lat']))
    x,y = m(lonall,latall)

    eastern_Aus = maskoceans(lonall,latall,empty)
    eastern_Aus = np.ma.masked_where(eastern_Aus == 0.0,eastern_Aus)
    cs = m.pcolor(x,y,eastern_Aus)
    plt.title("Climate zones in eastern Australia")
    plt.show()
    return eastern_Aus
    

def plotBasic(title,labels=True,grid=True,):
    """
    A function to plot and display a basic plot of ACCESS,
    AWAP, or HadISST datasets.

    Parameters:
    -----------
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
    title : enter a string
    """
    m
    

    if grid == True:
        gridWhole(-43.75,-8.75,1.25,114.375,155.625,1.875)
        gridLabels(-43.75,-8.75,2.5,114.375,155.625,7.5)
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

    plt.title(title)

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
#Plot a map of the Koppen climate zones used in this study
from awap_prepare import awap_Annual
Dict = mapAWAP(awap_Annual)
plotKoppen(Dict)

#Plot common grid (make sure to change base map in "maps_sub.py"
gridded_plot = plotBasic(title='Common grid for analysing ACCESS1.3 and AWAP data',labels=True,grid=True)
plt.show(gridded_plot)

#Plot interpolated AWAP data (1900)
from awap_prepare import year1900
dict1 = mapAWAPinterpolated(year1900)
plot(year1900[:,:],dict1,oceans=True)
plt.show(plot)
"""
