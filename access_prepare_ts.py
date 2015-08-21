"""
Script to prepare ACCESS1.3 sea surface temperature data for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 21 August 2015.
"""

import netCDF4 as n
import numpy as np
from numpy import ma

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

from data import access_ts_r1, access_ts_r2, access_ts_r3

from cwd import *
cwdInFunction()

#Make sure to run with (a) correct data, and (b) all three runs
"""
Choose data to analyse: access_pr_r1, access_pr_r2, access_pr_r3
"""
data_in = raw_input('Enter the data for analysis: ')
if data_in == 'access_ts_r1':
    data_in = access_ts_r1
elif data_in == 'access_ts_r2':
    data_in = access_ts_r2
else:
    data_in = access_ts_r3
data = n.Dataset(data_in,'r')

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
    return dataCelsius

def accessTrim():
    """
    A function to read in an ACCESS dataset and trim it to the period
    June 1900 to May 2005.

    Note: data_flat: months,latitude,longitude
    """
    data1 = dataCelsius[605:1865]
    data_flat = np.ma.masked_outside(data1,Min,Max)
    return data_flat

def bugHad():
    """
    A function to allow direct comparison with the HadiSST dataset,
    which has a discontinuity at the dateline (see 'bugfix()' in
    'hadisst_prepare.py'). 

    January 1982 is time '984', and the date-line is longitude [96] (180 E).
    This affects computation of the IPO TPI index only (not Nino3.4).
    """
    b = data_flat[:]
    b[984:,:,96] = -9999.0
    dataFix = np.ma.masked_less_equal(b,-9999.0)
    return dataFix

def accessAnnual():
    """
    A function to convert flat data to an array with all 105 years
    and 12 months for all latitudes and longitudes.

    Note: accessData[year,month,lat,lon]
    e.g. accessData[104,11,144,191]
         = May 2005 at -180 deg N (-90 deg S) and 0 deg E (0 deg E = prime meridian)
    """
    data = np.reshape(dataFix,(105,12,145,192))
    return data

    """
    data = np.reshape(dataFix,(105,12,145,192))
    for i in data:
        data[i] = np.mean[...]
    return data

    new = np.zeros(105)
    print new
    count = 0
    a = 0
    b = 12
    for i in dataFix:
        new[count] = np.mean(dataFix[a:b:,:,:])
        print new[count]
        a += 12
        b += 12
        count +=1

    data = np.reshape(new,(105,145,192))
    return data
    """

def accessJune():
    """
    A function to produce an array of June data for all 105 years.
    Note: June[year,lat,lon]
    """
    June = dataFix[0::12]
    June = np.ma.masked_outside(June,Min,Max)
    data = np.reshape(June,(105,145,192))
    return June

def accessJuly():
    """
    A function to produce an array of July data for all 105 years.
    Note: July[year,lat,lon]
    """
    July = dataFix[1::12]
    July = np.ma.masked_outside(July,Min,Max)
    data = np.reshape(July,(105,145,192))
    return July

def accessAugust():
    """
    A function to produce an array of August data for all 105 years.
    Note: August[year,lat,lon]
    """
    August = dataFix[2::12]
    August = np.ma.masked_outside(August,Min,Max)
    data = np.reshape(August,(105,145,192))
    return August

def accessSeptember():
    """
    A function to produce an array of September data for all 105 years.
    Note: September[year,lat,lon]
    """
    September = dataFix[3::12]
    September = np.ma.masked_outside(September,Min,Max)
    data = np.reshape(September,(105,145,192))
    return September

def accessOctober():
    """
    A function to produce an array of October data for all 105 years.
    Note: October[year,lat,lon]
    """
    October = dataFix[4::12]
    October = np.ma.masked_outside(October,Min,Max)
    data = np.reshape(October,(105,145,192))
    return October

def accessNovember():
    """
    A function to produce an array of November data for all 105 years.
    Note: November[year,lat,lon]
    """
    November = dataFix[5::12]
    November = np.ma.masked_outside(November,Min,Max)
    data = np.reshape(November,(105,145,192))
    return November

def accessDecember():
    """
    A function to produce an array of December data for all 105 years.
    Note: December[year,lat,lon]
    """
    December = dataFix[6::12]
    December = np.ma.masked_outside(December,Min,Max)
    data = np.reshape(December,(105,145,192))
    return December

def accessJanuary():
    """
    A function to produce an array of January data for all 105 years.
    Note: January[year,lat,lon]
    """
    January = dataFix[7::12]
    January = np.ma.masked_outside(January,Min,Max)
    data = np.reshape(January,(105,145,192))
    return January

def accessFebruary():
    """
    A function to produce an array of Feburary data for all 105 years.
    Note: February[year,lat,lon]
    """
    February = dataFix[8::12]
    February = np.ma.masked_outside(February,Min,Max)
    data = np.reshape(February,(105,145,192))
    return February

def accessMarch():
    """
    A function to produce an array of March data for all 105 years.
    Note: March[year,lat,lon]
    """
    March = dataFix[9::12]
    March = np.ma.masked_outside(March,Min,Max)
    data = np.reshape(March,(105,145,192))
    return March

def accessApril():
    """
    A function to produce an array of April data for all 105 years.
    Note: April[year,lat,lon]
    """
    April = dataFix[10::12]
    April = np.ma.masked_outside(April,Min,Max)
    data = np.reshape(April,(105,145,192))
    return April

def accessMay():
    """
    A function to produce an array of May data for all 105 years.
    Note: May[year,lat,lon]
    """
    May = dataFix[11::12]
    May = np.ma.masked_outside(May,Min,Max)
    data = np.reshape(May,(105,145,192))
    return May

def accessJJA():
    """
    A function to produce an array of JJA seasonal data (average of
    all three months at each location) for all 105 years.
    Note: JJA[year,lat,lon]
    """
    JJA_flat = dataFix[0::12] + dataFix[1::12] + dataFix[2::12]
    JJA_flat /= 3.0
    JJA = np.ma.masked_outside(JJA_flat,Min,Max)
    data = np.reshape(JJA,(105,145,192))
    return JJA

def accessSON():
    """
    A function to produce an array of SON seasonal data (average of
    all three months at each location) for all 105 years.
    Note: SON[year,lat,lon]
    """
    SON_flat = dataFix[3::12] + dataFix[4::12] + dataFix[5::12]
    SON_flat /= 3.0
    SON = np.ma.masked_outside(SON_flat,Min,Max)
    data = np.reshape(SON,(105,145,192))
    return SON

def accessDJF():
    """
    A function to produce an array of DJF seasonal data (average of
    all three months at each location) for all 105 years.
    Note: DJF[year,lat,lon]
    """
    DJF_flat = dataFix[6::12] + dataFix[7::12] + dataFix[8::12]
    DJF_flat /= 3.0
    DJF = np.ma.masked_outside(DJF_flat,Min,Max)
    data = np.reshape(DJF,(105,145,192))
    return DJF

def accessMAM():
    """
    A function to produce an array of MAM seasonal data (average of
    all three months at each location) for all 105 years.
    Note: MAM[year,lat,lon]
    """
    MAM_flat = dataFix[9::12] + dataFix[10::12] + dataFix[11::12]
    MAM_flat /= 3.0
    MAM = np.ma.masked_outside(MAM_flat,Min,Max)
    data = np.reshape(MAM,(105,145,192))
    return MAM

#Prepare data for analysis
Min = -2.0
Max = 35.0
dataCelsius = KtoC()
data_flat = accessTrim()
dataFix = bugHad()

#Divide into time bins

ts_Annual = accessAnnual()

ts_June = accessJune()
ts_July = accessJuly()
ts_August = accessAugust()
ts_September = accessSeptember()
ts_October = accessOctober()
ts_November = accessNovember()
ts_December = accessDecember()
ts_January = accessJanuary()
ts_February = accessFebruary()
ts_March = accessMarch()
ts_April = accessApril()
ts_May = accessMay()

ts_JJA = accessJJA()
ts_SON = accessSON()
ts_DJF = accessDJF()
ts_MAM = accessMAM()
