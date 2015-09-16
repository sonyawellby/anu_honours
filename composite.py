"""
Set of routines to stratify ENSO/IPO and rainfall data
for composite analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 15 September 2015.
"""
import numpy as np

from enso_csv import posHad,negHad,neutralHad, posR1,negR1,neutralR1,\
     posR2,negR2,neutralR2,posR3,negR3,neutralR3

import access_trimmed

from cwd import cwdInFunction
cwdInFunction()

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
