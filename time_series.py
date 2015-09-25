"""
A file to compute time-series plots of ENSO and IPO indicies.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 25 September 2015.
"""

import netCDF4 as n
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pylab
from plot import multiGeneral
from maps_sub import saveFig
from cwd import cwdInFunction
cwdInFunction()

from ENSO_IPO_corr import hadISST_ENSO, R1_ENSO, R2_ENSO, R3_ENSO, hadISST_IPO,\
     R1_IPO, R2_IPO, R3_IPO

def linePlot(ENSO,IPO,filename):
    """
    A function to plot ENSO and IPO index data as a time-series.
    """
    list_x = range(1900,2005)
    x = np.asarray(list_x)

    plt.plot(x,ENSO)
    plt.plot(x,IPO)
    plt.legend(['Nino 3.4','TPI'], loc='upper left')
    plt.xlim(1900,2005)
    plt.xlabel('Years')
    plt.ylabel('Index values')
    savefig(filename)
    return

def generateTimeSeries():
    #HadISST
    linePlot(hadISST_ENSO[16],hadISST_IPO[16],"my_coding_routines/images/time_series/Annual/Had.png")
    linePlot(hadISST_ENSO[0],hadISST_IPO[0],"my_coding_routines/images/time_series/Jun/Had.png")
    linePlot(hadISST_ENSO[1],hadISST_IPO[1],"my_coding_routines/images/time_series/Jul/Had.png")
    linePlot(hadISST_ENSO[2],hadISST_IPO[2],"my_coding_routines/images/time_series/Aug/Had.png")
    linePlot(hadISST_ENSO[3],hadISST_IPO[3],"my_coding_routines/images/time_series/Sep/Had.png")
    linePlot(hadISST_ENSO[4],hadISST_IPO[4],"my_coding_routines/images/time_series/Oct/Had.png")
    linePlot(hadISST_ENSO[5],hadISST_IPO[5],"my_coding_routines/images/time_series/Nov/Had.png")
    linePlot(hadISST_ENSO[6],hadISST_IPO[6],"my_coding_routines/images/time_series/Dec/Had.png")
    linePlot(hadISST_ENSO[7],hadISST_IPO[7],"my_coding_routines/images/time_series/Jan/Had.png")
    linePlot(hadISST_ENSO[8],hadISST_IPO[8],"my_coding_routines/images/time_series/Feb/Had.png")
    linePlot(hadISST_ENSO[9],hadISST_IPO[9],"my_coding_routines/images/time_series/Mar/Had.png")
    linePlot(hadISST_ENSO[10],hadISST_IPO[10],"my_coding_routines/images/time_series/Apr/Had.png")
    linePlot(hadISST_ENSO[11],hadISST_IPO[11],"my_coding_routines/images/time_series/May/Had.png")
    linePlot(hadISST_ENSO[12],hadISST_IPO[12],"my_coding_routines/images/time_series/JJA/Had.png")
    linePlot(hadISST_ENSO[13],hadISST_IPO[13],"my_coding_routines/images/time_series/SON/Had.png")
    linePlot(hadISST_ENSO[14],hadISST_IPO[14],"my_coding_routines/images/time_series/DJF/Had.png")
    linePlot(hadISST_ENSO[15],hadISST_IPO[15],"my_coding_routines/images/time_series/MAM/Had.png")

    #ACCESS R1
    linePlot(R1_ENSO[16],R1_IPO[16],"my_coding_routines/images/time_series/Annual/R1.png")
    linePlot(R1_ENSO[0],R1_IPO[0],"my_coding_routines/images/time_series/Jun/R1.png")
    linePlot(R1_ENSO[1],R1_IPO[1],"my_coding_routines/images/time_series/Jul/R1.png")
    linePlot(R1_ENSO[2],R1_IPO[2],"my_coding_routines/images/time_series/Aug/R1.png")
    linePlot(R1_ENSO[3],R1_IPO[3],"my_coding_routines/images/time_series/Sep/R1.png")
    linePlot(R1_ENSO[4],R1_IPO[4],"my_coding_routines/images/time_series/Oct/R1.png")
    linePlot(R1_ENSO[5],R1_IPO[5],"my_coding_routines/images/time_series/Nov/R1.png")
    linePlot(R1_ENSO[6],R1_IPO[6],"my_coding_routines/images/time_series/Dec/R1.png")
    linePlot(R1_ENSO[7],R1_IPO[7],"my_coding_routines/images/time_series/Jan/R1.png")
    linePlot(R1_ENSO[8],R1_IPO[8],"my_coding_routines/images/time_series/Feb/R1.png")
    linePlot(R1_ENSO[9],R1_IPO[9],"my_coding_routines/images/time_series/Mar/R1.png")
    linePlot(R1_ENSO[10],R1_IPO[10],"my_coding_routines/images/time_series/Apr/R1.png")
    linePlot(R1_ENSO[11],R1_IPO[11],"my_coding_routines/images/time_series/May/R1.png")
    linePlot(R1_ENSO[12],R1_IPO[12],"my_coding_routines/images/time_series/JJA/R1.png")
    linePlot(R1_ENSO[13],R1_IPO[13],"my_coding_routines/images/time_series/SON/R1.png")
    linePlot(R1_ENSO[14],R1_IPO[14],"my_coding_routines/images/time_series/DJF/R1.png")
    linePlot(R1_ENSO[15],R1_IPO[15],"my_coding_routines/images/time_series/MAM/R1.png")

    #ACCESS R2
    linePlot(R2_ENSO[16],R2_IPO[16],"my_coding_routines/images/time_series/Annual/R2.png")
    linePlot(R2_ENSO[0],R2_IPO[0],"my_coding_routines/images/time_series/Jun/R2.png")
    linePlot(R2_ENSO[1],R2_IPO[1],"my_coding_routines/images/time_series/Jul/R2.png")
    linePlot(R2_ENSO[2],R2_IPO[2],"my_coding_routines/images/time_series/Aug/R2.png")
    linePlot(R2_ENSO[3],R2_IPO[3],"my_coding_routines/images/time_series/Sep/R2.png")
    linePlot(R2_ENSO[4],R2_IPO[4],"my_coding_routines/images/time_series/Oct/R2.png")
    linePlot(R2_ENSO[5],R2_IPO[5],"my_coding_routines/images/time_series/Nov/R2.png")
    linePlot(R2_ENSO[6],R2_IPO[6],"my_coding_routines/images/time_series/Dec/R2.png")
    linePlot(R2_ENSO[7],R2_IPO[7],"my_coding_routines/images/time_series/Jan/R2.png")
    linePlot(R2_ENSO[8],R2_IPO[8],"my_coding_routines/images/time_series/Feb/R2.png")
    linePlot(R2_ENSO[9],R2_IPO[9],"my_coding_routines/images/time_series/Mar/R2.png")
    linePlot(R2_ENSO[10],R2_IPO[10],"my_coding_routines/images/time_series/Apr/R2.png")
    linePlot(R2_ENSO[11],R2_IPO[11],"my_coding_routines/images/time_series/May/R2.png")
    linePlot(R2_ENSO[12],R2_IPO[12],"my_coding_routines/images/time_series/JJA/R2.png")
    linePlot(R2_ENSO[13],R2_IPO[13],"my_coding_routines/images/time_series/SON/R2.png")
    linePlot(R2_ENSO[14],R2_IPO[14],"my_coding_routines/images/time_series/DJF/R2.png")
    linePlot(R2_ENSO[15],R2_IPO[15],"my_coding_routines/images/time_series/MAM/R2.png")

    #ACCESS R3
    linePlot(R3_ENSO[16],R3_IPO[16],"my_coding_routines/images/time_series/Annual/R3.png")
    linePlot(R3_ENSO[0],R3_IPO[0],"my_coding_routines/images/time_series/Jun/R3.png")
    linePlot(R3_ENSO[1],R3_IPO[1],"my_coding_routines/images/time_series/Jul/R3.png")
    linePlot(R3_ENSO[2],R3_IPO[2],"my_coding_routines/images/time_series/Aug/R3.png")
    linePlot(R3_ENSO[3],R3_IPO[3],"my_coding_routines/images/time_series/Sep/R3.png")
    linePlot(R3_ENSO[4],R3_IPO[4],"my_coding_routines/images/time_series/Oct/R3.png")
    linePlot(R3_ENSO[5],R3_IPO[5],"my_coding_routines/images/time_series/Nov/R3.png")
    linePlot(R3_ENSO[6],R3_IPO[6],"my_coding_routines/images/time_series/Dec/R3.png")
    linePlot(R3_ENSO[7],R3_IPO[7],"my_coding_routines/images/time_series/Jan/R3.png")
    linePlot(R3_ENSO[8],R3_IPO[8],"my_coding_routines/images/time_series/Feb/R3.png")
    linePlot(R3_ENSO[9],R3_IPO[9],"my_coding_routines/images/time_series/Mar/R3.png")
    linePlot(R3_ENSO[10],R3_IPO[10],"my_coding_routines/images/time_series/Apr/R3.png")
    linePlot(R3_ENSO[11],R3_IPO[11],"my_coding_routines/images/time_series/May/R3.png")
    linePlot(R3_ENSO[12],R3_IPO[12],"my_coding_routines/images/time_series/JJA/R3.png")
    linePlot(R3_ENSO[13],R3_IPO[13],"my_coding_routines/images/time_series/SON/R3.png")
    linePlot(R3_ENSO[14],R3_IPO[14],"my_coding_routines/images/time_series/DJF/R3.png")
    linePlot(R3_ENSO[15],R3_IPO[15],"my_coding_routines/images/time_series/MAM/R3.png")
    return

def plotTimeSeries():
    Annual = multiGeneral("my_coding_routines/images/time_series/Annual.*png",4,1,"ENSO and IPO (1900-2005): Annual")
    Jun = multiGeneral("my_coding_routines/images/time_series/Jun.*png",4,1,"ENSO and IPO (1900-2005): June")
    Jul = multiGeneral("my_coding_routines/images/time_series/Jul.*png",4,1,"ENSO and IPO (1900-2005): July")
    Aug = multiGeneral("my_coding_routines/images/time_series/Aug.*png",4,1,"ENSO and IPO (1900-2005): August")
    Sep = multiGeneral("my_coding_routines/images/time_series/Sep.*png",4,1,"ENSO and IPO (1900-2005): September")
    Oct = multiGeneral("my_coding_routines/images/time_series/Oct.*png",4,1,"ENSO and IPO (1900-2005): October")
    Nov = multiGeneral("my_coding_routines/images/time_series/Nov.*png",4,1,"ENSO and IPO (1900-2005): November")
    Dec = multiGeneral("my_coding_routines/images/time_series/Dec.*png",4,1,"ENSO and IPO (1900-2005): December")
    Jan = multiGeneral("my_coding_routines/images/time_series/Jan.*png",4,1,"ENSO and IPO (1900-2005): January")
    Feb = multiGeneral("my_coding_routines/images/time_series/Feb.*png",4,1,"ENSO and IPO (1900-2005): February")
    Mar = multiGeneral("my_coding_routines/images/time_series/Mar.*png",4,1,"ENSO and IPO (1900-2005): March")
    Apr = multiGeneral("my_coding_routines/images/time_series/Apr.*png",4,1,"ENSO and IPO (1900-2005): April")
    May = multiGeneral("my_coding_routines/images/time_series/May.*png",4,1,"ENSO and IPO (1900-2005): May")
    JJA = multiGeneral("my_coding_routines/images/time_series/JJA.*png",4,1,"ENSO and IPO (1900-2005): JJA")
    SON = multiGeneral("my_coding_routines/images/time_series/SON.*png",4,1,"ENSO and IPO (1900-2005): SON")
    DJF = multiGeneral("my_coding_routines/images/time_series/DJF.*png",4,1,"ENSO and IPO (1900-2005): DJF")
    MAM = multiGeneral("my_coding_routines/images/time_series/MAM.*png",4,1,"ENSO and IPO (1900-2005): MAM")

    saveFig(Annual,"Annual","time_series/")
    saveFig(Jun,"June","time_series/")
    saveFig(Jul,"July","time_series/")
    saveFig(Aug,"August","time_series/")
    saveFig(Sep,"September","time_series/")
    saveFig(Oct,"October","time_series/")
    saveFig(Nov,"November","time_series/")
    saveFig(Dec,"December","time_series/")
    saveFig(Jan,"January","time_series/")
    saveFig(Feb,"February","time_series/")
    saveFig(Mar,"March","time_series/")
    saveFig(Apr,"April","time_series/")
    saveFig(May,"May","time_series/")
    saveFig(JJA,"JJA","time_series/")
    saveFig(SON,"SON","time_series/")
    saveFig(DJF,"DJF","time_series/")
    saveFig(MAM,"MAM","time_series/")
    return

generateTimeSeries()
plotTimeSeries()
