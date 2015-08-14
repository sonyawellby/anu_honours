"""
A set of routines to prepare ACCESS1.3 sea-surface temperature and
precipitation data for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 13 August 2015.
"""

import netCDF4 as n
import numpy as np
from numpy import ma

from cwd import *
cwdInFunction()

#Make sure to run with (a) correct data, and (b) all three runs
data1 = raw_input('Enter the name of the dataset to analyse: ')
data = n.Dataset(data1,'r')

#dataAWAP = n.Dataset('AWAP_1900-2014_monthly_precip_swACCESSgrid_v4.nc','r')
#data = n.Dataset('ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','r')
#data = n.Dataset('ACCESS_data/ts_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','r')

"""
Functions to prepare ACCESS1.3 sea-surface temperature data for analysis.
"""

def sstMissing():
    dataSST = data.variables['sst'][:]
    dataMiss = np.ma.masked_equal(dataSST,1e+20)
    return dataMiss

def KtoC():
    """
    A function to convert the ACCESS 'ts' variable from K to degrees Celsius
    so that data can be compared directly with HadISST data.

    0 degrees Celsius = 273.15 Kelvin

    Values with temperatures less than 0 degrees Celsius have been masked as
    land-based values return 'skin' temperature (and may distort results).
    """
    dataCelsius = data.variables['ts'][:]
    for i in dataCelsius:
        i -= 273.15
    # Mask land-based SSTs
    mx = np.ma.masked_less(dataCelsius,0)
    return mx

"""
Functions to prepare ACCESS1.3 sea-surface temperature data for analysis.
"""

def prMissing():
    dataPr = data.variables['pr'][:]
    dataMiss = np.ma.masked_equal(dataPr,1e+20)
    return dataMiss

def SectoDay():
    """
    A function to convert the ACCESS 'pr' variable from kg/m^2/s to kg/m^2/day
    so that data can be compared directly with AWAP data.

    The number of seconds in one day = 86400 seconds
    Differences between years in no. of seconds should not affect monthly averages
    of precipitation as the time scale averaged over (months) is sufficiently long.

    The conversion was made to kg/m^2/day rather than kg/m^2/month so that
    inconsistencies between ACCESS and AWAP datasets regarding the number of
    days in a month would not affect results.
    """
    dataDay = dataMiss
    #Mask values less than 0 (cannot have negative rainfall)
    dataDay = np.ma.masked_less(dataDay,0)
    for i in dataDay:
        i *= 86400
    return dataDay

def accessTrim():
    """
    A function to read in an ACCESS dataset and trim it to the period
    June 1900 to May 2005.

    Note: data_flat: months,latitude,longitude
    """
    full_data = dataFull
    data_flat = dataFull[605:1865]
    return data_flat

def accessAnnual():
    """
    A function to convert flat data to an array with all 105 years
    and 12 months for all latitudes and longitudes.

    Note: accessData[year,month,lat,lon]
    e.g. accessData[104,11,179,359]
         = May 2005 at 180 deg N (89.5 deg) and 360 deg E (179.5 deg E)
    """
    data = np.array(data_flat)
    data = np.reshape(data,(105,12,180,360))
    return data

def accessJune():
    """
    A function to produce an array of June data for all 105 years.
    Note: June[year,lat,lon]
    """
    June = data_flat[0::12]
    June = np.array(June)
    data = np.reshape(June,(105,180,360))
    return June

def accessJuly():
    """
    A function to produce an array of July data for all 105 years.
    Note: July[year,lat,lon]
    """
    July = data_flat[1::12]
    July = np.array(July)
    data = np.reshape(July,(105,180,360))
    return July

def accessAugust():
    """
    A function to produce an array of August data for all 105 years.
    Note: August[year,lat,lon]
    """
    August = data_flat[2::12]
    August = np.array(August)
    data = np.reshape(August,(105,180,360))
    return August

def accessSeptember():
    """
    A function to produce an array of September data for all 105 years.
    Note: September[year,lat,lon]
    """
    September = data_flat[3::12]
    September = np.array(September)
    data = np.reshape(September,(105,180,360))
    return September

def accessOctober():
    """
    A function to produce an array of October data for all 105 years.
    Note: October[year,lat,lon]
    """
    October = data_flat[4::12]
    October = np.array(October)
    data = np.reshape(October,(105,180,360))
    return October

def accessNovember():
    """
    A function to produce an array of November data for all 105 years.
    Note: November[year,lat,lon]
    """
    November = data_flat[5::12]
    November = np.array(November)
    data = np.reshape(November,(105,180,360))
    return November

def accessDecember():
    """
    A function to produce an array of December data for all 105 years.
    Note: December[year,lat,lon]
    """
    December = data_flat[6::12]
    December = np.array(December)
    data = np.reshape(December,(105,180,360))
    return December

def accessJanuary():
    """
    A function to produce an array of January data for all 105 years.
    Note: January[year,lat,lon]
    """
    January = data_flat[7::12]
    January = np.array(January)
    data = np.reshape(January,(105,180,360))
    return January

def accessFebruary():
    """
    A function to produce an array of Feburary data for all 105 years.
    Note: February[year,lat,lon]
    """
    February = data_flat[8::12]
    February = np.array(February)
    data = np.reshape(February,(105,180,360))
    return February

def accessMarch():
    """
    A function to produce an array of March data for all 105 years.
    Note: March[year,lat,lon]
    """
    March = data_flat[9::12]
    March = np.array(March)
    data = np.reshape(March,(105,180,360))
    return March

def accessApril():
    """
    A function to produce an array of April data for all 105 years.
    Note: April[year,lat,lon]
    """
    April = data_flat[10::12]
    April = np.array(April)
    data = np.reshape(April,(105,180,360))
    return April

def accessMay():
    """
    A function to produce an array of May data for all 105 years.
    Note: May[year,lat,lon]
    """
    May = data_flat[11::12]
    May = np.array(May)
    data = np.reshape(May,(105,180,360))
    return May

def accessJJA():
    """
    A function to produce an array of JJA seasonal data (average of
    all three months at each location) for all 105 years.
    Note: JJA[year,lat,lon]
    """
    JJA_flat = data_flat[0::12] + data_flat[1::12] + data_flat[2::12]
    JJA_flat /= 3.0
    JJA = np.array(JJA_flat)
    data = np.reshape(JJA,(105,180,360))
    return JJA

def accessSON():
    """
    A function to produce an array of SON seasonal data (average of
    all three months at each location) for all 105 years.
    Note: SON[year,lat,lon]
    """
    SON_flat = data_flat[3::12] + data_flat[4::12] + data_flat[5::12]
    SON_flat /= 3.0
    SON = np.array(SON_flat)
    data = np.reshape(SON,(105,180,360))
    return SON

def accessDJF():
    """
    A function to produce an array of DJF seasonal data (average of
    all three months at each location) for all 105 years.
    Note: DJF[year,lat,lon]
    """
    DJF_flat = data_flat[6::12] + data_flat[7::12] + data_flat[8::12]
    DJF_flat /= 3.0
    DJF = np.array(DJF_flat)
    data = np.reshape(DJF,(105,180,360))
    return DJF

def accessMAM():
    """
    A function to produce an array of MAM seasonal data (average of
    all three months at each location) for all 105 years.
    Note: MAM[year,lat,lon]
    """
    MAM_flat = data_flat[9::12] + data_flat[10::12] + data_flat[11::12]
    MAM_flat /= 3.0
    MAM = np.array(MAM_flat)
    data = np.reshape(MAM,(105,180,360))
    return MAM
