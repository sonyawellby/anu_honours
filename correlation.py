"""
A file to collate sub-routines used to correlate ENSO with rainfall
and the IPO with rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 10 November 2015.
"""
import netCDF4 as n
import numpy as np
import scipy.stats as stats
import numpy.ma as ma
from matplotlib import pyplot as plt
from plot import plot, mapCorr,mapCorrStratified

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

def average(array):
    """
    A function to produce one value for each year in the study period.
    """
    list1 = []
    for i in range(0,len(array)):
        list1.append(np.ma.mean(array[i]))
    array1 = np.asarray(list1)
    return array1

def corrAverage(rainfall,index):
    """
    Returns the average correlation value between an index and rainfall
    in Australia.
    """
    rain_array = average(rainfall)
    corr_Aus_full = stats.pearsonr(rain_array,index)
    corr_Aus = np.ma.masked_where(corr_Aus_full[1]>0.05,corr_Aus_full[0])
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
    #Eastern Australian region is from 140.625 degrees east (~Vic/NSW border)
    array_E_Aus = rainfall[:,:,14:]
    
    #Koppen classification areas in eastern Australia
    array_equatorial = rainfall[:,23:,14:]
    array_tropical = rainfall[:,19:23,14:]
    array_subtropical = rainfall[:,10:19,16:]
    array_desert = rainfall[:,9:17,14:15]

    grass1 = rainfall[:,17:19,14:15]
    grass2 = rainfall[:,4:17,15:16]
    grass3 = rainfall[:,4:9,14:15]

    temperate1 = rainfall[:,4:10,16:]
    temperate2 = rainfall[:,:4,14:20]

    #Compute average rainfall in the climate zones

    rain_E_Aus = average(array_E_Aus)
    rain_equatorial = average(array_equatorial)
    rain_tropical = average(array_tropical)
    rain_subtropical = average(array_subtropical)
    rain_desert = average(array_desert)

    grass1_av = average(grass1)
    grass2_av = average(grass2)
    grass3_av = average(grass3)
    grass_add1 = np.ma.add(grass1_av,grass2_av)
    grass_add2 = np.ma.add(grass_add1,grass3_av)
    rain_grassland = np.ma.divide(grass_add2,3.0)
    
    temperate1_av = average(temperate1)
    temperate2_av = average(temperate2)
    temperate_add = np.ma.add(temperate1_av,temperate2_av)
    rain_temperate = np.ma.divide(temperate_add,2.0)
    
    #Compute correlations for eastern Australia

    corr_E_Aus_full = stats.pearsonr(rain_E_Aus,index)
    corr_E_Aus = np.ma.masked_where(corr_E_Aus_full[1]>0.05,corr_E_Aus_full[0])
    
    corr_equatorial_full = stats.pearsonr(rain_equatorial,index)
    corr_equatorial = np.ma.masked_where(corr_equatorial_full[1]>0.05,corr_equatorial_full[0])

    corr_tropical_full = stats.pearsonr(rain_tropical,index)
    corr_tropical = np.ma.masked_where(corr_tropical_full[1]>0.05,corr_tropical_full[0])
    
    corr_subtropical_full = stats.pearsonr(rain_subtropical,index)
    corr_subtropical = np.ma.masked_where(corr_subtropical_full[1]>0.05,corr_subtropical_full[0])

    corr_desert_full = stats.pearsonr(rain_desert,index)
    corr_desert = np.ma.masked_where(corr_desert_full[1]>0.05,corr_desert_full[0])

    corr_grassland_full = stats.pearsonr(rain_grassland,index)
    corr_grassland = np.ma.masked_where(corr_grassland_full[1]>0.05,corr_grassland_full[0])

    corr_temperate_full = stats.pearsonr(rain_temperate,index)
    corr_temperate = np.ma.masked_where(corr_temperate_full[1]>0.05,corr_temperate_full[0])

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

def plotCorrStratified(rainfall,index,title,filepath):
    """
    A function to produce plots of correlations between
    one index and stratified (according to a second index) precipitation data.
    """
    var = corr(rainfall,index)
    var2 = ma.masked_invalid(var)
    Dict6 = mapCorrStratified(var2)
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
