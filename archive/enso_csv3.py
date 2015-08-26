"""
Set of routines to compute the Nino3.4 ENSO index
and write to CSV files.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 26 August 2015.
"""

from enso import *
from parameters import baseStart,baseEnd,baseSlice

from hadisst_prepare import dataFix_Had
import access_prepare_ts

def Nino34(dataset,baseStart,baseEnd,baseSlice,ACCESS=True):
    """
    A function to compute the unfiltered (mean SST anomaly) values
    of the Nino3.4 ENSO index.

    Parameters:
    -----------
    dataset : the SST dataset of interest.  From 'hadisst_prepare'
            or 'access_prepare_ts'.
    baseStart : The first year of the base period.  Give as index
            (e.g. [0=1900,104=2005]
    baseEnd : The last year of the base period.  Give as index
            (e.g. [0=1900,104=2005]
    ACCESS : (default = True)
            If using ACCESS data, set as 'True'.  Else set as 'False'.
    """
    if ACCESS==True:
        AreaENSO = areaENSO(dataset,ACCESS=True)
        BaseAreaENSO = baseAreaENSO(dataset,baseStart,baseEnd,baseSlice,ACCESS=True)
    elif ACCESS==False:
        AreaENSO = areaENSO(dataset,ACCESS=False)
        BaseAreaENSO = baseAreaENSO(dataset,baseStart,baseEnd,baseSlice,ACCESS=False)
    else:
        raise ValueError('Specify whether ACCESS or HadISST are used.')

    BaseMeanSST = baseMeanSST(BaseAreaENSO)
    Anomalies = anomalies(AreaENSO,BaseMeanSST)
    MeanAnom = meanAnom(Anomalies)
    return MeanAnom,AreaENSO

test = Nino34(dataFix_Had,baseStart=baseStart,baseEnd=baseEnd,baseSlice=baseSlice,ACCESS=False)
(MeanAnom,AreaENSO) = test

"""
def hadisstNino34():
"""
    #Generate ENSO Nino3.4 index for HadISST data:
"""
    ENSO_Had = Nino34(dataFix_Had,baseStart=baseStart,baseEnd=baseEnd,ACCESS=False)
    ENSO_running_Had = running(ENSO_Had,2,(len(ENSO_Had)-3))

    ENSO_phase_Had = ENSOphase(ENSO_running_Had,2,(len(ENSO_running_Had)-6))
    (ENSOpos, ENSOneg, ENSOneutral) = ENSO_phase_Had

    ENSO_crop_Had = cropRM(ENSO_running_Had)

    return ENSO_crop_Had,ENSO_phase_Had,ENSOpos,ENSOneg,ENSOneutral


def accessNino34():
"""
    #Generate ENSO Nino3.4 index for ACCESS SST data:
"""
    reload(access_prepare_ts)
    ENSO_Acc = Nino34(access_prepare_ts.dataFix_Acc,baseStart=baseStart,baseEnd=baseEnd,ACCESS=True)
    ENSO_running_Acc = running(ENSO_Acc,2,(len(ENSO_Acc)-3))

    ENSO_phase_Acc = ENSOphase(ENSO_running_Acc,2,(len(ENSO_running_Acc)-6))
    (ENSOpos, ENSOneg, ENSOneutral) = ENSO_phase_Acc

    ENSO_crop_Acc = cropRM(ENSO_running_Acc)

    return ENSO_crop_Acc,ENSOpos,ENSOneg,ENSOneutral


#HadISST data
HadNino = hadisstNino34()
(ENSO_crop_Had,ENSO_phase_Had,ENSOpos,ENSOneg,ENSOneutral) = HadNino

cropHad = ENSO_crop_Had
posHad = ENSOpos
negHad = ENSOneg
neutralHad = ENSOneutral

#access_ts_r1 data
r1 = accessNino34()
(ENSO_crop_Acc,ENSOpos,ENSOneg,ENSOneutral) = r1

cropR1 = ENSO_crop_Acc
posR1 = ENSOpos
negR1 = ENSOneg
neutralR1 = ENSOneutral

#access_ts_r2 data
r2 = accessNino34()
(ENSO_crop_Acc,ENSOpos,ENSOneg,ENSOneutral) = r2

cropR2 = ENSO_crop_Acc
posR2 = ENSOpos
negR2 = ENSOneg
neutralR2 = ENSOneutral

#access_ts_r3 data
r3 = accessNino34()
(ENSO_crop_Acc,ENSOpos,ENSOneg,ENSOneutral) = r3

cropR3 = ENSO_crop_Acc
posR3 = ENSOpos
negR3 = ENSOneg
neutralR3 = ENSOneutral


#Cropped running mean output to CSV:
output = np.column_stack((cropHad.flatten(),cropR1.flatten(),\
                          cropR2.flatten(),cropR3.flatten()))
np.savetxt('data/Nino3-4.csv',output,delimiter=',')
"""
