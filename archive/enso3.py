"""
Set of routines to compute the Nino3.4 ENSO index.
Nino3.4 region: -5 to 5 degrees N, 190 to 240 degrees E

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 26 August 2015.
"""

import netCDF4 as n
import numpy as np
import numpy.ma

from cwd import *
cwdInFunction()

#Can remove later:
from hadisst_prepare import dataFix_Had


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
    elif ACCESS==False:
        area = dataset[:,84:96,9:60] #5.5 to -5.5 N; -170.5 to -121.5 E
    else:
        raise ValueError('Specify whether ACCESS or HadISST data are being used.')
    return area

def baseAreaENSO(dataset,a,b,c,ACCESS=True):
    """
    A function to define the Nino3.4 area for the base time period.

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
    c :     The index of the first occurrence of the month computed
            within the dataset.  Used to slice the base period into
            values for this month only, to avoid seasonality when
            computing the Nino3.4 index.
    """
    #Account for Python slicing.
    b += 1
    
    if ACCESS==True:
        base_area = dataset[a:b:c,68:77,101:130] #-5.0 to 5.0 N; 189.375 to 241.875 E
    elif ACCESS==False:
        base_area = dataset[a:b:c,84:96,9:60] #5.5 to -5.5 N; -170.5 to -121.5 E
    else:
        raise ValueError('Specify whether ACCESS or HadISST data are being used.')
    return base_area

"""
def meanSST(area):

    A function to calculate the average SST values for each
    grid point in the Nino3.4 region for the entire
    period of analysis.

    Parameters:
    -----------
    area: the output of areaENSO()

    mean_SST = np.mean(area,axis=0)
    return mean_SST
"""
    
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
    in the Nino3.4 region.  Base period (mean) values are subtracted
    from each grid cell of the Nino3.4 area for each time step
    for the whole period of analysis.
    
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

    """
count = 0
while count <12:
	for i in AreaENSO:
	testz = AreaENSO[count::12]
	count += 1
print testz
"""

def meanAnom(anomalies):
    """
    A function to calculate the mean SST anonamlies (degrees
    Celsius) in the Nino3.4 box for each time step.

    Parameters:
    -----------
    anomalies:
        The output of anomalies().  Anomaly information
        for each grid cell in the Nino3.4 area for all times.
    """
    meanAnom = np.zeros(len(anomalies))
    count = 0
    for i in anomalies:
        meanAnom[count] = np.mean(i)
        count += 1
    return meanAnom


def running(dataset,start,end):
    """
    A function to calculate a five month running mean
    of SST anomalies (degrees Celsius) in the Nino3.4 region.

    Parameters:
    -----------
    Dataset : the dataset to calculate a five month running mean
            from.  Usually the output of meanAnom()
    Start : the index of the 'middle' month in the first five month
            block.  Will be [2] if start at [0].
    End : the index of the 'middle' month in the last five month
            block.  Will usually be (len(dataset)-3).
    """
    copy = dataset
    running = np.zeros((len(copy)-4))
    count_copy = start-2
    count_running = 0
    for i in dataset[start:end]:
        r_mean = np.mean(copy[count_copy:count_copy+5])
        running[count_running] += r_mean
        count_copy += 1
        count_running += 1
    return running

def cropRM(dataset):
    """
    A function to crop the running mean output (January 1900
    to December 2005) to study period (June 1900 to May 2005).
    This output is used for the CSV output (see enso_csv.py).

    Parameters:
    -----------
    Dataset : the output of running()
    """
    cropRM = dataset[3:((len(dataset))-5)]
    return cropRM

def ENSOphase(dataset,start,end):
    """
    A function to take a dataset and stratify it according to
    ENSO phase (positive, neutral, negative).  The ENSO definition
    applied is that of Trenberth et al. 1997 ('The Definition of
    El Nino',Bulletin of the American Meteorological Society).
    Three different arrays are returned (positive, negative,
    and neutral ENSO events).

    Parameters:
    -----------
    dataset : The input datset of running-means (i.e. running() ).
            It must include five more months of data than are
            analysing in order to determine whether +- 0.4 deg. Cel.
            is exceeded for six months or more.
    start : the index of the first element to analyse.  If using
            5 month running mean data this is likely to be [2]
            for June 1900.
    end : the index of the last element to analyse.  It is likely to
            be (len(dataset)-6) (the sixth from last element).
    """
    copy = dataset
    count = 0
    ENSOpos = None
    ENSOneg = None
    ENSOneutral = None
    for i in dataset[start:(end+1)]:
        if dataset[count] > 0.4 and dataset[count+1] > 0.4 and \
           dataset[count+2] > 0.4 and dataset[count+3] > 0.4 \
           and dataset[count+4] > 0.4 and dataset[count+5] > 0.4:
            ENSOpos = np.ma.masked_less_equal(copy, 0.4)
        elif dataset[count] < 0.4 and dataset[count+1] < 0.4 and \
             dataset[count+2] < 0.4 and dataset[count+3] < 0.4 \
               and dataset[count+4] < 0.4 and dataset[count+5] < 0.4:
            ENSOneg = np.ma.masked_greater_equal(copy,-0.4)
        else:
            ENSOneutral = np.ma.masked_outside(copy, 0.4, -0.4)
        count += 1
    return ENSOpos, ENSOneg, ENSOneutral

def cropPhase(dataset):
    """
    A function to crop the running mean output (June 1900
    to December 2005) to study period (June 1900 to May 2005).

    Dataset : the output of running()
    """
    cropPhase = dataset[3:((len(dataset))-5),:,:]
    return cropPhase