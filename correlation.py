"""
A file to collate sub-routines used to correlate ENSO with rainfall
and the IPO with rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 7 October 2015.
"""
import netCDF4 as n
import numpy as np
import scipy.stats as stats
import numpy.ma as ma
from matplotlib import pyplot as plt
from plot import plot, mapCorr

import maps_sub
import math

from cwd import cwdInFunction
cwdInFunction()

def averageArray(rainfall_data):
    """
    Returns the average rainfall value for each year in
    a given (typically 105 year) array.
    """
    list1 = []
    for i in rainfall_data:
        listtemp = []
        for j in i:
            listtemp.append(np.ma.mean(j))
        list1.append(listtemp)
    return list1

def corr(rainfall,index):
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
            a = stats.pearsonr(rainfall[:,count1,count2],index)
            if a[1] <= 0.05:
                corr_array[count1,count2] = a[0]
            else:
                corr_array[count1,count2] = 0.0
            count2 += 1
        count2 = 0
        count1 += 1
    corr_array_masked = np.ma.masked_where(corr_array == 0.0, corr_array)
    return corr_array_masked

def corrAverage(rainfall,index):
    """
    Returns the average correlation value between an index and rainfall
    in Australia.
    """
    array = corr(rainfall,index)
    corr_Aus = np.ma.average(array)
    return corr_Aus

def corrEastAus(rainfall,index):
    """
    A function to correlate rainfall (AWAP or ACCESS) with an index
    (e.g. IPO, ENSO), for eastern Australia only.  Masks non-significant
    values (p > 0.05).

    Parameters:
    -----------
    Rainfall: the dataset of rainfall.
    Index: the dataset of the index.
    """
    corr_array_masked = corr(rainfall,index)

    #Eastern Australian region is from 140.625 degrees east (~Vic/NSW border)
    corr_array_E_Aus = corr_array_masked[:,14:]
    
    #Koppen classification areas in eastern Australia
    corr_array_equatorial = corr_array_masked[23:,14:]
    corr_array_tropical = corr_array_masked[19:23,14:]
    corr_array_subtropical = corr_array_masked[10:19,16:]
    corr_array_desert = corr_array_masked[9:17,14:15]

    grass1 = corr_array_masked[17:19,14:15]
    grass2 = corr_array_masked[17:19,15:16]
    grass3 = corr_array_masked[4:17,15:16]
    grass4 = corr_array_masked[4:9,14:15]
    corr_array_grassland = np.ma.concatenate((grass1,grass2,grass3,grass4))

    temperate1 = corr_array_masked[4:10,16:]
    temperate2 = corr_array_masked[:4,14:20]
    corr_array_temperate = np.ma.concatenate((temperate1,temperate2))

    #Compute average correlations for eastern Australia
    corr_E_Aus = np.ma.average(corr_array_E_Aus)
    corr_equatorial = np.ma.average(corr_array_equatorial)
    corr_tropical = np.ma.average(corr_array_tropical)
    corr_subtropical = np.ma.average(corr_array_subtropical)
    corr_desert = np.ma.average(corr_array_desert)
    corr_grassland = np.ma.average(corr_array_grassland)
    corr_temperate = np.ma.average(corr_array_temperate)

    return corr_E_Aus,corr_equatorial,corr_tropical,\
           corr_subtropical,corr_desert,corr_grassland,corr_temperate

def plotCorr(rainfall,index,title,filepath):
    """
    A function to produce plots of correlations.
    """
    var = corr(rainfall,index)
    var2 = ma.masked_invalid(var)
    Dict6 = mapCorr()
    myplot = plot(var2,Dict6,labels=False,grid=False,oceans=False,cbar=True)
    reload(maps_sub)
    from maps_sub import saveFig
    saveFig(myplot,title,filepath)
    return

def corrDiff(array1,array2):
    """
    Return an array with the differences between observational (array1) and
    modelled (array2) data, only showing points where differences in observations
    are statistically significant (95% level, z-statistic if n > 30,
    t-statistic if n < 30; two-tailed). 
    """
    mean_array1 = np.ma.mean(array1)
    sd_array1 = np.ma.std(array1)
    diff = np.ma.subtract(array1,array2)
    
    if array1.count() > 30:
        diff_array_stat = (array2-mean_array1)/(sd_array1/math.sqrt(array1.count()))
        new_array = np.ma.masked_inside(diff_array_stat,-1.96,1.96)
    elif array1.count() <= 1:
        return
    else:
        df = array1.count() - 1
        df_list = [12.7065,4.3026,3.1824,2.7764,2.5706,2.4469,2.3646,2.3060,2.2621,2.2282,\
         2.2010,2.1788,2.1604,2.1448,2.1314,2.1199,2.1098,2.1009,2.0930,2.0860,\
         2.0796,2.0739,2.0686,2.0639,2.0596,2.0555,2.0518,2.0484,2.0452,2.0423]
        df_t = df_list[df-1]
        
        diff_array_stat = (array2-mean_array1)/(sd_array1/math.sqrt(array1.count()))
        new_array = np.ma.masked_inside(diff_array_stat,-df_t,df_t)
        
    new_array2 = np.ma.masked_where(new_array == True,diff)
    
    return new_array2

def plotCorrDiff(array1,array2,title,filepath):
    """
    A function to produce plots of correlation differences.

    Parameters:
    -----------
    array1 : observational dataset.  Output of corr()
    array2 : modelled dataset. Output of corr()
    """
    corrDiff_array = corrDiff(array1,array2)
    if corrDiff_array != None:
        Dict6 = mapCorr()
        myplot = plot(corrDiff_array,Dict6,labels=False,grid=False,oceans=False,cbar=True)
        reload(maps_sub)
        from maps_sub import saveFig
        saveFig(myplot,title,filepath)
    else:
        array = np.zeros((27,22))
        Dict6 = mapCorr()
        myplot = plot(array,Dict6,labels=False,grid=False,oceans=False,cbar=True)
        reload(maps_sub)
        from maps_sub import saveFig
        saveFig(myplot,title,filepath)
    return
