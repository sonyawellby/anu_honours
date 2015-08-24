"""
Set of functions to compute the TPI IPO index.

The TPI is defined by Henley et al. 2015 in
"A Tripole Index for the Interdecadal Pacific Oscillation"
(Climate Dynamics, published online 5 March 2015,
DOI: 10.1007/s00382-015-2525-1).
_____________________________________________________________
TPI region 1: 25-45N, 140E-145W = 25-45N, 140-215E
TPI region 2: -10 to 10N, 170E-90W = -10 to 10N, 170-270E
TPI region 3: -50 to -15N, 150E-160W = -50 to -15N, 150-200E.
_____________________________________________________________
Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 24 August 2015.
"""

import netCDF4 as n
import numpy as np
from scipy import signal

from cwd import *
cwdInFunction()

def areaTPI(dataset,ACCESS=True):
    """
    A function to take SST input and return the three TPI regions
    (given in the explanatory information above) for the whole
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


def baseAreaTPI(dataset,a,b,ACCESS=True):
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

def meanSST(area1,area2,area3):
    """
    A function to calculate the average SST values for each
    grid point in the three TPI regions for the entire
    period of analysis.

    Parameters:
    -----------
    area1, area2, area3 : the output of areaTPI()
    """
    mean_SST1 = np.mean(area1,axis=0)
    mean_SST2 = np.mean(area2,axis=0)
    mean_SST3 = np.mean(area3,axis=0)
    return mean_SST1, mean_SST2, mean_SST3

def baseMeanSST(base_area1,base_area2,base_area3):
    """
    A function to calculate the average SST values for each
    grid point in the three TPI regions for the base period
    specified in areaBase().

    Parameters:
    -----------
    base_area1, base_area2, base_area3 : the output of baseAreaTPI()
    """
    base_SST1 = np.mean(base_area1,axis=0)
    base_SST2 = np.mean(base_area2,axis=0)
    base_SST3 = np.mean(base_area3,axis=0)
    return base_SST1, base_SST2, base_SST3


def anomalies(area1,area2,area3,base_SST1,base_SST2,base_SST3):
    """
    A function to compute the SST anomalies (degrees Celsius)
    in each TPI region.  Base period values are subtracted
    from each grid cell of the TPI areas for the whole period
    of analysis.
    
    Parameters:
    -----------
    area1,area2,area3 : output from areaTPI().  Gives the TPI
                        areas for all years in the study period.
    base_SST1,base_SST2,base_SST2:
                        output from baseMeanSST().  Gives the TPI
                        areas for chosen base period.
    """
    for i in area1:
        anomalies1 = np.subtract(area1,base_SST1)
    for i in area2:
        anomalies2 = np.subtract(area2,base_SST2)
    for i in area3:
        anomalies3 = np.subtract(area3,base_SST3)
    return anomalies1,anomalies2,anomalies3


def meanAnom(anomalies1,anomalies2,anomalies3):
    """
    A fuction to calculate the mean SST anonamly
    in each TPI box for each time step.

    Parameters:
    -----------
    anomalies1,anomalies2,anomalies3:
        The output of anomalies().  Anomaly information
        for each grid cell in the TPI regions for all times.
    """
    meanAnom1 = np.zeros(105)
    count1 = 0
    meanAnom2 = np.zeros(105)
    count2 = 0
    meanAnom3 = np.zeros(105)
    count3 = 0
    for i in anomalies1:
        meanAnom1[count1] = np.mean(i)
        count1 += 1
    for i in anomalies2:
        meanAnom2[count2] = np.mean(i)
        count2 += 1
    for i in anomalies3:
        meanAnom3[count3] = np.mean(i)
        count3 += 1
    return meanAnom1, meanAnom2, meanAnom3

def TPIunfil(meanAnom1,meanAnom2,meanAnom3):
    """
    A function to return an array of the unfiltered
    TPI values for all years of analysis.

    TPI = SST_area2 - ((SST_area1 + SST_area3)/2)
    """
    a1a3 = np.add(meanAnom1,meanAnom3)
    div2 = np.divide(a1a3,2.0)
    TPI = np.subtract(meanAnom2,div2)
    return TPI

def TPI(n,rp,wn,TPIunfiltered):
    """
    A function to apply a 13 year Chebyshev low pass filter
    to the unfiltered TPI output, from TPIunfil().  The
    filter is a digital, type 1 (passband) Chebyshev filter.

    Parameters:
    -----------
    n = filter order (Henley et al.: n = 6).
    rp = peak to peak passband ripple. In decibels; positive number.
        (Henley et al.: rp = 13).
    wn = critical frequencies.  Between 0-1, where 1 is
        the Nyquist frequency, pi radians/sample.
        (Henley et al.: wn = 0.1).
    """
    b, a = signal.cheby1(n, rp, wn, btype='low', analog=False, output='ba')
    TPI = signal.lfilter(b,a,TPIunfiltered)
    return TPI
