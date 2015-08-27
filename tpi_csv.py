"""
Set of routines to compute the TPI IPO index and return
its output in the .csv file format.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 27 August 2015.
"""

import csv
from tpi import *
from parameters import baseStart,baseEnd,n,rp,wn

from hadisst_prepare import sst_January, sst_February, sst_March,\
     sst_April,sst_May,sst_June,sst_July,sst_August,sst_September,\
     sst_October,sst_November,sst_December

import access_prepare_ts


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
    if ACCESS==True:
        AreaTPI = areaTPI(dataset, ACCESS=True)
        (area1,area2,area3)=AreaTPI

        BaseAreaTPI = baseAreaTPI(dataset,baseStart,baseEnd,ACCESS=True)
        (base_area1,base_area2,base_area3) = BaseAreaTPI
    elif ACCESS==False:
        AreaTPI = areaTPI(dataset, ACCESS=False)
        (area1,area2,area3)=AreaTPI

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


def hadUF():
    """
    A function to compute the unfiltered HadISST TPI and return a flat array. 
    """
    Had_JanTPI_uf = unfilteredTPI(sst_January,baseStart,baseEnd,ACCESS=False)
    Had_FebTPI_uf = unfilteredTPI(sst_February,baseStart,baseEnd,ACCESS=False)
    Had_MarTPI_uf = unfilteredTPI(sst_March,baseStart,baseEnd,ACCESS=False)
    Had_AprTPI_uf = unfilteredTPI(sst_April,baseStart,baseEnd,ACCESS=False)
    Had_MayTPI_uf = unfilteredTPI(sst_May,baseStart,baseEnd,ACCESS=False)
    Had_JunTPI_uf = unfilteredTPI(sst_June,baseStart,baseEnd,ACCESS=False)
    Had_JulTPI_uf = unfilteredTPI(sst_July,baseStart,baseEnd,ACCESS=False)
    Had_AugTPI_uf = unfilteredTPI(sst_August,baseStart,baseEnd,ACCESS=False)
    Had_SepTPI_uf = unfilteredTPI(sst_September,baseStart,baseEnd,ACCESS=False)
    Had_OctTPI_uf = unfilteredTPI(sst_October,baseStart,baseEnd,ACCESS=False)
    Had_NovTPI_uf = unfilteredTPI(sst_November,baseStart,baseEnd,ACCESS=False)
    Had_DecTPI_uf = unfilteredTPI(sst_December,baseStart,baseEnd,ACCESS=False)

    Had_months_uf = np.array([Had_JanTPI_uf,Had_FebTPI_uf,Had_MarTPI_uf,Had_AprTPI_uf,\
                       Had_MayTPI_uf,Had_JunTPI_uf,Had_JulTPI_uf,Had_AugTPI_uf,\
                       Had_SepTPI_uf,Had_OctTPI_uf,Had_NovTPI_uf,Had_DecTPI_uf])

    Had_monthsTPI_uf = Had_months_uf.flatten('F')
    return Had_monthsTPI_uf

def accUF():
    """
    A function to compute the unfiltered ACCESS TPI and return a flat array. 
    """
    print 'Computing ACCESS unfiltered, flat array (all times).'
    reload(access_prepare_ts)
    from access_prepare_ts import ts_January, ts_February, ts_March,\
     ts_April,ts_May,ts_June,ts_July,ts_August,ts_September,\
     ts_October,ts_November,ts_December
    
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

    Acc_months_uf = np.array([Acc_JanTPI_uf,Acc_FebTPI_uf,Acc_MarTPI_uf,Acc_AprTPI_uf,\
                       Acc_MayTPI_uf,Acc_JunTPI_uf,Acc_JulTPI_uf,Acc_AugTPI_uf,\
                       Acc_SepTPI_uf,Acc_OctTPI_uf,Acc_NovTPI_uf,Acc_DecTPI_uf])

    Acc_monthsTPI_uf = Acc_months_uf.flatten('F')
    return Acc_monthsTPI_uf

"""
Compute unfiltered TPI indices
Enter: access_ts_r1, access_ts_r2,access_ts_r3
"""

Had_monthsTPI_uf = hadUF()
Acc_monthsTPI_uf_r1 = accUF()
Acc_monthsTPI_uf_r2 = accUF()
Acc_monthsTPI_uf_r3 = accUF()


"""
Compute filtered TPI indices
"""

Had_monthsTPI = TPI(Had_monthsTPI_uf,n,rp,wn)
Acc_monthsTPI_r1 = TPI(Acc_monthsTPI_uf_r1,n,rp,wn)
Acc_monthsTPI_r2 = TPI(Acc_monthsTPI_uf_r2,n,rp,wn)
Acc_monthsTPI_r3 = TPI(Acc_monthsTPI_uf_r3,n,rp,wn)

"""
Generate IPO phases
"""
IPO_phase_Had = IPOphase(Had_monthsTPI)
(IPOpos, IPOneg, IPOneutral) = IPO_phase_Had
posHad = IPOpos
negHad = IPOneg
neutralHad = IPOneutral

IPO_phase_r1 = IPOphase(Acc_monthsTPI_r1)
(IPOpos, IPOneg, IPOneutral) = IPO_phase_r1
posR1 = IPOpos
negR1 = IPOneg
neutralR1 = IPOneutral

IPO_phase_r2 = IPOphase(Acc_monthsTPI_r2)
(IPOpos, IPOneg, IPOneutral) = IPO_phase_r2
posR2 = IPOpos
negR2 = IPOneg
neutralR2 = IPOneutral

IPO_phase_r3 = IPOphase(Acc_monthsTPI_r3)
(IPOpos, IPOneg, IPOneutral) = IPO_phase_r3
posR3 = IPOpos
negR3 = IPOneg
neutralR3 = IPOneutral



"""
#Write filtered and unfiltered data to CSV files
"""
output = np.column_stack((Had_monthsTPI_uf.flatten(),Had_monthsTPI.flatten(),\
                          Acc_monthsTPI_uf_r1.flatten(),Acc_monthsTPI_r1.flatten(),\
                          Acc_monthsTPI_uf_r2.flatten(),Acc_monthsTPI_r2.flatten(),\
                          Acc_monthsTPI_uf_r3.flatten(),Acc_monthsTPI_r3.flatten()))
np.savetxt('data/TPI.csv',output,delimiter=',')

