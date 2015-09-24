"""
A file to collate sub-routines used to correlate ENSO with rainfall
and the IPO with rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 September 2015.
"""
import netCDF4 as n
import numpy as np
import scipy.stats as stats
import numpy.ma as ma
from matplotlib import pyplot as plt
from plot import plot, mapCorr

from indices_array import Nino34,TPI
import maps_sub
import math

#
from awap_prepare import awap_Annual
from access_trimmed import trim_Annual
#

from cwd import cwdInFunction
cwdInFunction()

from indices_time import Nino34_Jun, Nino34_Jul, Nino34_Aug, Nino34_Sep, \
     Nino34_Oct, Nino34_Nov, Nino34_Dec, Nino34_Jan, Nino34_Feb, Nino34_Mar,\
     Nino34_Apr, Nino34_May, Nino34_JJA, Nino34_SON, Nino34_DJF, Nino34_MAM,\
    Nino34_annual, TPI_Jun, TPI_Jul, TPI_Aug, TPI_Sep, TPI_Oct, TPI_Nov,\
    TPI_Dec, TPI_Jan, TPI_Feb, TPI_Mar, TPI_Apr, TPI_May, TPI_JJA, TPI_SON, \
    TPI_DJF, TPI_MAM, TPI_annual

def corr(rainfall,index,ind_num):
    """
    A function to correlate rainfall (AWAP or ACCESS) with an index
    (e.g. IPO, ENSO).  Masks non-significant values (p > 0.05).

    Parameters:
    -----------
    Rainfall: the dataset of rainfall.
    Index: the dataset of the index.
    """
    corr_array = np.zeros((27,22))
    count1 = 0
    while count1 < 27:
        count2 = 0
        while count2 < 22:
            a = stats.pearsonr(rainfall[:,count1,count2],index[ind_num])
            if a[1] <= 0.05:
                corr_array[count1,count2] = a[0]
            else:
                corr_array[count1,count2] = 0.0
            count2 += 1
        count2 = 0
        count1 += 1
    corr_array_masked = np.ma.masked_where(corr_array == 0.0, corr_array)
    return corr_array_masked

def corrDiff(array1,array2):
    """
    Return an array with the differences between observational (array1) and
    modelled (array2) data, only showing points where differences in observations
    are statistically significant (95% level, z-statistic). 
    """
    mean_array1 = np.ma.mean(array1)
    sd_array1 = np.ma.std(array1)
    #for i in array2:
    #    if (array2[i]-mean_array1)/(sd_array1/math.sqrt(mean_array1.count())) <= 1.65:
            
    #t_stat = 
    #pr_t_stat =
    diff = np.ma.subtract(array1,array2)
    diff_array_z_stat = (array2-mean_array1)/(sd_array1/math.sqrt(array1.count()))
    new_array = np.ma.masked_inside(diff_array_z_stat,-1.96,1.96)
    print new_array
    new_array2 = np.ma.masked_where(new_array == True,diff)
    #new_array2 = np.ma.masked_where(array2 <= pr_t_stat,array2)
    #diff = np.ma.subtract(new_array1,new_array2)
    return new_array2
"""
def test(array1,array2):
    mean_array1 = np.ma.mean(array1)
    sd_array1 = np.ma.std(array1)
    new_array = np.ma.masked_where(((array2-mean_array1)/(sd_array1/math.sqrt(mean_array1.count()))) <= 1.65,diff)
"""
def plotCorr(rainfall,index,ind_num,title,filepath):
    """
    A function to produce plots of correlations.
    """
    var = corr(rainfall,index,ind_num)
    var2 = ma.masked_invalid(var)
    Dict6 = mapCorr()
    myplot = plot(var2,Dict6,labels=False,grid=False,oceans=False,cbar=True)
    reload(maps_sub)
    from maps_sub import saveFig
    saveFig(myplot,title,filepath)
    return

arrayA = corr(awap_Annual,Nino34_annual,0)
arrayB = corr(trim_Annual,Nino34_annual,0)
test = corrDiff(arrayA,arrayB)
