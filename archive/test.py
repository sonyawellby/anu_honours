"""
A set of routines to prepare ACCESS sea surface temperature file for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 4 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

data = n.Dataset('ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','r')


"""
Limit the dataset to the area of interest (-43.125 to -10.625 deg N; 114.375 to 151.874 deg E)


data.variables['lat'] = data.variables['lat'][37:65]
print len(data.variables['lat'])
data.variables['lon'] = data.variables['lon'][61:82]
print len(data.variables['lon'])
"""

"""
Change the 'pr' variable from kg/m^2/s to mm/month so it is
compatibile with the AWAP dataset (which is, in its original form, measured in
m/day, and has X days in each month).  Note that the AWAP dataset has also
been modified so it, too, reports mm/month values.

NB: prc_monthly[1871][160][40] is: timestep, latitude, longitude
"""

prc_monthly = [data.variables['pr'][i]*data.variables['time'][i] for i in range(0,len(data.variables['time']))]
data.variables['pr'] = prc_monthly
    
timeData = data.variables['pr'][605:1864]


"""
Monthly data for Jun-May years (June 1900 to May 2004) - 104 year analysis.

e.g. months[month][year][longitude][latitude]
e.g. months[0][0][0][0] is June for 1900 at latitude -90 N and longitude 0 E
"""

Jun = timeData[0:1248:12]
Jul = timeData[1:1248:12]
Aug = timeData[2:1249:12]
Sep = timeData[3:1250:12]
Oct = timeData[4:1251:12]
Nov = timeData[5:1252:12]
Dec = timeData[6:1253:12]
Jan = timeData[7:1254:12]
Feb = timeData[8:1255:12]
Mar = timeData[9:1256:12]
Apr = timeData[10:1257:12]
May = timeData[11:1258:12]

months = np.array([Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May])