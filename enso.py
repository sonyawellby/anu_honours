"""
Set of routines to compute the Nino3.4 ENSO index.
Nino3.4 region: -5 to 5 degrees N, 190 to 240 degrees E

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 24 August 2015.
"""

import netCDF4 as n
import numpy as np
from scipy import signal

from cwd import *
cwdInFunction()

"""
from access_prepare_ts import ts_January,ts_February,ts_March,\
     ts_April,ts_May,ts_June,ts_July,ts_August,ts_September,\
     ts_October,ts_November,ts_December

from hadisst_prepare import sst_January,sst_February,sst_March,\
     sst_April,sst_May,sst_June,sst_July,sst_August,sst_September,\
     sst_October,sst_November,sst_December
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

def baseAreaENSO(dataset,a,b,ACCESS=True):
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
    a :     The earliest year in the base period.  Give as index
            (e.g. [0=1900,104=2005]
    b :     The latest year in the base period.  Give as index
            (e.g. [0=1900,104=2005]
    """
    if ACCESS==True:
        area = dataset[a:b,68:77,101:130] #-5.0 to 5.0 N; 189.375 to 241.875 E
    else:
        area = dataset[a:b,84:96,9:60] #5.5 to -5.5 N; -170.5 to -121.5 E
    return base_area

def meanSST(area):
    """
    A function to calculate the average SST values for each
    grid point in the Nino3.4 region for the entire
    period of analysis.

    Parameters:
    -----------
    area: the output of areaENSO()
    """
    mean_SST = np.mean(area,axis=0)
    return mean_SST

def baseMeanSST(base_area):
    """
    A function to calculate the average SST values for each
    grid point in the Nino3.4 region for the base period
    specified in areaBase().

    Parameters:
    -----------
    base_area : the output of baseAreaENSO()
    """
    base_SST = np.mean(base_area,axis=0)
    return base_SST

def anomalies(area,base_SST):
    """
    A function to compute the SST anomalies (degrees Celsius)
    in the Nino3.4 region.  Base period values are subtracted
    from each grid cell of the Nino3.4 area for the whole period
    of analysis.
    
    Parameters:
    -----------
    area : output from areaENSO().  Defines the Nino3.4
           area for all years in the study period.
    base_SST: output from baseMeanSST().  Defines the Nino3.4
              area for chosen base period.
    """
    for i in area:
        anomalies = np.subtract(area,base_SST)
    return anomalies

def meanAnom(anomalies):
    """
    A fuction to calculate the mean SST anonamly
    in the Nino3.4 box for each time step.

    Parameters:
    -----------
    anomalies:
        The output of anomalies().  Anomaly information
        for each grid cell in the Nino3.4 area for all times.
    """
    meanAnom = np.zeros(105)
    count = 0
    for i in anomalies:
        meanAnom1[count] = np.mean(i)
        count += 1
    return meanAnom


def ENSOunfil(meanAnom):
    """
    A function to return an array of the unfiltered
    ENSO values for all years of analysis.

    
    """
    a1a3 = np.add(meanAnom1,meanAnom3)
    div2 = np.divide(a1a3,2.0)
    TPI = np.subtract(meanAnom2,div2)
    return ENSO


   
#_____________________________________________    
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

