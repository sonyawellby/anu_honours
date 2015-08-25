"""
Set of routines to compute the Nino3.4 ENSO index
and write to CSV files.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 25 August 2015.
"""

from enso import *

from hadisst_prepare import sst_JanuaryEx,sst_FebruaryEx,sst_MarchEx,\
     sst_AprilEx,sst_MayEx,sst_JuneEx,sst_JulyEx,sst_AugustEx,sst_SeptemberEx,\
     sst_OctoberEx,sst_NovemberEx,sst_DecemberEx

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

testy = Nino34(sst_JanuaryEx,71,100,ACCESS=False)

"""
from access_prepare_ts import ts_January,ts_February,ts_March,\
     ts_April,ts_May,ts_June,ts_July,ts_August,ts_September,\
     ts_October,ts_November,ts_December

from hadisst_prepare import sst_January,sst_February,sst_March,\
     sst_April,sst_May,sst_June,sst_July,sst_August,sst_September,\
     sst_October,sst_November,sst_December
"""

"""
#test = [1,-1,3,4,5,6,7,8,9]
test = [-2,-0.3,0,0.2,1,5,0.4,-0.4,10,5,6,5,3,2,0.1,-5]

#run = [3,4,1,16,2,8,6,2,86]
test1 = running(test,2,(len(test)-3))

run = cropRM(test1)

ENSOphases = ENSOphase(test1,0,(len(test1)-6))
(ENSOpos,ENSOneg,ENSOneutral) = ENSOphases
"""

#_____________________________________________    
#from hadisst_prepare import sst_Annual
#from access_prepare_ts import ts_Annual,dataFix,ts_JJA


"""
def test():
    hi = "hi"
    bye = "bye"
    return hi,bye
    
test = test()
(hello,cya)=test #associates 'hello' and 'cya' with output of function (unpacks tuple)
"""

#Actual code
#areaENSO = areaENSO()
