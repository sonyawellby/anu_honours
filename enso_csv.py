"""
Set of routines to compute the Nino3.4 ENSO index
and write to CSV files.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 4 September 2015.
"""

from enso import *
from parameters import baseStart,baseEnd

from hadisst_prepare import dataFix_Had
import access_prepare_ts

def Nino34(dataset,baseStart,baseEnd,ACCESS=True):
    """
    A function to compute the unfiltered (mean SST anomaly) values
    of the Nino3.4 ENSO index.

    Parameters:
    -----------
    dataset : the SST dataset of interest.  Either dataFix_Had
            (from 'hadisst_prepare') or 'access_prepare_ts'.
    baseStart : The first year of the base period. Defined in
                'parameters.py' as 'baseStart'.
    baseEnd : The last year of the base period.  Defined in
            'parameters.py' as 'baseEnd'.
    ACCESS : (default = True)
            If using ACCESS data, set as 'True'.  Else set as 'False'.
    """
    if ACCESS==True:
        AreaENSO = areaENSO(dataset,ACCESS=True)
        baseJan = baseAreaENSO(dataset[0::12],baseStart,baseEnd,ACCESS=True)
        baseFeb = baseAreaENSO(dataset[1::12],baseStart,baseEnd,ACCESS=True)
        baseMar = baseAreaENSO(dataset[2::12],baseStart,baseEnd,ACCESS=True)
        baseApr = baseAreaENSO(dataset[3::12],baseStart,baseEnd,ACCESS=True)
        baseMay = baseAreaENSO(dataset[4::12],baseStart,baseEnd,ACCESS=True)
        baseJun = baseAreaENSO(dataset[5::12],baseStart,baseEnd,ACCESS=True)
        baseJul = baseAreaENSO(dataset[6::12],baseStart,baseEnd,ACCESS=True)
        baseAug = baseAreaENSO(dataset[7::12],baseStart,baseEnd,ACCESS=True)
        baseSep = baseAreaENSO(dataset[8::12],baseStart,baseEnd,ACCESS=True)
        baseOct = baseAreaENSO(dataset[9::12],baseStart,baseEnd,ACCESS=True)
        baseNov = baseAreaENSO(dataset[10::12],baseStart,baseEnd,ACCESS=True)
        baseDec = baseAreaENSO(dataset[11::12],baseStart,baseEnd,ACCESS=True)
    elif ACCESS==False:
        AreaENSO = areaENSO(dataset,ACCESS=False)
        baseJan = baseAreaENSO(dataset[0::12],baseStart,baseEnd,ACCESS=False)
        baseFeb = baseAreaENSO(dataset[1::12],baseStart,baseEnd,ACCESS=False)
        baseMar = baseAreaENSO(dataset[2::12],baseStart,baseEnd,ACCESS=False)
        baseApr = baseAreaENSO(dataset[3::12],baseStart,baseEnd,ACCESS=False)
        baseMay = baseAreaENSO(dataset[4::12],baseStart,baseEnd,ACCESS=False)
        baseJun = baseAreaENSO(dataset[5::12],baseStart,baseEnd,ACCESS=False)
        baseJul = baseAreaENSO(dataset[6::12],baseStart,baseEnd,ACCESS=False)
        baseAug = baseAreaENSO(dataset[7::12],baseStart,baseEnd,ACCESS=False)
        baseSep = baseAreaENSO(dataset[8::12],baseStart,baseEnd,ACCESS=False)
        baseOct = baseAreaENSO(dataset[9::12],baseStart,baseEnd,ACCESS=False)
        baseNov = baseAreaENSO(dataset[10::12],baseStart,baseEnd,ACCESS=False)
        baseDec = baseAreaENSO(dataset[11::12],baseStart,baseEnd,ACCESS=False)
    else:
        raise ValueError('Specify whether ACCESS or HadISST are used.')

    AreaMonth = areaMonth(AreaENSO)
    (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec) = AreaMonth

    MeanJanBase = baseMeanSST(baseJan)
    MeanFebBase = baseMeanSST(baseFeb)
    MeanMarBase = baseMeanSST(baseMar)
    MeanAprBase = baseMeanSST(baseApr)
    MeanMayBase = baseMeanSST(baseMay)
    MeanJunBase = baseMeanSST(baseJun)
    MeanJulBase = baseMeanSST(baseJul)
    MeanAugBase = baseMeanSST(baseAug)
    MeanSepBase = baseMeanSST(baseSep)
    MeanOctBase = baseMeanSST(baseOct)
    MeanNovBase = baseMeanSST(baseNov)
    MeanDecBase = baseMeanSST(baseDec)

    anomJan = anomalies(Jan,MeanJanBase)
    anomFeb = anomalies(Feb,MeanFebBase)
    anomMar = anomalies(Mar,MeanMarBase)
    anomApr = anomalies(Apr,MeanAprBase)
    anomMay = anomalies(May,MeanMayBase)
    anomJun = anomalies(Jun,MeanJunBase)
    anomJul = anomalies(Jul,MeanJulBase)
    anomAug = anomalies(Aug,MeanAugBase)
    anomSep = anomalies(Sep,MeanSepBase)
    anomOct = anomalies(Oct,MeanOctBase)
    anomNov = anomalies(Nov,MeanNovBase)
    anomDec = anomalies(Dec,MeanDecBase)

    anomJanFinal = meanAnom(anomJan)
    anomFebFinal = meanAnom(anomFeb)
    anomMarFinal = meanAnom(anomMar)
    anomAprFinal = meanAnom(anomApr)
    anomMayFinal = meanAnom(anomMay)
    anomJunFinal = meanAnom(anomJun)
    anomJulFinal = meanAnom(anomJul)
    anomAugFinal = meanAnom(anomAug)
    anomSepFinal = meanAnom(anomSep)
    anomOctFinal = meanAnom(anomOct)
    anomNovFinal = meanAnom(anomNov)
    anomDecFinal = meanAnom(anomDec)

    months = np.array([anomJanFinal,anomFebFinal,anomMarFinal,anomAprFinal,\
                   anomMayFinal,anomJunFinal,anomJulFinal,anomAugFinal,\
                   anomSepFinal,anomOctFinal,anomNovFinal,anomDecFinal])

    anomMonths = months.flatten('F')
    return anomMonths


def hadisstNino34():
    """
    Generate ENSO Nino3.4 index for HadISST data:
    """
    ENSO_Had = Nino34(dataFix_Had,baseStart=baseStart,baseEnd=baseEnd,ACCESS=False)
    ENSO_running_Had = running(ENSO_Had,2,(len(ENSO_Had)-3))

    ENSO_phase_Had = ENSOphase(ENSO_running_Had,2,(len(ENSO_running_Had)-6))
    (ENSOpos, ENSOneg, ENSOneutral) = ENSO_phase_Had

    ENSO_crop_Had = cropRM(ENSO_running_Had)

    return ENSO_crop_Had,ENSO_phase_Had,ENSOpos,ENSOneg,ENSOneutral


def accessNino34():
    """
    Generate ENSO Nino3.4 index for ACCESS SST data:
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
np.savetxt('data/Nino3-4_5079.csv',output,delimiter=',')

