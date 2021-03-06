"""
Routines to trim the ACCESS1.3 precipitation data down to the same co-ordinates
as the AWAP dataset (-43.7 deg N to -10.0 deg N, 114.373 deg E to 155.625 deg E).
This improves the ease of comparing the two datasets.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 15 September 2015.
"""

import netCDF4 as n
import numpy as np
from numpy import ma

from cwd import *
cwdInFunction()


import access_prepare_pr
from access_prepare_pr import mask, data_flat


def accessJune():
    """
    A function to produce an array of June data for all 105 years.
    Note: June[year,lat,lon]
    """
    June = data_flat[0::12,38:65,62:84]
    June = np.ma.masked_less(June,mask)
    data = np.reshape(June,(105,27,22))
    return June

def accessJuly():
    """
    A function to produce an array of July data for all 105 years.
    Note: July[year,lat,lon]
    """
    July = data_flat[1::12,38:65,62:84]
    July = np.ma.masked_less(July,mask)
    data = np.reshape(July,(105,27,22))
    return July

def accessAugust():
    """
    A function to produce an array of August data for all 105 years.
    Note: August[year,lat,lon]
    """
    August = data_flat[2::12,38:65,62:84]
    August = np.ma.masked_less(August,mask)
    data = np.reshape(August,(105,27,22))
    return August

def accessSeptember():
    """
    A function to produce an array of September data for all 105 years.
    Note: September[year,lat,lon]
    """
    September = data_flat[3::12,38:65,62:84]
    September = np.ma.masked_less(September,mask)
    data = np.reshape(September,(105,27,22))
    return September

def accessOctober():
    """
    A function to produce an array of October data for all 105 years.
    Note: October[year,lat,lon]
    """
    October = data_flat[4::12,38:65,62:84]
    October = np.ma.masked_less(October,mask)
    data = np.reshape(October,(105,27,22))
    return October

def accessNovember():
    """
    A function to produce an array of November data for all 105 years.
    Note: November[year,lat,lon]
    """
    November = data_flat[5::12,38:65,62:84]
    November = np.ma.masked_less(November,mask)
    data = np.reshape(November,(105,27,22))
    return November

def accessDecember():
    """
    A function to produce an array of December data for all 105 years.
    Note: December[year,lat,lon]
    """
    December = data_flat[6::12,38:65,62:84]
    December = np.ma.masked_less(December,mask)
    data = np.reshape(December,(105,27,22))
    return December

def accessJanuary():
    """
    A function to produce an array of January data for all 105 years.
    Note: January[year,lat,lon]
    """
    January = data_flat[7::12,38:65,62:84]
    January = np.ma.masked_less(January,mask)
    data = np.reshape(January,(105,27,22))
    return January

def accessFebruary():
    """
    A function to produce an array of Feburary data for all 105 years.
    Note: February[year,lat,lon]
    """
    February = data_flat[8::12,38:65,62:84]
    Feburary = np.ma.masked_less(February,mask)
    data = np.reshape(February,(105,27,22))
    return February

def accessMarch():
    """
    A function to produce an array of March data for all 105 years.
    Note: March[year,lat,lon]
    """
    March = data_flat[9::12,38:65,62:84]
    March = np.ma.masked_less(March,mask)
    data = np.reshape(March,(105,27,22))
    return March

def accessApril():
    """
    A function to produce an array of April data for all 105 years.
    Note: April[year,lat,lon]
    """
    April = data_flat[10::12,38:65,62:84]
    April = np.ma.masked_less(April,mask)
    data = np.reshape(April,(105,27,22))
    return April

def accessMay():
    """
    A function to produce an array of May data for all 105 years.
    Note: May[year,lat,lon]
    """
    May = data_flat[11::12,38:65,62:84]
    May = np.ma.masked_less(May,mask)
    data = np.reshape(May,(105,27,22))
    return May

def accessJJA():
    """
    A function to produce an array of JJA seasonal data (average of
    all three months at each location) for all 105 years.
    Note: JJA[year,lat,lon]
    """
    JJA_flat = data_flat[0::12,38:65,62:84] + data_flat[1::12,38:65,62:84] \
               + data_flat[2::12,38:65,62:84]
    JJA_flat /= 3.0
    JJA = np.ma.masked_less(JJA_flat,mask)
    data = np.reshape(JJA,(105,27,22))
    return JJA

def accessSON():
    """
    A function to produce an array of SON seasonal data (average of
    all three months at each location) for all 105 years.
    Note: SON[year,lat,lon]
    """
    SON_flat = data_flat[3::12,38:65,62:84] + data_flat[4::12,38:65,62:84] + \
               data_flat[5::12,38:65,62:84]
    SON_flat /= 3.0
    SON = np.ma.masked_less(SON_flat,mask)
    data = np.reshape(SON,(105,27,22))
    return SON

def accessDJF():
    """
    A function to produce an array of DJF seasonal data (average of
    all three months at each location) for all 105 years.
    Note: DJF[year,lat,lon]
    """
    DJF_flat = data_flat[6::12,38:65,62:84] + data_flat[7::12,38:65,62:84] + \
               data_flat[8::12,38:65,62:84]
    DJF_flat /= 3.0
    DJF = np.ma.masked_less(DJF_flat,mask)
    data = np.reshape(DJF,(105,27,22))
    return DJF

def accessMAM():
    """
    A function to produce an array of MAM seasonal data (average of
    all three months at each location) for all 105 years.
    Note: MAM[year,lat,lon]
    """
    MAM_flat = data_flat[9::12,38:65,62:84] + data_flat[10::12,38:65,62:84] + \
               data_flat[11::12,38:65,62:84]
    MAM_flat /= 3.0
    MAM = np.ma.masked_less(MAM_flat,mask)
    data = np.reshape(MAM,(105,27,22))
    return MAM

def trimAnnual():
    """
    A function to trim annual data to -43.7 deg N to -8.75 deg N,
    114.373 deg E to 153.75 deg E

    Note: accessData[year,month,lat,lon]
    e.g. accessData[104,0,0]
         = 2005 at -43.75 deg N and 114.375 deg E

    data.variables['lat'][37:64] - corresponds with data_flat[38:65,62:84]
    data.variables['lon'][61:83]
    """
    annual_flat = data_flat[0::12,38:65,62:84] + data_flat[1::12,38:65,62:84]+\
               data_flat[2::12,38:65,62:84] + data_flat[3::12,38:65,62:84] + \
               data_flat[4::12,38:65,62:84] + data_flat[5::12,38:65,62:84] + \
               data_flat[6::12,38:65,62:84] + data_flat[7::12,38:65,62:84] + \
               data_flat[8::12,38:65,62:84] + data_flat[9::12,38:65,62:84] + \
               data_flat[10::12,38:65,62:84] + data_flat[11::12,38:65,62:84]
    annual_flat /= 12.0
    annual = np.ma.masked_less(annual_flat,mask)
    annual = np.reshape(annual,(105,27,22))
    return annual

def output():
    """
    Produces annual, seasonal and monthly data.
    """
    trim_Annual = trimAnnual()
    trim_June = accessJune()
    trim_July = accessJuly()
    trim_August = accessAugust()
    trim_September = accessSeptember()
    trim_October = accessOctober()
    trim_November = accessNovember()
    trim_December = accessDecember()
    trim_January = accessJanuary()
    trim_February = accessFebruary()
    trim_March = accessMarch()
    trim_April = accessApril()
    trim_May = accessMay()
    trim_JJA = accessJJA()
    trim_SON = accessSON()
    trim_DJF = accessDJF()
    trim_MAM = accessMAM()

    return trim_Annual,trim_June, trim_July,\
     trim_August,trim_September,trim_October,trim_November,\
     trim_December,trim_January,trim_February,trim_March,\
     trim_April,trim_May,trim_JJA,trim_SON,trim_DJF,trim_MAM

trim = output()
(trim_Annual,trim_June, trim_July,\
     trim_August,trim_September,trim_October,trim_November,\
     trim_December,trim_January,trim_February,trim_March,\
     trim_April,trim_May,trim_JJA,trim_SON,trim_DJF,trim_MAM) = trim

