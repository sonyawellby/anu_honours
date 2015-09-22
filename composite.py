"""
Set of routines to stratify ENSO/IPO and rainfall data
for composite analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 17 September 2015.
"""
import numpy as np
import numpy.ma as ma

import indices_phase
import awap_prepare
import access_trimmed

import maps_sub
from matplotlib import pyplot as plt
from plot import plot, mapComposite, mapCompositeAnom, multi

from cwd import cwdInFunction
cwdInFunction()

def stratify(rainfall,index):
    """
    A function to mask  precipitation data that does not
    meet a given stratification requirement (e.g. mask
    all data except positive ENSO years, etc.).

    Parameters:
    -----------
    rainfall : the precipitation dataset (either AWAP,
                ACCESS1.3 R1, R2, or R3).
    index : the ENSO or IPO index corresponding with the
            time period of interest (e.g. positive ENSO, June). 
    """
    new = np.zeros((105,27,22))
    count = 0
    while count < 105:
        if isinstance(index[count],float)==False:
            new[count,:,:]=-9999.0
        else:
            new[count,:,:]=rainfall[count,:,:]
        count +=1
    masked_copy = ma.masked_where(new==-9999.0,new)
    return masked_copy

def stratifyAverage(data):
    """
    data : output of stratify().
    """
    stratAv = ma.mean(data,axis=0)
    return stratAv

def meanRainfall(data):
    """
    A function to return mean rainfall (mm) for non-stratified
    data.

    Parameters:
    -----------
    data : monthly, seasonal or annual data. E.g 'awap_prepare.awap_June'
        or 'access_trimmed.trim_June'.
    """
    meanRain = ma.mean(data,axis=0)
    return meanRain

def anomalies(data,stratified):
    """
    A function to return anomalies (mm) for stratified
    indices.

    Parameters:
    -----------
    
    """
    meanRain = meanRainfall(data)
    anomalies = stratified - meanRain
    return anomalies

def plotStrat(stratAv,precip_data,title,filepath):
    """
    A function to produce plots of stratified data.
    """
    var = ma.masked_invalid(stratAv)
    dict7 = mapComposite(precip_data)
    myplot = plot(var,dict7,labels=False,grid=False,oceans=False,cbar=True)
    reload(maps_sub)
    from maps_sub import saveFig
    saveFig(myplot,title,filepath)
    return

def plotStratAnom(rainAnom,precip_data,title,filepath):
    """
    A function to produce plots of stratified data.
    """
    var = ma.masked_invalid(rainAnom)
    dict8 = mapCompositeAnom(precip_data)
    myplot = plot(var,dict8,labels=False,grid=False,oceans=False,cbar=True)
    reload(maps_sub)
    from maps_sub import saveFig
    saveFig(myplot,title,filepath)
    return

def output(rainfall,index_IPO,index_ENSO,title,filepath,filepathA):
    strat_IPO = stratify(rainfall,index_IPO)
    strat_IPO_ENSO = stratify(strat_IPO,index_ENSO)
    rainStrat = stratifyAverage(strat_IPO_ENSO)
    rainAnom = anomalies(rainfall,rainStrat)
    plotStrat(rainStrat,rainfall,title,filepath)
    plotStratAnom(rainAnom,rainfall,title,filepathA)
    return

def number(rainfall,index_IPO,index_ENSO):
    strat_IPO = stratify(rainfall,index_IPO)
    strat_IPO_ENSO = stratify(strat_IPO,index_ENSO)
    rainStrat = stratifyAverage(strat_IPO_ENSO)
    number = rainStrat.count()
    return number
