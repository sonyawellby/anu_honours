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
    copy = rainfall
    count = 0
    for i in copy:
        if isinstance(index[count],float)==False:
            copy[count,:,:]=True
        else:
            pass
        count +=1
    masked_copy = ma.masked_where(copy==True,copy)
    return masked_copy

strat_IPOpos = stratify(awap_prepare.awap_June,indices_phase.IPO_posHad_Jun)
strat_IPOpos_ENSOpos = stratify(strat_IPOpos,indices_phase.ENSO_posHad_Jun)




