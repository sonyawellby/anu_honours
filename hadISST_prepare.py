"""
A set of routines to prepare HadISST sea-surface temperature data for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 6 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

def hadisstTrim():
    """
    A function to read in the HadISST dataset and trim it to the period
    June 1900 to May 2005.

    Note: data_flat: months,latitude,longitude
    """
    full_data = n.Dataset('HadISST_sst.nc','r')
    data_flat = full_data.variables['sst'][365:1625]
    return data_flat

data_flat = hadisstTrim()

def hadisstData():
    """
    A function to convert flat data to an array with all 105 years
    and 12 months for all latitudes and longitudes.

    Note: hadisstData[104,11,179,359] = May 2005 at 180 deg N and 360 deg E
    """
    data = np.array(data_flat)
    data = np.reshape(data,(105,12,180,360))
    return data
 
hadisstData = hadisstData()

def hadisstJune():
    """Docstring"""
    June = data_flat[0::12]
    June = np.array(June)
    data = np.reshape(June,(105,180,360))
    return June
June = hadisstJune()

    
