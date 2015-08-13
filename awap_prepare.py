"""
A set of routines to prepare AWAP precipitation data
for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 13 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

data = n.Dataset('AWAP_1900-2014_monthly_precip_swACCESSgrid_v4.nc','r')

def awapMissing():
    dataSST = data.variables['AWAP_precipitation'][:]
    dataMiss = np.ma.masked_equal(dataSST,-9999.0)
    return dataMiss

#Create function to accommodate for changes around dateline in 1982 onwards

def awapTrim():
    """
    A function to read in the HadISST dataset and trim it to the period
    June 1900 to May 2005.

    Note: data_flat: months,latitude,longitude
    """
    full_data = dataMiss
    data_flat = dataMiss[5:1265]
    return data_flat

def awapAnnual():
    """
    A function to convert flat data to an array with all 105 years
    and 12 months for all latitudes and longitudes.

    Note: hadisstData[year,month,lat,lon]
    e.g. hadisstData[104,11,179,359]
         = May 2005 at 180 deg N (89.5 deg) and 360 deg E (179.5 deg E)
    """
    data = np.array(data_flat)
    data = np.reshape(data,(105,12,27,22))
    return data

def awapJune():
    """
    A function to produce an array of June data for all 105 years.
    Note: June[year,lat,lon]
    """
    June = data_flat[0::12]
    June = np.array(June)
    data = np.reshape(June,(105,27,22))
    return June

def awapJuly():
    """
    A function to produce an array of July data for all 105 years.
    Note: July[year,lat,lon]
    """
    July = data_flat[1::12]
    July = np.array(July)
    data = np.reshape(July,(105,27,22))
    return July

def awapAugust():
    """
    A function to produce an array of August data for all 105 years.
    Note: August[year,lat,lon]
    """
    August = data_flat[2::12]
    August = np.array(August)
    data = np.reshape(August,(105,27,22))
    return August

def awapSeptember():
    """
    A function to produce an array of September data for all 105 years.
    Note: September[year,lat,lon]
    """
    September = data_flat[3::12]
    September = np.array(September)
    data = np.reshape(September,(105,27,22))
    return September

def awapOctober():
    """
    A function to produce an array of October data for all 105 years.
    Note: October[year,lat,lon]
    """
    October = data_flat[4::12]
    October = np.array(October)
    data = np.reshape(October,(105,27,22))
    return October

def awapNovember():
    """
    A function to produce an array of November data for all 105 years.
    Note: November[year,lat,lon]
    """
    November = data_flat[5::12]
    November = np.array(November)
    data = np.reshape(November,(105,27,22))
    return November

def awapDecember():
    """
    A function to produce an array of December data for all 105 years.
    Note: December[year,lat,lon]
    """
    December = data_flat[6::12]
    December = np.array(December)
    data = np.reshape(December,(105,27,22))
    return December

def awapJanuary():
    """
    A function to produce an array of January data for all 105 years.
    Note: January[year,lat,lon]
    """
    January = data_flat[7::12]
    January = np.array(January)
    data = np.reshape(January,(105,27,22))
    return January

def awapFebruary():
    """
    A function to produce an array of Feburary data for all 105 years.
    Note: February[year,lat,lon]
    """
    February = data_flat[8::12]
    February = np.array(February)
    data = np.reshape(February,(105,27,22))
    return February

def awapMarch():
    """
    A function to produce an array of March data for all 105 years.
    Note: March[year,lat,lon]
    """
    March = data_flat[9::12]
    March = np.array(March)
    data = np.reshape(March,(105,27,22))
    return March

def awapApril():
    """
    A function to produce an array of April data for all 105 years.
    Note: April[year,lat,lon]
    """
    April = data_flat[10::12]
    April = np.array(April)
    data = np.reshape(April,(105,27,22))
    return April

def awapMay():
    """
    A function to produce an array of May data for all 105 years.
    Note: May[year,lat,lon]
    """
    May = data_flat[11::12]
    May = np.array(May)
    data = np.reshape(May,(105,27,22))
    return May

def awapJJA():
    """
    A function to produce an array of JJA seasonal data (average of
    all three months at each location) for all 105 years.
    Note: JJA[year,lat,lon]
    """
    JJA_flat = data_flat[0::12] + data_flat[1::12] + data_flat[2::12]
    JJA_flat /= 3.0
    JJA = np.array(JJA_flat)
    data = np.reshape(JJA,(105,27,22))
    return JJA

def awapSON():
    """
    A function to produce an array of SON seasonal data (average of
    all three months at each location) for all 105 years.
    Note: SON[year,lat,lon]
    """
    SON_flat = data_flat[3::12] + data_flat[4::12] + data_flat[5::12]
    SON_flat /= 3.0
    SON = np.array(SON_flat)
    data = np.reshape(SON,(105,27,22))
    return SON

def awapDJF():
    """
    A function to produce an array of DJF seasonal data (average of
    all three months at each location) for all 105 years.
    Note: DJF[year,lat,lon]
    """
    DJF_flat = data_flat[6::12] + data_flat[7::12] + data_flat[8::12]
    DJF_flat /= 3.0
    DJF = np.array(DJF_flat)
    data = np.reshape(DJF,(105,27,22))
    return DJF

def awapMAM():
    """
    A function to produce an array of MAM seasonal data (average of
    all three months at each location) for all 105 years.
    Note: MAM[year,lat,lon]
    """
    MAM_flat = data_flat[9::12] + data_flat[10::12] + data_flat[11::12]
    MAM_flat /= 3.0
    MAM = np.array(MAM_flat)
    data = np.reshape(MAM,(105,27,22))
    return MAM

#Prepare data for analysis
dataMiss = awapMissing()
data_flat = awapTrim()

#Divide into time bins

awap_Annual = awapAnnual()

awap_June = awapJune()
awap_July = awapJuly()
awap_August = awapAugust()
awap_September = awapSeptember()
awap_October = awapOctober()
awap_November = awapNovember()
awap_December = awapDecember()
awap_January = awapJanuary()
awap_February = awapFebruary()
awap_March = awapMarch()
awap_April = awapApril()
awap_May = awapMay()

awap_JJA = awapJJA()
awap_SON = awapSON()
awap_DJF = awapDJF()
awap_MAM = awapMAM()
