"""
A file to compute Pearson's correlation coefficient and
significance for stratified ENSO and IPO indices.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 12 October 2015.
"""
import netCDF4 as n
import numpy as np
from scipy import stats
from ENSO_IPO_corr import correl
from cwd import cwdInFunction
from unpaired_t_test import *

cwdInFunction()

from indices_phase import ENSO_posHad_Jun,ENSO_posHad_Jul, ENSO_posHad_Aug,\
     ENSO_posHad_Sep,ENSO_posHad_Oct,ENSO_posHad_Nov,ENSO_posHad_Dec,\
     ENSO_posHad_Jan,ENSO_posHad_Feb,ENSO_posHad_Mar,ENSO_posHad_Apr,\
     ENSO_posHad_May,ENSO_posHad_JJA,ENSO_posHad_SON,ENSO_posHad_DJF,\
     ENSO_posHad_MAM,ENSO_posHad_annual,\
     ENSO_negHad_Jun,ENSO_negHad_Jul, ENSO_negHad_Aug,\
     ENSO_negHad_Sep,ENSO_negHad_Oct,ENSO_negHad_Nov,ENSO_negHad_Dec,\
     ENSO_negHad_Jan,ENSO_negHad_Feb,ENSO_negHad_Mar,ENSO_negHad_Apr,\
     ENSO_negHad_May,ENSO_negHad_JJA,ENSO_negHad_SON,ENSO_negHad_DJF,\
     ENSO_negHad_MAM,ENSO_negHad_annual,\
     ENSO_neutralHad_Jun,ENSO_neutralHad_Jul, ENSO_neutralHad_Aug,\
     ENSO_neutralHad_Sep,ENSO_neutralHad_Oct,ENSO_neutralHad_Nov,ENSO_neutralHad_Dec,\
     ENSO_neutralHad_Jan,ENSO_neutralHad_Feb,ENSO_neutralHad_Mar,ENSO_neutralHad_Apr,\
     ENSO_neutralHad_May,ENSO_neutralHad_JJA,ENSO_neutralHad_SON,ENSO_neutralHad_DJF,\
     ENSO_neutralHad_MAM,ENSO_neutralHad_annual,\
     IPO_posHad_Jun,IPO_posHad_Jul, IPO_posHad_Aug,\
     IPO_posHad_Sep,IPO_posHad_Oct,IPO_posHad_Nov,IPO_posHad_Dec,\
     IPO_posHad_Jan,IPO_posHad_Feb,IPO_posHad_Mar,IPO_posHad_Apr,\
     IPO_posHad_May,IPO_posHad_JJA,IPO_posHad_SON,IPO_posHad_DJF,\
     IPO_posHad_MAM,IPO_posHad_annual,\
     IPO_negHad_Jun,IPO_negHad_Jul, IPO_negHad_Aug,\
     IPO_negHad_Sep,IPO_negHad_Oct,IPO_negHad_Nov,IPO_negHad_Dec,\
     IPO_negHad_Jan,IPO_negHad_Feb,IPO_negHad_Mar,IPO_negHad_Apr,\
     IPO_negHad_May,IPO_negHad_JJA,IPO_negHad_SON,IPO_negHad_DJF,\
     IPO_negHad_MAM,IPO_negHad_annual,\
     IPO_neutralHad_Jun,IPO_neutralHad_Jul, IPO_neutralHad_Aug,\
     IPO_neutralHad_Sep,IPO_neutralHad_Oct,IPO_neutralHad_Nov,IPO_neutralHad_Dec,\
     IPO_neutralHad_Jan,IPO_neutralHad_Feb,IPO_neutralHad_Mar,IPO_neutralHad_Apr,\
     IPO_neutralHad_May,IPO_neutralHad_JJA,IPO_neutralHad_SON,IPO_neutralHad_DJF,\
     IPO_neutralHad_MAM,IPO_neutralHad_annual,\
     ENSO_posR1_Jun,ENSO_posR1_Jul, ENSO_posR1_Aug,\
     ENSO_posR1_Sep,ENSO_posR1_Oct,ENSO_posR1_Nov,ENSO_posR1_Dec,\
     ENSO_posR1_Jan,ENSO_posR1_Feb,ENSO_posR1_Mar,ENSO_posR1_Apr,\
     ENSO_posR1_May,ENSO_posR1_JJA,ENSO_posR1_SON,ENSO_posR1_DJF,\
     ENSO_posR1_MAM,ENSO_posR1_annual,\
     ENSO_negR1_Jun,ENSO_negR1_Jul, ENSO_negR1_Aug,\
     ENSO_negR1_Sep,ENSO_negR1_Oct,ENSO_negR1_Nov,ENSO_negR1_Dec,\
     ENSO_negR1_Jan,ENSO_negR1_Feb,ENSO_negR1_Mar,ENSO_negR1_Apr,\
     ENSO_negR1_May,ENSO_negR1_JJA,ENSO_negR1_SON,ENSO_negR1_DJF,\
     ENSO_negR1_MAM,ENSO_negR1_annual,\
     ENSO_neutralR1_Jun,ENSO_neutralR1_Jul, ENSO_neutralR1_Aug,\
     ENSO_neutralR1_Sep,ENSO_neutralR1_Oct,ENSO_neutralR1_Nov,ENSO_neutralR1_Dec,\
     ENSO_neutralR1_Jan,ENSO_neutralR1_Feb,ENSO_neutralR1_Mar,ENSO_neutralR1_Apr,\
     ENSO_neutralR1_May,ENSO_neutralR1_JJA,ENSO_neutralR1_SON,ENSO_neutralR1_DJF,\
     ENSO_neutralR1_MAM,ENSO_neutralR1_annual,\
     IPO_posR1_Jun,IPO_posR1_Jul, IPO_posR1_Aug,\
     IPO_posR1_Sep,IPO_posR1_Oct,IPO_posR1_Nov,IPO_posR1_Dec,\
     IPO_posR1_Jan,IPO_posR1_Feb,IPO_posR1_Mar,IPO_posR1_Apr,\
     IPO_posR1_May,IPO_posR1_JJA,IPO_posR1_SON,IPO_posR1_DJF,\
     IPO_posR1_MAM,IPO_posR1_annual,\
     IPO_negR1_Jun,IPO_negR1_Jul, IPO_negR1_Aug,\
     IPO_negR1_Sep,IPO_negR1_Oct,IPO_negR1_Nov,IPO_negR1_Dec,\
     IPO_negR1_Jan,IPO_negR1_Feb,IPO_negR1_Mar,IPO_negR1_Apr,\
     IPO_negR1_May,IPO_negR1_JJA,IPO_negR1_SON,IPO_negR1_DJF,\
     IPO_negR1_MAM,IPO_negR1_annual,\
     IPO_neutralR1_Jun,IPO_neutralR1_Jul, IPO_neutralR1_Aug,\
     IPO_neutralR1_Sep,IPO_neutralR1_Oct,IPO_neutralR1_Nov,IPO_neutralR1_Dec,\
     IPO_neutralR1_Jan,IPO_neutralR1_Feb,IPO_neutralR1_Mar,IPO_neutralR1_Apr,\
     IPO_neutralR1_May,IPO_neutralR1_JJA,IPO_neutralR1_SON,IPO_neutralR1_DJF,\
     IPO_neutralR1_MAM,IPO_neutralR1_annual,\
     ENSO_posR2_Jun,ENSO_posR2_Jul, ENSO_posR2_Aug,\
     ENSO_posR2_Sep,ENSO_posR2_Oct,ENSO_posR2_Nov,ENSO_posR2_Dec,\
     ENSO_posR2_Jan,ENSO_posR2_Feb,ENSO_posR2_Mar,ENSO_posR2_Apr,\
     ENSO_posR2_May,ENSO_posR2_JJA,ENSO_posR2_SON,ENSO_posR2_DJF,\
     ENSO_posR2_MAM,ENSO_posR2_annual,\
     ENSO_negR2_Jun,ENSO_negR2_Jul, ENSO_negR2_Aug,\
     ENSO_negR2_Sep,ENSO_negR2_Oct,ENSO_negR2_Nov,ENSO_negR2_Dec,\
     ENSO_negR2_Jan,ENSO_negR2_Feb,ENSO_negR2_Mar,ENSO_negR2_Apr,\
     ENSO_negR2_May,ENSO_negR2_JJA,ENSO_negR2_SON,ENSO_negR2_DJF,\
     ENSO_negR2_MAM,ENSO_negR2_annual,\
     ENSO_neutralR2_Jun,ENSO_neutralR2_Jul, ENSO_neutralR2_Aug,\
     ENSO_neutralR2_Sep,ENSO_neutralR2_Oct,ENSO_neutralR2_Nov,ENSO_neutralR2_Dec,\
     ENSO_neutralR2_Jan,ENSO_neutralR2_Feb,ENSO_neutralR2_Mar,ENSO_neutralR2_Apr,\
     ENSO_neutralR2_May,ENSO_neutralR2_JJA,ENSO_neutralR2_SON,ENSO_neutralR2_DJF,\
     ENSO_neutralR2_MAM,ENSO_neutralR2_annual,\
     IPO_posR2_Jun,IPO_posR2_Jul, IPO_posR2_Aug,\
     IPO_posR2_Sep,IPO_posR2_Oct,IPO_posR2_Nov,IPO_posR2_Dec,\
     IPO_posR2_Jan,IPO_posR2_Feb,IPO_posR2_Mar,IPO_posR2_Apr,\
     IPO_posR2_May,IPO_posR2_JJA,IPO_posR2_SON,IPO_posR2_DJF,\
     IPO_posR2_MAM,IPO_posR2_annual,\
     IPO_negR2_Jun,IPO_negR2_Jul, IPO_negR2_Aug,\
     IPO_negR2_Sep,IPO_negR2_Oct,IPO_negR2_Nov,IPO_negR2_Dec,\
     IPO_negR2_Jan,IPO_negR2_Feb,IPO_negR2_Mar,IPO_negR2_Apr,\
     IPO_negR2_May,IPO_negR2_JJA,IPO_negR2_SON,IPO_negR2_DJF,\
     IPO_negR2_MAM,IPO_negR2_annual,\
     IPO_neutralR2_Jun,IPO_neutralR2_Jul, IPO_neutralR2_Aug,\
     IPO_neutralR2_Sep,IPO_neutralR2_Oct,IPO_neutralR2_Nov,IPO_neutralR2_Dec,\
     IPO_neutralR2_Jan,IPO_neutralR2_Feb,IPO_neutralR2_Mar,IPO_neutralR2_Apr,\
     IPO_neutralR2_May,IPO_neutralR2_JJA,IPO_neutralR2_SON,IPO_neutralR2_DJF,\
     IPO_neutralR2_MAM,IPO_neutralR2_annual,\
     ENSO_posR3_Jun,ENSO_posR3_Jul, ENSO_posR3_Aug,\
     ENSO_posR3_Sep,ENSO_posR3_Oct,ENSO_posR3_Nov,ENSO_posR3_Dec,\
     ENSO_posR3_Jan,ENSO_posR3_Feb,ENSO_posR3_Mar,ENSO_posR3_Apr,\
     ENSO_posR3_May,ENSO_posR3_JJA,ENSO_posR3_SON,ENSO_posR3_DJF,\
     ENSO_posR3_MAM,ENSO_posR3_annual,\
     ENSO_negR3_Jun,ENSO_negR3_Jul, ENSO_negR3_Aug,\
     ENSO_negR3_Sep,ENSO_negR3_Oct,ENSO_negR3_Nov,ENSO_negR3_Dec,\
     ENSO_negR3_Jan,ENSO_negR3_Feb,ENSO_negR3_Mar,ENSO_negR3_Apr,\
     ENSO_negR3_May,ENSO_negR3_JJA,ENSO_negR3_SON,ENSO_negR3_DJF,\
     ENSO_negR3_MAM,ENSO_negR3_annual,\
     ENSO_neutralR3_Jun,ENSO_neutralR3_Jul, ENSO_neutralR3_Aug,\
     ENSO_neutralR3_Sep,ENSO_neutralR3_Oct,ENSO_neutralR3_Nov,ENSO_neutralR3_Dec,\
     ENSO_neutralR3_Jan,ENSO_neutralR3_Feb,ENSO_neutralR3_Mar,ENSO_neutralR3_Apr,\
     ENSO_neutralR3_May,ENSO_neutralR3_JJA,ENSO_neutralR3_SON,ENSO_neutralR3_DJF,\
     ENSO_neutralR3_MAM,ENSO_neutralR3_annual,\
     IPO_posR3_Jun,IPO_posR3_Jul, IPO_posR3_Aug,\
     IPO_posR3_Sep,IPO_posR3_Oct,IPO_posR3_Nov,IPO_posR3_Dec,\
     IPO_posR3_Jan,IPO_posR3_Feb,IPO_posR3_Mar,IPO_posR3_Apr,\
     IPO_posR3_May,IPO_posR3_JJA,IPO_posR3_SON,IPO_posR3_DJF,\
     IPO_posR3_MAM,IPO_posR3_annual,\
     IPO_negR3_Jun,IPO_negR3_Jul, IPO_negR3_Aug,\
     IPO_negR3_Sep,IPO_negR3_Oct,IPO_negR3_Nov,IPO_negR3_Dec,\
     IPO_negR3_Jan,IPO_negR3_Feb,IPO_negR3_Mar,IPO_negR3_Apr,\
     IPO_negR3_May,IPO_negR3_JJA,IPO_negR3_SON,IPO_negR3_DJF,\
     IPO_negR3_MAM,IPO_negR3_annual,\
     IPO_neutralR3_Jun,IPO_neutralR3_Jul, IPO_neutralR3_Aug,\
     IPO_neutralR3_Sep,IPO_neutralR3_Oct,IPO_neutralR3_Nov,IPO_neutralR3_Dec,\
     IPO_neutralR3_Jan,IPO_neutralR3_Feb,IPO_neutralR3_Mar,IPO_neutralR3_Apr,\
     IPO_neutralR3_May,IPO_neutralR3_JJA,IPO_neutralR3_SON,IPO_neutralR3_DJF,\
     IPO_neutralR3_MAM,IPO_neutralR3_annual

def corrStrat(array1,array2):
    list1 = []
    count = 0
    while count < 17:
        list1.append(correl(array1[count],array2[count]))
        count += 1
    array = np.asarray(list1)
    return array

#HadISST observational data

ENSO_posHad =[ENSO_posHad_annual,ENSO_posHad_JJA,ENSO_posHad_SON,ENSO_posHad_DJF,\
           ENSO_posHad_MAM,ENSO_posHad_Jun,ENSO_posHad_Jul,ENSO_posHad_Aug,\
           ENSO_posHad_Sep,ENSO_posHad_Oct,ENSO_posHad_Nov,ENSO_posHad_Dec,\
           ENSO_posHad_Jan,ENSO_posHad_Feb,ENSO_posHad_Mar,ENSO_posHad_Apr,\
           ENSO_posHad_May]

ENSO_negHad =[ENSO_negHad_annual,ENSO_negHad_JJA,ENSO_negHad_SON,ENSO_negHad_DJF,\
           ENSO_negHad_MAM,ENSO_negHad_Jun,ENSO_negHad_Jul,ENSO_negHad_Aug,\
           ENSO_negHad_Sep,ENSO_negHad_Oct,ENSO_negHad_Nov,ENSO_negHad_Dec,\
           ENSO_negHad_Jan,ENSO_negHad_Feb,ENSO_negHad_Mar,ENSO_negHad_Apr,\
           ENSO_negHad_May]

ENSO_neutralHad =[ENSO_neutralHad_annual,ENSO_neutralHad_JJA,ENSO_neutralHad_SON,ENSO_neutralHad_DJF,\
           ENSO_neutralHad_MAM,ENSO_neutralHad_Jun,ENSO_neutralHad_Jul,ENSO_neutralHad_Aug,\
           ENSO_neutralHad_Sep,ENSO_neutralHad_Oct,ENSO_neutralHad_Nov,ENSO_neutralHad_Dec,\
           ENSO_neutralHad_Jan,ENSO_neutralHad_Feb,ENSO_neutralHad_Mar,ENSO_neutralHad_Apr,\
           ENSO_neutralHad_May]

IPO_posHad =[IPO_posHad_annual,IPO_posHad_JJA,IPO_posHad_SON,IPO_posHad_DJF,\
           IPO_posHad_MAM,IPO_posHad_Jun,IPO_posHad_Jul,IPO_posHad_Aug,\
           IPO_posHad_Sep,IPO_posHad_Oct,IPO_posHad_Nov,IPO_posHad_Dec,\
           IPO_posHad_Jan,IPO_posHad_Feb,IPO_posHad_Mar,IPO_posHad_Apr,\
           IPO_posHad_May]

IPO_negHad =[IPO_negHad_annual,IPO_negHad_JJA,IPO_negHad_SON,IPO_negHad_DJF,\
           IPO_negHad_MAM,IPO_negHad_Jun,IPO_negHad_Jul,IPO_negHad_Aug,\
           IPO_negHad_Sep,IPO_negHad_Oct,IPO_negHad_Nov,IPO_negHad_Dec,\
           IPO_negHad_Jan,IPO_negHad_Feb,IPO_negHad_Mar,IPO_negHad_Apr,\
           IPO_negHad_May]

IPO_neutralHad =[IPO_neutralHad_annual,IPO_neutralHad_JJA,IPO_neutralHad_SON,IPO_neutralHad_DJF,\
           IPO_neutralHad_MAM,IPO_neutralHad_Jun,IPO_neutralHad_Jul,IPO_neutralHad_Aug,\
           IPO_neutralHad_Sep,IPO_neutralHad_Oct,IPO_neutralHad_Nov,IPO_neutralHad_Dec,\
           IPO_neutralHad_Jan,IPO_neutralHad_Feb,IPO_neutralHad_Mar,IPO_neutralHad_Apr,\
           IPO_neutralHad_May]

#ACCESS R1 data

ENSO_posR1 =[ENSO_posR1_annual,ENSO_posR1_JJA,ENSO_posR1_SON,ENSO_posR1_DJF,\
           ENSO_posR1_MAM,ENSO_posR1_Jun,ENSO_posR1_Jul,ENSO_posR1_Aug,\
           ENSO_posR1_Sep,ENSO_posR1_Oct,ENSO_posR1_Nov,ENSO_posR1_Dec,\
           ENSO_posR1_Jan,ENSO_posR1_Feb,ENSO_posR1_Mar,ENSO_posR1_Apr,\
           ENSO_posR1_May]

ENSO_negR1 =[ENSO_negR1_annual,ENSO_negR1_JJA,ENSO_negR1_SON,ENSO_negR1_DJF,\
           ENSO_negR1_MAM,ENSO_negR1_Jun,ENSO_negR1_Jul,ENSO_negR1_Aug,\
           ENSO_negR1_Sep,ENSO_negR1_Oct,ENSO_negR1_Nov,ENSO_negR1_Dec,\
           ENSO_negR1_Jan,ENSO_negR1_Feb,ENSO_negR1_Mar,ENSO_negR1_Apr,\
           ENSO_negR1_May]

ENSO_neutralR1 =[ENSO_neutralR1_annual,ENSO_neutralR1_JJA,ENSO_neutralR1_SON,ENSO_neutralR1_DJF,\
           ENSO_neutralR1_MAM,ENSO_neutralR1_Jun,ENSO_neutralR1_Jul,ENSO_neutralR1_Aug,\
           ENSO_neutralR1_Sep,ENSO_neutralR1_Oct,ENSO_neutralR1_Nov,ENSO_neutralR1_Dec,\
           ENSO_neutralR1_Jan,ENSO_neutralR1_Feb,ENSO_neutralR1_Mar,ENSO_neutralR1_Apr,\
           ENSO_neutralR1_May]

IPO_posR1 =[IPO_posR1_annual,IPO_posR1_JJA,IPO_posR1_SON,IPO_posR1_DJF,\
           IPO_posR1_MAM,IPO_posR1_Jun,IPO_posR1_Jul,IPO_posR1_Aug,\
           IPO_posR1_Sep,IPO_posR1_Oct,IPO_posR1_Nov,IPO_posR1_Dec,\
           IPO_posR1_Jan,IPO_posR1_Feb,IPO_posR1_Mar,IPO_posR1_Apr,\
           IPO_posR1_May]

IPO_negR1 =[IPO_negR1_annual,IPO_negR1_JJA,IPO_negR1_SON,IPO_negR1_DJF,\
           IPO_negR1_MAM,IPO_negR1_Jun,IPO_negR1_Jul,IPO_negR1_Aug,\
           IPO_negR1_Sep,IPO_negR1_Oct,IPO_negR1_Nov,IPO_negR1_Dec,\
           IPO_negR1_Jan,IPO_negR1_Feb,IPO_negR1_Mar,IPO_negR1_Apr,\
           IPO_negR1_May]

IPO_neutralR1 =[IPO_neutralR1_annual,IPO_neutralR1_JJA,IPO_neutralR1_SON,IPO_neutralR1_DJF,\
           IPO_neutralR1_MAM,IPO_neutralR1_Jun,IPO_neutralR1_Jul,IPO_neutralR1_Aug,\
           IPO_neutralR1_Sep,IPO_neutralR1_Oct,IPO_neutralR1_Nov,IPO_neutralR1_Dec,\
           IPO_neutralR1_Jan,IPO_neutralR1_Feb,IPO_neutralR1_Mar,IPO_neutralR1_Apr,\
           IPO_neutralR1_May]

#ACCESS R2 data

ENSO_posR2 =[ENSO_posR2_annual,ENSO_posR2_JJA,ENSO_posR2_SON,ENSO_posR2_DJF,\
           ENSO_posR2_MAM,ENSO_posR2_Jun,ENSO_posR2_Jul,ENSO_posR2_Aug,\
           ENSO_posR2_Sep,ENSO_posR2_Oct,ENSO_posR2_Nov,ENSO_posR2_Dec,\
           ENSO_posR2_Jan,ENSO_posR2_Feb,ENSO_posR2_Mar,ENSO_posR2_Apr,\
           ENSO_posR2_May]

ENSO_negR2 =[ENSO_negR2_annual,ENSO_negR2_JJA,ENSO_negR2_SON,ENSO_negR2_DJF,\
           ENSO_negR2_MAM,ENSO_negR2_Jun,ENSO_negR2_Jul,ENSO_negR2_Aug,\
           ENSO_negR2_Sep,ENSO_negR2_Oct,ENSO_negR2_Nov,ENSO_negR2_Dec,\
           ENSO_negR2_Jan,ENSO_negR2_Feb,ENSO_negR2_Mar,ENSO_negR2_Apr,\
           ENSO_negR2_May]

ENSO_neutralR2 =[ENSO_neutralR2_annual,ENSO_neutralR2_JJA,ENSO_neutralR2_SON,ENSO_neutralR2_DJF,\
           ENSO_neutralR2_MAM,ENSO_neutralR2_Jun,ENSO_neutralR2_Jul,ENSO_neutralR2_Aug,\
           ENSO_neutralR2_Sep,ENSO_neutralR2_Oct,ENSO_neutralR2_Nov,ENSO_neutralR2_Dec,\
           ENSO_neutralR2_Jan,ENSO_neutralR2_Feb,ENSO_neutralR2_Mar,ENSO_neutralR2_Apr,\
           ENSO_neutralR2_May]

IPO_posR2 =[IPO_posR2_annual,IPO_posR2_JJA,IPO_posR2_SON,IPO_posR2_DJF,\
           IPO_posR2_MAM,IPO_posR2_Jun,IPO_posR2_Jul,IPO_posR2_Aug,\
           IPO_posR2_Sep,IPO_posR2_Oct,IPO_posR2_Nov,IPO_posR2_Dec,\
           IPO_posR2_Jan,IPO_posR2_Feb,IPO_posR2_Mar,IPO_posR2_Apr,\
           IPO_posR2_May]

IPO_negR2 =[IPO_negR2_annual,IPO_negR2_JJA,IPO_negR2_SON,IPO_negR2_DJF,\
           IPO_negR2_MAM,IPO_negR2_Jun,IPO_negR2_Jul,IPO_negR2_Aug,\
           IPO_negR2_Sep,IPO_negR2_Oct,IPO_negR2_Nov,IPO_negR2_Dec,\
           IPO_negR2_Jan,IPO_negR2_Feb,IPO_negR2_Mar,IPO_negR2_Apr,\
           IPO_negR2_May]

IPO_neutralR2 =[IPO_neutralR2_annual,IPO_neutralR2_JJA,IPO_neutralR2_SON,IPO_neutralR2_DJF,\
           IPO_neutralR2_MAM,IPO_neutralR2_Jun,IPO_neutralR2_Jul,IPO_neutralR2_Aug,\
           IPO_neutralR2_Sep,IPO_neutralR2_Oct,IPO_neutralR2_Nov,IPO_neutralR2_Dec,\
           IPO_neutralR2_Jan,IPO_neutralR2_Feb,IPO_neutralR2_Mar,IPO_neutralR2_Apr,\
           IPO_neutralR2_May]

#ACCESS R3 data

ENSO_posR3 =[ENSO_posR3_annual,ENSO_posR3_JJA,ENSO_posR3_SON,ENSO_posR3_DJF,\
           ENSO_posR3_MAM,ENSO_posR3_Jun,ENSO_posR3_Jul,ENSO_posR3_Aug,\
           ENSO_posR3_Sep,ENSO_posR3_Oct,ENSO_posR3_Nov,ENSO_posR3_Dec,\
           ENSO_posR3_Jan,ENSO_posR3_Feb,ENSO_posR3_Mar,ENSO_posR3_Apr,\
           ENSO_posR3_May]

ENSO_negR3 =[ENSO_negR3_annual,ENSO_negR3_JJA,ENSO_negR3_SON,ENSO_negR3_DJF,\
           ENSO_negR3_MAM,ENSO_negR3_Jun,ENSO_negR3_Jul,ENSO_negR3_Aug,\
           ENSO_negR3_Sep,ENSO_negR3_Oct,ENSO_negR3_Nov,ENSO_negR3_Dec,\
           ENSO_negR3_Jan,ENSO_negR3_Feb,ENSO_negR3_Mar,ENSO_negR3_Apr,\
           ENSO_negR3_May]

ENSO_neutralR3 =[ENSO_neutralR3_annual,ENSO_neutralR3_JJA,ENSO_neutralR3_SON,ENSO_neutralR3_DJF,\
           ENSO_neutralR3_MAM,ENSO_neutralR3_Jun,ENSO_neutralR3_Jul,ENSO_neutralR3_Aug,\
           ENSO_neutralR3_Sep,ENSO_neutralR3_Oct,ENSO_neutralR3_Nov,ENSO_neutralR3_Dec,\
           ENSO_neutralR3_Jan,ENSO_neutralR3_Feb,ENSO_neutralR3_Mar,ENSO_neutralR3_Apr,\
           ENSO_neutralR3_May]

IPO_posR3 =[IPO_posR3_annual,IPO_posR3_JJA,IPO_posR3_SON,IPO_posR3_DJF,\
           IPO_posR3_MAM,IPO_posR3_Jun,IPO_posR3_Jul,IPO_posR3_Aug,\
           IPO_posR3_Sep,IPO_posR3_Oct,IPO_posR3_Nov,IPO_posR3_Dec,\
           IPO_posR3_Jan,IPO_posR3_Feb,IPO_posR3_Mar,IPO_posR3_Apr,\
           IPO_posR3_May]

IPO_negR3 =[IPO_negR3_annual,IPO_negR3_JJA,IPO_negR3_SON,IPO_negR3_DJF,\
           IPO_negR3_MAM,IPO_negR3_Jun,IPO_negR3_Jul,IPO_negR3_Aug,\
           IPO_negR3_Sep,IPO_negR3_Oct,IPO_negR3_Nov,IPO_negR3_Dec,\
           IPO_negR3_Jan,IPO_negR3_Feb,IPO_negR3_Mar,IPO_negR3_Apr,\
           IPO_negR3_May]

IPO_neutralR3 =[IPO_neutralR3_annual,IPO_neutralR3_JJA,IPO_neutralR3_SON,IPO_neutralR3_DJF,\
           IPO_neutralR3_MAM,IPO_neutralR3_Jun,IPO_neutralR3_Jul,IPO_neutralR3_Aug,\
           IPO_neutralR3_Sep,IPO_neutralR3_Oct,IPO_neutralR3_Nov,IPO_neutralR3_Dec,\
           IPO_neutralR3_Jan,IPO_neutralR3_Feb,IPO_neutralR3_Mar,IPO_neutralR3_Apr,\
           IPO_neutralR3_May]

# HadISST correlations
HadISST_corr_list = []
HadISST_corr_list.append(corrStrat(ENSO_posHad,IPO_posHad))
HadISST_corr_list.append(corrStrat(ENSO_posHad,IPO_negHad))
HadISST_corr_list.append(corrStrat(ENSO_posHad,IPO_neutralHad))
HadISST_corr_list.append(corrStrat(ENSO_negHad,IPO_posHad))
HadISST_corr_list.append(corrStrat(ENSO_negHad,IPO_negHad))
HadISST_corr_list.append(corrStrat(ENSO_negHad,IPO_neutralHad))
HadISST_corr_list.append(corrStrat(ENSO_neutralHad,IPO_posHad))
HadISST_corr_list.append(corrStrat(ENSO_neutralHad,IPO_negHad))
HadISST_corr_list.append(corrStrat(ENSO_neutralHad,IPO_neutralHad))
HadISST_corr = np.asarray(HadISST_corr_list)

# ACCESS R1 correlations
R1_corr_list = []
R1_corr_list.append(corrStrat(ENSO_posR1,IPO_posR1))
R1_corr_list.append(corrStrat(ENSO_posR1,IPO_negR1))
R1_corr_list.append(corrStrat(ENSO_posR1,IPO_neutralR1))
R1_corr_list.append(corrStrat(ENSO_negR1,IPO_posR1))
R1_corr_list.append(corrStrat(ENSO_negR1,IPO_negR1))
R1_corr_list.append(corrStrat(ENSO_negR1,IPO_neutralR1))
R1_corr_list.append(corrStrat(ENSO_neutralR1,IPO_posR1))
R1_corr_list.append(corrStrat(ENSO_neutralR1,IPO_negR1))
R1_corr_list.append(corrStrat(ENSO_neutralR1,IPO_neutralR1))
R1_corr = np.asarray(R1_corr_list)

# ACCESS R2 correlations
R2_corr_list = []
R2_corr_list.append(corrStrat(ENSO_posR2,IPO_posR2))
R2_corr_list.append(corrStrat(ENSO_posR2,IPO_negR2))
R2_corr_list.append(corrStrat(ENSO_posR2,IPO_neutralR2))
R2_corr_list.append(corrStrat(ENSO_negR2,IPO_posR2))
R2_corr_list.append(corrStrat(ENSO_negR2,IPO_negR2))
R2_corr_list.append(corrStrat(ENSO_negR2,IPO_neutralR2))
R2_corr_list.append(corrStrat(ENSO_neutralR2,IPO_posR2))
R2_corr_list.append(corrStrat(ENSO_neutralR2,IPO_negR2))
R2_corr_list.append(corrStrat(ENSO_neutralR2,IPO_neutralR2))
R2_corr = np.asarray(R2_corr_list)

# ACCESS R3 correlations
R3_corr_list = []
R3_corr_list.append(corrStrat(ENSO_posR3,IPO_posR3))
R3_corr_list.append(corrStrat(ENSO_posR3,IPO_negR3))
R3_corr_list.append(corrStrat(ENSO_posR3,IPO_neutralR3))
R3_corr_list.append(corrStrat(ENSO_negR3,IPO_posR3))
R3_corr_list.append(corrStrat(ENSO_negR3,IPO_negR3))
R3_corr_list.append(corrStrat(ENSO_negR3,IPO_neutralR3))
R3_corr_list.append(corrStrat(ENSO_neutralR3,IPO_posR3))
R3_corr_list.append(corrStrat(ENSO_neutralR3,IPO_negR3))
R3_corr_list.append(corrStrat(ENSO_neutralR3,IPO_neutralR3))
R3_corr = np.asarray(R3_corr_list)


#Output to CSV:
output = np.column_stack((HadISST_corr[0,:,0].flatten(),\
                          HadISST_corr[0,:,1].flatten(),\
                          HadISST_corr[1,:,0].flatten(),\
                          HadISST_corr[1,:,1].flatten(),\
                          HadISST_corr[2,:,0].flatten(),\
                          HadISST_corr[2,:,1].flatten(),\
                          HadISST_corr[3,:,0].flatten(),\
                          HadISST_corr[3,:,1].flatten(),\
                          HadISST_corr[4,:,0].flatten(),\
                          HadISST_corr[4,:,1].flatten(),\
                          HadISST_corr[5,:,0].flatten(),\
                          HadISST_corr[5,:,1].flatten(),\
                          HadISST_corr[6,:,0].flatten(),\
                          HadISST_corr[6,:,1].flatten(),\
                          HadISST_corr[7,:,0].flatten(),\
                          HadISST_corr[7,:,1].flatten(),\
                          HadISST_corr[8,:,0].flatten(),\
                          HadISST_corr[8,:,1].flatten(),\
                          R1_corr[0,:,0].flatten(),\
                          R1_corr[0,:,1].flatten(),\
                          R1_corr[1,:,0].flatten(),\
                          R1_corr[1,:,1].flatten(),\
                          R1_corr[2,:,0].flatten(),\
                          R1_corr[2,:,1].flatten(),\
                          R1_corr[3,:,0].flatten(),\
                          R1_corr[3,:,1].flatten(),\
                          R1_corr[4,:,0].flatten(),\
                          R1_corr[4,:,1].flatten(),\
                          R1_corr[5,:,0].flatten(),\
                          R1_corr[5,:,1].flatten(),\
                          R1_corr[6,:,0].flatten(),\
                          R1_corr[6,:,1].flatten(),\
                          R1_corr[7,:,0].flatten(),\
                          R1_corr[7,:,1].flatten(),\
                          R1_corr[8,:,0].flatten(),\
                          R1_corr[8,:,1].flatten(),\
                          R2_corr[0,:,0].flatten(),\
                          R2_corr[0,:,1].flatten(),\
                          R2_corr[1,:,0].flatten(),\
                          R2_corr[1,:,1].flatten(),\
                          R2_corr[2,:,0].flatten(),\
                          R2_corr[2,:,1].flatten(),\
                          R2_corr[3,:,0].flatten(),\
                          R2_corr[3,:,1].flatten(),\
                          R2_corr[4,:,0].flatten(),\
                          R2_corr[4,:,1].flatten(),\
                          R2_corr[5,:,0].flatten(),\
                          R2_corr[5,:,1].flatten(),\
                          R2_corr[6,:,0].flatten(),\
                          R2_corr[6,:,1].flatten(),\
                          R2_corr[7,:,0].flatten(),\
                          R2_corr[7,:,1].flatten(),\
                          R2_corr[8,:,0].flatten(),\
                          R2_corr[8,:,1].flatten(),\
                          R3_corr[0,:,0].flatten(),\
                          R3_corr[0,:,1].flatten(),\
                          R3_corr[1,:,0].flatten(),\
                          R3_corr[1,:,1].flatten(),\
                          R3_corr[2,:,0].flatten(),\
                          R3_corr[2,:,1].flatten(),\
                          R3_corr[3,:,0].flatten(),\
                          R3_corr[3,:,1].flatten(),\
                          R3_corr[4,:,0].flatten(),\
                          R3_corr[4,:,1].flatten(),\
                          R3_corr[5,:,0].flatten(),\
                          R3_corr[5,:,1].flatten(),\
                          R3_corr[6,:,0].flatten(),\
                          R3_corr[6,:,1].flatten(),\
                          R3_corr[7,:,0].flatten(),\
                          R3_corr[7,:,1].flatten(),\
                          R3_corr[8,:,0].flatten(),\
                          R3_corr[8,:,1].flatten()))

np.savetxt('data/Correlation_coefficients/correlations_stratified_3SD.csv',output,delimiter=',')

###################################################################################
# Check to see if stratified correlations are statistically significantly different
###################################################################################

#Check if data is statistically significant from ENSO/IPO neutral

had_pos_pos = unpaired_t_test(HadISST_corr[8,:,0],HadISST_corr[0,:,0])
had_neu_pos = unpaired_t_test(HadISST_corr[8,:,0],HadISST_corr[6,:,0])
had_neg_pos = unpaired_t_test(HadISST_corr[8,:,0],HadISST_corr[3,:,0])
had_pos_neu = unpaired_t_test(HadISST_corr[8,:,0],HadISST_corr[2,:,0])
had_neg_neu = unpaired_t_test(HadISST_corr[8,:,0],HadISST_corr[5,:,0])
had_pos_neg = unpaired_t_test(HadISST_corr[8,:,0],HadISST_corr[1,:,0])
had_neu_neg = unpaired_t_test(HadISST_corr[8,:,0],HadISST_corr[7,:,0])
had_neg_neg = unpaired_t_test(HadISST_corr[8,:,0],HadISST_corr[4,:,0])

hadISST_stat_sig = np.vstack((had_pos_pos,had_neu_pos,had_neg_pos,\
                              had_pos_neu,had_neg_neu,had_pos_neg,\
                              had_neu_neg,had_neg_neg))

R1_pos_pos = unpaired_t_test(R1_corr[8,:,0],R1_corr[0,:,0])
R1_neu_pos = unpaired_t_test(R1_corr[8,:,0],R1_corr[6,:,0])
R1_neg_pos = unpaired_t_test(R1_corr[8,:,0],R1_corr[3,:,0])
R1_pos_neu = unpaired_t_test(R1_corr[8,:,0],R1_corr[2,:,0])
R1_neg_neu = unpaired_t_test(R1_corr[8,:,0],R1_corr[5,:,0])
R1_pos_neg = unpaired_t_test(R1_corr[8,:,0],R1_corr[1,:,0])
R1_neu_neg = unpaired_t_test(R1_corr[8,:,0],R1_corr[7,:,0])
R1_neg_neg = unpaired_t_test(R1_corr[8,:,0],R1_corr[4,:,0])

R1_stat_sig = np.vstack((R1_pos_pos,R1_neu_pos,R1_neg_pos,\
                              R1_pos_neu,R1_neg_neu,R1_pos_neg,\
                              R1_neu_neg,R1_neg_neg))

R2_pos_pos = unpaired_t_test(R2_corr[8,:,0],R2_corr[0,:,0])
R2_neu_pos = unpaired_t_test(R2_corr[8,:,0],R2_corr[6,:,0])
R2_neg_pos = unpaired_t_test(R2_corr[8,:,0],R2_corr[3,:,0])
R2_pos_neu = unpaired_t_test(R2_corr[8,:,0],R2_corr[2,:,0])
R2_neg_neu = unpaired_t_test(R2_corr[8,:,0],R2_corr[5,:,0])
R2_pos_neg = unpaired_t_test(R2_corr[8,:,0],R2_corr[1,:,0])
R2_neu_neg = unpaired_t_test(R2_corr[8,:,0],R2_corr[7,:,0])
R2_neg_neg = unpaired_t_test(R2_corr[8,:,0],R2_corr[4,:,0])

R2_stat_sig = np.vstack((R2_pos_pos,R2_neu_pos,R2_neg_pos,\
                              R2_pos_neu,R2_neg_neu,R2_pos_neg,\
                              R2_neu_neg,R2_neg_neg))

R3_pos_pos = unpaired_t_test(R3_corr[8,:,0],R3_corr[0,:,0])
R3_neu_pos = unpaired_t_test(R3_corr[8,:,0],R3_corr[6,:,0])
R3_neg_pos = unpaired_t_test(R3_corr[8,:,0],R3_corr[3,:,0])
R3_pos_neu = unpaired_t_test(R3_corr[8,:,0],R3_corr[2,:,0])
R3_neg_neu = unpaired_t_test(R3_corr[8,:,0],R3_corr[5,:,0])
R3_pos_neg = unpaired_t_test(R3_corr[8,:,0],R3_corr[1,:,0])
R3_neu_neg = unpaired_t_test(R3_corr[8,:,0],R3_corr[7,:,0])
R3_neg_neg = unpaired_t_test(R3_corr[8,:,0],R3_corr[4,:,0])

R3_stat_sig = np.vstack((R3_pos_pos,R3_neu_pos,R3_neg_pos,\
                              R3_pos_neu,R3_neg_neu,R3_pos_neg,\
                              R3_neu_neg,R3_neg_neg))

#Check if ACCESS data is statistically significant from HadISST data
Had_R1_neu_neu = unpaired_t_test(HadISST_corr[8,:,0],R1_corr[8,:,0])
Had_R1_pos_pos = unpaired_t_test(HadISST_corr[0,:,0],R1_corr[0,:,0])
Had_R1_neu_pos = unpaired_t_test(HadISST_corr[6,:,0],R1_corr[6,:,0])
Had_R1_neg_pos = unpaired_t_test(HadISST_corr[3,:,0],R1_corr[3,:,0])
Had_R1_pos_neu = unpaired_t_test(HadISST_corr[2,:,0],R1_corr[2,:,0])
Had_R1_neg_neu = unpaired_t_test(HadISST_corr[5,:,0],R1_corr[5,:,0])
Had_R1_pos_neg = unpaired_t_test(HadISST_corr[1,:,0],R1_corr[1,:,0])
Had_R1_neu_neg = unpaired_t_test(HadISST_corr[7,:,0],R1_corr[7,:,0])
Had_R1_neg_neg = unpaired_t_test(HadISST_corr[4,:,0],R1_corr[4,:,0])

Had_R1_stat_sig = np.vstack((Had_R1_neu_neu,Had_R1_pos_pos,Had_R1_neu_pos,\
                             Had_R1_neg_pos,Had_R1_pos_neu,Had_R1_neg_neu,\
                             Had_R1_pos_neg,Had_R1_neu_neg,Had_R1_neg_neg))

Had_R2_neu_neu = unpaired_t_test(HadISST_corr[8,:,0],R2_corr[8,:,0])
Had_R2_pos_pos = unpaired_t_test(HadISST_corr[0,:,0],R2_corr[0,:,0])
Had_R2_neu_pos = unpaired_t_test(HadISST_corr[6,:,0],R2_corr[6,:,0])
Had_R2_neg_pos = unpaired_t_test(HadISST_corr[3,:,0],R2_corr[3,:,0])
Had_R2_pos_neu = unpaired_t_test(HadISST_corr[2,:,0],R2_corr[2,:,0])
Had_R2_neg_neu = unpaired_t_test(HadISST_corr[5,:,0],R2_corr[5,:,0])
Had_R2_pos_neg = unpaired_t_test(HadISST_corr[1,:,0],R2_corr[1,:,0])
Had_R2_neu_neg = unpaired_t_test(HadISST_corr[7,:,0],R2_corr[7,:,0])
Had_R2_neg_neg = unpaired_t_test(HadISST_corr[4,:,0],R2_corr[4,:,0])

Had_R2_stat_sig = np.vstack((Had_R2_neu_neu,Had_R2_pos_pos,Had_R2_neu_pos,\
                             Had_R2_neg_pos,Had_R2_pos_neu,Had_R2_neg_neu,\
                             Had_R2_pos_neg,Had_R2_neu_neg,Had_R2_neg_neg))

Had_R3_neu_neu = unpaired_t_test(HadISST_corr[8,:,0],R3_corr[8,:,0])
Had_R3_pos_pos = unpaired_t_test(HadISST_corr[0,:,0],R3_corr[0,:,0])
Had_R3_neu_pos = unpaired_t_test(HadISST_corr[6,:,0],R3_corr[6,:,0])
Had_R3_neg_pos = unpaired_t_test(HadISST_corr[3,:,0],R3_corr[3,:,0])
Had_R3_pos_neu = unpaired_t_test(HadISST_corr[2,:,0],R3_corr[2,:,0])
Had_R3_neg_neu = unpaired_t_test(HadISST_corr[5,:,0],R3_corr[5,:,0])
Had_R3_pos_neg = unpaired_t_test(HadISST_corr[1,:,0],R3_corr[1,:,0])
Had_R3_neu_neg = unpaired_t_test(HadISST_corr[7,:,0],R3_corr[7,:,0])
Had_R3_neg_neg = unpaired_t_test(HadISST_corr[4,:,0],R3_corr[4,:,0])

Had_R3_stat_sig = np.vstack((Had_R3_neu_neu,Had_R3_pos_pos,Had_R3_neu_pos,\
                             Had_R3_neg_pos,Had_R3_pos_neu,Had_R3_neg_neu,\
                             Had_R3_pos_neg,Had_R3_neu_neg,Had_R3_neg_neg))

#Check if rounds of ACCESS data are statistically significantly different
R1_R2_neu_neu = unpaired_t_test(R1_corr[8,:,0],R2_corr[8,:,0])
R1_R2_pos_pos = unpaired_t_test(R1_corr[0,:,0],R2_corr[0,:,0])
R1_R2_neu_pos = unpaired_t_test(R1_corr[6,:,0],R2_corr[6,:,0])
R1_R2_neg_pos = unpaired_t_test(R1_corr[3,:,0],R2_corr[3,:,0])
R1_R2_pos_neu = unpaired_t_test(R1_corr[2,:,0],R2_corr[2,:,0])
R1_R2_neg_neu = unpaired_t_test(R1_corr[5,:,0],R2_corr[5,:,0])
R1_R2_pos_neg = unpaired_t_test(R1_corr[1,:,0],R2_corr[1,:,0])
R1_R2_neu_neg = unpaired_t_test(R1_corr[7,:,0],R2_corr[7,:,0])
R1_R2_neg_neg = unpaired_t_test(R1_corr[4,:,0],R2_corr[4,:,0])

R1_R2_stat_sig = np.vstack((R1_R2_neu_neu,R1_R2_pos_pos,R1_R2_neu_pos,\
                            R1_R2_neg_pos,R1_R2_pos_neu,R1_R2_neg_neu,\
                            R1_R2_pos_neg,R1_R2_neu_neg,R1_R2_neg_neg))

R1_R3_neu_neu = unpaired_t_test(R1_corr[8,:,0],R3_corr[8,:,0])
R1_R3_pos_pos = unpaired_t_test(R1_corr[0,:,0],R3_corr[0,:,0])
R1_R3_neu_pos = unpaired_t_test(R1_corr[6,:,0],R3_corr[6,:,0])
R1_R3_neg_pos = unpaired_t_test(R1_corr[3,:,0],R3_corr[3,:,0])
R1_R3_pos_neu = unpaired_t_test(R1_corr[2,:,0],R3_corr[2,:,0])
R1_R3_neg_neu = unpaired_t_test(R1_corr[5,:,0],R3_corr[5,:,0])
R1_R3_pos_neg = unpaired_t_test(R1_corr[1,:,0],R3_corr[1,:,0])
R1_R3_neu_neg = unpaired_t_test(R1_corr[7,:,0],R3_corr[7,:,0])
R1_R3_neg_neg = unpaired_t_test(R1_corr[4,:,0],R3_corr[4,:,0])

R1_R3_stat_sig = np.vstack((R1_R3_neu_neu,R1_R3_pos_pos,R1_R3_neu_pos,\
                            R1_R3_neg_pos,R1_R3_pos_neu,R1_R3_neg_neu,\
                            R1_R3_pos_neg,R1_R3_neu_neg,R1_R3_neg_neg))

R2_R3_neu_neu = unpaired_t_test(R2_corr[8,:,0],R3_corr[8,:,0])
R2_R3_pos_pos = unpaired_t_test(R2_corr[0,:,0],R3_corr[0,:,0])
R2_R3_neu_pos = unpaired_t_test(R2_corr[6,:,0],R3_corr[6,:,0])
R2_R3_neg_pos = unpaired_t_test(R2_corr[3,:,0],R3_corr[3,:,0])
R2_R3_pos_neu = unpaired_t_test(R2_corr[2,:,0],R3_corr[2,:,0])
R2_R3_neg_neu = unpaired_t_test(R2_corr[5,:,0],R3_corr[5,:,0])
R2_R3_pos_neg = unpaired_t_test(R2_corr[1,:,0],R3_corr[1,:,0])
R2_R3_neu_neg = unpaired_t_test(R2_corr[7,:,0],R3_corr[7,:,0])
R2_R3_neg_neg = unpaired_t_test(R2_corr[4,:,0],R3_corr[4,:,0])

R2_R3_stat_sig = np.vstack((R2_R3_neu_neu,R2_R3_pos_pos,R2_R3_neu_pos,\
                            R2_R3_neg_pos,R2_R3_pos_neu,R2_R3_neg_neu,\
                            R2_R3_pos_neg,R2_R3_neu_neg,R2_R3_neg_neg))

#Output to CSV
output2 = np.hstack((Had_R1_stat_sig,Had_R2_stat_sig,Had_R3_stat_sig,\
                     R1_R2_stat_sig,R1_R3_stat_sig,R2_R3_stat_sig))
output3 = np.hstack((hadISST_stat_sig,R1_stat_sig,R2_stat_sig,R3_stat_sig))
np.savetxt('data/Correlation_coefficients/correlations_stratified_significance_3SD.csv',output2,delimiter=',')
np.savetxt('data/Correlation_coefficients/correlations_stratified_significance_neutral_3SD.csv',output3,delimiter=',')


