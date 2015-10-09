"""
A file that defines cross-correlation functions for use in other scripts.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 October 2015.
"""
import netCDF4 as n
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
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
    A function to create cross-correlation charts.

    Parameters:
    -----------
    data1: the array that remains static (i.e. not shifted)
    data2: the array that is shifted
    units : string.  Units of time that are being plotted (e.g. months, years).
    """

    plt.xcorr(data1,data2,maxlags=None)
    plt.ylabel('Cross-correlation [-1,1]')
    plt.xlabel('Lag ('+units+')')
    plt.title(title)
    savefig(filename)
    plt.close()
    return
