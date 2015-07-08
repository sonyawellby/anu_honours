"""
A routine to split HadISST SST netCDF data into different files according to
(a) year (June-May),(b) season,(c) month.

Written by Sonya Wellby for ENVS4055, 2015.
Last updated 8 July 2015.
"""

#Set working directory
import os
os.chdir("/home/sonya/Documents/")

import netCDF4 as n
import numpy as np

"""
ACCESS SST
"""

f = n.Dataset('HadISST_sst.nc','a')


#Finds time difference between months
time = f.variables['time_bnds']
timeDiff = [time[i]-time[i-1] for i in range(0,len(time))]
timeDiff.pop(0)
timeDiff.append(np.array([ 31.,  31.]))
timeDiffNP = np.array(timeDiff)
"""
months = np.reshape(timeDiffNP,(156,12))

#Create copy of dataset
m = f.variables

#Change units of 'time' variable (from seconds since 01/01/0001 to length (days))
days_time = [m['time'][i]-m['time'][i-1] for i in range(0,len(m['time']))]
days_time.pop(0)
days_time.append(30.5)

#Changes units of 'ts' variable (from deg C/day to deg C/month) so compatibile with AWAP dataset
#Note: prc_monthly[1871][160][40] is: timestep, latitude, longitude
sst_monthly = [m['ts'][i]*m['time'][i] for i in range(0,len(m['time']))]
m['ts'] = sst_monthly

#Monthly data for Jun-May years (June 1900 to May 2004) - 104 year analysis#MONTHLY DATA
#Note: jan[40][40][155] is: timestep, longitude, latitude
#Note: timestep 600 is January 1900
#Call XX_array when performing actual analyses
Jun1 = sst_monthly[605:1853:12]
Jun1_array = np.array(Jun1)

Jul1 = sst_monthly[606:1854:12]
Jul1_array = np.array(Jul1)

Aug1 = sst_monthly[607:1855:12]
Aug1_array = np.array(Aug1)

Sep1 = sst_monthly[608:1856:12]
Sep1_array = np.array(Sep1)

Oct1 = sst_monthly[609:1857:12]
Oct1_array = np.array(Oct1)

Nov1 = sst_monthly[610:1858:12]
Nov_array1 = np.array(Nov1)

Dec1 = sst_monthly[611:1859:12]
Dec1_array = np.array(Dec1)

Jan1 = sst_monthly[612:1860:12]
Jan1_array = np.array(Jan1)

Feb1 = sst_monthly[613:1861:12]
Feb1_array = np.array(Feb1)

Mar1 = sst_monthly[614:1862:12]
Mar1_array = np.array(Mar1)

Apr1 = sst_monthly[615:1863:12]
Apr1_array = np.array(Apr1)

May1 = sst_monthly[616:1864:12]
May1_array = np.array(May1)

#Seasonal data for Jun-May years (June 1900 to May 2004) - 104 year analysis
DJF1_flat = Dec1 + Jan1 + Feb1
DJF1_array = np.array(DJF1_flat)
DJF1 = np.reshape(DJF1_array, (104,3,145,192))

MAM1_flat = Mar1 + Apr1 + May1
MAM1_array = np.array(MAM1_flat)
MAM1 = np.reshape(MAM1_array, (104,3,145,192))

JJA1_flat = Jun1 + Jul1 + Aug1
JJA1_array = np.array(JJA1_flat)
JJA1 = np.reshape(JJA1_array, (104,3,145,192))

SON1_flat = Sep1 + Oct1 + Nov1
SON1_array = np.array(SON1_flat)
SON1 = np.reshape(JJA1_array, (104,3,145,192))

#Annual data for Jun-May years (Jun 1900 to May 2004) - 104 year analysis
annual1_flat = Jun1 + Jul1 + Aug1 + Sep1 + Oct1 + Nov1 + Dec1 + Jan1 + Feb1 + Mar1 + Apr1 + May1
annual1_array = np.array(annual1_flat)
annualJunToMay = np.reshape(annual1_array,(104,12,145,192))
"""
