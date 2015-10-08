"""
A function to compute statistical differences in means between two datasets
(usually observational (AWAP) and modelled (ACCESS R1, R2, R3) output)
by performing unpaired t-tests on independent samples.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 October 2015.
"""

import netCDF4 as n
import numpy as np
import scipy
from ENSO_IPO_corr import normal

from cwd import *
cwdInFunction()


def unpaired_t_test(array1,array2):
    """
    A function to test two independent samples for normality, test whether
    variances are equal or unequal, and return the two-tailed p-value for
    the null hypothesis that the means of the two samples are equal.
    """
    array1[np.isnan(array1)] = 0.0
    array2[np.isnan(array2)] = 0.0

    a = normal(array1) 
    b = normal(array2)

    if a or b <= 0.05:
    #If data is non-normal test for equality of variances with Levene's test.       
        levene = scipy.stats.levene(array1,array2)
        if levene[1] <= 0.05:
            #Unequal variances
            ttest = scipy.stats.ttest_ind(array1,array2,equal_var=False)
        else:
            #Equal variances
            ttest = scipy.stats.ttest_ind(array1,array2)
    else:
    #If data is normal, test for equality of variances with F test.
        F = scipy.var(array1)/scipy.var(array2)
        df1 = len(array1)-1
        df2 = len(array2)-1
        p_value = scipy.stats.f.cdf(F,df1,df2)

        if p_value <= 0.05:
            #Unequal variances
            ttest = scipy.stats.ttest_ind(array1,array2,equal_var=False)
        else:
            #Equal variances
            ttest = scipy.stats.ttest_ind(array1,array2,equal_var=False)

    p_value_ttest = ttest[1]
    
    return p_value_ttest
