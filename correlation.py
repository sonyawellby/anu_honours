"""
A file to correlate ENSO with rainfall and the IPO with rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 September 2015.
"""
import netCDF4 as n
import numpy as np

from indices_time import Nino34_Jun, Nino34_Jul, Nino34_Aug, Nino34_Sep, \
     Nino34_Oct, Nino34_Nov, Nino34_Dec, Nino34_Jan, Nino34_Feb, Nino34_Mar,\
     Nino34_Apr, Nino34_May, Nino34_JJA, Nino34_SON, Nino34_DJF, Nino34_MAM,\
    Nino34_annual, TPI_Jun, TPI_Jul, TPI_Aug, TPI_Sep, TPI_Oct, TPI_Nov,\
    TPI_Dec, TPI_Jan, TPI_Feb, TPI_Mar, TPI_Apr, TPI_May, TPI_JJA, TPI_SON, \
    TPI_DJF, TPI_MAM, TPI_annual

from awap_prepare import awap_June
from access_trimmed import trim_June

from cwd import cwdInFunction
cwdInFunction()

"""
def corrCoef(list1,list2,num):
    count = 0
    while count < 105:
        for i in list1[count]:
            for j in i:
                corrCoeff = np.corrcoef(j,list2[num][count])
                print corrCoeff
                count += 1
    return corrCoeff
"""
"""
def corrCoef(list1,list2,num):
    count = 0
    while count < 105:
        for i in list1[count]:
            corrCoeff = np.corrcoef(list1,list2[num])
            print corrCoeff
            count += 1
    return corrCoeff
"""

def correlCoef(list1,list2):
    count = 0
    new = []
    while count < 105:
        for i in range(27):
            for j in range(22):
                cc = np.ma.corrcoef(list1[count],list2[count])
                new.append(cc)
        count += 1
    new1 = np.asarray(new)
    return new


"""
def correlCoef(list1,list2):
    
    
a = np.array([awap_June,Nino34_Jun])
c = np.ma.corrcoef(a)
"""

test = correlCoef(awap_June,Nino34_Jun)





