"""
Set of routines to compute the Nino3.4 ENSO index
and write to CSV files.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 22 September 2015.
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


def hadisstNino34(var):
    """
    Generate ENSO Nino3.4 index for HadISST data:

    Parameters:
    -----------
    var : 'y' or 'n'.  Supplied by raw_input below.
    """
    if var == 'y':
        ENSO_Had = Nino34(dataFix_Had,baseStart=baseStart,baseEnd=baseEnd,ACCESS=False)
        ENSO_running_Had = running(ENSO_Had,2,(len(ENSO_Had)-3))

        ENSOsd = ensoSD(ENSO_running_Had,crop=True)
        (data,ENSOpos, ENSOneg, ENSOneutral) = ENSOsd
        ENSO_crop_Had = data
        ENSOpos1 = ENSOpos
        ENSOneg1 = ENSOneg
        ENSOneutral1 = ENSOneutral
        
        jja = runningSeasons(ENSO_running_Had,3,0,4)
        ENSO_JJA = ensoSD(jja)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_JJA
        ENSOpos_JJA = ENSOpos
        ENSOneg_JJA = ENSOneg
        ENSOneutral_JJA = ENSOneutral

        son = runningSeasons(ENSO_crop_Had,3,1,4)
        ENSO_SON = ensoSD(son)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_SON
        ENSOpos_SON = ENSOpos
        ENSOneg_SON = ENSOneg
        ENSOneutral_SON = ENSOneutral

        djf = runningSeasons(ENSO_crop_Had,3,2,4)
        ENSO_DJF = ensoSD(djf)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_DJF
        ENSOpos_DJF = ENSOpos
        ENSOneg_DJF = ENSOneg
        ENSOneutral_DJF = ENSOneutral

        mam = runningSeasons(ENSO_crop_Had,3,0,4)
        ENSO_MAM = ensoSD(mam)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_MAM
        ENSOpos_MAM = ENSOpos
        ENSOneg_MAM = ENSOneg
        ENSOneutral_MAM = ENSOneutral

        annual = runningSeasons(ENSO_crop_Had,12,0,1)
        Annual = ensoSD(annual)
        (data, ENSOpos, ENSOneg, ENSOneutral) = Annual
        ENSOpos_Annual = ENSOpos
        ENSOneg_Annual = ENSOneg
        ENSOneutral_Annual = ENSOneutral

        return ENSO_crop_Had,ENSOpos1,ENSOneg1,ENSOneutral1,ENSOpos_JJA,ENSOneg_JJA,\
           ENSOneutral_JJA,ENSOpos_SON,ENSOneg_SON,ENSOneutral_SON,ENSOpos_DJF,\
           ENSOneg_DJF,ENSOneutral_DJF,ENSOpos_MAM,ENSOneg_MAM,ENSOneutral_MAM,\
           ENSOpos_Annual,ENSOneg_Annual,ENSOneutral_Annual
        
    elif var == 'n':
        ENSO_Had = Nino34(dataFix_Had,baseStart=baseStart,baseEnd=baseEnd,ACCESS=False)
        ENSO_running_Had = running(ENSO_Had,2,(len(ENSO_Had)-3))

        ENSOsd = ensoSD(ENSO_running_Had,crop=True)
        (data,ENSOpos, ENSOneg, ENSOneutral) = ENSOsd
        ENSO_crop_Had = data
        ENSOpos1 = ENSOpos
        ENSOneg1 = ENSOneg
        ENSOneutral1 = ENSOneutral

        jja = runningSeasons(ENSO_crop_Had,3,0,4)
        ENSO_JJA = ensoSD(jja)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_JJA
        ENSOpos_JJA = ENSOpos
        ENSOneg_JJA = ENSOneg
        ENSOneutral_JJA = ENSOneutral

        son = runningSeasons(ENSO_crop_Had,3,1,4)
        ENSO_SON = ensoSD(son)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_SON
        ENSOpos_SON = ENSOpos
        ENSOneg_SON = ENSOneg
        ENSOneutral_SON = ENSOneutral

        djf = runningSeasons(ENSO_crop_Had,3,2,4)
        ENSO_DJF = ensoSD(djf)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_DJF
        ENSOpos_DJF = ENSOpos
        ENSOneg_DJF = ENSOneg
        ENSOneutral_DJF = ENSOneutral

        mam = runningSeasons(ENSO_crop_Had,3,0,4)
        ENSO_MAM = ensoSD(mam)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_MAM
        ENSOpos_MAM = ENSOpos
        ENSOneg_MAM = ENSOneg
        ENSOneutral_MAM = ENSOneutral

        annual = runningSeasons(ENSO_crop_Had,12,0,1)
        Annual = ensoSD(annual)
        (data, ENSOpos, ENSOneg, ENSOneutral) = Annual
        ENSOpos_Annual = ENSOpos
        ENSOneg_Annual = ENSOneg
        ENSOneutral_Annual = ENSOneutral

        return ENSO_crop_Had,ENSOpos1,ENSOneg1,ENSOneutral1,ENSOpos_JJA,ENSOneg_JJA,\
           ENSOneutral_JJA,ENSOpos_SON,ENSOneg_SON,ENSOneutral_SON,ENSOpos_DJF,\
           ENSOneg_DJF,ENSOneutral_DJF,ENSOpos_MAM,ENSOneg_MAM,ENSOneutral_MAM,\
            ENSOpos_Annual,ENSOneg_Annual,ENSOneutral_Annual
        
    else:
        pass
    return


def accessNino34(var):
    """
    Generate ENSO Nino3.4 index for ACCESS SST data:

    Parameters:
    -----------
    var : 'y' or 'n'.  Default is supplied by raw_input below.
    """
    reload(access_prepare_ts)
    if var == 'y':
        ENSO_Acc = Nino34(access_prepare_ts.dataFix_Acc,baseStart=baseStart,baseEnd=baseEnd,ACCESS=True)
        ENSO_running_Acc = running(ENSO_Acc,2,(len(ENSO_Acc)-3))

        ENSOsd = ensoSD(ENSO_running_Acc,crop=True)
        (data,ENSOpos, ENSOneg, ENSOneutral) = ENSOsd
        ENSO_crop_Acc = data
        ENSOpos1 = ENSOpos
        ENSOneg1 = ENSOneg
        ENSOneutral1 = ENSOneutral
        
        jja = runningSeasons(ENSO_crop_Acc,3,0,4)
        ENSO_JJA = ensoSD(jja)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_JJA
        ENSOpos_JJA = ENSOpos
        ENSOneg_JJA = ENSOneg
        ENSOneutral_JJA = ENSOneutral

        son = runningSeasons(ENSO_crop_Acc,3,1,4)
        ENSO_SON = ensoSD(son)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_SON
        ENSOpos_SON = ENSOpos
        ENSOneg_SON = ENSOneg
        ENSOneutral_SON = ENSOneutral

        djf = runningSeasons(ENSO_crop_Acc,3,2,4)
        ENSO_DJF = ensoSD(djf)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_DJF
        ENSOpos_DJF = ENSOpos
        ENSOneg_DJF = ENSOneg
        ENSOneutral_DJF = ENSOneutral

        mam = runningSeasons(ENSO_crop_Acc,3,0,4)
        ENSO_MAM = ensoSD(mam)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_MAM
        ENSOpos_MAM = ENSOpos
        ENSOneg_MAM = ENSOneg
        ENSOneutral_MAM = ENSOneutral

        annual = runningSeasons(ENSO_crop_Acc,12,0,1)
        Annual = ensoSD(annual)
        (data, ENSOpos, ENSOneg, ENSOneutral) = Annual
        ENSOpos_Annual = ENSOpos
        ENSOneg_Annual = ENSOneg
        ENSOneutral_Annual = ENSOneutral

        return ENSO_crop_Acc,ENSOpos1,ENSOneg1,ENSOneutral1,ENSOpos_JJA,ENSOneg_JJA,\
           ENSOneutral_JJA,ENSOpos_SON,ENSOneg_SON,ENSOneutral_SON,ENSOpos_DJF,\
           ENSOneg_DJF,ENSOneutral_DJF,ENSOpos_MAM,ENSOneg_MAM,ENSOneutral_MAM,\
           ENSOpos_Annual,ENSOneg_Annual,ENSOneutral_Annual
        
    elif var == 'n':
        ENSO_Acc = Nino34(access_prepare_ts.dataFix_Acc,baseStart=baseStart,baseEnd=baseEnd,ACCESS=True)
        ENSO_running_Acc = running(ENSO_Acc,2,(len(ENSO_Acc)-3))

        ENSOsd = ensoSD(ENSO_running_Acc,crop=True)
        (data,ENSOpos, ENSOneg, ENSOneutral) = ENSOsd
        ENSO_crop_Acc = data
        ENSOpos1 = ENSOpos
        ENSOneg1 = ENSOneg
        ENSOneutral1 = ENSOneutral

        jja = runningSeasons(ENSO_crop_Acc,3,0,4)
        ENSO_JJA = ensoSD(jja)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_JJA
        ENSOpos_JJA = ENSOpos
        ENSOneg_JJA = ENSOneg
        ENSOneutral_JJA = ENSOneutral

        son = runningSeasons(ENSO_crop_Acc,3,1,4)
        ENSO_SON = ensoSD(son)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_SON
        ENSOpos_SON = ENSOpos
        ENSOneg_SON = ENSOneg
        ENSOneutral_SON = ENSOneutral

        djf = runningSeasons(ENSO_crop_Acc,3,2,4)
        ENSO_DJF = ensoSD(djf)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_DJF
        ENSOpos_DJF = ENSOpos
        ENSOneg_DJF = ENSOneg
        ENSOneutral_DJF = ENSOneutral

        mam = runningSeasons(ENSO_crop_Acc,3,0,4)
        ENSO_MAM = ensoSD(mam)
        (data,ENSOpos,ENSOneg,ENSOneutral) = ENSO_MAM
        ENSOpos_MAM = ENSOpos
        ENSOneg_MAM = ENSOneg
        ENSOneutral_MAM = ENSOneutral

        annual = runningSeasons(ENSO_crop_Acc,12,0,1)
        Annual = ensoSD(annual)
        (data, ENSOpos, ENSOneg, ENSOneutral) = Annual
        ENSOpos_Annual = ENSOpos
        ENSOneg_Annual = ENSOneg
        ENSOneutral_Annual = ENSOneutral

        return ENSO_crop_Acc,ENSOpos1,ENSOneg1,ENSOneutral1,ENSOpos_JJA,ENSOneg_JJA,\
           ENSOneutral_JJA,ENSOpos_SON,ENSOneg_SON,ENSOneutral_SON,ENSOpos_DJF,\
           ENSOneg_DJF,ENSOneutral_DJF,ENSOpos_MAM,ENSOneg_MAM,ENSOneutral_MAM,\
           ENSOpos_Annual,ENSOneg_Annual,ENSOneutral_Annual

    else:
        pass
    return

var = raw_input("Are you computing normal standard deviations (i.e. not 2sd, 3sd)? y/n ")

#HadISST data
HadNino = hadisstNino34(var)
(ENSO_crop_Had,ENSOpos,ENSOneg,ENSOneutral,ENSOpos_JJA,ENSOneg_JJA,\
 ENSOneutral_JJA,ENSOpos_SON,ENSOneg_SON,ENSOneutral_SON,ENSOpos_DJF,\
 ENSOneg_DJF,ENSOneutral_DJF,ENSOpos_MAM,ENSOneg_MAM,ENSOneutral_MAM,\
 ENSOpos_Annual,ENSOneg_Annual,ENSOneutral_Annual) = HadNino

cropHad = ENSO_crop_Had
posHad = ENSOpos
negHad = ENSOneg
neutralHad = ENSOneutral

ENSOpos_JJA_Had = ENSOpos_JJA
ENSOneg_JJA_Had = ENSOneg_JJA
ENSOneutral_JJA_Had = ENSOneutral_JJA
ENSOpos_SON_Had = ENSOpos_SON
ENSOneg_SON_Had = ENSOneg_SON
ENSOneutral_SON_Had = ENSOneutral_SON
ENSOpos_DJF_Had = ENSOpos_DJF
ENSOneg_DJF_Had = ENSOneg_DJF
ENSOneutral_DJF_Had = ENSOneutral_DJF
ENSOpos_MAM_Had = ENSOpos_MAM
ENSOneg_MAM_Had = ENSOneg_MAM
ENSOneutral_MAM_Had = ENSOneutral_MAM
ENSOpos_Annual_Had = ENSOpos_Annual
ENSOneg_Annual_Had = ENSOneg_Annual
ENSOneutral_Annual_Had = ENSOneutral_Annual

#access_ts_r1 data
r1 = accessNino34(var)
(ENSO_crop_Acc,ENSOpos,ENSOneg,ENSOneutral,ENSOpos_JJA,ENSOneg_JJA,\
 ENSOneutral_JJA,ENSOpos_SON,ENSOneg_SON,ENSOneutral_SON,ENSOpos_DJF,\
 ENSOneg_DJF,ENSOneutral_DJF,ENSOpos_MAM,ENSOneg_MAM,ENSOneutral_MAM,\
 ENSOpos_Annual,ENSOneg_Annual,ENSOneutral_Annual) = r1

cropR1 = ENSO_crop_Acc
posR1 = ENSOpos
negR1 = ENSOneg
neutralR1 = ENSOneutral

ENSOpos_JJA_R1 = ENSOpos_JJA
ENSOneg_JJA_R1 = ENSOneg_JJA
ENSOneutral_JJA_R1 = ENSOneutral_JJA
ENSOpos_SON_R1 = ENSOpos_SON
ENSOneg_SON_R1 = ENSOneg_SON
ENSOneutral_SON_R1 = ENSOneutral_SON
ENSOpos_DJF_R1 = ENSOpos_DJF
ENSOneg_DJF_R1 = ENSOneg_DJF
ENSOneutral_DJF_R1 = ENSOneutral_DJF
ENSOpos_MAM_R1 = ENSOpos_MAM
ENSOneg_MAM_R1 = ENSOneg_MAM
ENSOneutral_MAM_R1 = ENSOneutral_MAM
ENSOpos_Annual_R1 = ENSOpos_Annual
ENSOneg_Annual_R1 = ENSOneg_Annual
ENSOneutral_Annual_R1 = ENSOneutral_Annual

#access_ts_r2 data
r2 = accessNino34(var)
(ENSO_crop_Acc,ENSOpos,ENSOneg,ENSOneutral,ENSOpos_JJA,ENSOneg_JJA,\
 ENSOneutral_JJA,ENSOpos_SON,ENSOneg_SON,ENSOneutral_SON,ENSOpos_DJF,\
 ENSOneg_DJF,ENSOneutral_DJF,ENSOpos_MAM,ENSOneg_MAM,ENSOneutral_MAM,\
 ENSOpos_Annual,ENSOneg_Annual,ENSOneutral_Annual) = r2

cropR2 = ENSO_crop_Acc
posR2 = ENSOpos
negR2 = ENSOneg
neutralR2 = ENSOneutral

ENSOpos_JJA_R2 = ENSOpos_JJA
ENSOneg_JJA_R2 = ENSOneg_JJA
ENSOneutral_JJA_R2 = ENSOneutral_JJA
ENSOpos_SON_R2 = ENSOpos_SON
ENSOneg_SON_R2 = ENSOneg_SON
ENSOneutral_SON_R2 = ENSOneutral_SON
ENSOpos_DJF_R2 = ENSOpos_DJF
ENSOneg_DJF_R2 = ENSOneg_DJF
ENSOneutral_DJF_R2 = ENSOneutral_DJF
ENSOpos_MAM_R2 = ENSOpos_MAM
ENSOneg_MAM_R2 = ENSOneg_MAM
ENSOneutral_MAM_R2 = ENSOneutral_MAM

ENSOpos_Annual_R2 = ENSOpos_Annual
ENSOneg_Annual_R2 = ENSOneg_Annual
ENSOneutral_Annual_R2 = ENSOneutral_Annual


#access_ts_r3 data
r3 = accessNino34(var)
(ENSO_crop_Acc,ENSOpos,ENSOneg,ENSOneutral,ENSOpos_JJA,ENSOneg_JJA,\
 ENSOneutral_JJA,ENSOpos_SON,ENSOneg_SON,ENSOneutral_SON,ENSOpos_DJF,\
 ENSOneg_DJF,ENSOneutral_DJF,ENSOpos_MAM,ENSOneg_MAM,ENSOneutral_MAM,\
 ENSOpos_Annual,ENSOneg_Annual,ENSOneutral_Annual) = r3

cropR3 = ENSO_crop_Acc
posR3 = ENSOpos
negR3 = ENSOneg
neutralR3 = ENSOneutral

ENSOpos_JJA_R3 = ENSOpos_JJA
ENSOneg_JJA_R3 = ENSOneg_JJA
ENSOneutral_JJA_R3 = ENSOneutral_JJA
ENSOpos_SON_R3 = ENSOpos_SON
ENSOneg_SON_R3 = ENSOneg_SON
ENSOneutral_SON_R3 = ENSOneutral_SON
ENSOpos_DJF_R3 = ENSOpos_DJF
ENSOneg_DJF_R3 = ENSOneg_DJF
ENSOneutral_DJF_R3 = ENSOneutral_DJF
ENSOpos_MAM_R3 = ENSOpos_MAM
ENSOneg_MAM_R3 = ENSOneg_MAM
ENSOneutral_MAM_R3 = ENSOneutral_MAM

ENSOpos_Annual_R3 = ENSOpos_Annual
ENSOneg_Annual_R3 = ENSOneg_Annual
ENSOneutral_Annual_R3 = ENSOneutral_Annual

"""
#Cropped running mean output to CSV:
output = np.column_stack((cropHad.flatten(),cropR1.flatten(),\
                          cropR2.flatten(),cropR3.flatten()))
np.savetxt('data/Nino3-4.csv',output,delimiter=',')

"""
