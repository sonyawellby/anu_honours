"""
Routine to check whether a NetCDF file of the ACCESS CMIP5 model is reading correctly.
Returns metadata and key information of file.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 28 July 2015.
"""

import netCDF4 as n
import numpy as np
        
def inputFile():
    """A function to import the dataset to be analysed.
	POSSIBLE FILES:
	ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc ...x3 Check right
	ACCESS_data/ts_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc ...x3 Check right
	HadISST_sst.nc
	AWAP_1900-2014_monthly_precip_v1.nc
    """
    dataFile=raw_input('Enter the filepath of the NetCDF4 file to analyse: ')

def cwd():
    """A function to set current working directory."""
    import os
    os.chdir("/home/sonya/Documents/")
    print os.getcwd()
    #If working directory set up correctly, this file should load
    f = open("my_coding_routines/foo.py","r")
    print f

def cwdInFunction():
    """Function to be used in setting the current working directory within a function."""
    import os
    os.chdir("/home/sonya/Documents/")
    
def metadata():
    """A function to return the metadata of a NetCDF4 file"""
    inputFile()    
    cwdInFunction()
    f = n.Dataset(dataFile,'r')
    return f
    f.close()

def dataType():
    """A function to print the type of NetCDF4 data (http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html)"""
    inputFile()    
    cwdInFunction()
    f = n.Dataset(dataFile,'r')
    return f.data_model
    f.close()

def dimensions():
    """Returns summary information on included dimensions"""
    inputFile()
    cwdInFunction()
    f = n.Dataset(dataFile,'r')
    return f.dimensions
    f.close()

def variables():
    """Returns list of variables in file"""
    inputFile()    
    cwdInFunction()
    f = n.Dataset(dataFile,'r')
    for v in f.variables:
        print(v)
    f.close()

def variablesInfo():
    """Returns data bounds for each variables in file"""
    inputFile()    
    cwdInFunction()
    f = n.Dataset(dataFile,'r')
    for v in f.variables:
        print 'Variable is',v
        print f.variables[v][:]
    f.close()
                  
    """
    print f.variables['pr']
    print f.variables['lat'][:]
    print f.variables['lon'][:]
    f.close()
    """
