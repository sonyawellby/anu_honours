"""
A script to create rainfall difference maps for ENSO positive and negative
phases, and IPO positive and negative phases.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 12 October 2015.
"""
import numpy as np
import numpy.ma as ma

from composite import *

from awap_prepare import awap_Annual,awap_JJA,awap_SON,\
     awap_DJF,awap_MAM,awap_June,awap_July,awap_August,\
     awap_September,awap_October,awap_November,awap_December,\
     awap_January,awap_February,awap_March,awap_April,awap_May

from access_trimmed import trim_Annual,trim_June, trim_July,\
     trim_August,trim_September,trim_October,trim_November,\
     trim_December,trim_January,trim_February,trim_March,\
     trim_April,trim_May,trim_JJA,trim_SON,trim_DJF,trim_MAM

from ENSO_IPO_corr_strat import ENSO_posHad, ENSO_negHad,\
     IPO_posHad, IPO_negHad,ENSO_posR1, ENSO_negR1,\
     IPO_posR1, IPO_negR1,ENSO_posR2, ENSO_negR2,\
     IPO_posR2, IPO_negR2,ENSO_posR3, ENSO_negR3,\
     IPO_posR3, IPO_negR3

from cwd import cwdInFunction
cwdInFunction()

def difference_maps_AWAP(sd,num):
    diff1 = difference(awap_Annual,ENSO_posHad[0],ENSO_negHad[0])
    plotStratDiff(diff1,awap_Annual,r'AWAP annual rainfall (ENSO positive - negative)'+sd,"difference_maps/Annual/"+num+"/awap")
    diff2 = difference(awap_JJA,ENSO_posHad[1],ENSO_negHad[1])
    plotStratDiff(diff2,awap_JJA,r'AWAP JJA rainfall (ENSO positive - negative)'+sd,"difference_maps/JJA/"+num+"/awap")
    diff3 = difference(awap_SON,ENSO_posHad[2],ENSO_negHad[2])
    plotStratDiff(diff3,awap_SON,r'AWAP SON rainfall (ENSO positive - negative)'+sd,"difference_maps/SON/"+num+"/awap")
    diff4 = difference(awap_DJF,ENSO_posHad[3],ENSO_negHad[3])
    plotStratDiff(diff4,awap_DJF,r'AWAP DJF rainfall (ENSO positive - negative)'+sd,"difference_maps/DJF/"+num+"/awap")
    diff5 = difference(awap_MAM,ENSO_posHad[4],ENSO_negHad[4])
    plotStratDiff(diff5,awap_MAM,r'AWAP MAM rainfall (ENSO positive - negative)'+sd,"difference_maps/MAM/"+num+"/awap")
    diff6 = difference(awap_June,ENSO_posHad[5],ENSO_negHad[5])
    plotStratDiff(diff6,awap_June,r'AWAP June rainfall (ENSO positive - negative)'+sd,"difference_maps/Jun/"+num+"/awap")
    diff7 = difference(awap_July,ENSO_posHad[6],ENSO_negHad[6])
    plotStratDiff(diff7,awap_July,r'AWAP July rainfall (ENSO positive - negative)'+sd,"difference_maps/Jul/"+num+"/awap")
    diff8 = difference(awap_August,ENSO_posHad[7],ENSO_negHad[7])
    plotStratDiff(diff8,awap_August,r'AWAP August rainfall (ENSO positive - negative)'+sd,"difference_maps/Aug/"+num+"/awap")
    diff9 = difference(awap_September,ENSO_posHad[8],ENSO_negHad[8])
    plotStratDiff(diff9,awap_September,r'AWAP September rainfall (ENSO positive - negative)'+sd,"difference_maps/Sep/"+num+"/awap")
    diff10 = difference(awap_October,ENSO_posHad[9],ENSO_negHad[9])
    plotStratDiff(diff10,awap_October,r'AWAP October rainfall (ENSO positive - negative)'+sd,"difference_maps/Oct/"+num+"/awap")
    diff11 = difference(awap_November,ENSO_posHad[10],ENSO_negHad[10])
    plotStratDiff(diff11,awap_November,r'AWAP November rainfall (ENSO positive - negative)'+sd,"difference_maps/Nov/"+num+"/awap")
    diff12 = difference(awap_December,ENSO_posHad[11],ENSO_negHad[11])
    plotStratDiff(diff12,awap_December,r'AWAP December rainfall (ENSO positive - negative)'+sd,"difference_maps/Dec/"+num+"/awap")
    diff13 = difference(awap_January,ENSO_posHad[12],ENSO_negHad[12])
    plotStratDiff(diff13,awap_January,r'AWAP January rainfall (ENSO positive - negative)'+sd,"difference_maps/Jan/"+num+"/awap")
    diff14 = difference(awap_February,ENSO_posHad[13],ENSO_negHad[13])
    plotStratDiff(diff14,awap_February,r'AWAP February rainfall (ENSO positive - negative)'+sd,"difference_maps/Feb/"+num+"/awap")
    diff15 = difference(awap_March,ENSO_posHad[14],ENSO_negHad[14])
    plotStratDiff(diff15,awap_March,r'AWAP March rainfall (ENSO positive - negative)'+sd,"difference_maps/Mar/"+num+"/awap")
    diff16 = difference(awap_April,ENSO_posHad[15],ENSO_negHad[15])
    plotStratDiff(diff16,awap_April,r'AWAP April rainfall (ENSO positive - negative)'+sd,"difference_maps/Apr/"+num+"/awap")
    diff17 = difference(awap_May,ENSO_posHad[16],ENSO_negHad[16])
    plotStratDiff(diff17,awap_Annual,r'AWAP May rainfall (ENSO positive - negative)'+sd,"difference_maps/May/"+num+"/awap")

    dif1 = difference(awap_Annual,IPO_negHad[0],IPO_posHad[0])
    plotStratDiff(dif1,awap_Annual,r'AWAP annual rainfall (IPO negative - positive)'+sd,"difference_maps/Annual/"+num+"/awap")
    dif2 = difference(awap_JJA,IPO_negHad[1],IPO_posHad[1])
    plotStratDiff(dif2,awap_JJA,r'AWAP JJA rainfall (IPO negative - positive)'+sd,"difference_maps/JJA/"+num+"/awap")
    dif3 = difference(awap_SON,IPO_negHad[2],IPO_posHad[2])
    plotStratDiff(dif3,awap_SON,r'AWAP SON rainfall (IPO negative - positive)'+sd,"difference_maps/SON/"+num+"/awap")
    dif4 = difference(awap_DJF,IPO_negHad[3],IPO_posHad[3])
    plotStratDiff(dif4,awap_DJF,r'AWAP DJF rainfall (IPO negative - positive)'+sd,"difference_maps/DJF/"+num+"/awap")
    dif5 = difference(awap_MAM,IPO_negHad[4],IPO_posHad[4])
    plotStratDiff(dif5,awap_MAM,r'AWAP MAM rainfall (IPO negative - positive)'+sd,"difference_maps/MAM/"+num+"/awap")
    dif6 = difference(awap_June,IPO_negHad[5],IPO_posHad[5])
    plotStratDiff(dif6,awap_June,r'AWAP June rainfall (IPO negative - positive)'+sd,"difference_maps/Jun/"+num+"/awap")
    dif7 = difference(awap_July,IPO_negHad[6],IPO_posHad[6])
    plotStratDiff(dif7,awap_July,r'AWAP July rainfall (IPO negative - positive)'+sd,"difference_maps/Jul/"+num+"/awap")
    dif8 = difference(awap_August,IPO_negHad[7],IPO_posHad[7])
    plotStratDiff(dif8,awap_August,r'AWAP August rainfall (IPO negative - positive)'+sd,"difference_maps/Aug/"+num+"/awap")
    dif9 = difference(awap_September,IPO_negHad[8],IPO_posHad[8])
    plotStratDiff(dif9,awap_September,r'AWAP September rainfall (IPO negative - positive)'+sd,"difference_maps/Sep/"+num+"/awap")
    dif10 = difference(awap_October,IPO_negHad[9],IPO_posHad[9])
    plotStratDiff(dif10,awap_October,r'AWAP October rainfall (IPO negative - positive)'+sd,"difference_maps/Oct/"+num+"/awap")
    dif11 = difference(awap_November,IPO_negHad[10],IPO_posHad[10])
    plotStratDiff(dif11,awap_November,r'AWAP November rainfall (IPO negative - positive)'+sd,"difference_maps/Nov/"+num+"/awap")
    dif12 = difference(awap_December,IPO_negHad[11],IPO_posHad[11])
    plotStratDiff(dif12,awap_December,r'AWAP December rainfall (IPO negative - positive)'+sd,"difference_maps/Dec/"+num+"/awap")
    dif13 = difference(awap_January,IPO_negHad[12],IPO_posHad[12])
    plotStratDiff(dif13,awap_January,r'AWAP January rainfall (IPO negative - positive)'+sd,"difference_maps/Jan/"+num+"/awap")
    dif14 = difference(awap_February,IPO_negHad[13],IPO_posHad[13])
    plotStratDiff(dif14,awap_February,r'AWAP February rainfall (IPO negative - positive)'+sd,"difference_maps/Feb/"+num+"/awap")
    dif15 = difference(awap_March,IPO_negHad[14],IPO_posHad[14])
    plotStratDiff(dif15,awap_March,r'AWAP March rainfall (IPO negative - positive)'+sd,"difference_maps/Mar/"+num+"/awap")
    dif16 = difference(awap_April,IPO_negHad[15],IPO_posHad[15])
    plotStratDiff(dif16,awap_April,r'AWAP April rainfall (IPO negative - positive)'+sd,"difference_maps/Apr/"+num+"/awap")
    dif17 = difference(awap_May,IPO_negHad[16],IPO_posHad[16])
    plotStratDiff(dif17,awap_Annual,r'AWAP May rainfall (IPO negative - positive)'+sd,"difference_maps/May/"+num+"/awap")
    return

def difference_maps_ACCESS(sd,num,roundNum):
    diff1 = difference(trim_Annual,ENSO_posHad[0],ENSO_negHad[0])
    plotStratDiff(diff1,trim_Annual,r'ACCESS '+roundNum+'  annual rainfall (ENSO positive - negative)'+sd,"difference_maps/Annual/"+num+"/"+roundNum)
    diff2 = difference(trim_JJA,ENSO_posHad[1],ENSO_negHad[1])
    plotStratDiff(diff2,trim_JJA,r'ACCESS '+roundNum+'  JJA rainfall (ENSO positive - negative)'+sd,"difference_maps/JJA/"+num+"/"+roundNum)
    diff3 = difference(trim_SON,ENSO_posHad[2],ENSO_negHad[2])
    plotStratDiff(diff3,trim_SON,r'ACCESS '+roundNum+'  SON rainfall (ENSO positive - negative)'+sd,"difference_maps/SON/"+num+"/"+roundNum)
    diff4 = difference(trim_DJF,ENSO_posHad[3],ENSO_negHad[3])
    plotStratDiff(diff4,trim_DJF,r'ACCESS '+roundNum+'  DJF rainfall (ENSO positive - negative)'+sd,"difference_maps/DJF/"+num+"/"+roundNum)
    diff5 = difference(trim_MAM,ENSO_posHad[4],ENSO_negHad[4])
    plotStratDiff(diff5,trim_MAM,r'ACCESS '+roundNum+'  MAM rainfall (ENSO positive - negative)'+sd,"difference_maps/MAM/"+num+"/"+roundNum)
    diff6 = difference(trim_June,ENSO_posHad[5],ENSO_negHad[5])
    plotStratDiff(diff6,trim_June,r'ACCESS '+roundNum+'  June rainfall (ENSO positive - negative)'+sd,"difference_maps/Jun/"+num+"/"+roundNum)
    diff7 = difference(trim_July,ENSO_posHad[6],ENSO_negHad[6])
    plotStratDiff(diff7,trim_July,r'ACCESS '+roundNum+'  July rainfall (ENSO positive - negative)'+sd,"difference_maps/Jul/"+num+"/"+roundNum)
    diff8 = difference(trim_August,ENSO_posHad[7],ENSO_negHad[7])
    plotStratDiff(diff8,trim_August,r'ACCESS '+roundNum+'  August rainfall (ENSO positive - negative)'+sd,"difference_maps/Aug/"+num+"/"+roundNum)
    diff9 = difference(trim_September,ENSO_posHad[8],ENSO_negHad[8])
    plotStratDiff(diff9,trim_September,r'ACCESS '+roundNum+'  September rainfall (ENSO positive - negative)'+sd,"difference_maps/Sep/"+num+"/"+roundNum)
    diff10 = difference(trim_October,ENSO_posHad[9],ENSO_negHad[9])
    plotStratDiff(diff10,trim_October,r'ACCESS '+roundNum+'  October rainfall (ENSO positive - negative)'+sd,"difference_maps/Oct/"+num+"/"+roundNum)
    diff11 = difference(trim_November,ENSO_posHad[10],ENSO_negHad[10])
    plotStratDiff(diff11,trim_November,r'ACCESS '+roundNum+'  November rainfall (ENSO positive - negative)'+sd,"difference_maps/Nov/"+num+"/"+roundNum)
    diff12 = difference(trim_December,ENSO_posHad[11],ENSO_negHad[11])
    plotStratDiff(diff12,trim_December,r'ACCESS '+roundNum+'  December rainfall (ENSO positive - negative)'+sd,"difference_maps/Dec/"+num+"/"+roundNum)
    diff13 = difference(trim_January,ENSO_posHad[12],ENSO_negHad[12])
    plotStratDiff(diff13,trim_January,r'ACCESS '+roundNum+'  January rainfall (ENSO positive - negative)'+sd,"difference_maps/Jan/"+num+"/"+roundNum)
    diff14 = difference(trim_February,ENSO_posHad[13],ENSO_negHad[13])
    plotStratDiff(diff14,trim_February,r'ACCESS '+roundNum+'  February rainfall (ENSO positive - negative)'+sd,"difference_maps/Feb/"+num+"/"+roundNum)
    diff15 = difference(trim_March,ENSO_posHad[14],ENSO_negHad[14])
    plotStratDiff(diff15,trim_March,r'ACCESS '+roundNum+'  March rainfall (ENSO positive - negative)'+sd,"difference_maps/Mar/"+num+"/"+roundNum)
    diff16 = difference(trim_April,ENSO_posHad[15],ENSO_negHad[15])
    plotStratDiff(diff16,trim_April,r'ACCESS '+roundNum+'  April rainfall (ENSO positive - negative)'+sd,"difference_maps/Apr/"+num+"/"+roundNum)
    diff17 = difference(trim_May,ENSO_posHad[16],ENSO_negHad[16])
    plotStratDiff(diff17,trim_Annual,r'ACCESS '+roundNum+'  May rainfall (ENSO positive - negative)'+sd,"difference_maps/May/"+num+"/"+roundNum)

    dif1 = difference(trim_Annual,IPO_negHad[0],IPO_posHad[0])
    plotStratDiff(dif1,trim_Annual,r'ACCESS '+roundNum+'  annual rainfall (IPO negative - positive)'+sd,"difference_maps/Annual/"+num+"/"+roundNum)
    dif2 = difference(trim_JJA,IPO_negHad[1],IPO_posHad[1])
    plotStratDiff(dif2,trim_JJA,r'ACCESS '+roundNum+' JJA rainfall (IPO negative - positive)'+sd,"difference_maps/JJA/"+num+"/"+roundNum)
    dif3 = difference(trim_SON,IPO_negHad[2],IPO_posHad[2])
    plotStratDiff(dif3,trim_SON,r'ACCESS '+roundNum+'  SON rainfall (IPO negative - positive)'+sd,"difference_maps/SON/"+num+"/"+roundNum)
    dif4 = difference(trim_DJF,IPO_negHad[3],IPO_posHad[3])
    plotStratDiff(dif4,trim_DJF,r'ACCESS '+roundNum+'  DJF rainfall (IPO negative - positive)'+sd,"difference_maps/DJF/"+num+"/"+roundNum)
    dif5 = difference(trim_MAM,IPO_negHad[4],IPO_posHad[4])
    plotStratDiff(dif5,trim_MAM,r'ACCESS '+roundNum+'  MAM rainfall (IPO negative - positive)'+sd,"difference_maps/MAM/"+num+"/"+roundNum)
    dif6 = difference(trim_June,IPO_negHad[5],IPO_posHad[5])
    plotStratDiff(dif6,trim_June,r'ACCESS '+roundNum+'  June rainfall (IPO negative - positive)'+sd,"difference_maps/Jun/"+num+"/"+roundNum)
    dif7 = difference(trim_July,IPO_negHad[6],IPO_posHad[6])
    plotStratDiff(dif7,trim_July,r'ACCESS '+roundNum+'  July rainfall (IPO negative - positive)'+sd,"difference_maps/Jul/"+num+"/"+roundNum)
    dif8 = difference(trim_August,IPO_negHad[7],IPO_posHad[7])
    plotStratDiff(dif8,trim_August,r'ACCESS '+roundNum+'  August rainfall (IPO negative - positive)'+sd,"difference_maps/Aug/"+num+"/"+roundNum)
    dif9 = difference(trim_September,IPO_negHad[8],IPO_posHad[8])
    plotStratDiff(dif9,trim_September,r'ACCESS '+roundNum+'  September rainfall (IPO negative - positive)'+sd,"difference_maps/Sep/"+num+"/"+roundNum)
    dif10 = difference(trim_October,IPO_negHad[9],IPO_posHad[9])
    plotStratDiff(dif10,trim_October,r'ACCESS '+roundNum+'  October rainfall (IPO negative - positive)'+sd,"difference_maps/Oct/"+num+"/"+roundNum)
    dif11 = difference(trim_November,IPO_negHad[10],IPO_posHad[10])
    plotStratDiff(dif11,trim_November,r'ACCESS '+roundNum+'  November rainfall (IPO negative - positive)'+sd,"difference_maps/Nov/"+num+"/"+roundNum)
    dif12 = difference(trim_December,IPO_negHad[11],IPO_posHad[11])
    plotStratDiff(dif12,trim_December,r'ACCESS '+roundNum+'  December rainfall (IPO negative - positive)'+sd,"difference_maps/Dec/"+num+"/"+roundNum)
    dif13 = difference(trim_January,IPO_negHad[12],IPO_posHad[12])
    plotStratDiff(dif13,trim_January,r'ACCESS '+roundNum+'  January rainfall (IPO negative - positive)'+sd,"difference_maps/Jan/"+num+"/"+roundNum)
    dif14 = difference(trim_February,IPO_negHad[13],IPO_posHad[13])
    plotStratDiff(dif14,trim_February,r'ACCESS '+roundNum+'  February rainfall (IPO negative - positive)'+sd,"difference_maps/Feb/"+num+"/"+roundNum)
    dif15 = difference(trim_March,IPO_negHad[14],IPO_posHad[14])
    plotStratDiff(dif15,trim_March,r'ACCESS '+roundNum+'  March rainfall (IPO negative - positive)'+sd,"difference_maps/Mar/"+num+"/"+roundNum)
    dif16 = difference(trim_April,IPO_negHad[15],IPO_posHad[15])
    plotStratDiff(dif16,trim_April,r'ACCESS '+roundNum+'  April rainfall (IPO negative - positive)'+sd,"difference_maps/Apr/"+num+"/"+roundNum)
    dif17 = difference(trim_May,IPO_negHad[16],IPO_posHad[16])
    plotStratDiff(dif17,trim_Annual,r'ACCESS '+roundNum+'  May rainfall (IPO negative - positive)'+sd,"difference_maps/May/"+num+"/"+roundNum)
    return

sd = '' # ' (2 $\sigma\)'
num = "1_SD"
difference_maps_AWAP(sd=sd,num=num)
difference_maps_ACCESS(sd=sd,num=num,roundNum='R1')
#difference_maps_ACCESS(sd=sd,num=num,roundNum='R2')
#difference_maps_ACCESS(sd=sd,num=num,roundNum='R3')
