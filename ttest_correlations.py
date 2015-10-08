"""
A file to compute statistical differences in means between observational (AWAP)
and modelled (ACCESS R1, R2, R3) output by performing unpaired t-tests on
independent samples.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 October 2015.
"""
from unpaired_t_test import *

from correlation_routine_awap import corrAverageENSO as awap_corrAverageENSO,\
     corrAverageEastENSO as awap_corrAverageEastENSO,corrAverageTPI as \
     awap_corrAverageTPI, corrAverageEastTPI as awap_corrAverageEastTPI

from correlation_routine_R1 import corrAverageENSO as R1_corrAverageENSO,\
     corrAverageEastENSO as R1_corrAverageEastENSO,corrAverageTPI as \
     R1_corrAverageTPI, corrAverageEastTPI as R1_corrAverageEastTPI

from correlation_routine_R2 import corrAverageENSO as R2_corrAverageENSO,\
     corrAverageEastENSO as R2_corrAverageEastENSO,corrAverageTPI as \
     R2_corrAverageTPI, corrAverageEastTPI as R2_corrAverageEastTPI

from correlation_routine_R3 import corrAverageENSO as R3_corrAverageENSO,\
     corrAverageEastENSO as R3_corrAverageEastENSO,corrAverageTPI as \
     R3_corrAverageTPI, corrAverageEastTPI as R3_corrAverageEastTPI

array_awap_corrAverageENSO = np.asarray(awap_corrAverageENSO)
array_awap_corrAverageTPI = np.asarray(awap_corrAverageTPI)
array_awap_corrAverageEastENSO = np.asarray(awap_corrAverageEastENSO)
array_awap_corrAverageEastTPI = np.asarray(awap_corrAverageEastTPI)

array_R1_corrAverageENSO = np.asarray(R1_corrAverageENSO)
array_R1_corrAverageTPI = np.asarray(R1_corrAverageTPI)
array_R1_corrAverageEastENSO = np.asarray(R1_corrAverageEastENSO)
array_R1_corrAverageEastTPI = np.asarray(R1_corrAverageEastTPI)

array_R2_corrAverageENSO = np.asarray(R2_corrAverageENSO)
array_R2_corrAverageTPI = np.asarray(R2_corrAverageTPI)
array_R2_corrAverageEastENSO = np.asarray(R2_corrAverageEastENSO)
array_R2_corrAverageEastTPI = np.asarray(R2_corrAverageEastTPI)

array_R3_corrAverageENSO = np.asarray(R3_corrAverageENSO)
array_R3_corrAverageTPI = np.asarray(R3_corrAverageTPI)
array_R3_corrAverageEastENSO = np.asarray(R3_corrAverageEastENSO)
array_R3_corrAverageEastTPI = np.asarray(R3_corrAverageEastTPI)

##############################################################################
#Significant difference from Australia or eastern Australia
##############################################################################

#ENSO

awap_ENSO_Aus_EAus = unpaired_t_test(array_awap_corrAverageENSO,array_awap_corrAverageEastENSO[:,0])
awap_ENSO_EAus_Equ = unpaired_t_test(array_awap_corrAverageEastENSO[:,0],array_awap_corrAverageEastENSO[:,1])
awap_ENSO_EAus_Trop = unpaired_t_test(array_awap_corrAverageEastENSO[:,0],array_awap_corrAverageEastENSO[:,2])
awap_ENSO_EAus_SubTrop = unpaired_t_test(array_awap_corrAverageEastENSO[:,0],array_awap_corrAverageEastENSO[:,3])
awap_ENSO_EAus_Des = unpaired_t_test(array_awap_corrAverageEastENSO[:,0],array_awap_corrAverageEastENSO[:,4])
awap_ENSO_EAus_Gr = unpaired_t_test(array_awap_corrAverageEastENSO[:,0],array_awap_corrAverageEastENSO[:,5])
awap_ENSO_EAus_Tem = unpaired_t_test(array_awap_corrAverageEastENSO[:,0],array_awap_corrAverageEastENSO[:,6])

awap_ENSO_regions = np.vstack((awap_ENSO_Aus_EAus,awap_ENSO_EAus_Equ,awap_ENSO_EAus_Trop,\
                                    awap_ENSO_EAus_SubTrop,awap_ENSO_EAus_Des,awap_ENSO_EAus_Gr,\
                                    awap_ENSO_EAus_Tem))

R1_ENSO_Aus_EAus = unpaired_t_test(array_R1_corrAverageENSO,array_R1_corrAverageEastENSO[:,0])
R1_ENSO_EAus_Equ = unpaired_t_test(array_R1_corrAverageEastENSO[:,0],array_R1_corrAverageEastENSO[:,1])
R1_ENSO_EAus_Trop = unpaired_t_test(array_R1_corrAverageEastENSO[:,0],array_R1_corrAverageEastENSO[:,2])
R1_ENSO_EAus_SubTrop = unpaired_t_test(array_R1_corrAverageEastENSO[:,0],array_R1_corrAverageEastENSO[:,3])
R1_ENSO_EAus_Des = unpaired_t_test(array_R1_corrAverageEastENSO[:,0],array_R1_corrAverageEastENSO[:,4])
R1_ENSO_EAus_Gr = unpaired_t_test(array_R1_corrAverageEastENSO[:,0],array_R1_corrAverageEastENSO[:,5])
R1_ENSO_EAus_Tem = unpaired_t_test(array_R1_corrAverageEastENSO[:,0],array_R1_corrAverageEastENSO[:,6])

R1_ENSO_regions = np.vstack((R1_ENSO_Aus_EAus,R1_ENSO_EAus_Equ,R1_ENSO_EAus_Trop,\
                                    R1_ENSO_EAus_SubTrop,R1_ENSO_EAus_Des,R1_ENSO_EAus_Gr,\
                                    R1_ENSO_EAus_Tem))

R2_ENSO_Aus_EAus = unpaired_t_test(array_R2_corrAverageENSO,array_R2_corrAverageEastENSO[:,0])
R2_ENSO_EAus_Equ = unpaired_t_test(array_R2_corrAverageEastENSO[:,0],array_R2_corrAverageEastENSO[:,1])
R2_ENSO_EAus_Trop = unpaired_t_test(array_R2_corrAverageEastENSO[:,0],array_R2_corrAverageEastENSO[:,2])
R2_ENSO_EAus_SubTrop = unpaired_t_test(array_R2_corrAverageEastENSO[:,0],array_R2_corrAverageEastENSO[:,3])
R2_ENSO_EAus_Des = unpaired_t_test(array_R2_corrAverageEastENSO[:,0],array_R2_corrAverageEastENSO[:,4])
R2_ENSO_EAus_Gr = unpaired_t_test(array_R2_corrAverageEastENSO[:,0],array_R2_corrAverageEastENSO[:,5])
R2_ENSO_EAus_Tem = unpaired_t_test(array_R2_corrAverageEastENSO[:,0],array_R2_corrAverageEastENSO[:,6])

R2_ENSO_regions = np.vstack((R2_ENSO_Aus_EAus,R2_ENSO_EAus_Equ,R2_ENSO_EAus_Trop,\
                                    R2_ENSO_EAus_SubTrop,R2_ENSO_EAus_Des,R2_ENSO_EAus_Gr,\
                                    R2_ENSO_EAus_Tem))

R3_ENSO_Aus_EAus = unpaired_t_test(array_R3_corrAverageENSO,array_R3_corrAverageEastENSO[:,0])
R3_ENSO_EAus_Equ = unpaired_t_test(array_R3_corrAverageEastENSO[:,0],array_R3_corrAverageEastENSO[:,1])
R3_ENSO_EAus_Trop = unpaired_t_test(array_R3_corrAverageEastENSO[:,0],array_R3_corrAverageEastENSO[:,2])
R3_ENSO_EAus_SubTrop = unpaired_t_test(array_R3_corrAverageEastENSO[:,0],array_R3_corrAverageEastENSO[:,3])
R3_ENSO_EAus_Des = unpaired_t_test(array_R3_corrAverageEastENSO[:,0],array_R3_corrAverageEastENSO[:,4])
R3_ENSO_EAus_Gr = unpaired_t_test(array_R3_corrAverageEastENSO[:,0],array_R3_corrAverageEastENSO[:,5])
R3_ENSO_EAus_Tem = unpaired_t_test(array_R3_corrAverageEastENSO[:,0],array_R3_corrAverageEastENSO[:,6])

R3_ENSO_regions = np.vstack((R3_ENSO_Aus_EAus,R3_ENSO_EAus_Equ,R3_ENSO_EAus_Trop,\
                                    R3_ENSO_EAus_SubTrop,R3_ENSO_EAus_Des,R3_ENSO_EAus_Gr,\
                                    R3_ENSO_EAus_Tem))

#TPI

awap_TPI_Aus_EAus = unpaired_t_test(array_awap_corrAverageTPI,array_awap_corrAverageEastTPI[:,0])
awap_TPI_EAus_Equ = unpaired_t_test(array_awap_corrAverageEastTPI[:,0],array_awap_corrAverageEastTPI[:,1])
awap_TPI_EAus_Trop = unpaired_t_test(array_awap_corrAverageEastTPI[:,0],array_awap_corrAverageEastTPI[:,2])
awap_TPI_EAus_SubTrop = unpaired_t_test(array_awap_corrAverageEastTPI[:,0],array_awap_corrAverageEastTPI[:,3])
awap_TPI_EAus_Des = unpaired_t_test(array_awap_corrAverageEastTPI[:,0],array_awap_corrAverageEastTPI[:,4])
awap_TPI_EAus_Gr = unpaired_t_test(array_awap_corrAverageEastTPI[:,0],array_awap_corrAverageEastTPI[:,5])
awap_TPI_EAus_Tem = unpaired_t_test(array_awap_corrAverageEastTPI[:,0],array_awap_corrAverageEastTPI[:,6])

awap_TPI_regions = np.vstack((awap_TPI_Aus_EAus,awap_TPI_EAus_Equ,awap_TPI_EAus_Trop,\
                                    awap_TPI_EAus_SubTrop,awap_TPI_EAus_Des,awap_TPI_EAus_Gr,\
                                    awap_TPI_EAus_Tem))

R1_TPI_Aus_EAus = unpaired_t_test(array_R1_corrAverageTPI,array_R1_corrAverageEastTPI[:,0])
R1_TPI_EAus_Equ = unpaired_t_test(array_R1_corrAverageEastTPI[:,0],array_R1_corrAverageEastTPI[:,1])
R1_TPI_EAus_Trop = unpaired_t_test(array_R1_corrAverageEastTPI[:,0],array_R1_corrAverageEastTPI[:,2])
R1_TPI_EAus_SubTrop = unpaired_t_test(array_R1_corrAverageEastTPI[:,0],array_R1_corrAverageEastTPI[:,3])
R1_TPI_EAus_Des = unpaired_t_test(array_R1_corrAverageEastTPI[:,0],array_R1_corrAverageEastTPI[:,4])
R1_TPI_EAus_Gr = unpaired_t_test(array_R1_corrAverageEastTPI[:,0],array_R1_corrAverageEastTPI[:,5])
R1_TPI_EAus_Tem = unpaired_t_test(array_R1_corrAverageEastTPI[:,0],array_R1_corrAverageEastTPI[:,6])

R1_TPI_regions = np.vstack((R1_TPI_Aus_EAus,R1_TPI_EAus_Equ,R1_TPI_EAus_Trop,\
                                    R1_TPI_EAus_SubTrop,R1_TPI_EAus_Des,R1_TPI_EAus_Gr,\
                                    R1_TPI_EAus_Tem))

R2_TPI_Aus_EAus = unpaired_t_test(array_R2_corrAverageTPI,array_R2_corrAverageEastTPI[:,0])
R2_TPI_EAus_Equ = unpaired_t_test(array_R2_corrAverageEastTPI[:,0],array_R2_corrAverageEastTPI[:,1])
R2_TPI_EAus_Trop = unpaired_t_test(array_R2_corrAverageEastTPI[:,0],array_R2_corrAverageEastTPI[:,2])
R2_TPI_EAus_SubTrop = unpaired_t_test(array_R2_corrAverageEastTPI[:,0],array_R2_corrAverageEastTPI[:,3])
R2_TPI_EAus_Des = unpaired_t_test(array_R2_corrAverageEastTPI[:,0],array_R2_corrAverageEastTPI[:,4])
R2_TPI_EAus_Gr = unpaired_t_test(array_R2_corrAverageEastTPI[:,0],array_R2_corrAverageEastTPI[:,5])
R2_TPI_EAus_Tem = unpaired_t_test(array_R2_corrAverageEastTPI[:,0],array_R2_corrAverageEastTPI[:,6])

R2_TPI_regions = np.vstack((R2_TPI_Aus_EAus,R2_TPI_EAus_Equ,R2_TPI_EAus_Trop,\
                                    R2_TPI_EAus_SubTrop,R2_TPI_EAus_Des,R2_TPI_EAus_Gr,\
                                    R2_TPI_EAus_Tem))

R3_TPI_Aus_EAus = unpaired_t_test(array_R3_corrAverageTPI,array_R3_corrAverageEastTPI[:,0])
R3_TPI_EAus_Equ = unpaired_t_test(array_R3_corrAverageEastTPI[:,0],array_R3_corrAverageEastTPI[:,1])
R3_TPI_EAus_Trop = unpaired_t_test(array_R3_corrAverageEastTPI[:,0],array_R3_corrAverageEastTPI[:,2])
R3_TPI_EAus_SubTrop = unpaired_t_test(array_R3_corrAverageEastTPI[:,0],array_R3_corrAverageEastTPI[:,3])
R3_TPI_EAus_Des = unpaired_t_test(array_R3_corrAverageEastTPI[:,0],array_R3_corrAverageEastTPI[:,4])
R3_TPI_EAus_Gr = unpaired_t_test(array_R3_corrAverageEastTPI[:,0],array_R3_corrAverageEastTPI[:,5])
R3_TPI_EAus_Tem = unpaired_t_test(array_R3_corrAverageEastTPI[:,0],array_R3_corrAverageEastTPI[:,6])

R3_TPI_regions = np.vstack((R3_TPI_Aus_EAus,R3_TPI_EAus_Equ,R3_TPI_EAus_Trop,\
                                    R3_TPI_EAus_SubTrop,R3_TPI_EAus_Des,R3_TPI_EAus_Gr,\
                                    R3_TPI_EAus_Tem))

#CSV

sig_diff_from_Aus = np.column_stack((awap_ENSO_regions,R1_ENSO_regions,\
                                     R2_ENSO_regions,R3_ENSO_regions,\
                                     awap_TPI_regions,R1_TPI_regions,\
                                     R2_TPI_regions,R3_TPI_regions))
np.savetxt('data/Correlation_coefficients/sig_diff_from_Aus.csv',sig_diff_from_Aus,delimiter=',')

##############################################################################
#Significant difference from AWAP
##############################################################################

#ENSO

awap_R1_Aus = unpaired_t_test(array_awap_corrAverageENSO,array_R1_corrAverageENSO)
awap_R1_EAus = unpaired_t_test(array_awap_corrAverageEastENSO[:,0],array_R1_corrAverageEastENSO[:,0])
awap_R1_Equ = unpaired_t_test(array_awap_corrAverageEastENSO[:,1],array_R1_corrAverageEastENSO[:,1])
awap_R1_Trop = unpaired_t_test(array_awap_corrAverageEastENSO[:,2],array_R1_corrAverageEastENSO[:,2])
awap_R1_SubTrop = unpaired_t_test(array_awap_corrAverageEastENSO[:,3],array_R1_corrAverageEastENSO[:,3])
awap_R1_Des = unpaired_t_test(array_awap_corrAverageEastENSO[:,4],array_R1_corrAverageEastENSO[:,4])
awap_R1_Gr = unpaired_t_test(array_awap_corrAverageEastENSO[:,5],array_R1_corrAverageEastENSO[:,5])
awap_R1_Tem = unpaired_t_test(array_awap_corrAverageEastENSO[:,6],array_R1_corrAverageEastENSO[:,6])

awap_R1_ENSO = np.vstack((awap_R1_Aus,awap_R1_EAus,awap_R1_Equ,\
                             awap_R1_Trop,awap_R1_SubTrop,awap_R1_Des,\
                             awap_R1_Gr,awap_R1_Tem))

awap_R2_Aus = unpaired_t_test(array_awap_corrAverageENSO,array_R2_corrAverageENSO)
awap_R2_EAus = unpaired_t_test(array_awap_corrAverageEastENSO[:,0],array_R2_corrAverageEastENSO[:,0])
awap_R2_Equ = unpaired_t_test(array_awap_corrAverageEastENSO[:,1],array_R2_corrAverageEastENSO[:,1])
awap_R2_Trop = unpaired_t_test(array_awap_corrAverageEastENSO[:,2],array_R2_corrAverageEastENSO[:,2])
awap_R2_SubTrop = unpaired_t_test(array_awap_corrAverageEastENSO[:,3],array_R2_corrAverageEastENSO[:,3])
awap_R2_Des = unpaired_t_test(array_awap_corrAverageEastENSO[:,4],array_R2_corrAverageEastENSO[:,4])
awap_R2_Gr = unpaired_t_test(array_awap_corrAverageEastENSO[:,5],array_R2_corrAverageEastENSO[:,5])
awap_R2_Tem = unpaired_t_test(array_awap_corrAverageEastENSO[:,6],array_R2_corrAverageEastENSO[:,6])

awap_R2_ENSO = np.vstack((awap_R2_Aus,awap_R2_EAus,awap_R2_Equ,\
                             awap_R2_Trop,awap_R2_SubTrop,awap_R2_Des,\
                             awap_R2_Gr,awap_R2_Tem))

awap_R3_Aus = unpaired_t_test(array_awap_corrAverageENSO,array_R3_corrAverageENSO)
awap_R3_EAus = unpaired_t_test(array_awap_corrAverageEastENSO[:,0],array_R3_corrAverageEastENSO[:,0])
awap_R3_Equ = unpaired_t_test(array_awap_corrAverageEastENSO[:,1],array_R3_corrAverageEastENSO[:,1])
awap_R3_Trop = unpaired_t_test(array_awap_corrAverageEastENSO[:,2],array_R3_corrAverageEastENSO[:,2])
awap_R3_SubTrop = unpaired_t_test(array_awap_corrAverageEastENSO[:,3],array_R3_corrAverageEastENSO[:,3])
awap_R3_Des = unpaired_t_test(array_awap_corrAverageEastENSO[:,4],array_R3_corrAverageEastENSO[:,4])
awap_R3_Gr = unpaired_t_test(array_awap_corrAverageEastENSO[:,5],array_R3_corrAverageEastENSO[:,5])
awap_R3_Tem = unpaired_t_test(array_awap_corrAverageEastENSO[:,6],array_R3_corrAverageEastENSO[:,6])

awap_R3_ENSO = np.vstack((awap_R3_Aus,awap_R3_EAus,awap_R3_Equ,\
                             awap_R3_Trop,awap_R3_SubTrop,awap_R3_Des,\
                             awap_R3_Gr,awap_R3_Tem))

#IPO

awap_R1_Aus = unpaired_t_test(array_awap_corrAverageTPI,array_R1_corrAverageTPI)
awap_R1_EAus = unpaired_t_test(array_awap_corrAverageEastTPI[:,0],array_R1_corrAverageEastTPI[:,0])
awap_R1_Equ = unpaired_t_test(array_awap_corrAverageEastTPI[:,1],array_R1_corrAverageEastTPI[:,1])
awap_R1_Trop = unpaired_t_test(array_awap_corrAverageEastTPI[:,2],array_R1_corrAverageEastTPI[:,2])
awap_R1_SubTrop = unpaired_t_test(array_awap_corrAverageEastTPI[:,3],array_R1_corrAverageEastTPI[:,3])
awap_R1_Des = unpaired_t_test(array_awap_corrAverageEastTPI[:,4],array_R1_corrAverageEastTPI[:,4])
awap_R1_Gr = unpaired_t_test(array_awap_corrAverageEastTPI[:,5],array_R1_corrAverageEastTPI[:,5])
awap_R1_Tem = unpaired_t_test(array_awap_corrAverageEastTPI[:,6],array_R1_corrAverageEastTPI[:,6])

awap_R1_IPO = np.vstack((awap_R1_Aus,awap_R1_EAus,awap_R1_Equ,\
                             awap_R1_Trop,awap_R1_SubTrop,awap_R1_Des,\
                             awap_R1_Gr,awap_R1_Tem))

awap_R2_Aus = unpaired_t_test(array_awap_corrAverageTPI,array_R2_corrAverageTPI)
awap_R2_EAus = unpaired_t_test(array_awap_corrAverageEastTPI[:,0],array_R2_corrAverageEastTPI[:,0])
awap_R2_Equ = unpaired_t_test(array_awap_corrAverageEastTPI[:,1],array_R2_corrAverageEastTPI[:,1])
awap_R2_Trop = unpaired_t_test(array_awap_corrAverageEastTPI[:,2],array_R2_corrAverageEastTPI[:,2])
awap_R2_SubTrop = unpaired_t_test(array_awap_corrAverageEastTPI[:,3],array_R2_corrAverageEastTPI[:,3])
awap_R2_Des = unpaired_t_test(array_awap_corrAverageEastTPI[:,4],array_R2_corrAverageEastTPI[:,4])
awap_R2_Gr = unpaired_t_test(array_awap_corrAverageEastTPI[:,5],array_R2_corrAverageEastTPI[:,5])
awap_R2_Tem = unpaired_t_test(array_awap_corrAverageEastTPI[:,6],array_R2_corrAverageEastTPI[:,6])

awap_R2_IPO = np.vstack((awap_R2_Aus,awap_R2_EAus,awap_R2_Equ,\
                             awap_R2_Trop,awap_R2_SubTrop,awap_R2_Des,\
                             awap_R2_Gr,awap_R2_Tem))

awap_R3_Aus = unpaired_t_test(array_awap_corrAverageTPI,array_R3_corrAverageTPI)
awap_R3_EAus = unpaired_t_test(array_awap_corrAverageEastTPI[:,0],array_R3_corrAverageEastTPI[:,0])
awap_R3_Equ = unpaired_t_test(array_awap_corrAverageEastTPI[:,1],array_R3_corrAverageEastTPI[:,1])
awap_R3_Trop = unpaired_t_test(array_awap_corrAverageEastTPI[:,2],array_R3_corrAverageEastTPI[:,2])
awap_R3_SubTrop = unpaired_t_test(array_awap_corrAverageEastTPI[:,3],array_R3_corrAverageEastTPI[:,3])
awap_R3_Des = unpaired_t_test(array_awap_corrAverageEastTPI[:,4],array_R3_corrAverageEastTPI[:,4])
awap_R3_Gr = unpaired_t_test(array_awap_corrAverageEastTPI[:,5],array_R3_corrAverageEastTPI[:,5])
awap_R3_Tem = unpaired_t_test(array_awap_corrAverageEastTPI[:,6],array_R3_corrAverageEastTPI[:,6])

awap_R3_IPO = np.vstack((awap_R3_Aus,awap_R3_EAus,awap_R3_Equ,\
                             awap_R3_Trop,awap_R3_SubTrop,awap_R3_Des,\
                             awap_R3_Gr,awap_R3_Tem))

sig_diff_from_AWAP = np.column_stack((awap_R1_ENSO,awap_R2_ENSO,\
                                     awap_R3_ENSO,awap_R1_IPO,\
                                     awap_R2_IPO,awap_R3_IPO))
np.savetxt('data/Correlation_coefficients/sig_diff_from_AWAP.csv',sig_diff_from_AWAP,delimiter=',')

##############################################################################
#Significant difference between ACCESS rounds
##############################################################################

#ENSO R1/R2

ENSO_R1_R2_Aus = unpaired_t_test(array_R1_corrAverageENSO,array_R2_corrAverageENSO)
ENSO_R1_R2_EAus = unpaired_t_test(array_R1_corrAverageEastENSO[:,0],array_R2_corrAverageEastENSO[:,0])
ENSO_R1_R2_Equ = unpaired_t_test(array_R1_corrAverageEastENSO[:,1],array_R2_corrAverageEastENSO[:,1])
ENSO_R1_R2_Trop = unpaired_t_test(array_R1_corrAverageEastENSO[:,2],array_R2_corrAverageEastENSO[:,2])
ENSO_R1_R2_SubTrop = unpaired_t_test(array_R1_corrAverageEastENSO[:,3],array_R2_corrAverageEastENSO[:,3])
ENSO_R1_R2_Des = unpaired_t_test(array_R1_corrAverageEastENSO[:,4],array_R2_corrAverageEastENSO[:,4])
ENSO_R1_R2_Gr = unpaired_t_test(array_R1_corrAverageEastENSO[:,5],array_R2_corrAverageEastENSO[:,5])
ENSO_R1_R2_Tem = unpaired_t_test(array_R1_corrAverageEastENSO[:,6],array_R2_corrAverageEastENSO[:,6])

ENSO_R1_R2 = np.vstack((ENSO_R1_R2_Aus,ENSO_R1_R2_EAus,\
                        ENSO_R1_R2_Equ,ENSO_R1_R2_Trop,\
                        ENSO_R1_R2_SubTrop,ENSO_R1_R2_Des,\
                        ENSO_R1_R2_Gr,ENSO_R1_R2_Tem))
                        
#ENSO R1/R3

ENSO_R1_R3_Aus = unpaired_t_test(array_R1_corrAverageENSO,array_R3_corrAverageENSO)
ENSO_R1_R3_EAus = unpaired_t_test(array_R1_corrAverageEastENSO[:,0],array_R3_corrAverageEastENSO[:,0])
ENSO_R1_R3_Equ = unpaired_t_test(array_R1_corrAverageEastENSO[:,1],array_R3_corrAverageEastENSO[:,1])
ENSO_R1_R3_Trop = unpaired_t_test(array_R1_corrAverageEastENSO[:,2],array_R3_corrAverageEastENSO[:,2])
ENSO_R1_R3_SubTrop = unpaired_t_test(array_R1_corrAverageEastENSO[:,3],array_R3_corrAverageEastENSO[:,3])
ENSO_R1_R3_Des = unpaired_t_test(array_R1_corrAverageEastENSO[:,4],array_R3_corrAverageEastENSO[:,4])
ENSO_R1_R3_Gr = unpaired_t_test(array_R1_corrAverageEastENSO[:,5],array_R3_corrAverageEastENSO[:,5])
ENSO_R1_R3_Tem = unpaired_t_test(array_R1_corrAverageEastENSO[:,6],array_R3_corrAverageEastENSO[:,6])

ENSO_R1_R3 = np.vstack((ENSO_R1_R3_Aus,ENSO_R1_R3_EAus,\
                        ENSO_R1_R3_Equ,ENSO_R1_R3_Trop,\
                        ENSO_R1_R3_SubTrop,ENSO_R1_R3_Des,\
                        ENSO_R1_R3_Gr,ENSO_R1_R3_Tem))

#ENSO R2/R3

ENSO_R2_R3_Aus = unpaired_t_test(array_R2_corrAverageENSO,array_R3_corrAverageENSO)
ENSO_R2_R3_EAus = unpaired_t_test(array_R2_corrAverageEastENSO[:,0],array_R3_corrAverageEastENSO[:,0])
ENSO_R2_R3_Equ = unpaired_t_test(array_R2_corrAverageEastENSO[:,1],array_R3_corrAverageEastENSO[:,1])
ENSO_R2_R3_Trop = unpaired_t_test(array_R2_corrAverageEastENSO[:,2],array_R3_corrAverageEastENSO[:,2])
ENSO_R2_R3_SubTrop = unpaired_t_test(array_R2_corrAverageEastENSO[:,3],array_R3_corrAverageEastENSO[:,3])
ENSO_R2_R3_Des = unpaired_t_test(array_R2_corrAverageEastENSO[:,4],array_R3_corrAverageEastENSO[:,4])
ENSO_R2_R3_Gr = unpaired_t_test(array_R2_corrAverageEastENSO[:,5],array_R3_corrAverageEastENSO[:,5])
ENSO_R2_R3_Tem = unpaired_t_test(array_R2_corrAverageEastENSO[:,6],array_R3_corrAverageEastENSO[:,6])

ENSO_R2_R3 = np.vstack((ENSO_R2_R3_Aus,ENSO_R2_R3_EAus,\
                        ENSO_R2_R3_Equ,ENSO_R2_R3_Trop,\
                        ENSO_R2_R3_SubTrop,ENSO_R2_R3_Des,\
                        ENSO_R2_R3_Gr,ENSO_R2_R3_Tem))

#TPI R1/R2

TPI_R1_R2_Aus = unpaired_t_test(array_R1_corrAverageTPI,array_R2_corrAverageTPI)
TPI_R1_R2_EAus = unpaired_t_test(array_R1_corrAverageEastTPI[:,0],array_R2_corrAverageEastTPI[:,0])
TPI_R1_R2_Equ = unpaired_t_test(array_R1_corrAverageEastTPI[:,1],array_R2_corrAverageEastTPI[:,1])
TPI_R1_R2_Trop = unpaired_t_test(array_R1_corrAverageEastTPI[:,2],array_R2_corrAverageEastTPI[:,2])
TPI_R1_R2_SubTrop = unpaired_t_test(array_R1_corrAverageEastTPI[:,3],array_R2_corrAverageEastTPI[:,3])
TPI_R1_R2_Des = unpaired_t_test(array_R1_corrAverageEastTPI[:,4],array_R2_corrAverageEastTPI[:,4])
TPI_R1_R2_Gr = unpaired_t_test(array_R1_corrAverageEastTPI[:,5],array_R2_corrAverageEastTPI[:,5])
TPI_R1_R2_Tem = unpaired_t_test(array_R1_corrAverageEastTPI[:,6],array_R2_corrAverageEastTPI[:,6])

TPI_R1_R2 = np.vstack((TPI_R1_R2_Aus,TPI_R1_R2_EAus,\
                        TPI_R1_R2_Equ,TPI_R1_R2_Trop,\
                        TPI_R1_R2_SubTrop,TPI_R1_R2_Des,\
                        TPI_R1_R2_Gr,TPI_R1_R2_Tem))

#TPI R1/R3

TPI_R1_R3_Aus = unpaired_t_test(array_R1_corrAverageTPI,array_R3_corrAverageTPI)
TPI_R1_R3_EAus = unpaired_t_test(array_R1_corrAverageEastTPI[:,0],array_R3_corrAverageEastTPI[:,0])
TPI_R1_R3_Equ = unpaired_t_test(array_R1_corrAverageEastTPI[:,1],array_R3_corrAverageEastTPI[:,1])
TPI_R1_R3_Trop = unpaired_t_test(array_R1_corrAverageEastTPI[:,2],array_R3_corrAverageEastTPI[:,2])
TPI_R1_R3_SubTrop = unpaired_t_test(array_R1_corrAverageEastTPI[:,3],array_R3_corrAverageEastTPI[:,3])
TPI_R1_R3_Des = unpaired_t_test(array_R1_corrAverageEastTPI[:,4],array_R3_corrAverageEastTPI[:,4])
TPI_R1_R3_Gr = unpaired_t_test(array_R1_corrAverageEastTPI[:,5],array_R3_corrAverageEastTPI[:,5])
TPI_R1_R3_Tem = unpaired_t_test(array_R1_corrAverageEastTPI[:,6],array_R3_corrAverageEastTPI[:,6])

TPI_R1_R3 = np.vstack((TPI_R1_R3_Aus,TPI_R1_R3_EAus,\
                        TPI_R1_R3_Equ,TPI_R1_R3_Trop,\
                        TPI_R1_R3_SubTrop,TPI_R1_R3_Des,\
                        TPI_R1_R3_Gr,TPI_R1_R3_Tem))

#TPI R2/R3

TPI_R2_R3_Aus = unpaired_t_test(array_R2_corrAverageTPI,array_R3_corrAverageTPI)
TPI_R2_R3_EAus = unpaired_t_test(array_R2_corrAverageEastTPI[:,0],array_R3_corrAverageEastTPI[:,0])
TPI_R2_R3_Equ = unpaired_t_test(array_R2_corrAverageEastTPI[:,1],array_R3_corrAverageEastTPI[:,1])
TPI_R2_R3_Trop = unpaired_t_test(array_R2_corrAverageEastTPI[:,2],array_R3_corrAverageEastTPI[:,2])
TPI_R2_R3_SubTrop = unpaired_t_test(array_R2_corrAverageEastTPI[:,3],array_R3_corrAverageEastTPI[:,3])
TPI_R2_R3_Des = unpaired_t_test(array_R2_corrAverageEastTPI[:,4],array_R3_corrAverageEastTPI[:,4])
TPI_R2_R3_Gr = unpaired_t_test(array_R2_corrAverageEastTPI[:,5],array_R3_corrAverageEastTPI[:,5])
TPI_R2_R3_Tem = unpaired_t_test(array_R2_corrAverageEastTPI[:,6],array_R3_corrAverageEastTPI[:,6])

TPI_R2_R3 = np.vstack((TPI_R2_R3_Aus,TPI_R2_R3_EAus,\
                        TPI_R2_R3_Equ,TPI_R2_R3_Trop,\
                        TPI_R2_R3_SubTrop,TPI_R2_R3_Des,\
                        TPI_R2_R3_Gr,TPI_R2_R3_Tem))

sig_diff_from_ACCESS = np.column_stack((ENSO_R1_R2,ENSO_R1_R3,\
                                        ENSO_R2_R3,TPI_R1_R2,
                                        TPI_R1_R3,TPI_R2_R3))
np.savetxt('data/Correlation_coefficients/sig_diff_from_ACCESS.csv',sig_diff_from_ACCESS,delimiter=',')
