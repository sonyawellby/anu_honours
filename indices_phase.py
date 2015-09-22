"""
Set of routines to define ENSO/IPO index data according to oscillation phase.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 22 September 2015.
"""
import numpy as np
import numpy.ma as ma

import enso_csv
import tpi_csv

def index2years(data):
    """
    A function to return index data (with length 1260) as yearly data
    (length 105).
    """
    Jun = data[0::12]
    Jul = data[1::12]
    Aug = data[2::12]
    Sep = data[3::12]
    Oct = data[4::12]
    Nov = data[5::12]
    Dec = data[6::12]
    Jan = data[7::12]
    Feb = data[8::12]
    Mar = data[9::12]
    Apr = data[10::12]
    May = data[11::12]
    
    return Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May

"""
ENSO phases
"""
#HadISST data

ENSO_posHad = index2years(enso_csv.posHad)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_posHad
ENSO_posHad_Jun = Jun
ENSO_posHad_Jul = Jul
ENSO_posHad_Aug = Aug
ENSO_posHad_Sep = Sep
ENSO_posHad_Oct = Oct
ENSO_posHad_Nov = Nov
ENSO_posHad_Dec = Dec
ENSO_posHad_Jan = Jan
ENSO_posHad_Feb = Feb
ENSO_posHad_Mar = Mar
ENSO_posHad_Apr = Apr
ENSO_posHad_May = May
ENSO_posHad_JJA = enso_csv.ENSOpos_JJA_Had
ENSO_posHad_SON = enso_csv.ENSOpos_SON_Had
ENSO_posHad_DJF = enso_csv.ENSOpos_DJF_Had
ENSO_posHad_MAM = enso_csv.ENSOpos_MAM_Had
ENSO_posHad_annual = enso_csv.ENSOpos_Annual_Had

ENSO_negHad = index2years(enso_csv.negHad)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_negHad
ENSO_negHad_Jun = Jun
ENSO_negHad_Jul = Jul
ENSO_negHad_Aug = Aug
ENSO_negHad_Sep = Sep
ENSO_negHad_Oct = Oct
ENSO_negHad_Nov = Nov
ENSO_negHad_Dec = Dec
ENSO_negHad_Jan = Jan
ENSO_negHad_Feb = Feb
ENSO_negHad_Mar = Mar
ENSO_negHad_Apr = Apr
ENSO_negHad_May = May
ENSO_negHad_JJA = enso_csv.ENSOneg_JJA_Had
ENSO_negHad_SON = enso_csv.ENSOneg_SON_Had
ENSO_negHad_DJF = enso_csv.ENSOneg_DJF_Had
ENSO_negHad_MAM = enso_csv.ENSOneg_MAM_Had
ENSO_negHad_annual = enso_csv.ENSOneg_Annual_Had

ENSO_neutralHad = index2years(enso_csv.neutralHad)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_neutralHad
ENSO_neutralHad_Jun = Jun
ENSO_neutralHad_Jul = Jul
ENSO_neutralHad_Aug = Aug
ENSO_neutralHad_Sep = Sep
ENSO_neutralHad_Oct = Oct
ENSO_neutralHad_Nov = Nov
ENSO_neutralHad_Dec = Dec
ENSO_neutralHad_Jan = Jan
ENSO_neutralHad_Feb = Feb
ENSO_neutralHad_Mar = Mar
ENSO_neutralHad_Apr = Apr
ENSO_neutralHad_May = May
ENSO_neutralHad_JJA = enso_csv.ENSOneutral_JJA_Had
ENSO_neutralHad_SON = enso_csv.ENSOneutral_SON_Had
ENSO_neutralHad_DJF = enso_csv.ENSOneutral_DJF_Had
ENSO_neutralHad_MAM = enso_csv.ENSOneutral_MAM_Had
ENSO_neutralHad_annual = enso_csv.ENSOneutral_Annual_Had

#ACCESS R1

ENSO_posR1 = index2years(enso_csv.posR1)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_posR1

ENSO_posR1_Jun = Jun
ENSO_posR1_Jul = Jul
ENSO_posR1_Aug = Aug
ENSO_posR1_Sep = Sep
ENSO_posR1_Oct = Oct
ENSO_posR1_Nov = Nov
ENSO_posR1_Dec = Dec
ENSO_posR1_Jan = Jan
ENSO_posR1_Feb = Feb
ENSO_posR1_Mar = Mar
ENSO_posR1_Apr = Apr
ENSO_posR1_May = May
ENSO_posR1_JJA = enso_csv.ENSOpos_JJA_R1
ENSO_posR1_SON = enso_csv.ENSOpos_SON_R1
ENSO_posR1_DJF = enso_csv.ENSOpos_DJF_R1
ENSO_posR1_MAM = enso_csv.ENSOpos_MAM_R1
ENSO_posR1_annual = enso_csv.ENSOpos_Annual_R1

ENSO_negR1 = index2years(enso_csv.negR1)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_negR1
ENSO_negR1_Jun = Jun
ENSO_negR1_Jul = Jul
ENSO_negR1_Aug = Aug
ENSO_negR1_Sep = Sep
ENSO_negR1_Oct = Oct
ENSO_negR1_Nov = Nov
ENSO_negR1_Dec = Dec
ENSO_negR1_Jan = Jan
ENSO_negR1_Feb = Feb
ENSO_negR1_Mar = Mar
ENSO_negR1_Apr = Apr
ENSO_negR1_May = May
ENSO_negR1_JJA = enso_csv.ENSOneg_JJA_R1
ENSO_negR1_SON = enso_csv.ENSOneg_SON_R1
ENSO_negR1_DJF = enso_csv.ENSOpos_DJF_R1
ENSO_negR1_MAM = enso_csv.ENSOpos_MAM_R1
ENSO_negR1_annual = enso_csv.ENSOneg_Annual_R1

ENSO_neutralR1 = index2years(enso_csv.neutralR1)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_neutralR1
ENSO_neutralR1_Jun = Jun
ENSO_neutralR1_Jul = Jul
ENSO_neutralR1_Aug = Aug
ENSO_neutralR1_Sep = Sep
ENSO_neutralR1_Oct = Oct
ENSO_neutralR1_Nov = Nov
ENSO_neutralR1_Dec = Dec
ENSO_neutralR1_Jan = Jan
ENSO_neutralR1_Feb = Feb
ENSO_neutralR1_Mar = Mar
ENSO_neutralR1_Apr = Apr
ENSO_neutralR1_May = May
ENSO_neutralR1_JJA = enso_csv.ENSOneutral_JJA_R1
ENSO_neutralR1_SON = enso_csv.ENSOneutral_SON_R1
ENSO_neutralR1_DJF = enso_csv.ENSOneutral_DJF_R1
ENSO_neutralR1_MAM = enso_csv.ENSOneutral_MAM_R1
ENSO_neutralR1_annual = enso_csv.ENSOneutral_Annual_R1

#ACCESS R2
ENSO_posR2 = index2years(enso_csv.posR2)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_posR2
ENSO_posR2_Jun = Jun
ENSO_posR2_Jul = Jul
ENSO_posR2_Aug = Aug
ENSO_posR2_Sep = Sep
ENSO_posR2_Oct = Oct
ENSO_posR2_Nov = Nov
ENSO_posR2_Dec = Dec
ENSO_posR2_Jan = Jan
ENSO_posR2_Feb = Feb
ENSO_posR2_Mar = Mar
ENSO_posR2_Apr = Apr
ENSO_posR2_May = May
ENSO_posR2_JJA = enso_csv.ENSOpos_JJA_R2
ENSO_posR2_SON = enso_csv.ENSOpos_SON_R2
ENSO_posR2_DJF = enso_csv.ENSOpos_DJF_R2
ENSO_posR2_MAM = enso_csv.ENSOpos_MAM_R2
ENSO_posR2_annual = enso_csv.ENSOpos_Annual_R2

ENSO_negR2 = index2years(enso_csv.negR2)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_negR2
ENSO_negR2_Jun = Jun
ENSO_negR2_Jul = Jul
ENSO_negR2_Aug = Aug
ENSO_negR2_Sep = Sep
ENSO_negR2_Oct = Oct
ENSO_negR2_Nov = Nov
ENSO_negR2_Dec = Dec
ENSO_negR2_Jan = Jan
ENSO_negR2_Feb = Feb
ENSO_negR2_Mar = Mar
ENSO_negR2_Apr = Apr
ENSO_negR2_May = May
ENSO_negR2_JJA = enso_csv.ENSOneg_JJA_R2
ENSO_negR2_SON = enso_csv.ENSOneg_SON_R2
ENSO_negR2_DJF = enso_csv.ENSOneg_DJF_R2
ENSO_negR2_MAM = enso_csv.ENSOneg_MAM_R2
ENSO_negR2_annual = enso_csv.ENSOneg_Annual_R2

ENSO_neutralR2 = index2years(enso_csv.neutralR2)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_neutralR2
ENSO_neutralR2_Jun = Jun
ENSO_neutralR2_Jul = Jul
ENSO_neutralR2_Aug = Aug
ENSO_neutralR2_Sep = Sep
ENSO_neutralR2_Oct = Oct
ENSO_neutralR2_Nov = Nov
ENSO_neutralR2_Dec = Dec
ENSO_neutralR2_Jan = Jan
ENSO_neutralR2_Feb = Feb
ENSO_neutralR2_Mar = Mar
ENSO_neutralR2_Apr = Apr
ENSO_neutralR2_May = May
ENSO_neutralR2_JJA = enso_csv.ENSOneutral_JJA_R2
ENSO_neutralR2_SON = enso_csv.ENSOneutral_SON_R2
ENSO_neutralR2_DJF = enso_csv.ENSOneutral_DJF_R2
ENSO_neutralR2_MAM = enso_csv.ENSOneutral_MAM_R2
ENSO_neutralR2_annual = enso_csv.ENSOneutral_Annual_R2

#ACCESS R3

ENSO_posR3 = index2years(enso_csv.posR3)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_posR3
ENSO_posR3_Jun = Jun
ENSO_posR3_Jul = Jul
ENSO_posR3_Aug = Aug
ENSO_posR3_Sep = Sep
ENSO_posR3_Oct = Oct
ENSO_posR3_Nov = Nov
ENSO_posR3_Dec = Dec
ENSO_posR3_Jan = Jan
ENSO_posR3_Feb = Feb
ENSO_posR3_Mar = Mar
ENSO_posR3_Apr = Apr
ENSO_posR3_May = May
ENSO_posR3_JJA = enso_csv.ENSOpos_JJA_R3
ENSO_posR3_SON = enso_csv.ENSOpos_SON_R3
ENSO_posR3_DJF = enso_csv.ENSOpos_DJF_R3
ENSO_posR3_MAM = enso_csv.ENSOpos_MAM_R3
ENSO_posR3_annual = enso_csv.ENSOpos_Annual_R3

ENSO_negR3 = index2years(enso_csv.negR3)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_negR3
ENSO_negR3_Jun = Jun
ENSO_negR3_Jul = Jul
ENSO_negR3_Aug = Aug
ENSO_negR3_Sep = Sep
ENSO_negR3_Oct = Oct
ENSO_negR3_Nov = Nov
ENSO_negR3_Dec = Dec
ENSO_negR3_Jan = Jan
ENSO_negR3_Feb = Feb
ENSO_negR3_Mar = Mar
ENSO_negR3_Apr = Apr
ENSO_negR3_May = May
ENSO_negR3_JJA = enso_csv.ENSOneg_JJA_R3
ENSO_negR3_SON = enso_csv.ENSOneg_SON_R3
ENSO_negR3_DJF = enso_csv.ENSOneg_DJF_R3
ENSO_negR3_MAM = enso_csv.ENSOneg_MAM_R3
ENSO_negR3_annual = enso_csv.ENSOneg_Annual_R3

ENSO_neutralR3 = index2years(enso_csv.neutralR3)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = ENSO_neutralR3
ENSO_neutralR3_Jun = Jun
ENSO_neutralR3_Jul = Jul
ENSO_neutralR3_Aug = Aug
ENSO_neutralR3_Sep = Sep
ENSO_neutralR3_Oct = Oct
ENSO_neutralR3_Nov = Nov
ENSO_neutralR3_Dec = Dec
ENSO_neutralR3_Jan = Jan
ENSO_neutralR3_Feb = Feb
ENSO_neutralR3_Mar = Mar
ENSO_neutralR3_Apr = Apr
ENSO_neutralR3_May = May
ENSO_neutralR3_JJA = enso_csv.ENSOneutral_JJA_R3
ENSO_neutralR3_SON = enso_csv.ENSOneutral_SON_R3
ENSO_neutralR3_DJF = enso_csv.ENSOneutral_DJF_R3
ENSO_neutralR3_MAM = enso_csv.ENSOneutral_MAM_R3
ENSO_neutralR3_annual = enso_csv.ENSOneutral_Annual_R3

"""
IPO phases
"""

#HadISST
IPO_posHad = index2years(tpi_csv.posHad)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_posHad
IPO_posHad_Jun = Jun
IPO_posHad_Jul = Jul
IPO_posHad_Aug = Aug
IPO_posHad_Sep = Sep
IPO_posHad_Oct = Oct
IPO_posHad_Nov = Nov
IPO_posHad_Dec = Dec
IPO_posHad_Jan = Jan
IPO_posHad_Feb = Feb
IPO_posHad_Mar = Mar
IPO_posHad_Apr = Apr
IPO_posHad_May = May
IPO_posHad_JJA = tpi_csv.Had_IPOpos_JJA
IPO_posHad_SON = tpi_csv.Had_IPOpos_SON
IPO_posHad_DJF = tpi_csv.Had_IPOpos_DJF
IPO_posHad_MAM = tpi_csv.Had_IPOpos_MAM
IPO_posHad_annual = tpi_csv.Had_IPOpos_Annual

IPO_negHad = index2years(tpi_csv.negHad)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_negHad
IPO_negHad_Jun = Jun
IPO_negHad_Jul = Jul
IPO_negHad_Aug = Aug
IPO_negHad_Sep = Sep
IPO_negHad_Oct = Oct
IPO_negHad_Nov = Nov
IPO_negHad_Dec = Dec
IPO_negHad_Jan = Jan
IPO_negHad_Feb = Feb
IPO_negHad_Mar = Mar
IPO_negHad_Apr = Apr
IPO_negHad_May = May
IPO_negHad_JJA = tpi_csv.Had_IPOneg_JJA
IPO_negHad_SON = tpi_csv.Had_IPOneg_SON
IPO_negHad_DJF = tpi_csv.Had_IPOneg_DJF
IPO_negHad_MAM = tpi_csv.Had_IPOneg_MAM
IPO_negHad_annual = tpi_csv.Had_IPOneg_Annual

IPO_neutralHad = index2years(tpi_csv.neutralHad)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_neutralHad
IPO_neutralHad_Jun = Jun
IPO_neutralHad_Jul = Jul
IPO_neutralHad_Aug = Aug
IPO_neutralHad_Sep = Sep
IPO_neutralHad_Oct = Oct
IPO_neutralHad_Nov = Nov
IPO_neutralHad_Dec = Dec
IPO_neutralHad_Jan = Jan
IPO_neutralHad_Feb = Feb
IPO_neutralHad_Mar = Mar
IPO_neutralHad_Apr = Apr
IPO_neutralHad_May = May
IPO_neutralHad_JJA = tpi_csv.Had_IPOneutral_JJA
IPO_neutralHad_SON = tpi_csv.Had_IPOneutral_SON
IPO_neutralHad_DJF = tpi_csv.Had_IPOneutral_DJF
IPO_neutralHad_MAM = tpi_csv.Had_IPOneutral_MAM
IPO_neutralHad_annual = tpi_csv.Had_IPOneutral_Annual

#ACCESS R1

IPO_posR1 = index2years(tpi_csv.posR1)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_posR1
IPO_posR1_Jun = Jun
IPO_posR1_Jul = Jul
IPO_posR1_Aug = Aug
IPO_posR1_Sep = Sep
IPO_posR1_Oct = Oct
IPO_posR1_Nov = Nov
IPO_posR1_Dec = Dec
IPO_posR1_Jan = Jan
IPO_posR1_Feb = Feb
IPO_posR1_Mar = Mar
IPO_posR1_Apr = Apr
IPO_posR1_May = May
IPO_posR1_JJA = tpi_csv.R1_IPOpos_JJA
IPO_posR1_SON = tpi_csv.R1_IPOpos_SON
IPO_posR1_DJF = tpi_csv.R1_IPOpos_DJF
IPO_posR1_MAM = tpi_csv.R1_IPOpos_MAM
IPO_posR1_annual = tpi_csv.R1_IPOpos_Annual

IPO_negR1 = index2years(tpi_csv.negR1)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_negR1
IPO_negR1_Jun = Jun
IPO_negR1_Jul = Jul
IPO_negR1_Aug = Aug
IPO_negR1_Sep = Sep
IPO_negR1_Oct = Oct
IPO_negR1_Nov = Nov
IPO_negR1_Dec = Dec
IPO_negR1_Jan = Jan
IPO_negR1_Feb = Feb
IPO_negR1_Mar = Mar
IPO_negR1_Apr = Apr
IPO_negR1_May = May
IPO_negR1_JJA = tpi_csv.R1_IPOneg_JJA
IPO_negR1_SON = tpi_csv.R1_IPOneg_SON
IPO_negR1_DJF = tpi_csv.R1_IPOneg_DJF
IPO_negR1_MAM = tpi_csv.R1_IPOneg_MAM
IPO_negR1_annual = tpi_csv.R1_IPOneg_Annual

IPO_neutralR1 = index2years(tpi_csv.neutralR1)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_neutralR1
IPO_neutralR1_Jun = Jun
IPO_neutralR1_Jul = Jul
IPO_neutralR1_Aug = Aug
IPO_neutralR1_Sep = Sep
IPO_neutralR1_Oct = Oct
IPO_neutralR1_Nov = Nov
IPO_neutralR1_Dec = Dec
IPO_neutralR1_Jan = Jan
IPO_neutralR1_Feb = Feb
IPO_neutralR1_Mar = Mar
IPO_neutralR1_Apr = Apr
IPO_neutralR1_May = May
IPO_neutralR1_JJA = tpi_csv.R1_IPOneutral_JJA
IPO_neutralR1_SON = tpi_csv.R1_IPOneutral_SON
IPO_neutralR1_DJF = tpi_csv.R1_IPOneutral_DJF
IPO_neutralR1_MAM = tpi_csv.R1_IPOneutral_MAM
IPO_neutralR1_annual = tpi_csv.R1_IPOneutral_Annual

#ACCESS R2

IPO_posR2 = index2years(tpi_csv.posR2)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_posR2
IPO_posR2_Jun = Jun
IPO_posR2_Jul = Jul
IPO_posR2_Aug = Aug
IPO_posR2_Sep = Sep
IPO_posR2_Oct = Oct
IPO_posR2_Nov = Nov
IPO_posR2_Dec = Dec
IPO_posR2_Jan = Jan
IPO_posR2_Feb = Feb
IPO_posR2_Mar = Mar
IPO_posR2_Apr = Apr
IPO_posR2_May = May
IPO_posR2_JJA = tpi_csv.R2_IPOpos_JJA
IPO_posR2_SON = tpi_csv.R2_IPOpos_SON
IPO_posR2_DJF = tpi_csv.R2_IPOpos_DJF
IPO_posR2_MAM = tpi_csv.R2_IPOpos_MAM
IPO_posR2_annual = tpi_csv.R2_IPOpos_Annual

IPO_negR2 = index2years(tpi_csv.negR2)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_negR2
IPO_negR2_Jun = Jun
IPO_negR2_Jul = Jul
IPO_negR2_Aug = Aug
IPO_negR2_Sep = Sep
IPO_negR2_Oct = Oct
IPO_negR2_Nov = Nov
IPO_negR2_Dec = Dec
IPO_negR2_Jan = Jan
IPO_negR2_Feb = Feb
IPO_negR2_Mar = Mar
IPO_negR2_Apr = Apr
IPO_negR2_May = May
IPO_negR2_JJA = tpi_csv.R2_IPOneg_JJA
IPO_negR2_SON = tpi_csv.R2_IPOneg_SON
IPO_negR2_DJF = tpi_csv.R2_IPOneg_DJF
IPO_negR2_MAM = tpi_csv.R2_IPOneg_MAM
IPO_negR2_annual = tpi_csv.R2_IPOneg_Annual

IPO_neutralR2 = index2years(tpi_csv.neutralR2)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_neutralR2
IPO_neutralR2_Jun = Jun
IPO_neutralR2_Jul = Jul
IPO_neutralR2_Aug = Aug
IPO_neutralR2_Sep = Sep
IPO_neutralR2_Oct = Oct
IPO_neutralR2_Nov = Nov
IPO_neutralR2_Dec = Dec
IPO_neutralR2_Jan = Jan
IPO_neutralR2_Feb = Feb
IPO_neutralR2_Mar = Mar
IPO_neutralR2_Apr = Apr
IPO_neutralR2_May = May
IPO_neutralR2_JJA = tpi_csv.R2_IPOneutral_JJA
IPO_neutralR2_SON = tpi_csv.R2_IPOneutral_SON
IPO_neutralR2_DJF = tpi_csv.R2_IPOneutral_DJF
IPO_neutralR2_MAM = tpi_csv.R2_IPOneutral_MAM
IPO_neutralR2_annual = tpi_csv.R2_IPOneutral_Annual

#ACCESS R3

IPO_posR3 = index2years(tpi_csv.posR3)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_posR3
IPO_posR3_Jun = Jun
IPO_posR3_Jul = Jul
IPO_posR3_Aug = Aug
IPO_posR3_Sep = Sep
IPO_posR3_Oct = Oct
IPO_posR3_Nov = Nov
IPO_posR3_Dec = Dec
IPO_posR3_Jan = Jan
IPO_posR3_Feb = Feb
IPO_posR3_Mar = Mar
IPO_posR3_Apr = Apr
IPO_posR3_May = May
IPO_posR3_JJA = tpi_csv.R3_IPOpos_JJA
IPO_posR3_SON = tpi_csv.R3_IPOpos_SON
IPO_posR3_DJF = tpi_csv.R3_IPOpos_DJF
IPO_posR3_MAM = tpi_csv.R3_IPOpos_MAM
IPO_posR3_annual = tpi_csv.R3_IPOpos_Annual

IPO_negR3 = index2years(tpi_csv.negR3)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_negR3
IPO_negR3_Jun = Jun
IPO_negR3_Jul = Jul
IPO_negR3_Aug = Aug
IPO_negR3_Sep = Sep
IPO_negR3_Oct = Oct
IPO_negR3_Nov = Nov
IPO_negR3_Dec = Dec
IPO_negR3_Jan = Jan
IPO_negR3_Feb = Feb
IPO_negR3_Mar = Mar
IPO_negR3_Apr = Apr
IPO_negR3_May = May
IPO_negR3_JJA = tpi_csv.R3_IPOneg_JJA
IPO_negR3_SON = tpi_csv.R3_IPOneg_SON
IPO_negR3_DJF = tpi_csv.R3_IPOneg_DJF
IPO_negR3_MAM = tpi_csv.R3_IPOneg_MAM
IPO_negR3_annual = tpi_csv.R3_IPOneg_Annual

IPO_neutralR3 = index2years(tpi_csv.neutralR3)
(Jun,Jul,Aug,Sep,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May) = IPO_neutralR3
IPO_neutralR3_Jun = Jun
IPO_neutralR3_Jul = Jul
IPO_neutralR3_Aug = Aug
IPO_neutralR3_Sep = Sep
IPO_neutralR3_Oct = Oct
IPO_neutralR3_Nov = Nov
IPO_neutralR3_Dec = Dec
IPO_neutralR3_Jan = Jan
IPO_neutralR3_Feb = Feb
IPO_neutralR3_Mar = Mar
IPO_neutralR3_Apr = Apr
IPO_neutralR3_May = May
IPO_neutralR3_JJA = tpi_csv.R3_IPOneutral_JJA
IPO_neutralR3_SON = tpi_csv.R3_IPOneutral_SON
IPO_neutralR3_DJF = tpi_csv.R3_IPOneutral_DJF
IPO_neutralR3_MAM = tpi_csv.R3_IPOneutral_MAM
IPO_neutralR3_annual = tpi_csv.R3_IPOneutral_Annual

