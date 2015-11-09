"""
A file that defines cross-correlation functions for use in other scripts.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 October 2015.
"""
import netCDF4 as n
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
import math
from pylab import savefig
from cwd import cwdInFunction

cwdInFunction()


def xCorrel(array1,array2):
    """
    This function returns an array of cross correlations.  Higher absolute
    values indicate the highest correlation.  The default mode for
    numpy.correlated is 'full'/2.

    Parameters:
    -----------
    array1: the array that remains static (i.e. not shifted)
    array2: the array that is shifted
    """
    xcor = scipy.signal.correlate(array1,array2,'full')
    return xcor

def plotXCorrel(data1,data2,units,title,filename):
    """
    A function to create cross-correlation charts.  95%
    confidence intervals are generated: +- 2/sqrt(n)

    Parameters:
    -----------
    data1: the array that remains static (i.e. not shifted)
    data2: the array that is shifted
    units : string.  Units of time that are being plotted (e.g. months, years).
    """

    confid_int_a = 2.0/(math.sqrt(len(data1)))
    confid_int_b = -2.0/(math.sqrt(len(data1)))

    plt.xcorr(data1,data2,maxlags=None)
    plt.ylabel('Cross-correlation [-1,1]')
    plt.xlabel('Lag ('+units+')')
    plt.axhline(y = confid_int_a,ls='dashed')
    plt.axhline(y = confid_int_b,ls='dashed')
    plt.title(title)
    savefig(filename)
    plt.close()
    return
