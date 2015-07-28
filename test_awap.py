import os
os.chdir("/home/sonya/Documents/")
print os.getcwd()

import netCDF4 as n
import numpy as np

f = n.Dataset('AWAP_nc/AWAP_Run26j_precip/ann_Precip_19001231_v1.nc','r')
