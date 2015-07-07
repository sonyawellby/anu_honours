"""
Routines to:
1)Regrid the AWAP dataset to ACCESS1.3 grid size (1.25 NS,1.875 EW) in
the region developed in (1).
2)Extract AWAP and ACCESS1.3 (precipitation) data points for Aus. region

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 6 July 2015.
"""
#Check current working directory
import os
os.chdir("/home/sonya/Documents/")
print os.getcwd()

"""
If working directory set up correctly, this file should load
#f = open("my_coding_routines/foo.py","r")
"""

import netCDF4 as n
import numpy as np

accessData = n.Dataset('ACCESS_data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc','r')
access = accessData.variables['pr']
accessArray = np.reshape(access,(1872,145,192))

"""
awapData = n.Dataset('','r')
awap = awapData.variables['xx_prc']
awapArray = np.reshape(awap,(lengthx,lonx,latx))
"""

"""
1) Regrid AWAP data (0.05 x 0.05) to ACCESS1.3 grid size (1.25 NS, 1.875 EW)
"""
awap_regrid = np.zeros((len(awapArray),145,192))
#Regrid longitude
count = 0
while count < 145:
    for a[count] in awap_regrid:
        for i in awapArray[:,i:i+25,:]:
            av = 0
            av += i
            a /= 25.0
            awap_regrid = a
            count += 1 

#Regrid latitude - as above but use new longitude values

"""
2) Extract AWAP and ACCESS1.3 data points over Aus region (105 to 180 E, -50 to 0 N)
"""
#will need to change values according to AWAP grid bounds; can make smaller
accessAus = accessArray[:,56:96,32:72] #105 to 180 E, -50 to 0 N

#repeat for AWAP
#e.g.
#access = accessData.variables['pr']
#accessArray = np.reshape(access,(1872,145,192))


