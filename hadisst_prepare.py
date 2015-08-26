"""
A set of routines to prepare HadISST1.1 sea-surface temperature data.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 25 August 2015.
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

def hadisstTrimExt():
    """
    A function to read in the HadISST dataset and trim it to the period
    January 1900 to December 2005.  For use in computing Nino3.4 running
    means and ENSO phases (see enso.py).

    Note: data_flat: months,latitude,longitude
    """
    data_flat_ext = data.variables['sst'][360:1632]
    data_flat_ext = np.ma.masked_less(data_flat_ext,mask)
    return data_flat_ext

def bugFix(dataset,ext=False):
    """
    A function to mask values along the dateline from 1982 onwards
    (http://hadobs.metoffice.com/hadisst/ - see the comment on
    this webpage from 13 March 2015.)  January 1982 is time '984',
    and the date-line spans longitude [0] and longitude [359]
    (-179.5 E to 179.5 E).
    This affects computation of the IPO TPI index only (not Nino3.4).

    Parameters:
    -----------
    dataset : Either data_flat or data_flat_ext
    ext : (default = False)
            If the dataset has been extended to Jan 1900-Dec 2005,
            ext should be set to 'True'.  In this case, the timeslice
            changes to accommodate for the extra five months at the
            beginning of the extended dataset.
    """
    b = dataset[:]
    if ext==False:
        b[984:,:,0:360:359] = -9999.0
    else:
        b[989:,:,0:360:359] = -9999.0
    dataFix = np.ma.masked_less_equal(b,-9999.0)
    return dataFix

"""
#Can only be used with 105 year data.
def hadisstAnnual():
    
    A function to convert flat data to an array with all 105 years
    and 12 months for all latitudes and longitudes.

    Note: hadisstData[year,month,lat,lon]
    e.g. hadisstData[104,11,179,359]
         = May 2005 at 180 deg N (89.5 deg) and 360 deg E (179.5 deg E)

    NB: can currently only be used with 105 year data (e.g. data_flat).
    
    data = np.reshape(dataFix,(105,12,180,360))
    return data
"""

def hadisstJune(years,start):
    """
    A function to produce an array of June data for all 105 years.
    Note: June[year,lat,lon]

    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 0
            For 106 years = 5
    """
    June = dataFix[start::12]
    June = np.ma.masked_less(June,mask)
    data = np.reshape(June,(years,180,360))
    return June

def hadisstJuly(years,start):
    """
    A function to produce an array of July data for all 105 years.
    Note: July[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 1
            For 106 years = 6
    """
    July = dataFix[start::12]
    July = np.ma.masked_less(July,mask)
    data = np.reshape(July,(years,180,360))
    return July

def hadisstAugust(years,start):
    """
    A function to produce an array of August data for all 105 years.
    Note: August[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 2
            For 106 years = 7
    """
    August = dataFix[start::12]
    August = np.ma.masked_less(August,mask)
    data = np.reshape(August,(years,180,360))
    return August

def hadisstSeptember(years,start):
    """
    A function to produce an array of September data for all 105 years.
    Note: September[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 3
            For 106 years = 8
    """
    September = dataFix[start::12]
    September = np.ma.masked_less(September,mask)
    data = np.reshape(September,(years,180,360))
    return September

def hadisstOctober(years,start):
    """
    A function to produce an array of October data for all 105 years.
    Note: October[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 4
            For 106 years = 9
    """
    October = dataFix[start::12]
    October = np.ma.masked_less(October,mask)
    data = np.reshape(October,(years,180,360))
    return October

def hadisstNovember(years,start):
    """
    A function to produce an array of November data for all 105 years.
    Note: November[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 5
            For 106 years = 10
    """
    November = dataFix[start::12]
    November = np.ma.masked_less(November,mask)
    data = np.reshape(November,(years,180,360))
    return November

def hadisstDecember(years,start):
    """
    A function to produce an array of December data for all 105 years.
    Note: December[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 6
            For 106 years = 11
    """
    December = dataFix[start::12]
    December = np.ma.masked_less(December,mask)
    data = np.reshape(December,(years,180,360))
    return December

def hadisstJanuary(years,start):
    """
    A function to produce an array of January data for all 105 years.
    Note: January[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 7
            For 106 years = 0
    """
    January = dataFix[start::12]
    January = np.ma.masked_less(January,mask)
    data = np.reshape(January,(years,180,360))
    return January

def hadisstFebruary(years,start):
    """
    A function to produce an array of Feburary data for all 105 years.
    Note: February[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 8
            For 106 years = 1
    """
    February = dataFix[start::12]
    February = np.ma.masked_less(February,mask)
    data = np.reshape(February,(years,180,360))
    return February

def hadisstMarch(years,start):
    """
    A function to produce an array of March data for all 105 years.
    Note: March[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 9
            For 106 years = 2
    """
    March = dataFix[start::12]
    March = np.ma.masked_less(March,mask)
    data = np.reshape(March,(years,180,360))
    return March

def hadisstApril(years,start):
    """
    A function to produce an array of April data for all 105 years.
    Note: April[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 10
            For 106 years = 3
    """
    April = dataFix[start::12]
    April = np.ma.masked_less(April,mask)
    data = np.reshape(April,(years,180,360))
    return April

def hadisstMay(years,start):
    """
    A function to produce an array of May data for all 105 years.
    Note: May[year,lat,lon]
    
    Parameters:
    -----------
    years: the number of years recording this month.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start: the index to start slicing from (coinciding with the
            first instance of this month).
            For 105 years = 11
            For 106 years = 4
    """
    May = dataFix[start::12]
    May = np.ma.masked_less(May,mask)
    data = np.reshape(May,(years,180,360))
    return May

def hadisstJJA(years,start1,start2,start3):
    """
    A function to produce an array of JJA seasonal data (average of
    all three months at each location) for all 105 years.
    Note: JJA[year,lat,lon]

    Parameters:
    -----------
    years: the number of years recording this seasons.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start1: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 0
            For 106 years = 5
    start2: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 1
            For 106 years = 6
    start3: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 2
            For 106 years = 7
    """
    JJA_flat = dataFix[start1::12] + dataFix[start2::12] + dataFix[start3::12]
    JJA_flat /= 3.0
    JJA = np.ma.masked_less(JJA_flat,mask)
    data = np.reshape(JJA,(years,180,360))
    return JJA

def hadisstSON(years,start1,start2,start3):
    """
    A function to produce an array of SON seasonal data (average of
    all three months at each location) for all 105 years.
    Note: SON[year,lat,lon]

    Parameters:
    -----------
    years: the number of years recording this seasons.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start1: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 3
            For 106 years = 8
    start2: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 4
            For 106 years = 9
    start3: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 5
            For 106 years = 10
    """
    SON_flat = dataFix[start1::12] + dataFix[start2::12] + dataFix[start3::12]
    SON_flat /= 3.0
    SON = np.ma.masked_less(SON_flat,mask)
    data = np.reshape(SON,(years,180,360))
    return SON

def hadisstDJF(years,start1,start2,start3):
    """
    A function to produce an array of DJF seasonal data (average of
    all three months at each location) for all 105 years.
    Note: DJF[year,lat,lon]

    Parameters:
    -----------
    years: the number of years recording this seasons.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start1: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 6
            For 106 years = 11
    start2: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 7
            For 106 years = 0
    start3: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 8
            For 106 years = 1
    """
    DJF_flat = dataFix[start1::12] + dataFix[start2::12] + dataFix[start3::12]
    DJF_flat /= 3.0
    DJF = np.ma.masked_less(DJF_flat,mask)
    data = np.reshape(DJF,(years,180,360))
    return DJF

def hadisstMAM(years,start1,start2,start3):
    """
    A function to produce an array of MAM seasonal data (average of
    all three months at each location) for all 105 years.
    Note: MAM[year,lat,lon]

    Parameters:
    -----------
    years: the number of years recording this seasons.  If using
            data_flat this will be 105, if using data_flat_ext
            this will be 106.
    start1: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 9
            For 106 years = 2
    start2: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 10
            For 106 years = 3
    start3: the index to start slicing from for the first month in
            this season (coinciding with the first instance of this month).
            For 105 years = 11
            For 106 years = 4
    """
    MAM_flat = dataFix[start1::12] + dataFix[start2::12] + dataFix[start3::12]
    MAM_flat /= 3.0
    MAM = np.ma.masked_less(MAM_flat,mask)
    data = np.reshape(MAM,(years,180,360))
    return MAM

#Make lat/lon data accessible for use in other files
latHad = data.variables['latitude'][:]
lonHad = data.variables['longitude'][:]
latHad_units = data.variables['latitude'].units
lonHad_units = data.variables['longitude'].units

#Prepare data for analysis
mask = -10.0 #Mask values less than -10 deg Celsius to remove no-data values of -1e+30
data_flat = hadisstTrim()
data_flat_ext = hadisstTrimExt()


#Divide into time bins - June 1900 to May 2005
dataFix = bugFix(data_flat)

#sst_Annual = hadisstAnnual()

sst_June = hadisstJune(105,0)
sst_July = hadisstJuly(105,1)
sst_August = hadisstAugust(105,2)
sst_September = hadisstSeptember(105,3)
sst_October = hadisstOctober(105,4)
sst_November = hadisstNovember(105,5)
sst_December = hadisstDecember(105,6)
sst_January = hadisstJanuary(105,7)
sst_February = hadisstFebruary(105,8)
sst_March = hadisstMarch(105,9)
sst_April = hadisstApril(105,10)
sst_May = hadisstMay(105,11)

sst_JJA = hadisstJJA(105,0,1,2)
sst_SON = hadisstSON(105,3,4,5)
sst_DJF = hadisstDJF(105,6,7,8)
sst_MAM = hadisstMAM(105,9,10,11)


#Divide into time bins - January 1900 to December 2005
dataFix_Had = bugFix(data_flat_ext,ext=True)
"""
sst_JuneEx = hadisstJune(106,5)
sst_JulyEx = hadisstJuly(106,6)
sst_AugustEx = hadisstAugust(106,7)
sst_SeptemberEx = hadisstSeptember(106,8)
sst_OctoberEx = hadisstOctober(106,9)
sst_NovemberEx = hadisstNovember(106,10)
sst_DecemberEx = hadisstDecember(106,11)
sst_JanuaryEx = hadisstJanuary(106,0)
sst_FebruaryEx = hadisstFebruary(106,1)
sst_MarchEx = hadisstMarch(106,2)
sst_AprilEx = hadisstApril(106,3)
sst_MayEx = hadisstMay(106,4)

sst_JJAEx = hadisstJJA(106,5,6,7)
sst_SONEx = hadisstSON(106,8,9,10)
sst_DJFEx = hadisstDJF(106,11,0,1)
sst_MAMEx = hadisstMAM(106,2,3,4)
"""
