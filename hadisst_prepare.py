"""
A set of routines to prepare HadISST1.1 sea-surface temperature data.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 21 August 2015.
"""

import netCDF4 as n
import numpy as np

from data import hadisst

from cwd import *
cwdInFunction()

data = n.Dataset(hadisst,'r')

def hadisstTrim():
    """
    A function to read in the HadISST dataset and trim it to the period
    June 1900 to May 2005.

    Note: data_flat: months,latitude,longitude
    """
    data_flat = data.variables['sst'][365:1625]
    data_flat = np.ma.masked_less(data_flat,mask)
    return data_flat

def bugFix():
    """
    A function to mask values along the dateline from 1982 onwards
    (http://hadobs.metoffice.com/hadisst/ - see the comment on
    this webpage from 13 March 2015.)  January 1982 is time '984',
    and the date-line spans longitude [0] and longitude [359]
    (-179.5 E to 179.5 E).
    This affects computation of the IPO TPI index only (not Nino3.4).
    """
    b = data_flat[:]
    b[984:,:,0:360:359] = -9999.0
    dataFix = np.ma.masked_less_equal(b,-9999.0)
    return dataFix

def hadisstAnnual():
    """
    A function to convert flat data to an array with all 105 years
    and 12 months for all latitudes and longitudes.

    Note: hadisstData[year,month,lat,lon]
    e.g. hadisstData[104,11,179,359]
         = May 2005 at 180 deg N (89.5 deg) and 360 deg E (179.5 deg E)
    """
    data = np.reshape(dataFix,(105,12,180,360))
    return data

def hadisstJune():
    """
    A function to produce an array of June data for all 105 years.
    Note: June[year,lat,lon]
    """
    June = dataFix[0::12]
    June = np.ma.masked_less(June,mask)
    data = np.reshape(June,(105,180,360))
    return June

def hadisstJuly():
    """
    A function to produce an array of July data for all 105 years.
    Note: July[year,lat,lon]
    """
    July = dataFix[1::12]
    July = np.ma.masked_less(July,mask)
    data = np.reshape(July,(105,180,360))
    return July

def hadisstAugust():
    """
    A function to produce an array of August data for all 105 years.
    Note: August[year,lat,lon]
    """
    August = dataFix[2::12]
    August = np.ma.masked_less(August,mask)
    data = np.reshape(August,(105,180,360))
    return August

def hadisstSeptember():
    """
    A function to produce an array of September data for all 105 years.
    Note: September[year,lat,lon]
    """
    September = dataFix[3::12]
    September = np.ma.masked_less(September,mask)
    data = np.reshape(September,(105,180,360))
    return September

def hadisstOctober():
    """
    A function to produce an array of October data for all 105 years.
    Note: October[year,lat,lon]
    """
    October = dataFix[4::12]
    October = np.ma.masked_less(October,mask)
    data = np.reshape(October,(105,180,360))
    return October

def hadisstNovember():
    """
    A function to produce an array of November data for all 105 years.
    Note: November[year,lat,lon]
    """
    November = dataFix[5::12]
    November = np.ma.masked_less(November,mask)
    data = np.reshape(November,(105,180,360))
    return November

def hadisstDecember():
    """
    A function to produce an array of December data for all 105 years.
    Note: December[year,lat,lon]
    """
    December = dataFix[6::12]
    December = np.ma.masked_less(December,mask)
    data = np.reshape(December,(105,180,360))
    return December

def hadisstJanuary():
    """
    A function to produce an array of January data for all 105 years.
    Note: January[year,lat,lon]
    """
    January = dataFix[7::12]
    January = np.ma.masked_less(January,mask)
    data = np.reshape(January,(105,180,360))
    return January

def hadisstFebruary():
    """
    A function to produce an array of Feburary data for all 105 years.
    Note: February[year,lat,lon]
    """
    February = dataFix[8::12]
    February = np.ma.masked_less(February,mask)
    data = np.reshape(February,(105,180,360))
    return February

def hadisstMarch():
    """
    A function to produce an array of March data for all 105 years.
    Note: March[year,lat,lon]
    """
    March = dataFix[9::12]
    March = np.ma.masked_less(March,mask)
    data = np.reshape(March,(105,180,360))
    return March

def hadisstApril():
    """
    A function to produce an array of April data for all 105 years.
    Note: April[year,lat,lon]
    """
    April = dataFix[10::12]
    April = np.ma.masked_less(April,mask)
    data = np.reshape(April,(105,180,360))
    return April

def hadisstMay():
    """
    A function to produce an array of May data for all 105 years.
    Note: May[year,lat,lon]
    """
    May = dataFix[11::12]
    May = np.ma.masked_less(May,mask)
    data = np.reshape(May,(105,180,360))
    return May

def hadisstJJA():
    """
    A function to produce an array of JJA seasonal data (average of
    all three months at each location) for all 105 years.
    Note: JJA[year,lat,lon]
    """
    JJA_flat = dataFix[0::12] + data_flat[1::12] + data_flat[2::12]
    JJA_flat /= 3.0
    JJA = np.ma.masked_less(JJA_flat,mask)
    data = np.reshape(JJA,(105,180,360))
    return JJA

def hadisstSON():
    """
    A function to produce an array of SON seasonal data (average of
    all three months at each location) for all 105 years.
    Note: SON[year,lat,lon]
    """
    SON_flat = dataFix[3::12] + data_flat[4::12] + data_flat[5::12]
    SON_flat /= 3.0
    SON = np.ma.masked_less(SON_flat,mask)
    data = np.reshape(SON,(105,180,360))
    return SON

def hadisstDJF():
    """
    A function to produce an array of DJF seasonal data (average of
    all three months at each location) for all 105 years.
    Note: DJF[year,lat,lon]
    """
    DJF_flat = dataFix[6::12] + data_flat[7::12] + data_flat[8::12]
    DJF_flat /= 3.0
    DJF = np.ma.masked_less(DJF_flat,mask)
    data = np.reshape(DJF,(105,180,360))
    return DJF

def hadisstMAM():
    """
    A function to produce an array of MAM seasonal data (average of
    all three months at each location) for all 105 years.
    Note: MAM[year,lat,lon]
    """
    MAM_flat = dataFix[9::12] + data_flat[10::12] + data_flat[11::12]
    MAM_flat /= 3.0
    MAM = np.ma.masked_less(MAM_flat,mask)
    data = np.reshape(MAM,(105,180,360))
    return MAM

#Make lat/lon data accessible for use in other files
latHad = data.variables['latitude'][:]
lonHad = data.variables['longitude'][:]
latHad_units = data.variables['latitude'].units
lonHad_units = data.variables['longitude'].units

#Prepare data for analysis
mask = -10.0 #Mask values less than -10 deg Celsius to remove no-data values of -1e+30
data_flat = hadisstTrim()
dataFix = bugFix()

#Divide into time bins

sst_Annual = hadisstAnnual()

sst_June = hadisstJune()
sst_July = hadisstJuly()
sst_August = hadisstAugust()
sst_September = hadisstSeptember()
sst_October = hadisstOctober()
sst_November = hadisstNovember()
sst_December = hadisstDecember()
sst_January = hadisstJanuary()
sst_February = hadisstFebruary()
sst_March = hadisstMarch()
sst_April = hadisstApril()
sst_May = hadisstMay()

sst_JJA = hadisstJJA()
sst_SON = hadisstSON()
sst_DJF = hadisstDJF()
sst_MAM = hadisstMAM()

