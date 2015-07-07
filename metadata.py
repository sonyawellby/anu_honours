"""
Routine to check whether a NetCDF file of the ACCESS CMIP5 model is reading correctly.
Returns metadata and key information of file.

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

f = n.Dataset('ACCESS_data/prc_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','a')

#Prints metadata
print f

#Prints type of netCDF file (http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html)
print f.data_model

#Returns summary information on included dimensions
print f.dimensions

#Returns variables
for v in f.variables:
    print(v)

#Returns information on variables
print f.variables['prc']

print f.variables['lat'][:]
print f.variables['lon'][:]

f.close()
