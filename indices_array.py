"""
A file to import CSV index data and change it to a 2D NumPy array.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 September 2015.
"""

from cwd import cwdInFunction
import csv
import numpy as np

cwdInFunction()

def csv2array(filename):
    """
    A function to convert CSV index data to a NumPy array.
    
    Parameters:
    -----------
    Filename : specify the filepath of the CSV file to convert.
    """
    ind = open(filename,'rU')
    csvReader = csv.reader(ind)

    indx = []

    for row in csvReader:
        indx.append(row)
    ind.close()

    indx_array = np.array(indx)
    indx_array_tr = np.transpose(indx_array)
    index = indx_array_tr.astype(np.float)
    return index

Nino34 = csv2array('data/Nino3-4.csv')
TPI = csv2array('data/TPI.csv')
