"""
A set of routines to prepare AWAP precipitation data
(Run 26j) for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 15 September 2015.
"""

import netCDF4 as n
import numpy as np

from data import awap

from cwd import *
cwdInFunction()

data = n.Dataset(awap,'a')

def lat(num_lat):
    """
    A function to replace empty latitudinal values in the resampled
    AWAP dataset with actual latitudinal values.

    num_lat : 27 or 670
    """
    start = -43.75
    newlist = []
    for i in range(0,num_lat):
        i = start
        newlist.append(i)
        start += 1.25
    data.variables['latitude'][:] = newlist[:]
    return data.variables['latitude'][:]

def lon(num_lon):
    """
    A function to replace empty longitudinal values in the resampled
    AWAP dataset with actual longitudinal values.

    num_long : 22 or 813
    """
    start_lon = 114.375
    newlist_lon = []
    for i in range(0,num_lon):
        i = start_lon
        newlist_lon.append(i)
        start_lon += 1.875
    data.variables['longitude'][:] = newlist_lon[:]
    return data.variables['longitude'][:]

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

def awapJune(len_lat,len_lon):
    """
    A function to produce an array of June data for all 105 years.
    Note: June[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    June = data_flat[0::12]
    June = np.ma.masked_less(June,mask)
    data = np.reshape(June,(105,len_lat,len_lon))
    return June

def awapJuly(len_lat,len_lon):
    """
    A function to produce an array of July data for all 105 years.
    Note: July[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    July = data_flat[1::12]
    July = np.ma.masked_less(July,mask)
    data = np.reshape(July,(105,len_lat,len_lon))
    return July

def awapAugust(len_lat,len_lon):
    """
    A function to produce an array of August data for all 105 years.
    Note: August[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    August = data_flat[2::12]
    August = np.ma.masked_less(August,mask)
    data = np.reshape(August,(105,len_lat,len_lon))
    return August

def awapSeptember(len_lat,len_lon):
    """
    A function to produce an array of September data for all 105 years.
    Note: September[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    September = data_flat[3::12]
    September = np.ma.masked_less(September,mask)
    data = np.reshape(September,(105,len_lat,len_lon))
    return September

def awapOctober(len_lat,len_lon):
    """
    A function to produce an array of October data for all 105 years.
    Note: October[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    October = data_flat[4::12]
    October = np.ma.masked_less(October,mask)
    data = np.reshape(October,(105,len_lat,len_lon))
    return October

def awapNovember(len_lat,len_lon):
    """
    A function to produce an array of November data for all 105 years.
    Note: November[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    November = data_flat[5::12]
    November = np.ma.masked_less(November,mask)
    data = np.reshape(November,(105,len_lat,len_lon))
    return November

def awapDecember(len_lat,len_lon):
    """
    A function to produce an array of December data for all 105 years.
    Note: December[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    December = data_flat[6::12]
    December = np.ma.masked_less(December,mask)
    data = np.reshape(December,(105,len_lat,len_lon))
    return December

def awapJanuary(len_lat,len_lon):
    """
    A function to produce an array of January data for all 105 years.
    Note: January[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    January = data_flat[7::12]
    January = np.ma.masked_less(January,mask)
    data = np.reshape(January,(105,len_lat,len_lon))
    return January

def awapFebruary(len_lat,len_lon):
    """
    A function to produce an array of Feburary data for all 105 years.
    Note: February[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    February = data_flat[8::12]
    February = np.ma.masked_less(February,mask)
    data = np.reshape(February,(105,len_lat,len_lon))
    return February

def awapMarch(len_lat,len_lon):
    """
    A function to produce an array of March data for all 105 years.
    Note: March[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    March = data_flat[9::12]
    March = np.ma.masked_less(March,mask)
    data = np.reshape(March,(105,len_lat,len_lon))
    return March

def awapApril(len_lat,len_lon):
    """
    A function to produce an array of April data for all 105 years.
    Note: April[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    April = data_flat[10::12]
    April = np.ma.masked_less(April,mask)
    data = np.reshape(April,(105,len_lat,len_lon))
    return April

def awapMay(len_lat,len_lon):
    """
    A function to produce an array of May data for all 105 years.
    Note: May[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    May = data_flat[11::12]
    May = np.ma.masked_less(May,mask)
    data = np.reshape(May,(105,len_lat,len_lon))
    return May

def awapJJA(len_lat,len_lon):
    """
    A function to produce an array of JJA seasonal data (average of
    all three months at each location) for all 105 years.
    Note: JJA[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    JJA_flat = data_flat[0::12] + data_flat[1::12] + data_flat[2::12]
    JJA_flat /= 3.0
    JJA = np.ma.masked_less(JJA_flat,mask)
    data = np.reshape(JJA,(105,len_lat,len_lon))
    return JJA

def awapSON(len_lat,len_lon):
    """
    A function to produce an array of SON seasonal data (average of
    all three months at each location) for all 105 years.
    Note: SON[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    SON_flat = data_flat[3::12] + data_flat[4::12] + data_flat[5::12]
    SON_flat /= 3.0
    SON = np.ma.masked_less(SON_flat,mask)
    data = np.reshape(SON,(105,len_lat,len_lon))
    return SON

def awapDJF(len_lat,len_lon):
    """
    A function to produce an array of DJF seasonal data (average of
    all three months at each location) for all 105 years.
    Note: DJF[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    DJF_flat = data_flat[6::12] + data_flat[7::12] + data_flat[8::12]
    DJF_flat /= 3.0
    DJF = np.ma.masked_less(DJF_flat,mask)
    data = np.reshape(DJF,(105,len_lat,len_lon))
    return DJF

def awapMAM(len_lat,len_lon):
    """
    A function to produce an array of MAM seasonal data (average of
    all three months at each location) for all 105 years.
    Note: MAM[year,lat,lon]

    len_lat : 27
    len_lon : 22
    """
    MAM_flat = data_flat[9::12] + data_flat[10::12] + data_flat[11::12]
    MAM_flat /= 3.0
    MAM = np.ma.masked_less(MAM_flat,mask)
    data = np.reshape(MAM,(105,len_lat,len_lon))
    return MAM

def awapAnnual(len_lat,len_lon):
    """
    A function to convert flat data to an array with all 105 years
    for all latitudes and longitudes.

    Note: awapAnnual[year,lat,lon]
    e.g. awapAnnual[104,26,22]
         = 2005 at -11.25 deg N and 153.75 deg E

    len_lat : 27
    len_lon : 22
    """
    annual_flat = data_flat[0::12] + data_flat[1::12] + data_flat[2::12] + \
                  data_flat[3::12] + data_flat[4::12] + data_flat[5::12] + \
                  data_flat[6::12] + data_flat[7::12] + data_flat[8::12] + \
                  data_flat[9::12] + data_flat[10::12] + data_flat[11::12]
    annual_flat /= 12.0
    annual = np.ma.masked_less(annual_flat,mask)
    annual = np.reshape(annual,(105,len_lat,len_lon))
    return annual

def awap1900(len_lat,len_lon):
    """
    A function to create an array of Jan 1900 to Dec 1900, so that mapped output
    can be produced that directly compares interpolated/uninterpolated data.
    """
    year1900 = dataDay[0:12]
    year1900 = np.ma.masked_less(year1900,mask)
    year1900_data = np.reshape(year1900,(12,len_lat,len_lon))
    year1900_data_av = np.ma.mean(year1900_data,axis=0)
    return year1900_data_av
    

#Update lon/lat values
longitude = lon(num_lon=22)
latitude = lat(num_lat=27)
awap_lat_units = data.variables['latitude'].units
awap_lon_units = data.variables['longitude'].units

#Prepare data for analysis
mask = 0.0 #Mask values less than 0 (cannot have negative rainfall)
dataDay = m2mm()
data_flat = awapTrim()

#Divide into time bins
awap_Annual = awapAnnual(27,22)

awap_June = awapJune(27,22)
awap_July = awapJuly(27,22)
awap_August = awapAugust(27,22)
awap_September = awapSeptember(27,22)
awap_October = awapOctober(27,22)
awap_November = awapNovember(27,22)
awap_December = awapDecember(27,22)
awap_January = awapJanuary(27,22)
awap_February = awapFebruary(27,22)
awap_March = awapMarch(27,22)
awap_April = awapApril(27,22)
awap_May = awapMay(27,22)

awap_JJA = awapJJA(27,22)
awap_SON = awapSON(27,22)
awap_DJF = awapDJF(27,22)
awap_MAM = awapMAM(27,22)

#Make Jan 1900-Dec 1900
year1900 = awap1900(27,22)
