"""
A file to create scatterplots showing the relationship between
ENSO and the IPO.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 11 October 2015.
"""

from ENSO_IPO_corr import hadISST_ENSO,R1_ENSO,R2_ENSO,\
     R3_ENSO,hadISST_IPO,R1_IPO,R2_IPO,R3_IPO,scatPlot
from plot import multiScatter
from maps_sub import saveFig
from cwd import *
cwdInFunction()


def scatter():
    """
    Generate scatterplots of Nino3.4/TPI relationship
    """
    scatPlot(hadISST_ENSO[16],hadISST_IPO[16],"Correlation between ENSO and IPO indices, 1900-2005 (Correlation between ENSO and IPO indices, 1900-2005 (HadISST1))","my_coding_routines/images/scatter/Annual/2")
    scatPlot(hadISST_ENSO[0],hadISST_IPO[0],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Jun/2")
    scatPlot(hadISST_ENSO[1],hadISST_IPO[1],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Jul/2")
    scatPlot(hadISST_ENSO[2],hadISST_IPO[2],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Aug/2")
    scatPlot(hadISST_ENSO[3],hadISST_IPO[3],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Sep/2")
    scatPlot(hadISST_ENSO[4],hadISST_IPO[4],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Oct/2")
    scatPlot(hadISST_ENSO[5],hadISST_IPO[5],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Nov/2")
    scatPlot(hadISST_ENSO[6],hadISST_IPO[6],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Dec/2")
    scatPlot(hadISST_ENSO[7],hadISST_IPO[7],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Jan/2")
    scatPlot(hadISST_ENSO[8],hadISST_IPO[8],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Feb/2")
    scatPlot(hadISST_ENSO[9],hadISST_IPO[9],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Mar/2")
    scatPlot(hadISST_ENSO[10],hadISST_IPO[10],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/Apr/2")
    scatPlot(hadISST_ENSO[11],hadISST_IPO[11],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/May/2")
    scatPlot(hadISST_ENSO[12],hadISST_IPO[12],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/JJA/2")
    scatPlot(hadISST_ENSO[13],hadISST_IPO[13],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/SON/2")
    scatPlot(hadISST_ENSO[14],hadISST_IPO[13],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/DJF/2")
    scatPlot(hadISST_ENSO[15],hadISST_IPO[15],"Correlation between ENSO and IPO indices, 1900-2005 (HadISST1)","my_coding_routines/images/scatter/MAM/2")

    scatPlot(R1_ENSO[16],R1_IPO[16],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Annual/3")
    scatPlot(R1_ENSO[0],R1_IPO[0],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Jun/3")
    scatPlot(R1_ENSO[1],R1_IPO[1],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Jul/3")
    scatPlot(R1_ENSO[2],R1_IPO[2],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Aug/3")
    scatPlot(R1_ENSO[3],R1_IPO[3],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Sep/3")
    scatPlot(R1_ENSO[4],R1_IPO[4],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Oct/3")
    scatPlot(R1_ENSO[5],R1_IPO[5],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Nov/3")
    scatPlot(R1_ENSO[6],R1_IPO[6],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Dec/3")
    scatPlot(R1_ENSO[7],R1_IPO[7],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Jan/3")
    scatPlot(R1_ENSO[8],R1_IPO[8],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Feb/3")
    scatPlot(R1_ENSO[9],R1_IPO[9],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Mar/3")
    scatPlot(R1_ENSO[10],R1_IPO[10],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/Apr/3")
    scatPlot(R1_ENSO[11],R1_IPO[11],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/May/3")
    scatPlot(R1_ENSO[12],R1_IPO[12],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/JJA/3")
    scatPlot(R1_ENSO[13],R1_IPO[13],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/SON/3")
    scatPlot(R1_ENSO[14],R1_IPO[14],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/DJF/3")
    scatPlot(R1_ENSO[15],R1_IPO[15],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R1)","my_coding_routines/images/scatter/MAM/3")

    scatPlot(R2_ENSO[16],R2_IPO[16],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Annual/4")
    scatPlot(R2_ENSO[0],R2_IPO[0],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Jun/4")
    scatPlot(R2_ENSO[1],R2_IPO[1],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Jul/4")
    scatPlot(R2_ENSO[2],R2_IPO[2],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Aug/4")
    scatPlot(R2_ENSO[3],R2_IPO[3],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Sep/4")
    scatPlot(R2_ENSO[4],R2_IPO[4],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Oct/4")
    scatPlot(R2_ENSO[5],R2_IPO[5],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Nov/4")
    scatPlot(R2_ENSO[6],R2_IPO[6],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Dec/4")
    scatPlot(R2_ENSO[7],R2_IPO[7],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Jan/4")
    scatPlot(R2_ENSO[8],R2_IPO[8],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Feb/4")
    scatPlot(R2_ENSO[9],R2_IPO[9],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Mar/4")
    scatPlot(R2_ENSO[10],R2_IPO[10],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/Apr/4")
    scatPlot(R2_ENSO[11],R2_IPO[11],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/May/4")
    scatPlot(R2_ENSO[12],R2_IPO[12],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/JJA/4")
    scatPlot(R2_ENSO[13],R2_IPO[13],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/SON/4")
    scatPlot(R2_ENSO[14],R2_IPO[14],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/DJF/4")
    scatPlot(R2_ENSO[15],R2_IPO[15],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R2)","my_coding_routines/images/scatter/MAM/4")
    
    scatPlot(R3_ENSO[16],R3_IPO[16],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Annual/1")
    scatPlot(R3_ENSO[0],R3_IPO[0],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Jun/1")
    scatPlot(R3_ENSO[1],R3_IPO[1],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Jul/1")
    scatPlot(R3_ENSO[2],R3_IPO[2],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Aug/1")
    scatPlot(R3_ENSO[3],R3_IPO[3],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Sep/1")
    scatPlot(R3_ENSO[4],R3_IPO[4],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Oct/1")
    scatPlot(R3_ENSO[5],R3_IPO[5],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Nov/1")
    scatPlot(R3_ENSO[6],R3_IPO[6],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Dec/1")
    scatPlot(R3_ENSO[7],R3_IPO[7],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Jan/1")
    scatPlot(R3_ENSO[8],R3_IPO[8],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Feb/1")
    scatPlot(R3_ENSO[9],R3_IPO[9],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Mar/1")
    scatPlot(R3_ENSO[10],R3_IPO[10],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/Apr/1")
    scatPlot(R3_ENSO[11],R3_IPO[11],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/May/1")
    scatPlot(R3_ENSO[12],R3_IPO[12],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/JJA/1")
    scatPlot(R3_ENSO[13],R3_IPO[13],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/SON/1")
    scatPlot(R3_ENSO[14],R3_IPO[14],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/DJF/1")
    scatPlot(R3_ENSO[15],R3_IPO[15],"Correlation between ENSO and IPO indices, 1900-2005 (ACCESS1.3 R3)","my_coding_routines/images/scatter/MAM/1")
    return

scatter()
