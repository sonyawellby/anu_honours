"""
Script to prepare ACCESS1.3 sea-surface temperature data for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 13 August 2015.
"""

import netCDF4 as n
import numpy as np
from numpy import ma

from cwd import *
cwdInFunction()

from access_prepare import *

data = n.Dataset('ACCESS_data/ts_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','r')

#Prepare data for analysis
dataMiss = sstMissing()
dataCelsius = KtoC()
dataFull = dataCelsius

#Divide into time bins
data_flat = accessTrim()

accessAnnual = accessAnnual()

June = accessJune()
July = accessJuly()
August = accessAugust()
September = accessSeptember()
October = accessOctober()
November = accessNovember()
December = accessDecember()
January = accessJanuary()
February = accessFebruary()
March = accessMarch()
April = accessApril()
May = accessMay()

JJA = accessJJA()
SON = accessSON()
DJF = accessDJF()
MAM = accessMAM()
