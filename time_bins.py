"""
A file to split ACCESS netCDF data into different directories according to
(a) year (June-May),(b) season,(c) month.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated June 2015.
"""

#Check current working directory
import os
os.chdir("/home/sonya/Documents/")
print os.getcwd()
#If working directory set up correctly, this file should load
#f = open("my_coding_routines/foo.py","r")

import netCDF4 as n
import numpy as np

f = n.Dataset('ACCESS_data/prc_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','a')

#Checks span of entire dataset
print f.variables['time'][1871:1872] #December 2005
print f.variables['time'][0:1] #January 1850

#Finds time difference between months
time = f.variables['time']
timeDiff = [time[i]-time[i-1] for i in range(0,len(time))]
timeDiff.pop(0)
timeDiff.append(30.5)
timeDiffNP = np.array(timeDiff)
months = np.reshape(timeDiffNP,(156,12))
"""
#Print all Januaries
print months[:,0]
#Check all months of length 156
for i, x in enumerate(months):
	print len(months[:,i])
"""

#Create copy of dataset
m = f.variables

#Change units of 'time' variable (from seconds since 01/01/0001 to length (days))
days_time = [m['time'][i]-m['time'][i-1] for i in range(0,len(m['time']))]
days_time.pop(0)
days_time.append(30.5)

#Changes units of 'prc' variable (from mm/day to mm/month) so compatibile with AWAP dataset
#Note: prc_monthly[1871][160][40] is: timestep, latitude, longitude
prc_monthly = [m['prc'][i]*m['time'][i] for i in range(0,len(m['time']))]
m['prc'] = prc_monthly

#MONTHLY DATA
#Data for Jan-Dec years (Jan 1900 to Dec 2005) - 105 year analysis
#Note: jan[40][40][155] is: timestep, longitude, latitude
#Note: timestep 600 is January 1900
#Call XX_array when performing actual analyses
Jan = prc_monthly[600::12]
Jan_array = np.array(Jan)

Feb = prc_monthly[601::12]
Feb_array = np.array(Feb)

Mar = prc_monthly[602::12]
Mar_array = np.array(Mar)

Apr = prc_monthly[603::12]
Apr_array = np.array(Apr)

May = prc_monthly[604::12]
May_array = np.array(May)

Jun = prc_monthly[605::12]
Jun_array = np.array(Jun)

Jul = prc_monthly[606::12]
Jul_array = np.array(Jul)

Aug = prc_monthly[607::12]
Aug_array = np.array(Aug)

Sep = prc_monthly[608::12]
Sep_array = np.array(Sep)

Oct = prc_monthly[609::12]
Oct_array = np.array(Oct)

Nov = prc_monthly[610::12]
Nov_array = np.array(Nov)

Dec = prc_monthly[611::12]
Dec_array = np.array(Dec)

#SEASONAL DATA
#Data for Jan-Dec years (Jan 1900 to Dec 2005) - 105 year analysis
#e.g. MAM_flat[][][] = timestep, longitude, latitude
#for DJF, exclude JF 1900/include D 1899?  Exclude Dec 2005?
DJF_flat = Dec + Jan + Feb
DJF_array = np.array(DJF_flat)
DJF = np.reshape(DJF_array, (106,3,145,192))

MAM_flat = Mar + Apr + May
MAM_array = np.array(MAM_flat)
MAM = np.reshape(MAM_array, (106,3,145,192))

JJA_flat = Jun + Jul + Aug
JJA_array = np.array(JJA_flat)
JJA = np.reshape(JJA_array, (106,3,145,192))

SON_flat = Sep + Oct + Nov
SON_array = np.array(SON_flat)
SON = np.reshape(JJA_array, (106,3,145,192))

#ANNUAL DATA
#Data for Jan-Dec years (Jan 1900 to Dec 2005) - 105 year analysis
annual_flat = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec
annual_array = np.array(annual_flat)
annualJanToDec = np.reshape(annual_array,(106,12,145,192))

#Monthly data for Jun-May years (June 1900 to May 2004) - 104 year analysis
Jun1 = prc_monthly[605:1853:12]
Jun1_array = np.array(Jun1)

Jul1 = prc_monthly[606:1854:12]
Jul1_array = np.array(Jul1)

Aug1 = prc_monthly[607:1855:12]
Aug1_array = np.array(Aug1)

Sep1 = prc_monthly[608:1856:12]
Sep1_array = np.array(Sep1)

Oct1 = prc_monthly[609:1857:12]
Oct_array1 = np.array(Oct1)

Nov1 = prc_monthly[610:1858:12]
Nov_array1 = np.array(Nov1)

Dec1 = prc_monthly[611:1859:12]
Dec1_array = np.array(Dec1)

Jan1 = prc_monthly[612:1860:12]
Jan1_array = np.array(Jan1)

Feb1 = prc_monthly[613:1861:12]
Feb1_array = np.array(Feb1)

Mar1 = prc_monthly[614:1862:12]
Mar1_array = np.array(Mar1)

Apr1 = prc_monthly[615:1863:12]
Apr1_array = np.array(Apr1)

May1 = prc_monthly[616:1864:12]
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
