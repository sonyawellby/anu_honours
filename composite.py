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

import maps_sub
from matplotlib import pyplot as plt
from plot import plot, mapAWAP

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
    stratAv = ma.mean(data,axis=0)
    return stratAv

def plotStrat(stratAv,precip_data,title,filepath):
    """
    A function to produce plots of stratified data.
    """
    var = ma.masked_invalid(stratAv)
    dict1 = mapAWAP(precip_data)
    myplot = plot(var,dict1,labels=False,grid=False,oceans=False,cbar=True)
    reload(maps_sub)
    from maps_sub import saveFig
    saveFig(myplot,title,filepath)
    return

"""
AWAP
"""
#June

Jun_strat_IPOpos = stratify(awap_prepare.awap_June,indices_phase.IPO_posHad_Jun)
Jun_strat_IPOpos_ENSOpos = stratify(Jun_strat_IPOpos,indices_phase.ENSO_posHad_Jun)
Jun1 = stratifyAverage(Jun_strat_IPOpos_ENSOpos)
plotStrat(Jun1,awap_prepare.awap_June,"1","/composite/AWAP/June/June")

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
"""
reload(access_trimmed) #this didn't work

#June
R1_Jun_strat_IPOpos = stratify(access_trimmed.trim_June,indices_phase.IPO_posR1_Jun)
R1_Jun_strat_IPOpos_ENSOpos = stratify(R1_Jun_strat_IPOpos,indices_phase.ENSO_posR1_Jun)
Jun2 = stratifyAverage(R1_Jun_strat_IPOpos_ENSOpos)
plotStrat(Jun2,access_trimmed.trim_June,"1","/composite/R1/June/June")
