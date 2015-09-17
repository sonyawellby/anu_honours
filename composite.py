"""
Set of routines to stratify ENSO/IPO and rainfall data
for composite analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 16 September 2015.
"""
import numpy as np
import numpy.ma as ma

import indices_phase
import awap_prepare
import access_trimmed
from access_trimmed import trim_June
"""
trim_Annual,trim_June, trim_July,\
     trim_August,trim_September,trim_October,trim_November,\
     trim_December,trim_January,trim_February,trim_March,\
     trim_April,trim_May,trim_JJA,trim_SON,trim_DJF,trim_MAM
"""

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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#AWAP
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
AWAP: June
"""
output(awap_prepare.awap_June,indices_phase.IPO_posHad_Jun,indices_phase.ENSO_posHad_Jun,\
       "IpEp","/composite/1_sd/rainfall/AWAP/June/1","/composite/1_sd/rainfall_anomalies/AWAP/June/1")
output(awap_prepare.awap_June,indices_phase.IPO_posHad_Jun,indices_phase.ENSO_neutralHad_Jun,\
       "IpEne","/composite/1_sd/rainfall/AWAP/June/2","/composite/1_sd/rainfall_anomalies/AWAP/June/2")
output(awap_prepare.awap_June,indices_phase.IPO_posHad_Jun,indices_phase.ENSO_negHad_Jun,\
       "IpEn","/composite/1_sd/rainfall/AWAP/June/3","/composite/1_sd/rainfall_anomalies/AWAP/June/3")
output(awap_prepare.awap_June,indices_phase.IPO_neutralHad_Jun,indices_phase.ENSO_posHad_Jun,\
       "IneEp","/composite/1_sd/rainfall/AWAP/June/4","/composite/1_sd/rainfall_anomalies/AWAP/June/4")
output(awap_prepare.awap_June,indices_phase.IPO_neutralHad_Jun,indices_phase.ENSO_neutralHad_Jun,\
       "IneEne","/composite/1_sd/rainfall/AWAP/June/5","/composite/1_sd/rainfall_anomalies/AWAP/June/5")
output(awap_prepare.awap_June,indices_phase.IPO_neutralHad_Jun,indices_phase.ENSO_negHad_Jun,\
       "IneEn","/composite/1_sd/rainfall/AWAP/June/6","/composite/1_sd/rainfall_anomalies/AWAP/June/6")
output(awap_prepare.awap_June,indices_phase.IPO_negHad_Jun,indices_phase.ENSO_posHad_Jun,\
       "InEp","/composite/1_sd/rainfall/AWAP/June/7","/composite/1_sd/rainfall_anomalies/AWAP/June/7")
output(awap_prepare.awap_June,indices_phase.IPO_negHad_Jun,indices_phase.ENSO_neutralHad_Jun,\
       "InEne","/composite/1_sd/rainfall/AWAP/June/8","/composite/1_sd/rainfall_anomalies/AWAP/June/8")
output(awap_prepare.awap_June,indices_phase.IPO_negHad_Jun,indices_phase.ENSO_negHad_Jun,\
       "InEn","/composite/1_sd/rainfall/AWAP/June/9","/composite/1_sd/rainfall_anomalies/AWAP/June/9")
AWAP_June = multi("/composite/1_sd/rainfall/AWAP/June/*.png",3,3,title='AWAP June: mean rainfall')
AWAP_June_Anom = multi("/composite/1_sd/rainfall_anomalies/AWAP/June/*.png",3,3,title='AWAP June: mean rainfall anomalies')
maps_sub.saveFig(AWAP_June,"AWAP_June","/composite/1_sd_compiled/AWAP")
maps_sub.saveFig(AWAP_June_Anom,"AWA_June_Anom","/composite/1_sd_compiled/AWAP")

"""
#June: IPO pos, ENSO pos
Jun_strat_IPOpos = stratify(awap_prepare.awap_June,indices_phase.IPO_posHad_Jun)
Jun_strat_IPOpos_ENSOpos = stratify(Jun_strat_IPOpos,indices_phase.ENSO_posHad_Jun)
Jun1 = stratifyAverage(Jun_strat_IPOpos_ENSOpos)
plotStrat(Jun1,awap_prepare.awap_June,"IpEp","/composite/1_sd/rainfall/AWAP/June/1")
Jun1A = anomalies(awap_prepare.awap_June,Jun1)
plotStratAnom(JunA,awap_prepare.awap_June,"","/composite/1_sd/rainfall_anomalies/AWAP/June/1")

#June: IPO pos, ENSO neg
Jun_strat_IPOpos_ENSOneg = stratify(Jun_strat_IPOpos,indices_phase.ENSO_negHad_Jun)
Jun2 = stratifyAverage(Jun_strat_IPOpos_ENSOneg)
plotStrat(Jun2,awap_prepare.awap_June,"IpEn","/composite/1_sd/rainfall/AWAP/June/2")
Jun2A = anomalies(awap_prepare.awap_June,Jun2)
plotStratAnom(Jun2A,awap_prepare.awap_June,"","/composite/1_sd/rainfall_anomalies/AWAP/June/2")

#June: IPO pos, ENSO neutral
Jun_strat_IPOpos_ENSOneut = stratify(Jun_strat_IPOpos,indices_phase.ENSO_neutralHad_Jun)
Jun3 = stratifyAverage(Jun_strat_IPOpos_ENSOneut)
plotStrat(Jun3,awap_prepare.awap_June,"IpEne","/composite/1_sd/rainfall/AWAP/June/3")
Jun3A = anomalies(awap_prepare.awap_June,Jun3)
plotStratAnom(Jun3A,awap_prepare.awap_June,"","/composite/1_sd/rainfall_anomalies/AWAP/June/3")

#June: IPO neg, ENSO pos
Jun_strat_IPOneg = stratify(awap_prepare.awap_June,indices_phase.IPO_negHad_Jun)
Jun_strat_IPOneg_ENSOpos = stratify(Jun_strat_IPOneg,indices_phase.ENSO_posHad_Jun)
Jun4 = stratifyAverage(Jun_strat_IPOneg_ENSOpos)
plotStrat(Jun4,awap_prepare.awap_June,"InEp","/composite/1_sd/rainfall/AWAP/June/4")
Jun4A = anomalies(awap_prepare.awap_June,Jun4)
plotStratAnom(Jun4A,awap_prepare.awap_June,"","/composite/1_sd/rainfall_anomalies/AWAP/June/4")

#June: IPO neg, ENSO neg
Jun_strat_IPOneg_ENSOneg = stratify(Jun_strat_IPOneg,indices_phase.ENSO_negHad_Jun)
Jun5 = stratifyAverage(Jun_strat_IPOneg_ENSOneg)
plotStrat(Jun5,awap_prepare.awap_June,"InEn","/composite/1_sd/rainfall/AWAP/June/5")
Jun5A = anomalies(awap_prepare.awap_June,Jun5)
plotStratAnom(Jun5A,awap_prepare.awap_June,"","/composite/1_sd/rainfall_anomalies/AWAP/June/5")

#June: IPO neg, ENSO neutral
Jun_strat_IPOneg_ENSOneut = stratify(Jun_strat_IPOneg,indices_phase.ENSO_neutralHad_Jun)
Jun6 = stratifyAverage(Jun_strat_IPOneg_ENSOneut)
plotStrat(Jun6,awap_prepare.awap_June,"InEne","/composite/1_sd/rainfall/AWAP/June/6")
Jun6A = anomalies(awap_prepare.awap_June,Jun6)
plotStratAnom(Jun6A,awap_prepare.awap_June,"","/composite/1_sd/rainfall_anomalies/AWAP/June/6")

------------
#June: IPO neutral, ENSO pos
Jun_strat_IPOneut = stratify(awap_prepare.awap_June,indices_phase.IPO_neutHad_Jun)
Jun_strat_IPOneut_ENSOpos = stratify(Jun_strat_IPOneut,indices_phase.ENSO_posHad_Jun)
Jun7 = stratifyAverage(Jun_strat_IPOneut_ENSOpos)
plotStrat(Jun7,awap_prepare.awap_June,"IneEp","/composite/1_sd/rainfall/AWAP/June/7")
Jun7A = anomalies(awap_prepare.awap_June,Jun7)
plotStratAnom(Jun7A,awap_prepare.awap_June,"","/composite/1_sd/rainfall_anomalies/AWAP/June/7")

#June: IPO neutral, ENSO neg
Jun_strat_IPOneg_ENSOneg = stratify(Jun_strat_IPOneg,indices_phase.ENSO_negHad_Jun)
Jun5 = stratifyAverage(Jun_strat_IPOneg_ENSOneg)
plotStrat(Jun5,awap_prepare.awap_June,"IneEn","/composite/1_sd/rainfall/AWAP/June/8")
Jun5A = anomalies(awap_prepare.awap_June,Jun5)
plotStratAnom(Jun5A,awap_prepare.awap_June,"","/composite/1_sd/rainfall_anomalies/AWAP/June/8")

#June: IPO neutral, ENSO neutral
Jun_strat_IPOneg_ENSOneut = stratify(Jun_strat_IPOneg,indices_phase.ENSO_neutralHad_Jun)
Jun6 = stratifyAverage(Jun_strat_IPOneg_ENSOneut)
plotStrat(Jun6,awap_prepare.awap_June,"IneEne","/composite/1_sd/rainfall/AWAP/June/9")
Jun6A = anomalies(awap_prepare.awap_June,Jun6)
plotStratAnom(Jun6A,awap_prepare.awap_June,"","/composite/1_sd/rainfall_anomalies/AWAP/June/9")
--------------
"""


"""
Jun_strat_IPOpos_ENSOneg = stratify(Jun_strat_IPOpos,indices_phase.ENSO_negHad_Jun)
Jun_strat_IPOpos_ENSOneut = stratify(Jun_strat_IPOpos,indices_phase.ENSO_neutralHad_Jun)

Jun_strat_IPOneg = stratify(awap_prepare.awap_June,indices_phase.IPO_negHad_Jun)
Jun_strat_IPOneg_ENSOpos = stratify(Jun_strat_IPOneg,indices_phase.ENSO_posHad_Jun)
Jun_strat_IPOneg_ENSOneg = stratify(Jun_strat_IPOneg,indices_phase.ENSO_negHad_Jun)
Jun_strat_IPOneg_ENSOneut = stratify(Jun_strat_IPOneg,indices_phase.ENSO_neutralHad_Jun)

Jun_strat_IPOneut = stratify(awap_prepare.awap_June,indices_phase.IPO_neutralHad_Jun)
Jun_strat_IPOneut_ENSOpos = stratify(Jun_strat_IPOneut,indices_phase.ENSO_posHad_Jun)
Jun_strat_IPOneut_ENSOneg = stratify(Jun_strat_IPOneut,indices_phase.ENSO_negHad_Jun)
Jun_strat_IPOneut_ENSOneut = stratify(Jun_strat_IPOneut,indices_phase.ENSO_neutralHad_Jun)
"""
"""
#July

Jul_strat_IPOpos = stratify(awap_prepare.awap_July,indices_phase.IPO_posHad_Jul)
Jul_strat_IPOpos_ENSOpos = stratify(Jul_strat_IPOpos,indices_phase.ENSO_posHad_Jul)
Jul_strat_IPOpos_ENSOneg = stratify(Jul_strat_IPOpos,indices_phase.ENSO_negHad_Jul)
Jul_strat_IPOpos_ENSOneut = stratify(Jul_strat_IPOpos,indices_phase.ENSO_neutralHad_Jul)

Jul_strat_IPOneg = stratify(awap_prepare.awap_July,indices_phase.IPO_negHad_Jul)
Jul_strat_IPOneg_ENSOpos = stratify(Jul_strat_IPOneg,indices_phase.ENSO_posHad_Jul)
Jul_strat_IPOneg_ENSOneg = stratify(Jul_strat_IPOneg,indices_phase.ENSO_negHad_Jul)
Jul_strat_IPOneg_ENSOneut = stratify(Jul_strat_IPOneg,indices_phase.ENSO_neutralHad_Jul)

Jul_strat_IPOneut = stratify(awap_prepare.awap_July,indices_phase.IPO_neutralHad_Jul)
Jul_strat_IPOneut_ENSOpos = stratify(Jul_strat_IPOneut,indices_phase.ENSO_posHad_Jul)
Jul_strat_IPOneut_ENSOneg = stratify(Jul_strat_IPOneut,indices_phase.ENSO_negHad_Jul)
Jul_strat_IPOneut_ENSOneut = stratify(Jul_strat_IPOneut,indices_phase.ENSO_neutralHad_Jul)

#August

Aug_strat_IPOpos = stratify(awap_prepare.awap_August,indices_phase.IPO_posHad_Aug)
Aug_strat_IPOpos_ENSOpos = stratify(Aug_strat_IPOpos,indices_phase.ENSO_posHad_Aug)
Aug_strat_IPOpos_ENSOneg = stratify(Aug_strat_IPOpos,indices_phase.ENSO_negHad_Aug)
Aug_strat_IPOpos_ENSOneut = stratify(Aug_strat_IPOpos,indices_phase.ENSO_neutralHad_Aug)

Aug_strat_IPOneg = stratify(awap_prepare.awap_August,indices_phase.IPO_negHad_Aug)
Aug_strat_IPOneg_ENSOpos = stratify(Aug_strat_IPOneg,indices_phase.ENSO_posHad_Aug)
Aug_strat_IPOneg_ENSOneg = stratify(Aug_strat_IPOneg,indices_phase.ENSO_negHad_Aug)
Aug_strat_IPOneg_ENSOneut = stratify(Aug_strat_IPOneg,indices_phase.ENSO_neutralHad_Aug)

Aug_strat_IPOneut = stratify(awap_prepare.awap_August,indices_phase.IPO_neutralHad_Aug)
Aug_strat_IPOneut_ENSOpos = stratify(Aug_strat_IPOneut,indices_phase.ENSO_posHad_Aug)
Aug_strat_IPOneut_ENSOneg = stratify(Aug_strat_IPOneut,indices_phase.ENSO_negHad_Aug)
Aug_strat_IPOneut_ENSOneut = stratify(Aug_strat_IPOneut,indices_phase.ENSO_neutralHad_Aug)
"""

"""
ACCESS1.3 R1

reload(access_trimmed) #this didn't work - because ACCESS_trimmed itself isn't updating
from access_trimmed import trim_June

#June
R1_Jun_strat_IPOpos = stratify(access_trimmed.trim_June,indices_phase.IPO_posR1_Jun)
R1_Jun_strat_IPOpos_ENSOpos = stratify(R1_Jun_strat_IPOpos,indices_phase.ENSO_posR1_Jun)
Jun2 = stratifyAverage(R1_Jun_strat_IPOpos_ENSOpos)
#plotStrat(Jun2,access_trimmed.trim_June,"","/composite/1_sd/rainfall/R1/June/1")
"""
