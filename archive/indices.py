"""
This routine determines the ENSO strength (in Nino3.4 region: 5 degrees NS,
190-240 degrees E).

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 July 2015.
"""

#Check current working directory
import os
os.chdir("/home/sonya/Documents/")
print os.getcwd()
#If working directory set up correctly, this file should load
#f = open("my_coding_routines/foo.py","r")

import netCDF4 as n
import numpy as np

import time_bins as t

#Change to SST file
f = n.Dataset('ACCESS_data/ts_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','a')
SST1 = f.variables['ts']
SST2 = np.array(SST1)
SST_array = np.reshape(SST2,(1872,145,192))

"""
ENSO
"""
#time, longitude [0-144], latitude [0-191].  Nino3.4 = 190:240 EW, -5:5 NS
nino34_array = SST_array[600:,101:129,68:76]
nino34 = np.zeros(1272)

count = 0
for index in nino34:
    a = np.average(nino34_array[count,:,:])
    nino34[count] = a
    count += 1





"""
"""
#IPO
"""
#Region 1: 25N-45N, 140-145EW
IPO_array1 = SST_array[600:,101:129,68:76]
IPO1 = np.zeros(1272)

count = 0
for index in IPO1:
    a = np.average(IPO_array1[count,:,:])
    IPO1[count] = a
    count += 1

#Region 2: 10S-10N, 170E-90W 
IPO_array2 = SST_array[600:,101:129,68:76]
IPO2 = np.zeros(1272)

count = 0
for index in IPO2:
    a = np.average(IPO_array2[count,:,:])
    IPO2[count] = a
    count += 1

#Region 3: 50S-15S, 150E-160W 
IPO_array3 = SST_array[600:,101:129,68:76]
IPO3 = np.zeros(1272)
    
count = 0
for index in IPO3:
    a = np.average(IPO_array3[count,:,:])
    IPO3[count] = a
    count += 1

TPI = np.zeros(len(IPO_array1))
count = 0
for index in TPI:
    a = IPO2 - ((IPO1+IPO3)/2.0)
    TPI[count] = a
    count += 1
"""
