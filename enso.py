"""
Set of routines to compute the Nino3.4 ENSO index.
Nino3.4 region: -5 to 5 degrees N, 190 to 240 degrees E

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 22 September 2015.
"""

import netCDF4 as n
import numpy as np
import numpy.ma

from parameters import num
from cwd import *
cwdInFunction()

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
    dataset : SST data for all months and years in study period;
            either from hadisst_prepare.py or access_ts.py
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

def areaMonth(dataset):
    """
    A function to slice the original dataset into its constituent months.
    This data is used later when computing SST anomalies (comparing each month
    in the dataset with the average value for that month for the base period).

    Parameters:
    -----------
    dataset : SST data for all months and years in study period;
            either from hadisst_prepare.py or access_ts.py
    """
    Jan = dataset[0::12]
    Feb = dataset[1::12]
    Mar = dataset[2::12]
    Apr = dataset[3::12]
    May = dataset[4::12]
    Jun = dataset[5::12]
    Jul = dataset[6::12]
    Aug = dataset[7::12]
    Sep = dataset[8::12]
    Oct = dataset[9::12]
    Nov = dataset[10::12]
    Dec = dataset[11::12]
    return Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec

def baseAreaENSO(dataset,a,b,ACCESS=True):
    """
    A function to define the Nino3.4 area for the base time period.

    In cases where the grid cells do not exactly match the region,
    the grid-cell beginning/ending outside of the range was chosen
    to ensure all of the area was encompassed.  E.g. 189.375 E was
    chosen rather than 191.25 E for eastern bound (190.0 E) of
    the region.
    
    Parameters:
    -----------
    dataset : monthly subset of SST data from hadisst_prepare or access_ts
    ACCESS : (default = True)
            if the data is from access_ts, is "True".  Otherwise the
            HadISST data is analysed. This accommodates
            for differences in longitudinal/latitudinal starting points.
    a :     The earliest year in the base period.  Give as index
            (e.g. [0=1900].  Given in 'parameters.py'.
    b :     The latest year in the base period.  Give as index
            (e.g. [0=1900]. Given in 'parameters.py'.
    """
    #Account for Python slicing.
    b += 1
    
    if ACCESS==True:
        base_area = dataset[a:b,68:77,101:130] #-5.0 to 5.0 N; 189.375 to 241.875 E
    elif ACCESS==False:
        base_area = dataset[a:b,84:96,9:60] #5.5 to -5.5 N; -170.5 to -121.5 E
    else:
        raise ValueError('Specify whether ACCESS or HadISST data are being used.')
    return base_area
    
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
    in the Nino3.4 region.  The base period mean values - baseMeanSST() - 
    for each grid cell are subtracted from each grid cell of the Nino3.4 area
    for each time step for the whole period of analysis.
    
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
    A function to crop the running mean output (March 1900
    to October 2005) to study period (June 1900 to May 2005).
    This output is used for the CSV output (see enso_csv.py)
    and for cropping ENSOphase data.

    Parameters:
    -----------
    Dataset : the output of running()
    """
    cropRM = dataset[3:((len(dataset))-5)]
    return cropRM

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
    A function to break the running mean dataset into seasonal subsets.

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

def ENSOnegPhase(dataset,n,m,o):
    """
    A function to mask all values in the cropped running mean dataset (length
    1260) that are not ENSO negative (SST anomalies > 0.4 degrees Celsius).

    Parameters:
    -----------
    dataset : Output from running().
    n : the size of the chunk (e.g. 3 months, 12 months).
    m : the starting element in the list (e.g. 0 = June 1990.
    o : the number of the element in the list at which the next instance of
        the season of interest, or the next year, begins.
    """
    
    new = chunks(dataset,n)
    newlist = []

    list1 = range(m,len(new),o)
    for i in list1:
        newlist.append(new[i])
    newarray = np.asarray(newlist)
    
    array = np.zeros([105])

    count = 0
    for i in newarray:
        if i[0]>0.4 and i[1]>0.4 and i[2]>0.4 and i[3]>0.4 and \
           i[4]>0.4 and i[5]>0.4:
            array[count] = np.mean(newarray[count])
        elif i[1]>0.4 and i[2]>0.4 and i[3]>0.4 and i[4]>0.4 and \
           i[5]>0.4 and i[6]>0.4:
            array[count] = np.mean(newarray[count])
        elif i[2]>0.4 and i[3]>0.4 and i[4]>0.4 and i[5]>0.4 and \
           i[6]>0.4 and i[7]>0.4:
            array[count] = np.mean(newarray[count])
        elif i[3]>0.4 and i[4]>0.4 and i[5]>0.4 and i[6]>0.4 and \
           i[7]>0.4 and i[8]>0.4:
            array[count] = np.mean(newarray[count])
        elif i[4]>0.4 and i[5]>0.4 and i[6]>0.4 and i[7]>0.4 and \
           i[8]>0.4 and i[9]>0.4:
            array[count] = np.mean(newarray[count])
        elif i[5]>0.4 and i[6]>0.4 and i[7]>0.4 and i[8]>0.4 and \
           i[9]>0.4 and i[10]>0.4:
            array[count] = np.mean(newarray[count])
        elif i[6]>0.4 and i[7]>0.4 and i[8]>0.4 and i[9]>0.4 and \
           i[10]>0.4 and i[11]>0.4:
            array[count] = np.mean(newarray[count])
        else:
            array[count] = 0.0
        count += 1
        
    negENSO_Annual = np.ma.masked_values(array,0.0)
    return negENSO_Annual

def ENSOposPhase(dataset,n,m,o):
    """
    A function to mask all values in the cropped running mean dataset (length
    1260) that are not ENSO positive (SST anomalies < -0.4 degrees Celsius).

    Parameters:
    -----------
    dataset : Output from running().
    n : the size of the chunk (e.g. 3 months, 12 months).
    m : the starting element in the list (e.g. 0 = June 1990.
    o : the number of the element in the list at which the next instance of
        the season of interest, or the next year, begins.
    """
    
    new = chunks(dataset,n)
    newlist = []

    list1 = range(m,len(new),o)
    for i in list1:
        newlist.append(new[i])
    newarray = np.asarray(newlist)
    
    array = np.zeros([105])

    count = 0
    for i in newarray:
        if i[0]<-0.4 and i[1]<-0.4 and i[2]<-0.4 and i[3]<-0.4 and \
           i[4]<-0.4 and i[5]<-0.4:
            array[count] = np.mean(newarray[count])
        elif i[1]<-0.4 and i[2]<-0.4 and i[3]<-0.4 and i[4]<-0.4 and \
           i[5]<-0.4 and i[6]<-0.4:
            array[count] = np.mean(newarray[count])
        elif i[2]<-0.4 and i[3]<-0.4 and i[4]<-0.4 and i[5]<-0.4 and \
           i[6]<-0.4 and i[7]<-0.4:
            array[count] = np.mean(newarray[count])
        elif i[3]<-0.4 and i[4]<-0.4 and i[5]<-0.4 and i[6]<-0.4 and \
           i[7]<-0.4 and i[8]<-0.4:
            array[count] = np.mean(newarray[count])
        elif i[4]<-0.4 and i[5]<-0.4 and i[6]<-0.4 and i[7]<-0.4 and \
           i[8]<-0.4 and i[9]<-0.4:
            array[count] = np.mean(newarray[count])
        elif i[5]<-0.4 and i[6]<-0.4 and i[7]<-0.4 and i[8]<-0.4 and \
           i[9]<-0.4 and i[10]<-0.4:
            array[count] = np.mean(newarray[count])
        elif i[6]<-0.4 and i[7]<-0.4 and i[8]<-0.4 and i[9]<-0.4 and \
           i[10]<-0.4 and i[11]<-0.4:
            array[count] = np.mean(newarray[count])
        else:
            array[count] = 0.0
        count += 1
        
    posENSO_Annual = np.ma.masked_values(array,0.0)
    return posENSO_Annual

def ENSOneutralPhase(dataset,n,m,o):
    """
    A function to mask all ENSO non-neutral values in the cropped running mean
    dataset (length 1260).

    Parameters:
    -----------
    dataset : Output from running().
    n : the size of the chunk (e.g. 3 months, 12 months).
    m : the starting element in the list (e.g. 0 = June 1990.
    o : the number of the element in the list at which the next instance of
        the season of interest, or the next year, begins.
    """

    new = chunks(dataset,n)
    newlist = []

    list1 = range(m,len(new),o)
    for i in list1:
        newlist.append(new[i])
    newarray = np.asarray(newlist)

    array = np.empty([105])
    count = 0
    while count < len(array):
        array[count] = np.mean(newarray[count])
        count += 1
    
    neg = ENSOnegPhase(dataset,12,0,1)
    pos = ENSOposPhase(dataset,12,0,1)

    neutral = np.ma.masked_where(neg.mask==False,array)
    neutralENSO_Annual = np.ma.masked_where(pos.mask==False,neutral)
    return neutralENSO_Annual

def ensoSD(dataset,sd=num,crop=False):
    """
    A function to stratify ENSO SST anomaly data according to standard
    deviations.

    Parameters:
    -----------
    dataset : output of running().
    sd : standard deviations.  Defined in "parameters.py".
    """
    if crop == True:
        data = cropRM(dataset)
    else:
        data = dataset
    std = np.std(dataset)*sd
    ENSOneutral = numpy.ma.masked_outside(data,std,-std)
    ENSOpos = numpy.ma.masked_greater(data,-std)
    ENSOneg = numpy.ma.masked_less(data,std)
    return data, ENSOpos, ENSOneg, ENSOneutral

def enso(dataset,n,m,o,crop=False):
    """
    A function to stratify ENSO SST anomaly data according to SST anomalies
    (anomalies > 0.4 degrees Celsius = negative ENSO, anomalies < -0.4
    degrees Celsius = positive ENSO).

    Parameters:
    -----------
    dataset : output of running().
    n : the size of the chunk (e.g. 3 months, 12 months).
    m : the starting element in the list (e.g. 0 = June 1990.
    o : the number of the element in the list at which the next instance of
        the season of interest, or the next year, begins.
    crop : states whether the data needs to be cropped from length 1268 to
           length 1260.  Default = False.
    
    """
    if crop == True:
        data = cropRM(dataset)
    else:
        data = dataset
        
    ENSOneutral = ENSOneutralPhase(data,n,m,o)
    ENSOpos = ENSOposPhase(data,n,m,o)
    ENSOneg = ENSOnegPhase(data,n,m,o)

    neutralAll = numpy.ma.masked_outside(data,-0.4,0.4)
    posAll = numpy.ma.masked_greater(data,-0.4)
    negAll = numpy.ma.masked_less(data,0.4)
    return data, ENSOpos, ENSOneg, ENSOneutral,posAll,negAll,neutralAll
