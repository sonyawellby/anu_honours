"""
Routines to plot maps of Australia with Matplotlib library.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 7 July 2015. 
"""

#Check current working directory
from metadata import cwd

import netCDF4 as n
import numpy as np

from matplotlib import cm, pyplot as plt
import pylab
import Image
from mpl_toolkits.basemap import Basemap, maskoceans

def mapsExplan():
    """A function to plot maps for explanatory material"""
    m = Basemap(projection='cyl', resolution='c',\
                llcrnrlat=-50,urcrnrlat=0,\
                llcrnrlon=110,urcrnrlon=160)
    m.drawcoastlines()
    
    m.drawstates()
    states_lon = [145.5,142,146.5,144,144,133,133,122]
    states_lat = [-42.5,-37,-35,-32,-22,-30,-23,-25]
    x,y = m(states_lon, states_lat)
    m.plot(x, y, 'bo',markersize=0)
    labels = ['Tas.','Vic.','A.C.T.','N.S.W.','Qld','S.A.','N.T.','W.A.']
    for label, xpt, ypt in zip(labels,x,y):
        plt.text(xpt,ypt,label)

    m.fillcontinents(color='0.75',lake_color='white')
    m.drawmapboundary(fill_color='white')
    # Change these values to fit what gridded to
    #m.drawparallels(np.arange(-50.,1.,1.25),labels=[True,False,True,True])
    #m.drawmeridians(np.arange(110.,161.,1.875),labels=[True,True,False,True])
    # May need to remove padding
    plt.xlabel("Longitude (degrees east)",labelpad=25)
    plt.ylabel("Latitude (degrees south)",labelpad=35)
    plt.title("Australia")

    plt.show()
    if raw_input('Do you want to save this image? y/n ') == 'y':
        a = raw_input('Enter name of file: ')
        if raw_input('Save as .png? y/n: ') == 'y':
            plt.savefig('my_coding_routines/images/'+a+'.png')
        else:
            print('Will be saved as a .pdf')
            plt.savefig('my_coding_routines/images/'+a+'.pdf')
    else:
        print('Image will not be saved.')
"""
"""
#Maps for main data analysis
"""
data = n.Dataset('ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','r')
pr_time = data.variables['pr'][1700,:,:]
pr_units = data.variables['pr'].units
lat = data.variables['lat'][:]
lat_units = data.variables['lat'].units
lon = data.variables['lon'][:]
lon_units = data.variables['lon'].units
data.close()

#set basemap according to regridding
m = Basemap(projection='cyl', resolution='c',\
            llcrnrlat=-50,urcrnrlat=0,\
            llcrnrlon=110,urcrnrlon=160)
m.drawcoastlines()
#m.drawstates()

[lonall,latall] = np.meshgrid(lon,lat)
x,y = m(lonall,latall)
pr_time_land = maskoceans(lonall,latall,pr_time)

cs = m.pcolor(x,y,pr_time_land)
plt.title('Title here (units)')
m.drawparallels(np.arange(-50.,1.,10),labels=[True,False,True,True], linewidth=0.0)
m.drawmeridians(np.arange(110.,161.,10),labels=[True,True,False,True],linewidth=0.0)
plt.xlabel("Longitude (degrees east)",labelpad=25)
plt.ylabel("Latitude (degrees south)",labelpad=35)

cbar = m.colorbar(cs, location='right', pad="10%")
cbar.set_label('Precipitation ('+ pr_units + ')')

plt.show()
#plt.savefig('my_coding_routines/title.png') #Can also use .pdf

"""
#Combine multiple (nine) maps into one
"""

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
