"""
A file to test for cross-correlation between the ENSO and IPO indices.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 September 2015.
"""
import netCDF4 as n
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

from indices_time import indexTime
from indices_array import Nino34, TPI
from pylab import savefig
from cwd import cwdInFunction

cwdInFunction()

enso = indexTime(Nino34)
(Nino34_Jun, Nino34_Jul, Nino34_Aug, Nino34_Sep, Nino34_Oct, Nino34_Nov, \
 Nino34_Dec, Nino34_Jan, Nino34_Feb, Nino34_Mar, Nino34_Apr, Nino34_May,\
 Nino34_JJA, Nino34_SON, Nino34_DJF, Nino34_MAM, Nino34_annual) = enso

ipo = indexTime(TPI)
(TPI_Jun, TPI_Jul, TPI_Aug, TPI_Sep, TPI_Oct, TPI_Nov, TPI_Dec, \
 TPI_Jan, TPI_Feb, TPI_Mar, TPI_Apr, TPI_May,\
 TPI_JJA, TPI_SON, TPI_DJF, TPI_MAM, TPI_annual) = ipo

"""
def xCorrel(index1,index2,num1,num2):
"""
#    Cross-correlation test.
"""
    xcor = scipy.signal.correlate(index1[num1],index2[num2])
    return xcor
"""

def plotXCorrel(data1,data2,title,filename):
    a = plt.xcorr(data1,data2)
    plt.ylabel('Cross-correlation')
    plt.xlabel('Lag')
    plt.title(title)
    savefig(filename)
    #plt.show()
    plt.close()
    return


def xCorrelAll(num1,num2):
    """
    Correlations between Nino 3.4 and TPI data derived from HadISST1 (observations)
    """
    June = xCorrel(Nino34_Jun,TPI_Jun,num1,num2)
    July = xCorrel(Nino34_Jul,TPI_Jul,num1,num2)
    August = xCorrel(Nino34_Aug,TPI_Aug,num1,num2)
    September = xCorrel(Nino34_Sep,TPI_Sep,num1,num2)
    October = xCorrel(Nino34_Oct,TPI_Oct,num1,num2)
    November = xCorrel(Nino34_Nov,TPI_Nov,num1,num2)
    December = xCorrel(Nino34_Dec,TPI_Dec,num1,num2)
    January = xCorrel(Nino34_Jan,TPI_Jan,num1,num2)
    February = xCorrel(Nino34_Feb,TPI_Feb,num1,num2)
    March = xCorrel(Nino34_Mar,TPI_Mar,num1,num2)
    April = xCorrel(Nino34_Apr,TPI_Apr,num1,num2)
    May = xCorrel(Nino34_May,TPI_May,num1,num2)
    JJA = xCorrel(Nino34_JJA,TPI_JJA,num1,num2)
    SON = xCorrel(Nino34_SON,TPI_SON,num1,num2)
    DJF = xCorrel(Nino34_DJF,TPI_DJF,num1,num2)
    MAM = xCorrel(Nino34_MAM,TPI_MAM,num1,num2)
    annual = xCorrel(Nino34_annual,TPI_annual,num1,num2)
    return June, July, August, September, October, November, December, January,\
           February, March, April, May, JJA, SON, DJF, MAM, annual

#June = Nino34_Jun[1],TPI_Jun[1]
"""
xcorrHad = xCorrelAll(0,1)
(June, July, August, September, October, November, December, January,\
           February, March, April, May, JJA, SON, DJF, MAM, annual) = xcorrHad
"""
"""
a = plt.xcorr(Nino34_JJA[0],TPI_JJA[0])
plt.ylabel('Cross-correlation measure')
plt.xlabel('Lag')
plt.show(a)
"""
plotXCorrel(Nino34_JJA[0],TPI_JJA[0],"JJA","xcorr/JJA_Had.png")
plotXCorrel(Nino34_SON[0],TPI_SON[0],"SON","xcorr/SON_Had.png")



