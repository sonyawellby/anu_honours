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
import StringIO
from mpl_toolkits.basemap import Basemap, maskoceans

import glob

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

def gridWhole(a,b,c,d,e,f):
    """
    A function to superimpose a grid over a map at
    the 1.25 (lat) by 1.875 (lon) degree resolution.

    Parameters:
    -----------
    a = latitudinal value in the lower-left corner
    b = latitudinal value in the upper-left corner
    c = latitudinal step-size
    d = longitudinal value in the lower-left corner
    e = longitudinal value in the lower-right corner
    f = longitudinal step-size 
    """
    m.drawparallels(np.arange(a,b,c),labels=[False,False,False,False])
    m.drawmeridians(np.arange(d,e,f),labels=[False,False,False,False])
    gridLabels(a,b,c,d,e,f)

def gridLabels(a,b,c,d,e,f):
    """
    A function to show the longitudinal/latitudinal
    dimensions of the map plotted.

    Parameters:
    -----------
    a = latitudinal value in the lower-left corner
    b = latitudinal value in the upper-left corner
    c = latitudinal step-size
    d = longitudinal value in the lower-left corner
    e = longitudinal value in the lower-right corner
    f = longitudinal step-size 
    """
    m.drawparallels(np.arange(a,b,c),labels=[True,False,True,True],linewidth=0.0)
    m.drawmeridians(np.arange(d,e,f),labels=[True,True,False,True],linewidth=0.0)

def saveFig(plot,title,filename,ext='png'):
    """
    A function to save figures produced.
    Parameters
    ----------
    plot : The figure to save.
    ext : string (default = 'png')
        The file extension.  An alternate file extension can also be entered via
        raw_input.
    """
    if title == "":
        pass
    else:
        plt.title(title,fontsize=18)
    fileName = "%s%s.%s" %("my_coding_routines/images/",filename,ext)
    plt.savefig(fileName)

    plt.close()


m = mapBase()

def multi():
    """
    Docstring
    """

    fig = plt.figure(1)
    #mainTitle = raw_input("Enter the main title: ")
    mainTitle = "Hooray"
    plt.suptitle(mainTitle,fontsize = 18)

    fileList = glob.glob('my_coding_routines/images/test/*.png')
    print fileList

    values = []
    num = 1
    for i in fileList:
        values.append(num)
        num += 1

    dictionary = dict(zip(values,fileList))
        
    for key in fileList:
        #im = Image.open(dictionary[key])
        im = Image.open(StringIO.StringIO(buffer))
        StringIO.StringIO().seek(0)
        fig.add_subplot(3,3,im)
    
    plt.show(fig)
    #plt.savefig('my_coding_routines/images/title.png') #Can also use .pdf


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
