"""
A file to compute time-series plots of ENSO and IPO indicies.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 October 2015.
"""

import netCDF4 as n
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pylab
from plot import multiGeneral
from maps_sub import saveFig
from cross_corr_routine import flatten
from cwd import cwdInFunction
cwdInFunction()

from ENSO_IPO_corr import hadISST_ENSO, R1_ENSO, R2_ENSO, R3_ENSO, hadISST_IPO,\
     R1_IPO, R2_IPO, R3_IPO
from awap_prepare import awap_Annual,awap_June,awap_July,awap_August,\
     awap_September,awap_October,awap_November,awap_December,\
     awap_January,awap_February,awap_March,awap_April,awap_May,\
     awap_JJA,awap_SON,awap_DJF,awap_MAM
from access_trimmed import trim_Annual,trim_June, trim_July,\
     trim_August,trim_September,trim_October,trim_November,\
     trim_December,trim_January,trim_February,trim_March,\
     trim_April,trim_May,trim_JJA,trim_SON,trim_DJF,trim_MAM

def linePlot(ENSO,IPO,rainfall,title,filename):
    """
    A function to plot ENSO and IPO index data as a time-series.
    """
    list_x = range(1900,2005)
    x = np.asarray(list_x)

    plt.plot(x,ENSO)
    plt.plot(x,IPO)
    plt.plot(x,rainfall,'r--')
    plt.legend(['Nino 3.4','TPI','Mean rainfall (mm/day)'], loc='upper left')
    plt.xlim(1900,2005)
    plt.xlabel('Years')
    plt.ylabel('Index values/mean rainfall (mm/day)')
    plt.title(title)
    plt.savefig(filename)
    plt.close
    return

def generateTimeSeriesAWAP():
    #HadISST
    linePlot(hadISST_ENSO[16],hadISST_IPO[16],awap_Annual1,"AWAP annual time series","my_coding_routines/images/time_series/Annual/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[0],hadISST_IPO[0],awap_June1,"AWAP June time series","my_coding_routines/images/time_series/Jun/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[1],hadISST_IPO[1],awap_July1,"AWAP July time series","my_coding_routines/images/time_series/Jul/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[2],hadISST_IPO[2],awap_August1,"AWAP August time series","my_coding_routines/images/time_series/Aug/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[3],hadISST_IPO[3],awap_September1,"AWAP September time series","my_coding_routines/images/time_series/Sep/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[4],hadISST_IPO[4],awap_October1,"AWAP October time series","my_coding_routines/images/time_series/Oct/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[5],hadISST_IPO[5],awap_November1,"AWAP November time series","my_coding_routines/images/time_series/Nov/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[6],hadISST_IPO[6],awap_December1,"AWAP December time series","my_coding_routines/images/time_series/Dec/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[7],hadISST_IPO[7],awap_January1,"AWAP January time series","my_coding_routines/images/time_series/Jan/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[8],hadISST_IPO[8],awap_February1,"AWAP February time series","my_coding_routines/images/time_series/Feb/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[9],hadISST_IPO[9],awap_March1,"AWAP March time series","my_coding_routines/images/time_series/Mar/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[10],hadISST_IPO[10],awap_April1,"AWAP April time series","my_coding_routines/images/time_series/Apr/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[11],hadISST_IPO[11],awap_May1,"AWAP May time series","my_coding_routines/images/time_series/May/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[12],hadISST_IPO[12],awap_JJA1,"AWAP JJA time series","my_coding_routines/images/time_series/JJA/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[13],hadISST_IPO[13],awap_SON1,"AWAP SON time series","my_coding_routines/images/time_series/SON/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[14],hadISST_IPO[14],awap_DJF1,"AWAP DJF time series","my_coding_routines/images/time_series/DJF/Had.png")
    plt.close()
    linePlot(hadISST_ENSO[15],hadISST_IPO[15],awap_MAM1,"AWAP MAM time series","my_coding_routines/images/time_series/MAM/Had.png")
    plt.close()
    return

def generateTimeSeriesACCESS(ENSO,IPO,roundNum):
    #ACCESS R1
    linePlot(ENSO[16],IPO[16],trim_Annual1,"ACCESS "+roundNum+" annual time series","my_coding_routines/images/time_series/Annual/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[0],IPO[0],trim_June1,"ACCESS "+roundNum+" June time series","my_coding_routines/images/time_series/Jun/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[1],IPO[1],trim_July1,"ACCESS "+roundNum+" July time series","my_coding_routines/images/time_series/Jul/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[2],IPO[2],trim_August1,"ACCESS "+roundNum+" August time series","my_coding_routines/images/time_series/Aug/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[3],IPO[3],trim_September1,"ACCESS "+roundNum+" September time series","my_coding_routines/images/time_series/Sep/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[4],IPO[4],trim_October1,"ACCESS "+roundNum+" October time series","my_coding_routines/images/time_series/Oct/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[5],IPO[5],trim_November1,"ACCESS "+roundNum+" November time series","my_coding_routines/images/time_series/Nov/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[6],IPO[6],trim_December1,"ACCESS "+roundNum+" December time series","my_coding_routines/images/time_series/Dec/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[7],IPO[7],trim_January1,"ACCESS "+roundNum+" January time series","my_coding_routines/images/time_series/Jan/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[8],IPO[8],trim_February1,"ACCESS "+roundNum+" February time series","my_coding_routines/images/time_series/Feb/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[9],IPO[9],trim_March1,"ACCESS "+roundNum+" March time series","my_coding_routines/images/time_series/Mar/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[10],IPO[10],trim_April1,"ACCESS "+roundNum+" April time series","my_coding_routines/images/time_series/Apr/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[11],IPO[11],trim_May1,"ACCESS "+roundNum+" May time series","my_coding_routines/images/time_series/May/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[12],IPO[12],trim_JJA1,"ACCESS "+roundNum+" JJA time series","my_coding_routines/images/time_series/JJA/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[13],IPO[13],trim_SON1,"ACCESS "+roundNum+" SON time series","my_coding_routines/images/time_series/SON/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[14],IPO[14],trim_DJF1,"ACCESS "+roundNum+" DJF time series","my_coding_routines/images/time_series/DJF/"+roundNum+".png")
    plt.close()
    linePlot(ENSO[15],IPO[15],trim_MAM1,"ACCESS "+roundNum+" MAM time series","my_coding_routines/images/time_series/MAM/"+roundNum+".png")
    plt.close()
    return

awap_Annual1 = flatten(awap_Annual)
awap_June1 = flatten(awap_June)
awap_July1 = flatten(awap_July)
awap_August1 = flatten(awap_August)
awap_September1 = flatten(awap_September)
awap_October1 = flatten(awap_October)
awap_November1 = flatten(awap_November)
awap_December1 = flatten(awap_December)
awap_January1 = flatten(awap_January)
awap_February1 = flatten(awap_February)
awap_March1 = flatten(awap_March)
awap_April1 = flatten(awap_April)
awap_May1 = flatten(awap_May)
awap_JJA1 = flatten(awap_JJA)
awap_SON1 = flatten(awap_SON)
awap_DJF1 = flatten(awap_DJF)
awap_MAM1 = flatten(awap_MAM)

trim_Annual1 = flatten(trim_Annual)
trim_June1 = flatten(trim_June)
trim_July1 = flatten(trim_July)
trim_August1 = flatten(trim_August)
trim_September1 = flatten(trim_September)
trim_October1 = flatten(trim_October)
trim_November1 = flatten(trim_November)
trim_December1 = flatten(trim_December)
trim_January1 = flatten(trim_January)
trim_February1 = flatten(trim_February)
trim_March1 = flatten(trim_March)
trim_April1 = flatten(trim_April)
trim_May1 = flatten(trim_May)
trim_JJA1 = flatten(trim_JJA)
trim_SON1 = flatten(trim_SON)
trim_DJF1 = flatten(trim_DJF)
trim_MAM1 = flatten(trim_MAM)

generateTimeSeriesAWAP()
generateTimeSeriesACCESS(ENSO=R1_ENSO,IPO=R1_IPO,roundNum='R1')
generateTimeSeriesACCESS(ENSO=R2_ENSO,IPO=R2_IPO,roundNum='R2')
generateTimeSeriesACCESS(ENSO=R3_ENSO,IPO=R3_IPO,roundNum='R3')
