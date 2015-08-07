"""
A set of routines to prepare HadISST (version 1.1.) sea-surface temperature data
for analysis.  Data file 'HadISST_sst.nc' from
http://www.metoffice.gov.uk/hadobs/hadisst/data/download.html

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 7 August 2015.
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

def hadisstAnnual():
    """
    A function to convert flat data to an array with all 105 years
    and 12 months for all latitudes and longitudes.

    Note: hadisstData[year,month,lat,lon]
    e.g. hadisstData[104,11,179,359]
         = May 2005 at 180 deg N (89.5 deg) and 360 deg E (179.5 deg E)
    """
    data = np.array(data_flat)
    data = np.reshape(data,(105,12,180,360))
    return data
 
hadisstAnnual = hadisstAnnual()

def hadisstJune():
    """
    A function to produce an array of June data for all 105 years.
    Note: June[year,lat,lon]
    """
    June = data_flat[0::12]
    June = np.array(June)
    data = np.reshape(June,(105,180,360))
    return June
June = hadisstJune()

def hadisstJuly():
    """
    A function to produce an array of July data for all 105 years.
    Note: July[year,lat,lon]
    """
    July = data_flat[1::12]
    July = np.array(July)
    data = np.reshape(July,(105,180,360))
    return July
July = hadisstJuly()

def hadisstAugust():
    """
    A function to produce an array of August data for all 105 years.
    Note: August[year,lat,lon]
    """
    August = data_flat[2::12]
    August = np.array(August)
    data = np.reshape(August,(105,180,360))
    return August
August = hadisstAugust()

def hadisstSeptember():
    """
    A function to produce an array of September data for all 105 years.
    Note: September[year,lat,lon]
    """
    September = data_flat[3::12]
    September = np.array(September)
    data = np.reshape(September,(105,180,360))
    return September
September = hadisstSeptember()

def hadisstOctober():
    """
    A function to produce an array of October data for all 105 years.
    Note: October[year,lat,lon]
    """
    October = data_flat[4::12]
    October = np.array(October)
    data = np.reshape(October,(105,180,360))
    return October
October = hadisstOctober()

def hadisstNovember():
    """
    A function to produce an array of November data for all 105 years.
    Note: November[year,lat,lon]
    """
    November = data_flat[5::12]
    November = np.array(November)
    data = np.reshape(November,(105,180,360))
    return November
November = hadisstNovember()

def hadisstDecember():
    """
    A function to produce an array of December data for all 105 years.
    Note: December[year,lat,lon]
    """
    December = data_flat[6::12]
    December = np.array(December)
    data = np.reshape(December,(105,180,360))
    return December
December = hadisstDecember()

def hadisstJanuary():
    """
    A function to produce an array of January data for all 105 years.
    Note: January[year,lat,lon]
    """
    January = data_flat[7::12]
    January = np.array(January)
    data = np.reshape(January,(105,180,360))
    return January
January = hadisstJanuary()

def hadisstFebruary():
    """
    A function to produce an array of Feburary data for all 105 years.
    Note: February[year,lat,lon]
    """
    February = data_flat[8::12]
    February = np.array(February)
    data = np.reshape(February,(105,180,360))
    return February
February = hadisstFebruary()

def hadisstMarch():
    """
    A function to produce an array of March data for all 105 years.
    Note: March[year,lat,lon]
    """
    March = data_flat[9::12]
    March = np.array(March)
    data = np.reshape(March,(105,180,360))
    return March
March = hadisstMarch()

def hadisstApril():
    """
    A function to produce an array of April data for all 105 years.
    Note: April[year,lat,lon]
    """
    April = data_flat[10::12]
    April = np.array(April)
    data = np.reshape(April,(105,180,360))
    return April
April = hadisstApril()

def hadisstMay():
    """
    A function to produce an array of May data for all 105 years.
    Note: May[year,lat,lon]
    """
    May = data_flat[11::12]
    May = np.array(May)
    data = np.reshape(May,(105,180,360))
    return May
May = hadisstMay()

def hadisstJJA():
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
JJA = hadisstJJA()

def hadisstSON():
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
SON = hadisstSON()

def hadisstDJF():
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
DJF = hadisstDJF()

def hadisstMAM():
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
MAM = hadisstMAM()

    
