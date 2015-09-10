"""
A file to correlate ENSO with rainfall and the IPO with rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 September 2015.
"""
import netCDF4 as n
import numpy as np
import scipy.stats as stats
import numpy.ma as ma

from indices_array import Nino34,TPI 


from indices_time import Nino34_Jun, Nino34_Jul, Nino34_Aug, Nino34_Sep, \
     Nino34_Oct, Nino34_Nov, Nino34_Dec, Nino34_Jan, Nino34_Feb, Nino34_Mar,\
     Nino34_Apr, Nino34_May, Nino34_JJA, Nino34_SON, Nino34_DJF, Nino34_MAM,\
    Nino34_annual, TPI_Jun, TPI_Jul, TPI_Aug, TPI_Sep, TPI_Oct, TPI_Nov,\
    TPI_Dec, TPI_Jan, TPI_Feb, TPI_Mar, TPI_Apr, TPI_May, TPI_JJA, TPI_SON, \
    TPI_DJF, TPI_MAM, TPI_annual


from awap_prepare import awap_June,awap_JJA
from access_trimmed import trim_June

from matplotlib import pyplot as plt
from plot import plot, mapCorr

from cwd import cwdInFunction
cwdInFunction()


def corr(rainfall,index,ind_num):
    """
    A function to correlate rainfall (AWAP or ACCESS) with an index
    (e.g. IPO, ENSO).

    Parameters:
    -----------
    Rainfall: the dataset of rainfall.
    Index: the dataset of the index.
    """
    corr_array = np.zeros((27,22))
    count1 = 0
    while count1 < 27:
        count2 = 0
        while count2 < 22:
            a = stats.pearsonr(rainfall[:,count1,count2],index[ind_num])
            #print a
            corr_array[count1,count2] = a[0]
            count2 += 1
            #print "count2 = ",count2
        count1 +=1
        count2 = 0
    return corr_array
    

#test = corr(awap_June,Nino34_Jun)
test = corr(awap_JJA,TPI_JJA,1)
test1 = ma.masked_invalid(test)
Dict6 = mapCorr()
myplot = plot(test1,Dict6,labels=False,grid=False,oceans=False,cbar=True)
plt.show(myplot)
