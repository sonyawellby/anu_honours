"""
Set of routines to compute the TPI IPO index and return
its output in the .csv file format.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 24 August 2015.
"""
#Check if need still:
"""
#from access_prepare_ts import ts_Annual,dataFix,ts_JJA,ts_January
#area1 = ts_Annual[60:90,92:109,74:116]
#area1a = ts_JJA[60:90,92:109,74:116]
"""

import csv
from tpi import *

from hadisst_prepare import sst_January, sst_February, sst_March,\
     sst_April,sst_May,sst_June,sst_July,sst_August,sst_September,\
     sst_October,sst_November,sst_December

from access_prepare_ts import ts_January, ts_February, ts_March,\
     ts_April,ts_May,ts_June,ts_July,ts_August,ts_September,\
     ts_October,ts_November,ts_December


def unfilteredTPI(dataset,baseStart,baseEnd,ACCESS=True):
    """
    A function to compute the unfiltered values of the TPI.

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
    if ACCESS=True:
        AreaTPI = areaTPI(dataset, ACCESS=True)
        (area1,area2,area3)=AreaTPI #Unpacks tuple so can access 'area1','area2','area3'

        BaseAreaTPI = baseAreaTPI(dataset,baseStart,baseEnd,ACCESS=True)
        (base_area1,base_area2,base_area3) = BaseAreaTPI
    elif:
        AreaTPI = areaTPI(dataset, ACCESS=False)
        (area1,area2,area3)=AreaTPI #Unpacks tuple so can access 'area1','area2','area3'

        BaseAreaTPI = baseAreaTPI(dataset,baseStart,baseEnd,ACCESS=False)
        (base_area1,base_area2,base_area3) = BaseAreaTPI
    else:
        raise ValueError('Specify whether ACCESS or HadISST are used.')

    BaseMeanSST = baseMeanSST(base_area1,base_area2,base_area3)
    (base_SST1,base_SST2,base_SST3)= BaseMeanSST

    Anomalies = anomalies(area1,area2,area3,base_SST1,base_SST2,base_SST3)
    (anomalies1,anomalies2,anomalies3) = Anomalies

    MeanAnom = meanAnom(anomalies1,anomalies2,anomalies3)
    (meanAnom1, meanAnom2, meanAnom3) = MeanAnom

    TPIunfiltered = TPIunfil(meanAnom1,meanAnom2,meanAnom3)
    return TPIunfiltered

def season(month1,month2,month3):
    """
    A function to compute the TPI (filtered or unfiltered)
    for the four seasons.

    Parameters:
    -----------
    month1,month2,month3: the three months to be averaged;
        months are computed from unfilteredTPI() or
        filteredTPI().
    """
    m1m2 = np.add(month1,month2)
    m1m2m3 = np.add(m1m2,month3)
    average = np.divide(m1m2m3,3.0)
    return average

def annual(season1,season2,season3,season4):
    """
    A function to compute the annual TPI (filtered or unfiltered)
    values.

    Parameters:
    -----------
    season1,season2,season3,season4:
        the four seasons to be averaged;
        seasons are computed from season().
    """
    s1s2 = np.add(season1,season2)
    s3s4 = np.add(season3,season4)
    seasons_all = np.add(s1s2,s3s4)
    average = np.divide(seasons_all,4.0)
    return average

#Define base period
baseStart = 70
baseEnd = 90

#Define Chebyshev low pass filter parameters
n = 6
rp = 13
wn = 0.1

"""
Compute unfiltered Hadisst TPI indices
"""

#MONTHLY
Had_JanTPI_uf = unfilteredTPI(sst_January,baseStart,baseEnd)
Had_FebTPI_uf = unfilteredTPI(sst_February,baseStart,baseEnd)
Had_MarTPI_uf = unfilteredTPI(sst_March,baseStart,baseEnd)
Had_AprTPI_uf = unfilteredTPI(sst_April,baseStart,baseEnd)
Had_MayTPI_uf = unfilteredTPI(sst_May,baseStart,baseEnd)
Had_JunTPI_uf = unfilteredTPI(sst_June,baseStart,baseEnd)
Had_JulTPI_uf = unfilteredTPI(sst_July,baseStart,baseEnd)
Had_AugTPI_uf = unfilteredTPI(sst_August,baseStart,baseEnd)
Had_SepTPI_uf = unfilteredTPI(sst_September,baseStart,baseEnd)
Had_OctTPI_uf = unfilteredTPI(sst_October,baseStart,baseEnd)
Had_NovTPI_uf = unfilteredTPI(sst_November,baseStart,baseEnd)
Had_DecTPI_uf = unfilteredTPI(sst_December,baseStart,baseEnd)

#SEASONAL
Had_DJF_uf = season(Had_DecTPI_uf,Had_JanTPI_uf,Had_FebTPI_uf)
Had_MAM_uf = season(Had_MarTPI_uf,Had_AprTPI_uf,Had_MayTPI_uf)
Had_JJA_uf = season(Had_JunTPI_uf,Had_JulTPI_uf,Had_AugTPI_uf)
Had_SON_uf = season(Had_SepTPI_uf,Had_OctTPI_uf,Had_NovTPI_uf)

#ANNUAL
Had_annual_uf = annual(Had_DJF_uf,Had_MAM_uf,Had_JJA_uf,Had_SON_uf)

"""
Compute filtered HadISST TPI indices
"""

#MONTHLY
Had_JanTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_FebTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_MarTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_AprTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_MayTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_JunTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_JulTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_AugTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_SepTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_OctTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_NovTPI = TPI(n,rp,wn,Had_JanTPI_uf)
Had_DecTPI = TPI(n,rp,wn,Had_JanTPI_uf)

#SEASONAL
Had_DJF = season(Had_DecTPI,Had_JanTPI,Had_FebTPI)
Had_MAM = season(Had_MarTPI,Had_AprTPI,Had_MayTPI)
Had_JJA = season(Had_JunTPI,Had_JulTPI,Had_AugTPI)
Had_SON = season(Had_SepTPI,Had_OctTPI,Had_NovTPI)

#ANNUAL
Had_annual = annual(Had_DJF,Had_MAM,Had_JJA,Had_SON)


"""
Compute ACCESS SST TPI indices
"""

#MONTHLY
Acc_JanTPI_uf = unfilteredTPI(ts_January,baseStart,baseEnd)
Acc_FebTPI_uf = unfilteredTPI(ts_February,baseStart,baseEnd)
Acc_MarTPI_uf = unfilteredTPI(ts_March,baseStart,baseEnd)
Acc_AprTPI_uf = unfilteredTPI(ts_April,baseStart,baseEnd)
Acc_MayTPI_uf = unfilteredTPI(ts_May,baseStart,baseEnd)
Acc_JunTPI_uf = unfilteredTPI(ts_June,baseStart,baseEnd)
Acc_JulTPI_uf = unfilteredTPI(ts_July,baseStart,baseEnd)
Acc_AugTPI_uf = unfilteredTPI(ts_August,baseStart,baseEnd)
Acc_SepTPI_uf = unfilteredTPI(ts_September,baseStart,baseEnd)
Acc_OctTPI_uf = unfilteredTPI(ts_October,baseStart,baseEnd)
Acc_NovTPI_uf = unfilteredTPI(ts_November,baseStart,baseEnd)
Acc_DecTPI_uf = unfilteredTPI(ts_December,baseStart,baseEnd)

#SEASONAL
Acc_DJF_uf = season(Acc_DecTPI_uf,Acc_JanTPI_uf,Acc_FebTPI_uf)
Acc_MAM_uf = season(Acc_MarTPI_uf,Acc_AprTPI_uf,Acc_MayTPI_uf)
Acc_JJA_uf = season(Acc_JunTPI_uf,Acc_JulTPI_uf,Acc_AugTPI_uf)
Acc_SON_uf = season(Acc_SepTPI_uf,Acc_OctTPI_uf,Acc_NovTPI_uf)

#ANNUAL
Acc_annual_uf = annual(Acc_DJF_uf,Acc_MAM_uf,Acc_JJA_uf,Acc_SON_uf)

"""
Compute filtered ACCESS SST TPI indices
"""

#MONTHLY
Acc_JanTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_FebTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_MarTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_AprTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_MayTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_JunTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_JulTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_AugTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_SepTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_OctTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_NovTPI = TPI(n,rp,wn,Acc_JanTPI_uf)
Acc_DecTPI = TPI(n,rp,wn,Acc_JanTPI_uf)

#SEASONAL
Acc_DJF = season(Acc_DecTPI,Acc_JanTPI,Acc_FebTPI)
Acc_MAM = season(Acc_MarTPI,Acc_AprTPI,Acc_MayTPI)
Acc_JJA = season(Acc_JunTPI,Acc_JulTPI,Acc_AugTPI)
Acc_SON = season(Acc_SepTPI,Acc_OctTPI,Acc_NovTPI)

#ANNUAL
Acc_annual = annual(Acc_DJF,Acc_MAM,Acc_JJA,Acc_SON)


"""
Write data to CSV files
"""
  
hadisst_uf = np.column_stack((Had_annual_uf.flatten(),Had_DJF_uf.flatten(),Had_MAM_uf.flatten(),\
                          Had_JJA_uf.flatten(),Had_SON_uf.flatten(),Had_JanTPI_uf.flatten(),\
                          Had_FebTPI_uf.flatten(),Had_MarTPI_uf.flatten(),Had_AprTPI_uf.flatten(),
                          Had_MayTPI_uf.flatten(),Had_JunTPI_uf.flatten(),Had_JulTPI_uf.flatten(),\
                          Had_AugTPI_uf.flatten(),Had_SepTPI_uf.flatten(),Had_OctTPI_uf.flatten(),\
                          Had_NovTPI_uf.flatten(),Had_DecTPI_uf.flatten()))
np.savetxt('data/hadisst_unfiltered.csv',hadisst_uf,delimiter=',')

hadisst_f = np.column_stack((Had_annual.flatten(),Had_DJF.flatten(),Had_MAM.flatten(),\
                          Had_JJA.flatten(),Had_SON.flatten(),Had_JanTPI.flatten(),\
                          Had_FebTPI.flatten(),Had_MarTPI.flatten(),Had_AprTPI.flatten(),
                          Had_MayTPI.flatten(),Had_JunTPI.flatten(),Had_JulTPI.flatten(),\
                          Had_AugTPI.flatten(),Had_SepTPI.flatten(),Had_OctTPI.flatten(),\
                          Had_NovTPI.flatten(),Had_DecTPI.flatten()))
np.savetxt('data/hadisst_filtered.csv',hadisst_f,delimiter=',')

access_uf = np.column_stack((Acc_annual_uf.flatten(),Acc_DJF_uf.flatten(),Acc_MAM_uf.flatten(),\
                          Acc_JJA_uf.flatten(),Acc_SON_uf.flatten(),Acc_JanTPI_uf.flatten(),\
                          Acc_FebTPI_uf.flatten(),Acc_MarTPI_uf.flatten(),Acc_AprTPI_uf.flatten(),
                          Acc_MayTPI_uf.flatten(),Acc_JunTPI_uf.flatten(),Acc_JulTPI_uf.flatten(),\
                          Acc_AugTPI_uf.flatten(),Acc_SepTPI_uf.flatten(),Acc_OctTPI_uf.flatten(),\
                          Acc_NovTPI_uf.flatten(),Acc_DecTPI_uf.flatten()))
np.savetxt('data/access_unfiltered.csv',access_uf,delimiter=',')

access_f = np.column_stack((Acc_annual.flatten(),Acc_DJF.flatten(),Acc_MAM.flatten(),\
                          Acc_JJA.flatten(),Acc_SON.flatten(),Acc_JanTPI.flatten(),\
                          Acc_FebTPI.flatten(),Acc_MarTPI.flatten(),Acc_AprTPI.flatten(),
                          Acc_MayTPI.flatten(),Acc_JunTPI.flatten(),Acc_JulTPI.flatten(),\
                          Acc_AugTPI.flatten(),Acc_SepTPI.flatten(),Acc_OctTPI.flatten(),\
                          Acc_NovTPI.flatten(),Acc_DecTPI.flatten()))
np.savetxt('data/access_filtered.csv',access_f,delimiter=',')

