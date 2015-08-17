"""
Sub-functions to support plot.py

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 17 August 2015. 
"""

import netCDF4 as n
import numpy as np

from matplotlib import cm, pyplot as plt
import pylab
import Image
from mpl_toolkits.basemap import Basemap, maskoceans

from cwd import *

cwdInFunction()

def mapBase():
    """
    A function to plot a map of the Australian region to which
    data can then be added.

    The map region () is slightly larger than the region over which
    data is plotted (-43.75 to -12.5 deg N, 114.375 to 153.75
    deg E).

    """
    m = Basemap(projection='cyl', resolution='c',\
        llcrnrlat=-47.0,urcrnrlat=-7.5,\
        llcrnrlon=112.0,urcrnrlon=156.0)
    m.drawcoastlines()
    return m

def states():
    """
    A function to plot a blank map of Australia with the states
    and their labels.  The function does not show the plot, but
    allows it to be super-imposed on another plot if this function
    is called.
    """
    m.drawstates()
    states_lon = [145.5,142,146.5,144,144,133,133,122]
    states_lat = [-42.5,-37,-35,-32,-22,-30,-23,-25]
    x,y = m(states_lon, states_lat)
    m.plot(x, y, 'bo',markersize=0)
    labels = ['Tas.','Vic.','A.C.T.','N.S.W.','Qld','S.A.','N.T.','W.A.']
    for label, xpt, ypt in zip(labels,x,y):
        plt.text(xpt,ypt,label)
    return plt

def grey():
    """
    A function to fill a map with grey.
    """
    m.fillcontinents(color='0.75',lake_color='white')
    m.drawmapboundary(fill_color='white')
    return plt

def grid(wholeGrid = False):
    """
    Docstring
    """
    if wholeGrid == True:
        # Change these values to fit what gridded to
        # Draw the grid
        m.drawparallels(np.arange(-43.75,-11.25,1.25),labels=[False,False,False,False])
        m.drawmeridians(np.arange(114.375,153.75,1.875),labels=[False,False,False,False])
        # Draw the labels
        m.drawparallels(np.arange(-43.75,-11.25,1.25),labels=[True,False,True,True],linewidth=0.0)
        m.drawmeridians(np.arange(114.375,153.75,7.5),labels=[True,True,False,True],linewidth=0.0)
    else:
        # Change these values to fit what gridded to
        m.drawparallels(np.arange(-43.75,-11.25,31.25),labels=[True,False,True,True],linewidth=0.0)
        m.drawmeridians(np.arange(114.375,153.75,37.5),labels=[True,True,False,True],linewidth=0.0)

def labels():
    """
    Docstring
    """
    plt.xlabel("Longitude (degrees east)",labelpad=25)
    plt.ylabel("Latitude (degrees south)",labelpad=55)

m = mapBase()

#plot = states()
#plt.show(plot)

def mapBasic(states=False,grid=False,labels=True,title=True,save=False):
    """A function to plot basic map of Australian region.

    Parameters:
    ----------
    states : (default = False)
        Plots the states and their names.
    grid : (default = False)
        Plots latitudinal and longitudinal grids at spacing of grid used in
        analysis.
    labels : (default = True)
        Plots axis labels for longitude and latitude.
    title : (default = True)
        Asks user for name of graph title.
    save : (default = False)
        Saves image to 'images' folder by invoking saveFig().  If set to 'None',
        the images is neither displayed nor saved.
    """
    """
    m = Basemap(projection='cyl', resolution='c',\
                llcrnrlat=-50,urcrnrlat=0,\
                llcrnrlon=110,urcrnrlon=160)
    """
                
    m.drawcoastlines()
    if states == True:
        m.drawstates()
        states_lon = [145.5,142,146.5,144,144,133,133,122]
        states_lat = [-42.5,-37,-35,-32,-22,-30,-23,-25]
        x,y = m(states_lon, states_lat)
        m.plot(x, y, 'bo',markersize=0)
        labels = ['Tas.','Vic.','A.C.T.','N.S.W.','Qld','S.A.','N.T.','W.A.']
        for label, xpt, ypt in zip(labels,x,y):
            plt.text(xpt,ypt,label)

        if raw_input('Do you want to fill Australia with grey? y/n ')== 'y':
            m.fillcontinents(color='0.75',lake_color='white')
            m.drawmapboundary(fill_color='white')

    if grid == True:
        if raw_input("Do you want the whole map gridded? y/n ")=='y':
            # Change these values to fit what gridded to
            # Draw the grid
            m.drawparallels(np.arange(-43.75,-11.25,1.25),labels=[False,False,False,False])
            m.drawmeridians(np.arange(114.375,153.75,1.875),labels=[False,False,False,False])
            # Draw the labels
            m.drawparallels(np.arange(-43.75,-11.25,1.25),labels=[True,False,True,True],linewidth=0.0)
            m.drawmeridians(np.arange(114.375,153.75,7.5),labels=[True,True,False,True],linewidth=0.0)
        else:
            # Change these values to fit what gridded to
            m.drawparallels(np.arange(-43.75,-11.25,31.25),labels=[True,False,True,True],linewidth=0.0)
            m.drawmeridians(np.arange(114.375,153.75,37.5),labels=[True,True,False,True],linewidth=0.0)

    if labels == True:
        # May need to remove padding
        plt.xlabel("Longitude (degrees east)",labelpad=25)
        plt.ylabel("Latitude (degrees south)",labelpad=55)

    if save == True and title == True:
        titleName = raw_input("Enter the graph title (don't forget units): ")
        plt.title(titleName,fontsize=18)
        saveFig()
    elif save == 'None':
        pass
    else:
        plt.show()

def saveFig(ext='png'):
    """A function to save figures produced.
    Parameters
    ----------
    ext : string (default = 'png')
        The file extension.  An alternate file extension can also be entered via
        raw_input.
    """
    if raw_input('Save as a .png file? y/n ')== 'y':
        a = raw_input('Enter name of file: ')
        fileName = "%s%s.%s" %("my_coding_routines/images/",a,ext)
        plt.savefig(fileName)
    else:
        ext = raw_input('Enter the file extension (including .): ')
        a = raw_input('Enter name of file: ')
        fileName = "%s%s.%s" %("my_coding_routines/images/",a,ext)
        plt.savefig(fileName)
    plt.close()

def saveMulti():
    """Docstring here"""
    fig = plt.figure(1)
    mainTitle = raw_input("Enter the main title: ")
    plt.suptitle(mainTitle,fontsize = 18)

    num_images = int(raw_input("Enter integer of number of images want to combine: "))
    fileList = {}
    for i in range(1,num_images +1):
        count = 0
        mapMain()
        imgName = raw_input("Enter the filename of the image you have just made: ")
        imageName = "%s%s" %("my_coding_routines/images/",imgName)
        fileList.update({'image%s'%i: imageName})
        count += 1

    for key in fileList:
        for value in key:
            fig.add_subplot(3,1,i)
    print fileList
    #plt.show()
    plt.savefig('my_coding_routines/images/title.png') #Can also use .pdf

    #plt.show()

def saveMult():
    """A function to save multiple (nine) maps in one."""

    fig = plt.figure()
    mainTitle = raw_input("Enter the main title: ")
    plt.suptitle(mainTitle,fontsize = 18)

    num_images = int(raw_input("Enter integer of number of images want to combine: "))
    fileList = {}
    for i in range(1,num_images +1):
        count = 0
        imgName = raw_input("Enter the name of the image you want to add: ")
        imageName = "%s%s" %("my_coding_routines/images/",imgName)
        fileList.update({'image%s'%i: imageName})
        count += 1

    for key in fileList:
        for value in key:
            fig.add_subplot(3,3,i)
        #plt.show()
        plt.savefig('my_coding_routines/title.png') #Can also use .pdf

"""
    fig1 = fig.add_subplot(331)
    fig1.set_title("Title here",fontsize = 14)
    Enter code for first map
    m = Basemap(projection='cyl', resolution='c',\
                llcrnrlat=-50,urcrnrlat=0,\
                llcrnrlon=110,urcrnrlon=160)
    #Repeat as needed

    plt.show()
    #plt.savefig('my_coding_routines/title.png') #Can also use .pdf
"""

def mapMain():
    """A function to plot maps for main data analysis"""
    dataFile = raw_input("Enter the filepath of the data you want to map: ")
    # e.g. ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc
    data = n.Dataset(dataFile,'r')

    units_name = raw_input("What variable is being measured? ")
    if raw_input("Is data ACCESS data? y/n ")=='y':
        lat = data.variables['lat'][:]
        lat_units = data.variables['lat'].units
        lon = data.variables['lon'][:]
        lon_units = data.variables['lon'].units

        if units_name == "Precipitation":
            #change
            var_time = data.variables['pr'][1700,:,:]
            var_units = data.variables['pr'].units
            data.close()
        else:
            #change
            var_time = data.variables['ts'][1700,:,:]
            var_units = data.variables['ts'].units
            data.close()
    else:
        lat = data.variables['latitude'][:]
        lat_units = data.variables['latitude'].units
        lon = data.variables['longitude'][:]
        lon_units = data.variables['longitude'].units

        if raw_input("Is data HadISST data? y/n ")=='y':
            var_time = data.variables['sst'][:]
            var_units = data.variables['sst'].units
            data.close()
        else:
            var_time = data.variables['AWAP_precipitation']
            var_units = data.variables['AWAP_precipitation'].units
            data.close()

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
