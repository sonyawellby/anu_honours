"""
A file to create scatterplots showing the relationship between
ENSO and the IPO.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 25 September 2015.
"""

from ENSO_IPO_corr import *
from plot import multiScatter


def scatter():
    """
    Generate scatterplots of Nino3.4/TPI relationship
    """
    scatPlot(hadISST_ENSO_norm[16],hadISST_IPO_norm[16],"HadISST1","my_coding_routines/images/scatter/Annual/2")
    scatPlot(hadISST_ENSO_norm[0],hadISST_IPO_norm[0],"HadISST1","my_coding_routines/images/scatter/Jun/2")
    scatPlot(hadISST_ENSO_norm[1],hadISST_IPO_norm[1],"HadISST1","my_coding_routines/images/scatter/Jul/2")
    scatPlot(hadISST_ENSO_norm[2],hadISST_IPO_norm[2],"HadISST1","my_coding_routines/images/scatter/Aug/2")
    scatPlot(hadISST_ENSO_norm[3],hadISST_IPO_norm[3],"HadISST1","my_coding_routines/images/scatter/Sep/2")
    scatPlot(hadISST_ENSO_norm[4],hadISST_IPO_norm[4],"HadISST1","my_coding_routines/images/scatter/Oct/2")
    scatPlot(hadISST_ENSO_norm[5],hadISST_IPO_norm[5],"HadISST1","my_coding_routines/images/scatter/Nov/2")
    scatPlot(hadISST_ENSO_norm[6],hadISST_IPO_norm[6],"HadISST1","my_coding_routines/images/scatter/Dec/2")
    scatPlot(hadISST_ENSO_norm[7],hadISST_IPO_norm[7],"HadISST1","my_coding_routines/images/scatter/Jan/2")
    scatPlot(hadISST_ENSO_norm[8],hadISST_IPO_norm[8],"HadISST1","my_coding_routines/images/scatter/Feb/2")
    scatPlot(hadISST_ENSO_norm[9],hadISST_IPO_norm[9],"HadISST1","my_coding_routines/images/scatter/Mar/2")
    scatPlot(hadISST_ENSO_norm[10],hadISST_IPO_norm[10],"HadISST1","my_coding_routines/images/scatter/Apr/2")
    scatPlot(hadISST_ENSO_norm[11],hadISST_IPO_norm[11],"HadISST1","my_coding_routines/images/scatter/May/2")
    scatPlot(hadISST_ENSO_norm[12],hadISST_IPO_norm[12],"HadISST1","my_coding_routines/images/scatter/JJA/2")
    scatPlot(hadISST_ENSO_norm[13],hadISST_IPO_norm[13],"HadISST1","my_coding_routines/images/scatter/SON/2")
    scatPlot(hadISST_ENSO_norm[14],hadISST_IPO_norm[13],"HadISST1","my_coding_routines/images/scatter/DJF/2")
    scatPlot(hadISST_ENSO_norm[15],hadISST_IPO_norm[15],"HadISST1","my_coding_routines/images/scatter/MAM/2")

    scatPlot(R1_ENSO_norm[16],R1_IPO_norm[16],"ACCESS1.3 R1","my_coding_routines/images/scatter/Annual/3")
    scatPlot(R1_ENSO_norm[0],R1_IPO_norm[0],"ACCESS1.3 R1","my_coding_routines/images/scatter/Jun/3")
    scatPlot(R1_ENSO_norm[1],R1_IPO_norm[1],"ACCESS1.3 R1","my_coding_routines/images/scatter/Jul/3")
    scatPlot(R1_ENSO_norm[2],R1_IPO_norm[2],"ACCESS1.3 R1","my_coding_routines/images/scatter/Aug/3")
    scatPlot(R1_ENSO_norm[3],R1_IPO_norm[3],"ACCESS1.3 R1","my_coding_routines/images/scatter/Sep/3")
    scatPlot(R1_ENSO_norm[4],R1_IPO_norm[4],"ACCESS1.3 R1","my_coding_routines/images/scatter/Oct/3")
    scatPlot(R1_ENSO_norm[5],R1_IPO_norm[5],"ACCESS1.3 R1","my_coding_routines/images/scatter/Nov/3")
    scatPlot(R1_ENSO_norm[6],R1_IPO_norm[6],"ACCESS1.3 R1","my_coding_routines/images/scatter/Dec/3")
    scatPlot(R1_ENSO_norm[7],R1_IPO_norm[7],"ACCESS1.3 R1","my_coding_routines/images/scatter/Jan/3")
    scatPlot(R1_ENSO_norm[8],R1_IPO_norm[8],"ACCESS1.3 R1","my_coding_routines/images/scatter/Feb/3")
    scatPlot(R1_ENSO_norm[9],R1_IPO_norm[9],"ACCESS1.3 R1","my_coding_routines/images/scatter/Mar/3")
    scatPlot(R1_ENSO_norm[10],R1_IPO_norm[10],"ACCESS1.3 R1","my_coding_routines/images/scatter/Apr/3")
    scatPlot(R1_ENSO_norm[11],R1_IPO_norm[11],"ACCESS1.3 R1","my_coding_routines/images/scatter/May/3")
    scatPlot(R1_ENSO_norm[12],R1_IPO_norm[12],"ACCESS1.3 R1","my_coding_routines/images/scatter/JJA/3")
    scatPlot(R1_ENSO_norm[13],R1_IPO_norm[13],"ACCESS1.3 R1","my_coding_routines/images/scatter/SON/3")
    scatPlot(R1_ENSO_norm[14],R1_IPO_norm[14],"ACCESS1.3 R1","my_coding_routines/images/scatter/DJF/3")
    scatPlot(R1_ENSO_norm[15],R1_IPO_norm[15],"ACCESS1.3 R1","my_coding_routines/images/scatter/MAM/3")

    scatPlot(R2_ENSO_norm[16],R2_IPO_norm[16],"ACCESS1.3 R2","my_coding_routines/images/scatter/Annual/4")
    scatPlot(R2_ENSO_norm[0],R2_IPO_norm[0],"ACCESS1.3 R2","my_coding_routines/images/scatter/Jun/4")
    scatPlot(R2_ENSO_norm[1],R2_IPO_norm[1],"ACCESS1.3 R2","my_coding_routines/images/scatter/Jul/4")
    scatPlot(R2_ENSO_norm[2],R2_IPO_norm[2],"ACCESS1.3 R2","my_coding_routines/images/scatter/Aug/4")
    scatPlot(R2_ENSO_norm[3],R2_IPO_norm[3],"ACCESS1.3 R2","my_coding_routines/images/scatter/Sep/4")
    scatPlot(R2_ENSO_norm[4],R2_IPO_norm[4],"ACCESS1.3 R2","my_coding_routines/images/scatter/Oct/4")
    scatPlot(R2_ENSO_norm[5],R2_IPO_norm[5],"ACCESS1.3 R2","my_coding_routines/images/scatter/Nov/4")
    scatPlot(R2_ENSO_norm[6],R2_IPO_norm[6],"ACCESS1.3 R2","my_coding_routines/images/scatter/Dec/4")
    scatPlot(R2_ENSO_norm[7],R2_IPO_norm[7],"ACCESS1.3 R2","my_coding_routines/images/scatter/Jan/4")
    scatPlot(R2_ENSO_norm[8],R2_IPO_norm[8],"ACCESS1.3 R2","my_coding_routines/images/scatter/Feb/4")
    scatPlot(R2_ENSO_norm[9],R2_IPO_norm[9],"ACCESS1.3 R2","my_coding_routines/images/scatter/Mar/4")
    scatPlot(R2_ENSO_norm[10],R2_IPO_norm[10],"ACCESS1.3 R2","my_coding_routines/images/scatter/Apr/4")
    scatPlot(R2_ENSO_norm[11],R2_IPO_norm[11],"ACCESS1.3 R2","my_coding_routines/images/scatter/May/4")
    scatPlot(R2_ENSO_norm[12],R2_IPO_norm[12],"ACCESS1.3 R2","my_coding_routines/images/scatter/JJA/4")
    scatPlot(R2_ENSO_norm[13],R2_IPO_norm[13],"ACCESS1.3 R2","my_coding_routines/images/scatter/SON/4")
    scatPlot(R2_ENSO_norm[14],R2_IPO_norm[14],"ACCESS1.3 R2","my_coding_routines/images/scatter/DJF/4")
    scatPlot(R2_ENSO_norm[15],R2_IPO_norm[15],"ACCESS1.3 R2","my_coding_routines/images/scatter/MAM/4")

    scatPlot(R3_ENSO_norm[16],R3_IPO_norm[16],"ACCESS1.3 R3","my_coding_routines/images/scatter/Annual/1")
    scatPlot(R3_ENSO_norm[0],R3_IPO_norm[0],"ACCESS1.3 R3","my_coding_routines/images/scatter/Jun/1")
    scatPlot(R3_ENSO_norm[1],R3_IPO_norm[1],"ACCESS1.3 R3","my_coding_routines/images/scatter/Jul/1")
    scatPlot(R3_ENSO_norm[2],R3_IPO_norm[2],"ACCESS1.3 R3","my_coding_routines/images/scatter/Aug/1")
    scatPlot(R3_ENSO_norm[3],R3_IPO_norm[3],"ACCESS1.3 R3","my_coding_routines/images/scatter/Sep/1")
    scatPlot(R3_ENSO_norm[4],R3_IPO_norm[4],"ACCESS1.3 R3","my_coding_routines/images/scatter/Oct/1")
    scatPlot(R3_ENSO_norm[5],R3_IPO_norm[5],"ACCESS1.3 R3","my_coding_routines/images/scatter/Nov/1")
    scatPlot(R3_ENSO_norm[6],R3_IPO_norm[6],"ACCESS1.3 R3","my_coding_routines/images/scatter/Dec/1")
    scatPlot(R3_ENSO_norm[7],R3_IPO_norm[7],"ACCESS1.3 R3","my_coding_routines/images/scatter/Jan/1")
    scatPlot(R3_ENSO_norm[8],R3_IPO_norm[8],"ACCESS1.3 R3","my_coding_routines/images/scatter/Feb/1")
    scatPlot(R3_ENSO_norm[9],R3_IPO_norm[9],"ACCESS1.3 R3","my_coding_routines/images/scatter/Mar/1")
    scatPlot(R3_ENSO_norm[10],R3_IPO_norm[10],"ACCESS1.3 R3","my_coding_routines/images/scatter/Apr/1")
    scatPlot(R3_ENSO_norm[11],R3_IPO_norm[11],"ACCESS1.3 R3","my_coding_routines/images/scatter/May/1")
    scatPlot(R3_ENSO_norm[12],R3_IPO_norm[12],"ACCESS1.3 R3","my_coding_routines/images/scatter/JJA/1")
    scatPlot(R3_ENSO_norm[13],R3_IPO_norm[13],"ACCESS1.3 R3","my_coding_routines/images/scatter/SON/1")
    scatPlot(R3_ENSO_norm[14],R3_IPO_norm[14],"ACCESS1.3 R3","my_coding_routines/images/scatter/DJF/1")
    scatPlot(R3_ENSO_norm[15],R3_IPO_norm[15],"ACCESS1.3 R3","my_coding_routines/images/scatter/MAM/1")
    return

def plotMultiScatter():
    Annual = multiScatter("my_coding_routines/images/scatter/Annual/*.png",2,2,"Correlation between ENSO and the IPO: Annual")
    Jun = multiScatter("my_coding_routines/images/scatter/Jun/*.png",2,2,"Correlation between ENSO and the IPO: June")
    Jul = multiScatter("my_coding_routines/images/scatter/Jul/*.png",2,2,"Correlation between ENSO and the IPO: July")
    Aug = multiScatter("my_coding_routines/images/scatter/Aug/*.png",2,2,"Correlation between ENSO and the IPO: August")
    Sep = multiScatter("my_coding_routines/images/scatter/Sep/*.png",2,2,"Correlation between ENSO and the IPO: September")
    Oct = multiScatter("my_coding_routines/images/scatter/Oct/*.png",2,2,"Correlation between ENSO and the IPO: October")
    Nov = multiScatter("my_coding_routines/images/scatter/Nov/*.png",2,2,"Correlation between ENSO and the IPO: November")
    Dec = multiScatter("my_coding_routines/images/scatter/Dec/*.png",2,2,"Correlation between ENSO and the IPO: December")
    Jan = multiScatter("my_coding_routines/images/scatter/Jan/*.png",2,2,"Correlation between ENSO and the IPO: January")
    Feb = multiScatter("my_coding_routines/images/scatter/Feb/*.png",2,2,"Correlation between ENSO and the IPO: February")
    Mar = multiScatter("my_coding_routines/images/scatter/Mar/*.png",2,2,"Correlation between ENSO and the IPO: March")
    Apr = multiScatter("my_coding_routines/images/scatter/Apr/*.png",2,2,"Correlation between ENSO and the IPO: April")
    May = multiScatter("my_coding_routines/images/scatter/May/*.png",2,2,"Correlation between ENSO and the IPO: May")
    JJA = multiScatter("my_coding_routines/images/scatter/JJA/*.png",2,2,"Correlation between ENSO and the IPO: JJA")
    SON = multiScatter("my_coding_routines/images/scatter/SON/*.png",2,2,"Correlation between ENSO and the IPO: SON")
    DJF = multiScatter("my_coding_routines/images/scatter/DJF/*.png",2,2,"Correlation between ENSO and the IPO: DJF")
    MAM = multiScatter("my_coding_routines/images/scatter/MAM/*.png",2,2,"Correlation between ENSO and the IPO: MAM")

    saveFig(Annual,"Annual","scatter/")
    saveFig(Jun,"June","scatter/")
    saveFig(Jul,"July","scatter/")
    saveFig(Aug,"August","scatter/")
    saveFig(Sep,"September","scatter/")
    saveFig(Oct,"October","scatter/")
    saveFig(Nov,"November","scatter/")
    saveFig(Dec,"December","scatter/")
    saveFig(Jan,"January","scatter/")
    saveFig(Feb,"February","scatter/")
    saveFig(Mar,"March","scatter/")
    saveFig(Apr,"April","scatter/")
    saveFig(May,"May","scatter/")
    saveFig(JJA,"JJA","scatter/")
    saveFig(SON,"SON","scatter/")
    saveFig(DJF,"DJF","scatter/")
    saveFig(MAM,"MAM","scatter/")
    return

#scatter()
#plotMultiScatter()
