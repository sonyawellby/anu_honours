"""
Set of routines to compute the TPI IPO index and return
its output in the .csv file format.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 25 September 2015.
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


def hadisst_access_TPI(dataTPI):
    """
    Generate IPO TPI index for HadISST and ACCESS data.

    Parameters:
    ------------
    dataTPI: either Had_monthsTPI or Acc_monthsTPI_r1 or Acc_monthsTPI_r2
            or Acc_monthsTPI_r3
    """

    jja = runningSeasons(dataTPI,3,0,4)
    IPO_JJA = IPOphase(jja)
    (IPOpos_JJA,IPOneg_JJA,IPOneutral_JJA) = IPO_JJA

    son = runningSeasons(dataTPI,3,1,4)
    IPO_SON = IPOphase(son)
    (IPOpos_SON,IPOneg_SON,IPOneutral_SON) = IPO_SON

    djf = runningSeasons(dataTPI,3,2,4)
    IPO_DJF = IPOphase(djf)
    (IPOpos_DJF,IPOneg_DJF,IPOneutral_DJF) = IPO_DJF

    mam = runningSeasons(dataTPI,3,0,4)
    IPO_MAM = IPOphase(mam)
    (IPOpos_MAM,IPOneg_MAM,IPOneutral_MAM) = IPO_MAM

    annual = runningSeasons(dataTPI,12,0,1)
    Annual = IPOphase(annual)
    (IPOpos_Annual, IPOneg_Annual, IPOneutral_Annual) = Annual

    return IPOpos_JJA,IPOneg_JJA,\
           IPOneutral_JJA,IPOpos_SON,IPOneg_SON,IPOneutral_SON,IPOpos_DJF,\
           IPOneg_DJF,IPOneutral_DJF,IPOpos_MAM,IPOneg_MAM,IPOneutral_MAM,\
           IPOpos_Annual,IPOneg_Annual,IPOneutral_Annual
     

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

IPO_had_JJA = runningSeasons(Had_monthsTPI,3,0,4)
IPO_had_SON = runningSeasons(Had_monthsTPI,3,1,4)
IPO_had_DJF = runningSeasons(Had_monthsTPI,3,2,4)
IPO_had_MAM = runningSeasons(Had_monthsTPI,3,3,4)
IPO_had_Annual = runningSeasons(Had_monthsTPI,12,0,1)

IPO_R1_JJA = runningSeasons(Acc_monthsTPI_r1,3,0,4)
IPO_R1_SON = runningSeasons(Acc_monthsTPI_r1,3,1,4)
IPO_R1_DJF = runningSeasons(Acc_monthsTPI_r1,3,2,4)
IPO_R1_MAM = runningSeasons(Acc_monthsTPI_r1,3,3,4)
IPO_R1_Annual = runningSeasons(Acc_monthsTPI_r1,12,0,1)

IPO_R2_JJA = runningSeasons(Acc_monthsTPI_r2,3,0,4)
IPO_R2_SON = runningSeasons(Acc_monthsTPI_r2,3,1,4)
IPO_R2_DJF = runningSeasons(Acc_monthsTPI_r2,3,2,4)
IPO_R2_MAM = runningSeasons(Acc_monthsTPI_r2,3,3,4)
IPO_R2_Annual = runningSeasons(Acc_monthsTPI_r2,12,0,1)

IPO_R3_JJA = runningSeasons(Acc_monthsTPI_r3,3,0,4)
IPO_R3_SON = runningSeasons(Acc_monthsTPI_r3,3,1,4)
IPO_R3_DJF = runningSeasons(Acc_monthsTPI_r3,3,2,4)
IPO_R3_MAM = runningSeasons(Acc_monthsTPI_r3,3,3,4)
IPO_R3_Annual = runningSeasons(Acc_monthsTPI_r3,12,0,1)


"""
Generate IPO phases (mask the data according to IPO phases)
"""
#HadISST
seasons_Had = hadisst_access_TPI(Had_monthsTPI)
(IPOpos_JJA,IPOneg_JJA,\
           IPOneutral_JJA,IPOpos_SON,IPOneg_SON,IPOneutral_SON,IPOpos_DJF,\
           IPOneg_DJF,IPOneutral_DJF,IPOpos_MAM,IPOneg_MAM,IPOneutral_MAM,\
           IPOpos_Annual,IPOneg_Annual,IPOneutral_Annual) = seasons_Had

IPO_Had = IPOphase(Had_monthsTPI)
(IPOpos, IPOneg, IPOneutral) = IPO_Had
posHad = IPOpos
negHad = IPOneg
neutralHad = IPOneutral

Had_IPOpos_JJA = IPOpos_JJA
Had_IPOneg_JJA = IPOneg_JJA
Had_IPOneutral_JJA = IPOneutral_JJA
Had_IPOpos_SON = IPOpos_SON
Had_IPOneg_SON = IPOneg_SON
Had_IPOneutral_SON = IPOneutral_SON
Had_IPOpos_DJF = IPOpos_DJF
Had_IPOneg_DJF = IPOneg_DJF
Had_IPOneutral_DJF = IPOneutral_DJF
Had_IPOpos_MAM = IPOpos_MAM
Had_IPOneg_MAM = IPOneg_MAM
Had_IPOneutral_MAM = IPOneutral_MAM
Had_IPOpos_Annual = IPOpos_Annual
Had_IPOneg_Annual = IPOneg_Annual
Had_IPOneutral_Annual = IPOneutral_Annual

#ACCESS R1

seasons_R1 = hadisst_access_TPI(Acc_monthsTPI_r1)
(IPOpos_JJA,IPOneg_JJA,\
           IPOneutral_JJA,IPOpos_SON,IPOneg_SON,IPOneutral_SON,IPOpos_DJF,\
           IPOneg_DJF,IPOneutral_DJF,IPOpos_MAM,IPOneg_MAM,IPOneutral_MAM,\
           IPOpos_Annual,IPOneg_Annual,IPOneutral_Annual) = seasons_R1

IPO_phase_r1 = IPOphase(Acc_monthsTPI_r1)
(IPOpos, IPOneg, IPOneutral) = IPO_phase_r1
posR1 = IPOpos
negR1 = IPOneg
neutralR1 = IPOneutral

R1_IPOpos_JJA = IPOpos_JJA
R1_IPOneg_JJA = IPOneg_JJA
R1_IPOneutral_JJA = IPOneutral_JJA
R1_IPOpos_SON = IPOpos_SON
R1_IPOneg_SON = IPOneg_SON
R1_IPOneutral_SON = IPOneutral_SON
R1_IPOpos_DJF = IPOpos_DJF
R1_IPOneg_DJF = IPOneg_DJF
R1_IPOneutral_DJF = IPOneutral_DJF
R1_IPOpos_MAM = IPOpos_MAM
R1_IPOneg_MAM = IPOneg_MAM
R1_IPOneutral_MAM = IPOneutral_MAM
R1_IPOpos_Annual = IPOpos_Annual
R1_IPOneg_Annual = IPOneg_Annual
R1_IPOneutral_Annual = IPOneutral_Annual

#ACCESS R2

seasons_R2 = hadisst_access_TPI(Acc_monthsTPI_r2)
(IPOpos_JJA,IPOneg_JJA,\
           IPOneutral_JJA,IPOpos_SON,IPOneg_SON,IPOneutral_SON,IPOpos_DJF,\
           IPOneg_DJF,IPOneutral_DJF,IPOpos_MAM,IPOneg_MAM,IPOneutral_MAM,\
           IPOpos_Annual,IPOneg_Annual,IPOneutral_Annual) = seasons_R2

IPO_phase_r2 = IPOphase(Acc_monthsTPI_r2)
(IPOpos, IPOneg, IPOneutral) = IPO_phase_r2
posR2 = IPOpos
negR2 = IPOneg
neutralR2 = IPOneutral

R2_IPOpos_JJA = IPOpos_JJA
R2_IPOneg_JJA = IPOneg_JJA
R2_IPOneutral_JJA = IPOneutral_JJA
R2_IPOpos_SON = IPOpos_SON
R2_IPOneg_SON = IPOneg_SON
R2_IPOneutral_SON = IPOneutral_SON
R2_IPOpos_DJF = IPOpos_DJF
R2_IPOneg_DJF = IPOneg_DJF
R2_IPOneutral_DJF = IPOneutral_DJF
R2_IPOpos_MAM = IPOpos_MAM
R2_IPOneg_MAM = IPOneg_MAM
R2_IPOneutral_MAM = IPOneutral_MAM
R2_IPOpos_Annual = IPOpos_Annual
R2_IPOneg_Annual = IPOneg_Annual
R2_IPOneutral_Annual = IPOneutral_Annual

#ACCESS R3

seasons_R3 = hadisst_access_TPI(Acc_monthsTPI_r3)
(IPOpos_JJA,IPOneg_JJA,\
           IPOneutral_JJA,IPOpos_SON,IPOneg_SON,IPOneutral_SON,IPOpos_DJF,\
           IPOneg_DJF,IPOneutral_DJF,IPOpos_MAM,IPOneg_MAM,IPOneutral_MAM,\
           IPOpos_Annual,IPOneg_Annual,IPOneutral_Annual) = seasons_R3

IPO_phase_r3 = IPOphase(Acc_monthsTPI_r3)
(IPOpos, IPOneg, IPOneutral) = IPO_phase_r3
posR3 = IPOpos
negR3 = IPOneg
neutralR3 = IPOneutral

R3_IPOpos_JJA = IPOpos_JJA
R3_IPOneg_JJA = IPOneg_JJA
R3_IPOneutral_JJA = IPOneutral_JJA
R3_IPOpos_SON = IPOpos_SON
R3_IPOneg_SON = IPOneg_SON
R3_IPOneutral_SON = IPOneutral_SON
R3_IPOpos_DJF = IPOpos_DJF
R3_IPOneg_DJF = IPOneg_DJF
R3_IPOneutral_DJF = IPOneutral_DJF
R3_IPOpos_MAM = IPOpos_MAM
R3_IPOneg_MAM = IPOneg_MAM
R3_IPOneutral_MAM = IPOneutral_MAM
R3_IPOpos_Annual = IPOpos_Annual
R3_IPOneg_Annual = IPOneg_Annual
R3_IPOneutral_Annual = IPOneutral_Annual


"""
Write filtered and unfiltered data to CSV files
"""

output = np.column_stack((Had_monthsTPI_uf.flatten(),Had_monthsTPI.flatten(),\
                          Acc_monthsTPI_uf_r1.flatten(),Acc_monthsTPI_r1.flatten(),\
                          Acc_monthsTPI_uf_r2.flatten(),Acc_monthsTPI_r2.flatten(),\
                          Acc_monthsTPI_uf_r3.flatten(),Acc_monthsTPI_r3.flatten()))
np.savetxt('data/TPI.csv',output,delimiter=',')


