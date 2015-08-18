"""
Set of routines to compute the Nino3.4 ENSO index.
Nino3.4 region: -5 to 5 degrees N, 190 to 240 degrees E

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 18 August 2015.
"""

import netCDF4 as n
import numpy as np

from cwd import *
cwdInFunction()

def base(dataset,ACCESS=True):
    """
    A function to determine average SSTs in the Nino3.4 region.
    Parameters:
    -----------
    dataset : SST data of monthly, seasonal or annual resolution;
            either from hadisst_prepare or access_ts
    ACCESS : (default = True)
            if the data is from access_ts, is "True".  This accommodates
            for differences in longitudinal/latitudinal starting points.
    """
    #Define Nino3.4 area
    if ACCESS==True:
        area = dataset[count,68:78,101:130] #101=189.375
        #[101]=189.375, [102]=191.26.  [101] was chosen as includes all
        #of Nino3.4 range.  It is also closer to 190.0 deg E.
    else:
        area = dataset[count,84:96,9:60] #5.5 to -5.5 N; -170.5 to -121.5 E
    
