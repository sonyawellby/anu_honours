"""
A file to compute Pearson's correlation coefficient and
significance for the ENSO and the IPO indices.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 September 2015.
"""
import netCDF4 as n
import numpy as np
import scipy.stats

from indices_time import indexTime 
from indices_array import Nino34, TPI
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


def normal(data,num):
    #Checks to see if dataset is normally distributed.
    dat = np.array(data[num])
    z,pval = scipy.stats.mstats.normaltest(dat)
    return pval


def correl(index1,index2,num1,num2):
    """
    Pearson's correlation coefficient [-1,1]
    """
    cc = scipy.stats.pearsonr(index1[num1],index2[num2])
    return cc

#Correlations between Nino 3.4 and TPI data derived from HadISST1 (observations)
def correlAll(num1,num2):
    June = correl(Nino34_Jun,TPI_Jun,num1,num2)
    July = correl(Nino34_Jul,TPI_Jul,num1,num2)
    August = correl(Nino34_Aug,TPI_Aug,num1,num2)
    September = correl(Nino34_Sep,TPI_Sep,num1,num2)
    October = correl(Nino34_Oct,TPI_Oct,num1,num2)
    November = correl(Nino34_Nov,TPI_Nov,num1,num2)
    December = correl(Nino34_Dec,TPI_Dec,num1,num2)
    January = correl(Nino34_Jan,TPI_Jan,num1,num2)
    February = correl(Nino34_Feb,TPI_Feb,num1,num2)
    March = correl(Nino34_Mar,TPI_Mar,num1,num2)
    April = correl(Nino34_Apr,TPI_Apr,num1,num2)
    May = correl(Nino34_May,TPI_May,num1,num2)
    JJA = correl(Nino34_JJA,TPI_JJA,num1,num2)
    SON = correl(Nino34_SON,TPI_SON,num1,num2)
    DJF = correl(Nino34_DJF,TPI_DJF,num1,num2)
    MAM = correl(Nino34_MAM,TPI_MAM,num1,num2)
    annual = correl(Nino34_annual,TPI_annual,num1,num2)
    return June, July, August, September, October, November, December, January,\
           February, March, April, May, JJA, SON, DJF, MAM, annual

#HadISST1
corr = correlAll(0,1)
(June, July, August, September, October, November, December, January,\
           February, March, April, May, JJA, SON, DJF, MAM, annual) = corr

Had_June = June
Had_July = July
Had_August = August
Had_September = September
Had_October = October
Had_November = November
Had_December = December
Had_January = January
Had_February = February
Had_March = March
Had_April = April
Had_May = May
Had_JJA = JJA
Had_SON = SON
Had_DJF = DJF
Had_MAM = MAM
Had_annual = annual

HadISST_all = np.array([Had_June, Had_July, Had_August, Had_September, \
                     Had_October, Had_November, Had_December, \
                     Had_January, Had_February, Had_March,Had_April, \
                     Had_May, Had_JJA, Had_SON, Had_DJF,\
                    Had_MAM,Had_annual])

HadISST = np.array([Had_June[0], Had_July[0], Had_August[0], Had_September[0], \
                     Had_October[0], Had_November[0], Had_December[0], \
                     Had_January[0], Had_February[0], Had_March[0],Had_April[0], \
                     Had_May[0], Had_JJA[0], Had_SON[0], Had_DJF[0],\
                    Had_MAM[0],Had_annual[0]])

HadISST_sig = np.array([Had_June[1], Had_July[1], Had_August[1], Had_September[1],\
                     Had_October[1], Had_November[1], Had_December[1], \
                     Had_January[1], Had_February[1], Had_March[1],Had_April[1], \
                     Had_May[1], Had_JJA[1], Had_SON[1], Had_DJF[1],\
                    Had_MAM[1],Had_annual[1]])


#ACCESS1.3 R1
corr = correlAll(1,3)
(June, July, August, September, October, November, December, January,\
           February, March, April, May, JJA, SON, DJF, MAM, annual) = corr

AccR1_June = June
AccR1_July = July
AccR1_August = August
AccR1_September = September
AccR1_October = October
AccR1_November = November
AccR1_December = December
AccR1_January = January
AccR1_February = February
AccR1_March = March
AccR1_April = April
AccR1_May = May
AccR1_JJA = JJA
AccR1_SON = SON
AccR1_DJF = DJF
AccR1_MAM = MAM
AccR1_annual = annual

accessR1 = np.array([AccR1_June[0], AccR1_July[0], AccR1_August[0],\
                     AccR1_September[0], AccR1_October[0], \
            AccR1_November[0], AccR1_December[0], AccR1_January[0],\
                     AccR1_February[0], \
            AccR1_March[0], AccR1_April[0], AccR1_May[0], AccR1_JJA[0],\
                     AccR1_SON[0], \
            AccR1_DJF[0], AccR1_MAM[0], AccR1_annual[0]])

accessR1_all = np.array([AccR1_June, AccR1_July, AccR1_August,\
                     AccR1_September, AccR1_October, \
            AccR1_November, AccR1_December, AccR1_January,AccR1_February, \
            AccR1_March, AccR1_April, AccR1_May, AccR1_JJA,AccR1_SON, \
            AccR1_DJF, AccR1_MAM, AccR1_annual])

accessR1_sig = np.array([AccR1_June[1], AccR1_July[1], AccR1_August[1],\
                     AccR1_September[1], AccR1_October[1], \
            AccR1_November[1], AccR1_December[1], AccR1_January[1],\
                     AccR1_February[1], \
            AccR1_March[1], AccR1_April[1], AccR1_May[1], AccR1_JJA[1],\
                     AccR1_SON[1], \
            AccR1_DJF[1], AccR1_MAM[1], AccR1_annual[1]])

#ACCESS1.3 R2
corr = correlAll(2,5)
(June, July, August, September, October, November, December, January,\
           February, March, April, May, JJA, SON, DJF, MAM, annual) = corr

AccR2_June = June
AccR2_July = July
AccR2_August = August
AccR2_September = September
AccR2_October = October
AccR2_November = November
AccR2_December = December
AccR2_January = January
AccR2_February = February
AccR2_March = March
AccR2_April = April
AccR2_May = May
AccR2_JJA = JJA
AccR2_SON = SON
AccR2_DJF = DJF
AccR2_MAM = MAM
AccR2_annual = annual

accessR2 = np.array([AccR2_June[0], AccR2_July[0], AccR2_August[0],\
                     AccR2_September[0], AccR2_October[0], \
            AccR2_November[0], AccR2_December[0], AccR2_January[0],\
                     AccR2_February[0], \
            AccR2_March[0], AccR2_April[0], AccR2_May[0], AccR2_JJA[0],\
                     AccR2_SON[0], \
            AccR2_DJF[0], AccR2_MAM[0], AccR2_annual[0]])

accessR2_all = np.array([AccR2_June, AccR2_July, AccR2_August,\
                     AccR2_September, AccR2_October, \
            AccR2_November, AccR2_December, AccR2_January,AccR2_February, \
            AccR2_March, AccR2_April, AccR2_May, AccR2_JJA,AccR2_SON, \
            AccR2_DJF, AccR2_MAM, AccR2_annual])

accessR2_sig = np.array([AccR2_June[1], AccR2_July[1], AccR2_August[1],\
                     AccR2_September[1], AccR2_October[1], \
            AccR2_November[1], AccR2_December[1], AccR2_January[1],\
                     AccR2_February[1], \
            AccR2_March[1], AccR2_April[1], AccR2_May[1], AccR2_JJA[1],\
                     AccR2_SON[1], \
            AccR2_DJF[1], AccR2_MAM[1], AccR2_annual[1]])

#ACCESS1.3 R3
corr = correlAll(3,7)
(June, July, August, September, October, November, December, January,\
           February, March, April, May, JJA, SON, DJF, MAM, annual) = corr

AccR3_June = June
AccR3_July = July
AccR3_August = August
AccR3_September = September
AccR3_October = October
AccR3_November = November
AccR3_December = December
AccR3_January = January
AccR3_February = February
AccR3_March = March
AccR3_April = April
AccR3_May = May
AccR3_JJA = JJA
AccR3_SON = SON
AccR3_DJF = DJF
AccR3_MAM = MAM
AccR3_annual = annual

accessR3 = np.array([AccR3_June[0], AccR3_July[0], AccR3_August[0],\
                     AccR3_September[0], AccR3_October[0], \
            AccR3_November[0], AccR3_December[0], AccR3_January[0],\
                     AccR3_February[0], \
            AccR3_March[0], AccR3_April[0], AccR3_May[0], AccR3_JJA[0],\
                     AccR3_SON[0], \
            AccR3_DJF[0], AccR3_MAM[0], AccR3_annual[0]])

accessR3_all = np.array([AccR3_June, AccR3_July, AccR3_August,\
                     AccR3_September, AccR3_October, \
            AccR3_November, AccR3_December, AccR3_January,AccR3_February, \
            AccR3_March, AccR3_April, AccR3_May, AccR3_JJA,AccR3_SON, \
            AccR3_DJF, AccR3_MAM, AccR3_annual])

accessR3_sig = np.array([AccR3_June[1], AccR3_July[1], AccR3_August[1],\
                     AccR3_September[1], AccR3_October[1], \
            AccR3_November[1], AccR3_December[1], AccR3_January[1],\
                     AccR3_February[1], \
            AccR3_March[1], AccR3_April[1], AccR3_May[1], AccR3_JJA[1],\
                     AccR3_SON[1], \
            AccR3_DJF[1], AccR3_MAM[1], AccR3_annual[1]])


"""
#Test to see if this function matches Excel's output:
hey = np.array([Nino34[0],TPI[1]])
hey1 = np.corrcoef(hey)
"""
