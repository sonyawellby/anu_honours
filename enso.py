"""
Set of routines to compute the Nino3.4 ENSO index.
Nino3.4 region: -5 to 5 degrees N, 190 to 240 degrees E

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 19 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

from access_prepare_ts import ts_January,ts_February,ts_March,\
     ts_April,ts_May,ts_June,ts_July,ts_August,ts_September,\
     ts_October,ts_November,ts_December

"""
from hadisst_prepare import sst_January,sst_February,sst_March,\
     sst_April,sst_May,sst_June,sst_July,sst_August,sst_September,\
     sst_October,sst_November,sst_December
"""


access = [ts_January,ts_February,ts_March,\
     ts_April,ts_May,ts_June,ts_July,ts_August,ts_September,\
     ts_October,ts_November,ts_December]
"""
hadisst = [sst_January,sst_February,sst_March,\
     sst_April,sst_May,sst_June,sst_July,sst_August,sst_September,\
     sst_October,sst_November,sst_December]
"""


#Function to define Nino3.4 area
def areaENSO(dataset,ACCESS=True):
    """
    A function to define the Nino3.4 area for entire time period.

    In cases where the grid cells do not exactly match the region,
    the grid-cell beginning/ending outside of the range was chosen
    to ensure all of the area was encompassed.  E.g. 189.375 E was
    chosen rather than 191.25 E for eastern bound (190.0 E) of
    the region.
    
    Parameters:
    -----------
    dataset : SST data of monthly, seasonal or annual resolution;
            either from hadisst_prepare or access_ts
    ACCESS : (default = True)
            if the data is from access_ts, is "True".  Otherwise the
            HadISST data is analysed. This accommodates
            for differences in longitudinal/latitudinal starting points.
    """
    if ACCESS==True:
        area = dataset[:,68:77,101:130] #-5.0 to 5.0 N; 189.375 to 241.875 E
    else:
        area = dataset[:,84:96,9:60] #5.5 to -5.5 N; -170.5 to -121.5 E
    return area


#Function to compute average SSTs in Nino3.4 region, all times
def avENSO(Area=area):
    """
    Docstring
    Parameters:
    -----------
    Area = (default=area)
        Array of the Nino3.4 region for all times.  Default:
        output from areaENSO() function.
    """
    arr_zeros = np.zeros_like(Area)
    for i in Area:
        
        
    
#Function to apply above to each month in 2 lists  

def baseENSO(dataset,a,b,ACCESS=True):
    """
    A function to determine average SSTs in the Nino3.4 region.

    In cases where the grid cells do not exactly match the region,
    the grid-cell beginning/ending outside of the range was chosen
    to ensure all of the area was encompassed.  E.g. 189.375 E was
    chosen rather than 191.25 E for eastern bound (190.0 E) of
    the region.
    
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
    #Define Nino3.4 area
    if ACCESS==True:
        area = dataset[a:b,68:77,101:130] #-5.0 to 5.0 N; 189.375 to 241.875 E
    else:
        area = dataset[a:b,84:96,9:60] #5.5 to -5.5 N; -170.5 to -121.5 E
    return area



        
    
#from hadisst_prepare import sst_Annual
from access_prepare_ts import ts_Annual,dataFix,ts_JJA


"""
def test():
    hi = "hi"
    bye = "bye"
    return hi,bye
    
test = test()
(hello,cya)=test #associates 'hello' and 'cya' with output of function (unpacks tuple)
"""

#Actual code
areaENSO = areaENSO()

