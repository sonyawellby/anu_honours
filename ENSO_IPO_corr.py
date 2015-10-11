"""
A file to compute Pearson's correlation coefficient and
significance for the ENSO and the IPO indices.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 25 September 2015.
"""
import netCDF4 as n
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pylab
#from statsmodels.stats.multicomp import pairwise_tukeyhsd

from enso_csv import enso_JJA_Had, enso_SON_Had, enso_DJF_Had,\
     enso_MAM_Had, enso_Annual_Had, enso_JJA_R1, enso_SON_R1,\
     enso_DJF_R1,enso_MAM_R1, enso_Annual_R1,enso_JJA_R2, \
     enso_SON_R2, enso_DJF_R2,enso_MAM_R2, enso_Annual_R2,\
     enso_JJA_R3, enso_SON_R3, enso_DJF_R3,enso_MAM_R3, \
     enso_Annual_R3

from tpi_csv import IPO_had_JJA,IPO_had_SON,IPO_had_DJF,\
     IPO_had_MAM,IPO_had_Annual,IPO_R1_JJA,IPO_R1_SON,\
     IPO_R1_DJF,IPO_R1_MAM,IPO_R1_Annual,IPO_R2_JJA,\
     IPO_R2_SON,IPO_R2_DJF,IPO_R2_MAM,IPO_R2_Annual,\
     IPO_R3_JJA,IPO_R3_SON,IPO_R3_DJF,IPO_R3_MAM,IPO_R3_Annual

from cwd import cwdInFunction
cwdInFunction()

from indices_phase import enso_Jun_Had,enso_Jul_Had,enso_Aug_Had,enso_Sep_Had,\
     enso_Oct_Had,enso_Nov_Had,enso_Dec_Had,enso_Jan_Had,\
     enso_Feb_Had,enso_Mar_Had,enso_Apr_Had,enso_May_Had,\
     enso_Jun_R1,enso_Jul_R1,enso_Aug_R1,enso_Sep_R1,\
     enso_Oct_R1,enso_Nov_R1,enso_Dec_R1,enso_Jan_R1,\
     enso_Feb_R1,enso_Mar_R1,enso_Apr_R1,enso_May_R1,\
     enso_Jun_R2,enso_Jul_R2,enso_Aug_R2,enso_Sep_R2,\
     enso_Oct_R2,enso_Nov_R2,enso_Dec_R2,enso_Jan_R2,\
     enso_Feb_R2,enso_Mar_R2,enso_Apr_R2,enso_May_R2,\
     enso_Jun_R3,enso_Jul_R3,enso_Aug_R3,enso_Sep_R3,\
     enso_Oct_R3,enso_Nov_R3,enso_Dec_R3,enso_Jan_R3,\
     enso_Feb_R3,enso_Mar_R3,enso_Apr_R3,enso_May_R3,\
     IPO_had_Jun,IPO_had_Jul,IPO_had_Aug,IPO_had_Sep,\
     IPO_had_Oct,IPO_had_Nov,IPO_had_Dec,IPO_had_Jan,\
     IPO_had_Feb,IPO_had_Mar,IPO_had_Apr,IPO_had_May,\
     IPO_R1_Jun,IPO_R1_Jul,IPO_R1_Aug,IPO_R1_Sep,\
     IPO_R1_Oct,IPO_R1_Nov,IPO_R1_Dec,IPO_R1_Jan,\
     IPO_R1_Feb,IPO_R1_Mar,IPO_R1_Apr,IPO_R1_May,\
     IPO_R2_Jun,IPO_R2_Jul,IPO_R2_Aug,IPO_R2_Sep,\
     IPO_R2_Oct,IPO_R2_Nov,IPO_R2_Dec,IPO_R2_Jan,\
     IPO_R2_Feb,IPO_R2_Mar,IPO_R2_Apr,IPO_R2_May,\
     IPO_R3_Jun,IPO_R3_Jul,IPO_R3_Aug,IPO_R3_Sep,\
     IPO_R3_Oct,IPO_R3_Nov,IPO_R3_Dec,IPO_R3_Jan,\
     IPO_R3_Feb,IPO_R3_Mar,IPO_R3_Apr,IPO_R3_May

def normal(data):
    """
    Checks to see if dataset is normally distributed.  Returns
    the p-value for the dataset (if p > 0.05 it is normally
    distributed; otherwise it is not).
    """
    dat = np.array(data)
    z,pval = stats.normaltest(dat)
    return pval

def printNormal():
    """
    Print the output of normal() for the index datasets used,
    to allow visual inspection.
    """
    for i in hadISST_ENSO:
        print "hadISST_ENSO ",normal(i)
    for i in R1_ENSO:
        print "R1_ENSO ", normal(i)
    for i in R2_ENSO:
        print "R2_ENSO ", normal(i)
    for i in R3_ENSO:
        print "R3_ENSO ", normal(i)
    for i in hadISST_IPO:
        print "hadISST_IPO ",normal(i)
    for i in R1_IPO:
        print "R1_IPO ", normal(i)
    for i in R2_IPO:
        print "R2_IPO ",normal(i)
    for i in R3_IPO:
        print "R3_IPO ",normal(i)
    return

def testNormal(data):
    """
    A function to test if index data is normally distributed;
    if not, the dataset is masked so that further correlation
    analyses cannot be performed.
    """
    count = 0
    copy = data[:]
    while count < len(copy):
        a = normal(copy[count])
        if a <= 0.05:
            copy[count] = np.ma.masked_where(copy[count],copy[count])
            count += 1
        else:
            count += 1
    return copy

def correl(index1,index2):
    """
    Pearson's correlation coefficient [-1,1]
    """
    cc = stats.pearsonr(index1,index2)
    return cc

def correlAll(list1,list2):
    """
    Correlations between Nino 3.4 and TPI data derived from HadISST1 (observations)
    """
    June = correl(list1[0],list2[0])
    July = correl(list1[1],list2[1])
    August = correl(list1[2],list2[2])
    September = correl(list1[3],list2[3])
    October = correl(list1[4],list2[4])
    November = correl(list1[5],list2[5])
    December = correl(list1[6],list2[6])
    January = correl(list1[7],list2[7])
    February = correl(list1[8],list2[8])
    March = correl(list1[9],list2[9])
    April = correl(list1[10],list2[10])
    May = correl(list1[11],list2[11])
    JJA = correl(list1[12],list2[12])
    SON = correl(list1[13],list2[13])
    DJF = correl(list1[14],list2[14])
    MAM = correl(list1[15],list2[15])
    annual = correl(list1[16],list2[16])
    return June, July, August, September, October, November, December, January,\
           February, March, April, May, JJA, SON, DJF, MAM, annual

def scatPlot(data_x_enso,data_y_ipo,title,filename):
    """
    Returns a scatterplot of the indices Nino 3.4 and the TPI.
    """
    axes = plt.gca()
    axes.set_xlim([-3.0,3.0])
    axes.set_ylim([-2.0,2.0])
    plt.scatter(data_x_enso, data_y_ipo)
    plt.xlabel("Nino 3.4")
    plt.ylabel("TPI")
    plt.title(title)
    plt.savefig(filename)
    plt.close()
    return

def corrANOVA(array1,array2,array3,array4):
    """
    A function to test if the means of the output from the four correlation
    datasets (observational, R1, R2, R3) are different.
    n = 12; N = 48.  DFbtw = 3, DFwthin = 44
    H0: all means are equal to each other.
    H1: not all means are equal.

    Parameters:
    -----------
    Output: the f_value (not the f table (critical f-value) statistic)
    """
    f_val,p_val = stats.f_oneway(array1,array2,array3,array4)
    return f_val, p_val

hadISST_ENSO = [enso_Jun_Had,enso_Jul_Had,enso_Aug_Had,enso_Sep_Had,\
                enso_Oct_Had,enso_Nov_Had,enso_Dec_Had,enso_Jan_Had,\
                enso_Feb_Had,enso_Mar_Had,enso_Apr_Had,enso_May_Had,\
                enso_JJA_Had, enso_SON_Had, enso_DJF_Had,enso_MAM_Had,\
                enso_Annual_Had]
R1_ENSO = [enso_Jun_R1,enso_Jul_R1,enso_Aug_R1,enso_Sep_R1,\
           enso_Oct_R1,enso_Nov_R1,enso_Dec_R1,enso_Jan_R1,\
           enso_Feb_R1,enso_Mar_R1,enso_Apr_R1,enso_May_R1,\
           enso_JJA_R1, enso_SON_R1,enso_DJF_R1,enso_MAM_R1,\
           enso_Annual_R1]
R2_ENSO = [enso_Jun_R2,enso_Jul_R2,enso_Aug_R2,enso_Sep_R2,\
           enso_Oct_R2,enso_Nov_R2,enso_Dec_R2,enso_Jan_R2,\
           enso_Feb_R2,enso_Mar_R2,enso_Apr_R2,enso_May_R2,\
           enso_JJA_R2, enso_SON_R2,enso_DJF_R2,enso_MAM_R2,\
           enso_Annual_R2]
R3_ENSO = [enso_Jun_R3,enso_Jul_R3,enso_Aug_R3,enso_Sep_R3,\
           enso_Oct_R3,enso_Nov_R3,enso_Dec_R3,enso_Jan_R3,\
           enso_Feb_R3,enso_Mar_R3,enso_Apr_R3,enso_May_R3,\
           enso_JJA_R3, enso_SON_R3,enso_DJF_R3,enso_MAM_R3,\
           enso_Annual_R3]

hadISST_IPO = [IPO_had_Jun,IPO_had_Jul,IPO_had_Aug,IPO_had_Sep,\
               IPO_had_Oct,IPO_had_Nov,IPO_had_Dec,IPO_had_Jan,\
               IPO_had_Feb,IPO_had_Mar,IPO_had_Apr,IPO_had_May,\
               IPO_had_JJA,IPO_had_SON,IPO_had_DJF,IPO_had_MAM,\
               IPO_had_Annual]
R1_IPO = [IPO_R1_Jun,IPO_R1_Jul,IPO_R1_Aug,IPO_R1_Sep,\
          IPO_R1_Oct,IPO_R1_Nov,IPO_R1_Dec,IPO_R1_Jan,\
          IPO_R1_Feb,IPO_R1_Mar,IPO_R1_Apr,IPO_R1_May,\
          IPO_R1_JJA,IPO_R1_SON,IPO_R1_DJF,IPO_R1_MAM,\
          IPO_R1_Annual]
R2_IPO = [IPO_R2_Jun,IPO_R2_Jul,IPO_R2_Aug,IPO_R2_Sep,\
          IPO_R2_Oct,IPO_R2_Nov,IPO_R2_Dec,IPO_R2_Jan,\
          IPO_R2_Feb,IPO_R2_Mar,IPO_R2_Apr,IPO_R2_May,\
          IPO_R2_JJA,IPO_R2_SON,IPO_R2_DJF,IPO_R2_MAM,\
          IPO_R2_Annual]
R3_IPO = [IPO_R3_Jun,IPO_R3_Jul,IPO_R3_Aug,IPO_R3_Sep,\
          IPO_R3_Oct,IPO_R3_Nov,IPO_R3_Dec,IPO_R3_Jan,\
          IPO_R3_Feb,IPO_R3_Mar,IPO_R3_Apr,IPO_R3_May,\
          IPO_R3_JJA,IPO_R3_SON,IPO_R3_DJF,IPO_R3_MAM,\
          IPO_R3_Annual]

"""
Test to see if indices are normally distributed.
"""
#printNormal()

hadISST_ENSO_norm = testNormal(hadISST_ENSO)
R1_ENSO_norm = testNormal(R1_ENSO)
R2_ENSO_norm = testNormal(R2_ENSO)
R3_ENSO_norm = testNormal(R3_ENSO)
hadISST_IPO_norm = testNormal(hadISST_IPO)
R1_IPO_norm = testNormal(R3_IPO)
R2_IPO_norm = testNormal(R2_IPO)
R3_IPO_norm = testNormal(R3_IPO)

"""
Correllations
"""

#Correlations - HadISST1
corr = correlAll(hadISST_ENSO_norm,hadISST_IPO_norm)
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
corr = correlAll(R1_ENSO_norm,R1_IPO_norm)
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
corr = correlAll(R2_ENSO_norm,R2_IPO_norm)
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
corr = correlAll(R3_ENSO_norm,R3_IPO_norm)
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

##################


####################
"""
test = corrANOVA(HadISST,accessR1,accessR2,accessR3)
#test1 = pairwise_tukeyhsd(HadISST,accessR1,accessR2,accessR3)
#test2 = normal(Nino34,0)

#test3 = linePlot(Nino34_annual[0],TPI_annual[0])


#Test to see if this function matches Excel's output:
hey = np.array([Nino34[0],TPI[1]])
hey1 = np.corrcoef(hey)
hey2 = stats.pearsonr(Nino34[0],TPI[1])
"""
