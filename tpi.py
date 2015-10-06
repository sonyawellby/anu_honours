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
Last updated 27 August 2015.
"""

import netCDF4 as n
import numpy as np
from scipy import signal

from parameters import num

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
    elif ACCESS==False:
        #45.5 to 25.5 N; (139.5-179.5)+(-179.5 to -145.5) E
        #[319:360] + [0:35]
        a = np.roll(dataset,41,axis=2)
        b = a[:,44:65,0:75]
        area1 = np.ma.masked_less_equal(b,0.0)
        
        #10.5 to -10.5 N; (169.5-179.5)+(-179.5 to -90.5) E
        #[349:360] + [0:90]
        c = np.roll(dataset,11,axis=2)
        d = c[:,79:101,0:100]
        area2 = np.ma.masked_less_equal(d,0.0)

        #-14.5 to -50.5 N; (149.5-179.5)+(-179.5 to -160.5) E
        #[329:360] + [0:20]
        e = np.roll(dataset,31,axis=2)
        f = e[:,104:141,0:50]
        area3 = np.ma.masked_less_equal(f,0.0)

    else:
        raise ValueError('Specify whether ACCESS or HadISST data are being used.')
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
    #Account for Python slicing.
    b += 1
    
    if ACCESS==True:
        base_area1 = dataset[a:b,92:109,74:116] #25 to 45 N; 138.75 to 215.625 E
        base_area2 = dataset[a:b,64:81,90:145] # -10 to 10 N; 168.75 to 270 E
        base_area3 = dataset[a:b,32:85,80:108] # -50 to -15N; 150 to 200.625 E
    elif ACCESS==False:
        #45.5 to 25.5 N; (139.5-179.5)+(-179.5 to -145.5) E
        #[319:360] + [0:35]
        c = np.roll(dataset,41,axis=2)
        d = c[a:b,44:65,0:75]
        base_area1 = np.ma.masked_less_equal(d,0.0)
        
        #10.5 to -10.5 N; (169.5-179.5)+(-179.5 to -90.5) E
        #[349:360] + [0:90]
        e = np.roll(dataset,11,axis=2)
        f = e[a:b,79:101,0:100]
        base_area2 = np.ma.masked_less_equal(f,0.0)
        
        #-14.5 to -50.5 N; (149.5-179.5)+(-179.5 to -160.5) E
        #[329:360] + [0:20]
        g = np.roll(dataset,31,axis=2)
        h = g[a:b,104:141,0:50]
        base_area3 = np.ma.masked_less_equal(h,0.0)

    else:
        raise ValueError('Specify whether ACCESS or HadISST data are being used.')

    return base_area1,base_area2,base_area3


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
    A function to calculate the mean SST anonamly
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

def TPI(dataset,n,rp,wn):
    """
    A function to apply a 13 year Chebyshev low pass filter
    to the unfiltered TPI output, from TPIunfil().  The
    filter design is a digital, type 1 (passband) Chebyshev filter.
    The filter itself is a zero-phase filter, as a forward-in-time
    only filter shifts the signal as it filters (resulting in
    a delayed signal).

    Parameters:
    -----------
    dataset : the data to filter.  Will either be: Had_monthsTPI_uf or
            Acc_monthsTPI_uf (see 'tpi_csv.py').
    n = filter order (Henley et al.: n = 6).
    rp = peak to peak passband ripple. In decibels; positive number.
        (Henley et al.: rp = 13).
    wn = critical frequencies.  Between 0-1, where 1 is
        the Nyquist frequency, pi radians/sample.
        (Henley et al.: wn = 0.1).
    """
    b, a = signal.cheby1(n, rp, wn, btype='low', analog=False, output='ba')
    TPI = signal.filtfilt(b,a,dataset)
    return TPI

def chunks(l,n):
    """
    A function to divide the output of running() into chunks of interest
    (e.g. annual, particular seasons).  Returns a list of lists, where the
    sub-lists are the months of a given season (number = 3), or all months
    in a year (number = 12).
    
    Parameters:
    -----------
    l : the list which will be broken into seasonal or annual chunks.
    n : the size of the seasonal or annual chunk (e.g. 3 = seasonal,
        12 = annual).
    """
    return [l[i:i+n] for i in range(0,len(l),n)]

def runningSeasons(dataset,n,m,o):
    """
    A function to break the running mean dataset into seasonal or annual
    subsets.

    Parameters:
    -----------
    dataset : Output from running().
    n : the size of the chunk (e.g. 3 months, 12 months).
    m : the starting element in the list (e.g. 0 = June 1990.
    o : the number of the element in the list at which the next instance of
        the season of interest, or the next year, begins.
    
    For example:
    JJA: runningSeasons(mylist,3,0,4)
    SON: runningSeasons(mylist,3,1,4)
    DJF: runningSeasons(mylist,3,2,4)
    MAM: runningSeasons(mylist,3,3,4)
    years: runningSeasons(mylist,12,0,1)
    """
    new = chunks(dataset,n)
    newlist = []

    list1 = range(m,len(new),o)
    for i in list1:
        newlist.append(new[i])
    newarray = np.asarray(newlist)

    newNewlist = []
    for i in newarray:
        newNewlist.append(np.average(i))
    newNewarray = np.asarray(newNewlist)

    return newNewarray

def IPOphase(dataset,sd=num):
    """
    A function to compute the phase of the TPI. Phases 1.5 standard
    deviations above or below the mean are classed as IPO positive
    and IPO negative phases, respectively.

    Parameters:
    ----------
    dataset : dataset of filtered TPI values. 
    """
    std = np.std(dataset)*sd

    copy = dataset
    
    IPOpos = np.ma.masked_less_equal(copy, std)
    IPOneg = np.ma.masked_greater_equal(copy,-std)
    IPOneutral = np.ma.masked_outside(copy, std, -std)
        
    return IPOpos, IPOneg, IPOneutral
