"""
Set of routines to stratify ENSO/IPO and rainfall data
for composite analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 17 September 2015.
"""
import numpy as np
import numpy.ma as ma

import maps_sub
from matplotlib import pyplot as plt
from plot import plot, mapComposite, mapCompositeAnom, multi,\
     mapDifference, mapStandardised

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
    A function to return rainfall anomalies (mm) for stratified
    indices.

    Parameters:
    -----------
    
    """
    climate_mean = meanRainfall(data[60:91])
    anomalies = np.ma.subtract(stratified,climate_mean)
    return anomalies

def difference(rainfall,index_more_rain,index_less_rain):
    """
    A function to plot differences in mean rainfall in the
    rain enhanced and rain reduced phases of ENSO and
    the IPO.
    """
    phase_more_rain = stratify(rainfall,index_more_rain)
    phase_less_rain = stratify(rainfall,index_less_rain)

    phase_more_rain_av = stratifyAverage(phase_more_rain)
    phase_less_rain_av = stratifyAverage(phase_less_rain)
    
    diff = np.ma.subtract(phase_more_rain_av,phase_less_rain_av)
    return diff

def plotStrat(stratAv,precip_data,title,filepath):
    """
    A function to produce plots of stratified data.
    """
    var = ma.masked_invalid(stratAv)
    dict7 = mapComposite(precip_data)
    myplot = plot(var,dict7,labels=False,grid=False,oceans=False,cbar=False)
    reload(maps_sub)
    from maps_sub import saveFig
    saveFig(myplot,title,filepath)
    return

def plotStratDiff(stratAv,precip_data,title,filepath):
    """
    A function to produce precipitation difference maps (between
    wet and dry phases of the ENSO and IPO).
    """
    var = ma.masked_invalid(stratAv)
    dict9 = mapDifference(precip_data)
    myplot = plot(var,dict9,labels=False,grid=False,oceans=False,cbar=True)
    reload(maps_sub)
    from maps_sub import saveFig
    saveFig(myplot,title,filepath)
    return

def plotStratStandardised(data,precip_data,title,filepath):
    """
    A function to produce standardised plots of stratified rainfall data.
    """
    var = ma.masked_invalid(data)
    dict10 = mapDifference(precip_data)
    myplot = plot(var,dict10,labels=False,grid=False,oceans=False,cbar=False)
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
    myplot = plot(var,dict8,labels=False,grid=False,oceans=False,cbar=False)
    reload(maps_sub)
    from maps_sub import saveFig
    saveFig(myplot,title,filepath)
    return

def output(rainfall,index_IPO,index_ENSO,title,filepath,filepathA):
    """
    A function to produce an image of (a) mean rainfall in a given ENSO and IPO state,
    and (b) mean rainfall anomalies in a given ENSO and IPO state.
    """
    strat_IPO = stratify(rainfall,index_IPO)
    strat_IPO_ENSO = stratify(strat_IPO,index_ENSO)
    rainStrat = stratifyAverage(strat_IPO_ENSO)
    rainAnom = anomalies(rainfall,rainStrat)
    plotStrat(rainStrat,rainfall,title,filepath)
    plotStratAnom(rainAnom,rainfall,title,filepathA)
    return

def number(rainfall,index_IPO,index_ENSO):
    """
    A function to return the number of years with a given ENSO-IPO state.
    """
    strat_IPO = stratify(rainfall,index_IPO)
    strat_IPO_ENSO = stratify(strat_IPO,index_ENSO)
    rainStrat = stratifyAverage(strat_IPO_ENSO)
    number = rainStrat.count()
    return number
