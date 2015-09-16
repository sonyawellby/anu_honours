"""
Set of routines to stratify ENSO/IPO and rainfall data
for composite analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 15 September 2015.
"""
import numpy as np
import numpy.ma as ma

from enso_csv import posHad,negHad,neutralHad, posR1,negR1,neutralR1,\
     posR2,negR2,neutralR2,posR3,negR3,neutralR3

import access_trimmed

from cwd import cwdInFunction
cwdInFunction()

def stratify(rainfall,index):
    copy = rainfall
    count = 0
    while count < len(rainfall):
        for i in index:
            if index[count] == True:
                ma.masked_equal(copy[count],True)
            else:
                pass
            count += 0
    return copy

"""
def stratify(dataset):

    blank = np.zeros(1260)
    for i in blank:
        if i in dataset == False:
            blank[i] == 1
        else:
            pass
    return blank
"""
