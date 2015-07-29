"""
Routines to plot maps of Australia with Matplotlib library.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 29 July 2015. 
"""

import netCDF4 as n
import numpy as np

from matplotlib import cm, pyplot as plt
import pylab
import Image
from mpl_toolkits.basemap import Basemap, maskoceans

from metadata import cwdInFunction

cwdInFunction()

#Import the base map
m = Basemap(projection='cyl', resolution='c',\
    llcrnrlat=-50,urcrnrlat=0,\
    llcrnrlon=110,urcrnrlon=160)


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

        if raw_input('Do you want to fill Australia with grey? y/n ')== 'y' or 'yes' or 'Yes' or 'YES':
            m.fillcontinents(color='0.75',lake_color='white')
            m.drawmapboundary(fill_color='white')

    if grid == True:
        # Change these values to fit what gridded to
        m.drawparallels(np.arange(-50.,1.,1.25),labels=[True,False,True,True],linewidth=0.0)
        m.drawmeridians(np.arange(110.,161.,1.875),labels=[True,True,False,True],linewidth=0.0)

    if labels == True:
        # May need to remove padding
        plt.xlabel("Longitude (degrees east)",labelpad=25)
        plt.ylabel("Latitude (degrees south)",labelpad=35)

    if save == True:
        if title == True:
            titleName = raw_input("Enter the graph title (don't forget units): ")
            plt.title(titleName)
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
    if raw_input('Save as a .png file? y/n ')== 'y' or 'yes' or 'Yes' or 'YES':
        a = raw_input('Enter name of file: ')
        fileName = "%s%s.%s" %("my_coding_routines/images/",a,ext)
        plt.savefig(fileName)
    else:
        ext = raw_input('Enter the file extension (including .): ')
        a = raw_input('Enter name of file: ')
        fileName = "%s%s.%s" %("my_coding_routines/images/",a,ext)
        plt.savefig(fileName)
    plt.close()

"""
def saveMult():
    A function to save multiple (nine) maps in one.

fig = plt.figure()
plt.suptitle("Main title",fontsize = 18)

fig1 = fig.add_subplot(331)
fig1.set_title("Title here",fontsize = 14)
#Enter code for first map
m = Basemap(projection='cyl', resolution='c',\
            llcrnrlat=-50,urcrnrlat=0,\
            llcrnrlon=110,urcrnrlon=160)
#Repeat as needed

plt.show()
#plt.savefig('my_coding_routines/title.png') #Can also use .pdf
"""


def mapMain():
    """A function to plot maps for main data analysis"""
    dataFile = 'ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc'
    data = n.Dataset(dataFile,'r')

    if raw_input("Is data ACCESS data? y/n ")=='y' or 'yes':
        lat = data.variables['lat'][:]
        lat_units = data.variables['lat'].units
        lon = data.variables['lon'][:]
        lon_units = data.variables['lon'].units

        if raw_input("Is data precipitation data? y/n ")=='y' or 'yes':
            #change
            var_time = data.variables['pr'][1700,:,:]
            var_units = data.variables['pr'].units
            data.close()
        else:
            #change
            var_time = data.variables['ts'][1700,:,:]
            var_units = data.variabels['ts'].units
            data.close()
    else:
        lat = data.variables['latitude'][:]
        lat_units = data.variables['latitude'].units
        lon = data.variables['longitude'][:]
        lon_units = data.variables['longitude'].units

        if raw_input("Is data HadISST data? y/n ")=='y' or 'yes':
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

    cs = m.pcolor(x,y,var_time_land)
    cbar = m.colorbar(cs, location='right', pad="10%")
    units_name = raw_input("What variable is being measured? ")
    cbar.set_label("%s ("+ var_units + ")") %units_name

    if raw_input("Do you want to save this image? y/n ")=='y' or 'yes':
        mapBasic(save=True)
    else:
        mapBasic()
