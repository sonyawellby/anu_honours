"""
Set of routines to compute the Nino3.4 ENSO index
and write to CSV files.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 25 August 2015.
"""

from enso import *

from hadisst_prepare import dataFix_Had
from access_prepare_ts import dataFix_Acc
"""
from hadisst_prepare import sst_JanuaryEx,sst_FebruaryEx,sst_MarchEx,\
     sst_AprilEx,sst_MayEx,sst_JuneEx,sst_JulyEx,sst_AugustEx,sst_SeptemberEx,\
     sst_OctoberEx,sst_NovemberEx,sst_DecemberEx

from access_prepare_ts import ts_January,ts_February,ts_March,\
     ts_April,ts_May,ts_June,ts_July,ts_August,ts_September,\
     ts_October,ts_November,ts_December

from hadisst_prepare import sst_January,sst_February,sst_March,\
     sst_April,sst_May,sst_June,sst_July,sst_August,sst_September,\
     sst_October,sst_November,sst_December
"""

def Nino34(dataset,baseStart,baseEnd,ACCESS=True):
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
        BaseAreaENSO = baseAreaENSO(dataset,baseStart,baseEnd,ACCESS=True)
    elif ACCESS==False:
        AreaENSO = areaENSO(dataset,ACCESS=False)
        BaseAreaENSO = baseAreaENSO(dataset,baseStart,baseEnd,ACCESS=False)
    else:
        raise ValueError('Specify whether ACCESS or HadISST are used.')

    BaseMeanSST = baseMeanSST(BaseAreaENSO)
    Anomalies = anomalies(AreaENSO,BaseMeanSST)
    MeanAnom = meanAnom(Anomalies)
    return MeanAnom

baseStart = 70
baseEnd = 100

#Generate ENSO Nino3.4 index for HadISST data:
ENSO_Had = Nino34(dataFix_Had,baseStart=baseStart,baseEnd=baseEnd,ACCESS=False)
ENSO_running_Had = running(ENSO_Had,2,(len(ENSO_Had)-3))

ENSO_phase_Had = ENSOphase(ENSO_running_Had,2,(len(ENSO_running_Had)-6))
(ENSOpos, ENSOneg, ENSOneutral) = ENSO_phase_Had
ENSOposHad = ENSOpos
ENSOnegHad = ENSOneg
ENSOneutralHad = ENSOneutral

ENSO_crop_Had = cropRM(ENSO_running_Had)
np.savetxt('data/Had_Nino3_4.csv',output,delimiter=',')

#Generate ENSO Nino3.4 index for ACCESS SST (access_ts_r1) data:
# Enter: 'access_ts_r1'
ENSO_Acc_r1 = Nino34(dataFix_Acc_r1,baseStart=baseStart,baseEnd=baseEnd,ACCESS=True)
ENSO_running_Acc_r1 = running(ENSO_Acc_r1,2,(len(ENSO_Acc_r1)-3))

ENSO_phase_Acc_r1 = ENSOphase(ENSO_running_Acc_r1,2,(len(ENSO_running_Acc_r1)-6))
(ENSOpos, ENSOneg, ENSOneutral) = ENSO_phase_Acc_r1
ENSOposAcc_r1 = ENSOpos
ENSOnegAcc_r1 = ENSOneg
ENSOneutralAcc_r1 = ENSOneutral

#Generate ENSO Nino3.4 index for ACCESS SST (access_ts_r2) data:
# Enter: 'access_ts_r2'
ENSO_Acc_r2 = Nino34(dataFix_Acc_r2,baseStart=baseStart,baseEnd=baseEnd,ACCESS=True)
ENSO_running_Acc_r2 = running(ENSO_Acc_r2,2,(len(ENSO_Acc_r2)-3))

ENSO_phase_Acc_r2 = ENSOphase(ENSO_running_Acc_r2,2,(len(ENSO_running_Acc_r2)-6))
(ENSOpos, ENSOneg, ENSOneutral) = ENSO_phase_Acc_r2
ENSOposAcc_r2 = ENSOpos
ENSOnegAcc_r2 = ENSOneg
ENSOneutralAcc_r2 = ENSOneutral


#Generate ENSO Nino3.4 index for ACCESS SST (access_ts_r3) data:
# Enter: 'access_ts_r3'
ENSO_Acc_r3 = Nino34(dataFix_Acc_r3,baseStart=baseStart,baseEnd=baseEnd,ACCESS=True)
ENSO_running_Acc_r3 = running(ENSO_Acc_r3,2,(len(ENSO_Acc_r3)-3))

ENSO_phase_Acc_r3 = ENSOphase(ENSO_running_Acc_r3,2,(len(ENSO_running_Acc_r3)-6))
(ENSOpos, ENSOneg, ENSOneutral) = ENSO_phase_Acc_r3
ENSOposAcc_r3 = ENSOpos
ENSOnegAcc_r3 = ENSOneg
ENSOneutralAcc_r3 = ENSOneutral

#Output to CSV:
ENSO_crop_Had = cropRM(ENSO_running_Had)
ENSO_crop_Acc_r1 = cropRM(ENSO_running_Acc_r1)
ENSO_crop_Acc_r2 = cropRM(ENSO_running_Acc_r2)
ENSO_crop_Acc_r3 = cropRM(ENSO_running_Acc_r3)

output = np.column_stack((ENSO_crop_Had.flatten(),ENSO_crop_Acc_r1.flatten(),\
                          ENSO_crop_Acc_r2.flatten(),ENSO_crop_Acc_r3.flatten()))
np.savetxt('data/Nino3_4.csv',output,delimiter=',')


"""
#test = [1,-1,3,4,5,6,7,8,9]
test = [-2,-0.3,0,0.2,1,5,0.4,-0.4,10,5,6,5,3,2,0.1,-5]

#run = [3,4,1,16,2,8,6,2,86]
test1 = running(test,2,(len(test)-3))

run = cropRM(test1)

ENSOphases = ENSOphase(test1,0,(len(test1)-6))
(ENSOpos,ENSOneg,ENSOneutral) = ENSOphases
"""

