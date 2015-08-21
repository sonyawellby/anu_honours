"""
Set of routines to compute the TPI IPO index.

TPI region 1: 25-45N, 140E-145W = 25-45N, 140-215E
TPI region 2: -10 to 10N, 170E-90W = -10 to 10N, 170-270E
TPI region 3: -50 to -15N, 150E-160W = -50 to -15N, 150-200E.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 19 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

def areaTPI(dataset,ACCESS=True):
    """
    A function to take SST input and return the three TPI regions, as
    described in the explanatory information above, for the whole
    study period.
    
    Parameters:
    -----------
    dataset : SST data of monthly, seasonal or annual resolution;
            either from hadisst_prepare or access_ts
    ACCESS : (default = True)
            if the data is from access_ts, is "True".  Otherwise the
            HadISST data is analysed. This distinction accommodates
            differences in longitudinal/latitudinal starting points.
    """

    if ACCESS==True:
        area1 = dataset[:,92:109,74:116] #25 to 45 N; 138.75 to 215.625 E
        area2 = dataset[:,64:81,90:145] # -10 to 10 N; 168.75 to 270 E
        area3 = dataset[:,32:85,80:108] # -50 to -15N; 150 to 200.625 E
    else:
        #45.5 to 25.5 N; (139.5-179.5)+(-179.5 to -145.5) E
        #[319:360] + [0:35]
        a = dataset[:,44:65,319:360]
        b = dataset[:,44:65,0:35]
        c = np.hstack((a,b))
        area1 = np.ma.masked_less_equal(c,0.0)
        
        #10.5 to -10.5 N; (169.5-179.5)+(-179.5 to -90.5) E
        #[349:360] + [0:90]
        d = dataset[:,79:101,349:360]
        e = dataset[:,79:101,0:90]
        f = np.hstack((d,e))
        area2 = np.ma.masked_less_equal(f,0.0)
        
        #-14.5 to -50.5 N; (149.5-179.5)+(-179.5 to -160.5) E
        #[329:360] + [0:20]
        g = dataset[:,104:141,329:360]
        h = dataset[:,104:141,0:20]
        i = np.hstack((g,h))
        area3 = np.ma.masked_less_equal(i,0.0)
    return area1,area2,area3


def areaBase(dataset,a,b,ACCESS=True):
    """
    A function to take SST input and return the three TPI regions, as
    described in the explanatory information above, for the base period.
    
    Parameters:
    -----------
    dataset : SST data of monthly, seasonal or annual resolution;
            either from hadisst_prepare or access_ts
    ACCESS : (default = True)
            if the data is from access_ts, is "True".  Otherwise the
            HadISST data is analysed. This accommodates
            for differences in longitudinal/latitudinal starting points.
    a :     The earliest year in the base period.  Give as index
            (e.g. [0=1900,104=2005]
    b :     The latest year in the base period.  Give as index
            (e.g. [0=1900,104=2005]
    """

    """
    Create TPI regions
    """
    if ACCESS==True:
        base_area1 = dataset[a:b,92:109,74:116] #25 to 45 N; 138.75 to 215.625 E
        base_area2 = dataset[a:b,64:81,90:145] # -10 to 10 N; 168.75 to 270 E
        base_area3 = dataset[a:b,32:85,80:108] # -50 to -15N; 150 to 200.625 E
    else:
        #45.5 to 25.5 N; (139.5-179.5)+(-179.5 to -145.5) E
        #[319:360] + [0:35]
        a = dataset[a:b,44:65,319:360]
        b = dataset[a:b,44:65,0:35]
        c = np.hstack((a,b))
        base_area1 = np.ma.masked_less_equal(c,0.0)
        
        #10.5 to -10.5 N; (169.5-179.5)+(-179.5 to -90.5) E
        #[349:360] + [0:90]
        d = dataset[a:b,79:101,349:360]
        e = dataset[a:b,79:101,0:90]
        f = np.hstack((d,e))
        base_area2 = np.ma.masked_less_equal(f,0.0)
        
        #-14.5 to -50.5 N; (149.5-179.5)+(-179.5 to -160.5) E
        #[329:360] + [0:20]
        g = dataset[a:b,104:141,329:360]
        h = dataset[a:b,104:141,0:20]
        i = np.hstack((g,h))
        base_area3 = np.ma.masked_less_equal(i,0.0)

    return base_area1,base_area2,base_area3

def baseArea(base_area):
    arr_zeros = np.zeros(16,42)
    for i in arr_zeros:
        arr_zeros[i] =

    for i in np.nditer(base_area):
        arr_zeros[i] = 
    



    """
    Calculate average SST in each grid point for base period
    """
    Region1 = np.zeros(area1)
    region1 = np.reshape(Region1,((a+b+1),(len(Region1)-(a+b+1))))
    count = 0
    for i in area1:
        a = np.mean(area1[count,:,:])
        region1[count] = a
        count += 1
    
    #
    nino34_array = SST_array[600:,101:129,68:76]
    nino34 = np.zeros(1272)

    count = 0
    for index in nino34:
        a = np.average(nino34_array[count,:,:])
        nino34[count] = a
        count += 1
    #
    """
    Calculate anomalies for each grid cell in time-series 
    """
    #Subtract the base period average for each grid cell from each grid cell

    """
    Calculate average anomaly for each TPI box for each point in time
    """

#from hadisst_prepare import sst_Annual
from access_prepare_ts import ts_Annual,dataFix,ts_JJA

area1 = ts_Annual[60:90,92:109,74:116]
area1a = ts_JJA[60:90,92:109,74:116]

#CODE TO KEEP#

areaTPI = areaTPI()
(area1,area2,area3)=areaTPI #Unpacks tuple so can access 'area1','area2','area3'

areaBase = areaBase()
(base_area1,base_area2,base_area3)=areaBase