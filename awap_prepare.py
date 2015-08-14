"""
A set of routines to prepare AWAP precipitation data
for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 14 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

data = n.Dataset('AWAP_1900-2014_monthly_precip_swACCESSgrid_v4.nc','a')

def lat():
    """
    A function to replace empty latitudinal values in the resampled
    AWAP dataset with actual latitudinal values.
    """
    start = -43.75
    newlist = []
    for i in range(0,27):
        i = start
        newlist.append(i)
        start += 1.25
    data.variables['latitude'][:] = newlist[:]

def lon():
    """
    A function to replace empty longitudinal values in the resampled
    AWAP dataset with actual longitudinal values.
    """
    start_lon = 114.375
    newlist_lon = []
    for i in range(0,22):
        i = start_lon
        newlist_lon.append(i)
        start_lon += 1.875
    data.variables['longitude'][:] = newlist_lon[:]   

def m2mm():
    """
    A function to convert precipitation units from metres/day to mm/day,
    so results can be directly compared with ACCESS precipitation data.
    """
    dataDay = data.variables['AWAP_precipitation'][:]
    for i in dataDay:
        i *= 1000
    return dataDay

def awapTrim():
    """
    A function to read in the HadISST dataset and trim it to the period
    June 1900 to May 2005.

    Note: data_flat: months,latitude,longitude
    """
    data_flat = dataDay[5:1265]
    data_flat = np.ma.masked_less(data_flat,mask)
    return data_flat

def awapAnnual():
    """
    A function to convert flat data to an array with all 105 years
    and 12 months for all latitudes and longitudes.

    Note: awapAnnual[year,month,lat,lon]
    e.g. awapAnnual[104,11,26,22]
         = May 2005 at -11.25 deg N and 153.75 deg E
    """
    data = np.reshape(data_flat,(105,12,27,22))
    return data

def awapJune():
    """
    A function to produce an array of June data for all 105 years.
    Note: June[year,lat,lon]
    """
    June = data_flat[0::12]
    June = np.ma.masked_less(June,mask)
    data = np.reshape(June,(105,27,22))
    return June

def awapJuly():
    """
    A function to produce an array of July data for all 105 years.
    Note: July[year,lat,lon]
    """
    July = data_flat[1::12]
    July = np.ma.masked_less(July,mask)
    data = np.reshape(July,(105,27,22))
    return July

def awapAugust():
    """
    A function to produce an array of August data for all 105 years.
    Note: August[year,lat,lon]
    """
    August = data_flat[2::12]
    August = np.ma.masked_less(August,mask)
    data = np.reshape(August,(105,27,22))
    return August

def awapSeptember():
    """
    A function to produce an array of September data for all 105 years.
    Note: September[year,lat,lon]
    """
    September = data_flat[3::12]
    September = np.ma.masked_less(September,mask)
    data = np.reshape(September,(105,27,22))
    return September

def awapOctober():
    """
    A function to produce an array of October data for all 105 years.
    Note: October[year,lat,lon]
    """
    October = data_flat[4::12]
    October = np.ma.masked_less(October,mask)
    data = np.reshape(October,(105,27,22))
    return October

def awapNovember():
    """
    A function to produce an array of November data for all 105 years.
    Note: November[year,lat,lon]
    """
    November = data_flat[5::12]
    November = np.ma.masked_less(November,mask)
    data = np.reshape(November,(105,27,22))
    return November

def awapDecember():
    """
    A function to produce an array of December data for all 105 years.
    Note: December[year,lat,lon]
    """
    December = data_flat[6::12]
    December = np.ma.masked_less(December,mask)
    data = np.reshape(December,(105,27,22))
    return December

def awapJanuary():
    """
    A function to produce an array of January data for all 105 years.
    Note: January[year,lat,lon]
    """
    January = data_flat[7::12]
    January = np.ma.masked_less(January,mask)
    data = np.reshape(January,(105,27,22))
    return January

def awapFebruary():
    """
    A function to produce an array of Feburary data for all 105 years.
    Note: February[year,lat,lon]
    """
    February = data_flat[8::12]
    February = np.ma.masked_less(February,mask)
    data = np.reshape(February,(105,27,22))
    return February

def awapMarch():
    """
    A function to produce an array of March data for all 105 years.
    Note: March[year,lat,lon]
    """
    March = data_flat[9::12]
    March = np.ma.masked_less(March,mask)
    data = np.reshape(March,(105,27,22))
    return March

def awapApril():
    """
    A function to produce an array of April data for all 105 years.
    Note: April[year,lat,lon]
    """
    April = data_flat[10::12]
    April = np.ma.masked_less(April,mask)
    data = np.reshape(April,(105,27,22))
    return April

def awapMay():
    """
    A function to produce an array of May data for all 105 years.
    Note: May[year,lat,lon]
    """
    May = data_flat[11::12]
    May = np.ma.masked_less(May,mask)
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
    JJA = np.ma.masked_less(JJA_flat,mask)
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
    SON = np.ma.masked_less(SON_flat,mask)
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
    DJF = np.ma.masked_less(DJF_flat,mask)
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
    MAM = np.ma.masked_less(MAM_flat,mask)
    data = np.reshape(MAM,(105,27,22))
    return MAM

#Update lon/lat values
longitude = lon()
latitude = lat()
awap_lat_units = data.variables['latitude'].units
awap_lon_units = data.variables['longitude'].units
awap_units = data.variables['AWAP_precipitation'].units

#Prepare data for analysis
mask = 0.0 #Mask values less than 0 (cannot have negative rainfall)
dataDay = m2mm()
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
