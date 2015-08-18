"""
This routine determines the ENSO strength (in Nino3.4 region: 5 degrees NS,
190-240 degrees E).

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 22 June 2015.
"""

#Check current working directory
import os
os.chdir("/home/sonya/Documents/")
print os.getcwd()
#If working directory set up correctly, this file should load
#f = open("my_coding_routines/foo.py","r")

import netCDF4 as n
import numpy as np

f_raw = 'ACCESS_data/prc_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc' #change to SST
f = n.Dataset(f_raw,'a')

#Define Nino3.4 area
nino34 = f.variables['prc'][:,-5:6,190:241] #change to SST

#Define base period Nino3.4 (1961-1990)
"""
1. For each grid point in Nino3.4 area, determine average SST in time-period
2. 
"""

import pylab
temp = f.variables['prc']

ntimes, ny, nx = shape(temp)
test1 = zeros((ny,nx,),dtype='f')

for i in xrange(ntimes):



"""nino34_base = f.variables['prc'][x:y,-5:6,190:241]


base_lat = f.variables['lat'][190:241]
base_lon = f.variables['lon'][-5:6]

nino34_base = f.variables['prc'][x,-5:6,190:241]"""


test = f.variables['prc'][:,-5,190:241]
for i in xrange









