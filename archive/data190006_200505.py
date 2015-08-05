"""
This file contains data variables from original data files containing only
data from June 1900 to May 2005.

Written by Sonya Wellby for ENVS4055, 2015.
Last updated 8 July 2015.
"""

#Set working directory
import os
os.chdir("/home/sonya/Documents/")

import netCDF4 as n
import numpy as np

#ACCESS data (precipitation)
from time_bins_ACCESS_pr import Jun1_array as Jun, Jul1_array as Jul, Aug1_array as Aug,\
     Sep1_array as Sep, Oct1_array as Oct, Nov1_array as Nov, Dec1_array as Dec,\
     Jan1_array as Jan, Feb1_array as Feb, Mar1_array as Mar, Apr1_array as Apr,\
     May1_array as May, DJF1 as DJF, MAM1 as MAM, JJA1 as JJA, SON1 as SON,\
     annualJunToMay as annual

#ACCESS data (SST)
from time_bins_ACCESS_ts import Jun1_array as Jun_SST, Jul1_array as Jul_SST,\
     Aug1_array as Aug_SST, Sep1_array as Sep_SST, Oct1_array as Oct_SST,\
     Nov1_array as Nov_SST, Dec1_array as Dec_SST,Jan1_array as Jan_SST, \
     Feb1_array as Feb_SST, Mar1_array as Mar_SST, Apr1_array as Apr_SST,\
     May1_array as May_SST, DJF1 as DJF_SST, MAM1 as MAM_SST, JJA1 as JJA_SST,\
     SON1 as SON_SST,annualJunToMay as annual_SST

#HadISST data (SST)
"""
from time_bins_ACCESS_ts import Jun1_array as Jun_SST, Jul1_array as Jul_SST,\
     Aug1_array as Aug_SST, Sep1_array as Sep_SST, Oct1_array as Oct_SST,\
     Nov1_array as Nov_SST, Dec1_array as Dec_SST,Jan1_array as Jan_SST, \
     Feb1_array as Feb_SST, Mar1_array as Mar_SST, Apr1_array as Apr_SST,\
     May1_array as May_SST, DJF1 as DJF_SST, MAM1 as MAM_SST, JJA1 as JJA_SST,\
     SON1 as SON_SST,annualJunToMay as annual_SST
"""
