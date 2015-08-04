"""
A set of routines to prepare ACCESS files (precipitation, sea surface
temperature) for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 4 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

data = n.Dataset('ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','r')

def diff():
    """
    A function to:
        (1) find how many days separate each month of the ACCESS dataset
        (2) reshape the dataset relative to days (rather than seconds since 01/01/0001
            on the Proleptic Gregorian calendar).
    """
    time = data.variables['time']
    timeDiff = [time[i]-time[i-1] for i in range(0,len(time))]
    timeDiff.pop(0)
    timeDiff.append(30.5)
    timeDiffNP = np.array(timeDiff)
    #Reshape the data array as 156 years of 12 months
    months = np.reshape(timeDiffNP,(156,12))

def units_pr():
    """
    A function to change the 'pr' variable from kg/m^2/s to mm/month so it is
    compatibile with the AWAP dataset (which is in its pure form measured in
    m/day, and has X days in each month).  Note that the AWAP dataset has also
    been modified so it, too, reports mm/month values.

    NB: prc_monthly[1871][160][40] is: timestep, latitude, longitude
    """
    prc_monthly = [data.variables['pr'][i]*data.variables['time'][i] for i in range(0,len(data.variables['time']))]
    data.variables['pr'] = prc_monthly

def month():
    """
    Monthly data for Jun-May years (June 1900 to May 2004) - 104 year analysis.
    
    Note: jan[40][40][155] is: timestep, longitude, latitude
    Note: timestep 600 is January 1900
    """
    Jun = prc_monthly[605:1853:12]
    Jun_array = np.array(Jun)

    Jul = prc_monthly[606:1854:12]
    Jul_array = np.array(Jul)

    Aug = prc_monthly[607:1855:12]
    Aug_array = np.array(Aug)

    Sep = prc_monthly[608:1856:12]
    Sep_array = np.array(Sep)

    Oct = prc_monthly[609:1857:12]
    Oct_array = np.array(Oct)

    Nov = prc_monthly[610:1858:12]
    Nov_array = np.array(Nov)

    Dec = prc_monthly[611:1859:12]
    Dec_array = np.array(Dec)

    Jan = prc_monthly[612:1860:12]
    Jan_array = np.array(Jan)

    Feb = prc_monthly[613:1861:12]
    Feb_array = np.array(Feb)

    Mar = prc_monthly[614:1862:12]
    Mar_array = np.array(Mar)

    Apr = prc_monthly[615:1863:12]
    Apr_array = np.array(Apr)

    May = prc_monthly[616:1864:12]
    May_array = np.array(May)

def season():
    """
    Seasonal data for Jun-May years (June 1900 to May 2004) - 104 year analysis
    """
    month()
    
    DJF_flat = Dec + Jan + Feb
    DJF_array = np.array(DJF_flat)
    DJF = np.reshape(DJF_array, (104,3,145,192))

    MAM_flat = Mar + Apr + May
    MAM_array = np.array(MAM_flat)
    MAM = np.reshape(MAM_array, (104,3,145,192))

    JJA_flat = Jun + Jul + Aug
    JJA_array = np.array(JJA_flat)
    JJA = np.reshape(JJA_array, (104,3,145,192))

    SON_flat = Sep1 + Oct1 + Nov1
    SON_array = np.array(SON_flat)
    SON = np.reshape(JJA_array, (104,3,145,192))


def annual():
    """
    Annual data for Jun-May years (Jun 1900 to May 2004) - 104 year analysis
    """
    month()
    
    annual_flat = Jun + Jul + Aug + Sep + Oct + Nov + Dec + Jan + Feb + Mar + Apr + May
    annual_array = np.array(annual_flat)
    annualJunToMay = np.reshape(annual_array,(104,12,145,192))
