import netCDF4 as n
import numpy as np
from metadata import cwdInFunction
from metadata import variables
from metadata import dataFile

cwdInFunction()

f = n.Dataset(dataFile,'r')

#print f.variables[d][1360][0][:]

#pr_time = data.variables['pr'][1700,:,:]
