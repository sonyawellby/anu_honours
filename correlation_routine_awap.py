"""
A file to correlate ENSO with AWAP rainfall and the IPO with AWAP rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 24 September 2015.
"""

from correlation import *

"""
from indices_time import Nino34_Jun, Nino34_Jul, Nino34_Aug, Nino34_Sep, \
     Nino34_Oct, Nino34_Nov, Nino34_Dec, Nino34_Jan, Nino34_Feb, Nino34_Mar,\
     Nino34_Apr, Nino34_May, Nino34_JJA, Nino34_SON, Nino34_DJF, Nino34_MAM,\
    Nino34_annual, TPI_Jun, TPI_Jul, TPI_Aug, TPI_Sep, TPI_Oct, TPI_Nov,\
    TPI_Dec, TPI_Jan, TPI_Feb, TPI_Mar, TPI_Apr, TPI_May, TPI_JJA, TPI_SON, \
    TPI_DJF, TPI_MAM, TPI_annual
"""
from indices_phase import enso_Jun_Had, enso_Jul_Had, enso_Aug_Had,\
     enso_Sep_Had, enso_Oct_Had, enso_Nov_Had,enso_Dec_Had,enso_Jan_Had,\
     enso_Feb_Had,enso_Mar_Had,enso_Apr_Had,enso_May_Had,IPO_had_Jun,\
     IPO_had_Jul,IPO_had_Aug,IPO_had_Sep,IPO_had_Oct,IPO_had_Nov,\
     IPO_had_Dec,IPO_had_Jan,IPO_had_Feb,IPO_had_Mar,IPO_had_Apr,IPO_had_May

from enso_csv import enso_JJA_Had, enso_SON_Had, enso_DJF_Had, enso_MAM_Had,\
     enso_Annual_Had

from tpi_csv import IPO_had_JJA, IPO_had_SON, IPO_had_DJF, IPO_had_MAM,\
     IPO_had_Annual

from awap_prepare import awap_Annual, awap_JJA,awap_SON,awap_DJF,awap_MAM,\
     awap_June, awap_July, awap_August, awap_September, awap_October, awap_November,\
     awap_December,awap_January,awap_February,awap_March,awap_April,awap_May
     
def awapCorrENSO():
    plotCorr(awap_Annual,enso_Annual_Had,"AWAP rainfall-Nino3.4 correlation - annual",\
             "/correlation/nino_awap/annual")
    plotCorr(awap_JJA,enso_JJA_Had,"AWAP rainfall-Nino3.4 correlation - JJA",\
             "/correlation/nino_awap/JJA")
    plotCorr(awap_SON,enso_SON_Had,"AWAP rainfall-Nino3.4 correlation - SON",\
             "/correlation/nino_awap/SON")
    plotCorr(awap_DJF,enso_DJF_Had,"AWAP rainfall-Nino3.4 correlation - DJF",\
             "/correlation/nino_awap/DJF")
    plotCorr(awap_MAM,enso_MAM_Had,"AWAP rainfall-Nino3.4 correlation - MAM",\
             "/correlation/nino_awap/MAM")
    plotCorr(awap_June,enso_Jun_Had,"AWAP rainfall-Nino3.4 correlation - June",\
             "/correlation/nino_awap/June")
    plotCorr(awap_July,enso_Jul_Had,"AWAP rainfall-Nino3.4 correlation - July",\
             "/correlation/nino_awap/July")
    plotCorr(awap_August,enso_Aug_Had,"AWAP rainfall-Nino3.4 correlation - August",\
             "/correlation/nino_awap/August")
    plotCorr(awap_September,enso_Sep_Had,"AWAP rainfall-Nino3.4 correlation - September",\
             "/correlation/nino_awap/September")
    plotCorr(awap_October,enso_Oct_Had,"AWAP rainfall-Nino3.4 correlation - October",\
             "/correlation/nino_awap/October")
    plotCorr(awap_November,enso_Nov_Had,"AWAP rainfall-Nino3.4 correlation - November",\
             "/correlation/nino_awap/November")
    plotCorr(awap_December,enso_Dec_Had,"AWAP rainfall-Nino3.4 correlation - December",\
             "/correlation/nino_awap/December")
    plotCorr(awap_January,enso_Jan_Had,"AWAP rainfall-Nino3.4 correlation - January",\
             "/correlation/nino_awap/January")
    plotCorr(awap_February,enso_Feb_Had,"AWAP rainfall-Nino3.4 correlation - February",\
             "/correlation/nino_awap/February")
    plotCorr(awap_March,enso_Mar_Had,"AWAP rainfall-Nino3.4 correlation - March",\
             "/correlation/nino_awap/March")
    plotCorr(awap_April,enso_Apr_Had,"AWAP rainfall-Nino3.4 correlation - April",\
             "/correlation/nino_awap/April")
    plotCorr(awap_May,enso_May_Had,"AWAP rainfall-Nino3.4 correlation - May",\
             "/correlation/nino_awap/May")
    return

def awapCorrIPO():
    plotCorr(awap_Annual,IPO_had_Annual,"AWAP rainfall-TPI correlation - annual",\
             "/correlation/tpi_awap/annual")
    plotCorr(awap_JJA,IPO_had_JJA,"AWAP rainfall-TPI correlation - JJA",\
             "/correlation/tpi_awap/JJA")
    plotCorr(awap_SON,IPO_had_SON,"AWAP rainfall-TPI correlation - SON",\
             "/correlation/tpi_awap/SON")
    plotCorr(awap_DJF,IPO_had_DJF,"AWAP rainfall-TPI correlation - DJF",\
             "/correlation/tpi_awap/DJF")
    plotCorr(awap_MAM,IPO_had_MAM,"AWAP rainfall-TPI correlation - MAM",\
             "/correlation/tpi_awap/MAM")
    plotCorr(awap_June,IPO_had_Jun,"AWAP rainfall-TPI correlation - June",\
             "/correlation/tpi_awap/June")
    plotCorr(awap_July,IPO_had_Jul,"AWAP rainfall-TPI correlation - July",\
             "/correlation/tpi_awap/July")
    plotCorr(awap_August,IPO_had_Aug,"AWAP rainfall-TPI correlation - August",\
             "/correlation/tpi_awap/August")
    plotCorr(awap_September,IPO_had_Sep,"AWAP rainfall-TPI correlation - September",\
             "/correlation/tpi_awap/September")
    plotCorr(awap_October,IPO_had_Oct,"AWAP rainfall-TPI correlation - October",\
             "/correlation/tpi_awap/October")
    plotCorr(awap_November,IPO_had_Nov,"AWAP rainfall-TPI correlation - November",\
             "/correlation/tpi_awap/November")
    plotCorr(awap_December,IPO_had_Dec,"AWAP rainfall-TPI correlation - December",\
             "/correlation/tpi_awap/December")
    plotCorr(awap_January,IPO_had_Jan,"AWAP rainfall-TPI correlation - January",\
             "/correlation/tpi_awap/January")
    plotCorr(awap_February,IPO_had_Feb,"AWAP rainfall-TPI correlation - February",\
             "/correlation/tpi_awap/February")
    plotCorr(awap_March,IPO_had_Mar,"AWAP rainfall-TPI correlation - March",\
             "/correlation/tpi_awap/March")
    plotCorr(awap_April,IPO_had_Apr,"AWAP rainfall-TPI correlation - April",\
             "/correlation/tpi_awap/April")
    plotCorr(awap_May,IPO_had_May,"AWAP rainfall-TPI correlation - May",\
             "/correlation/tpi_awap/May")
    return

def awapCorrENSO_data():
    awapCorrENSO_annual = corr(awap_Annual,enso_Annual_Had)
    awapCorrENSO_JJA = corr(awap_JJA,enso_JJA_Had)
    awapCorrENSO_SON = corr(awap_SON,enso_SON_Had)
    awapCorrENSO_DJF = corr(awap_DJF,enso_DJF_Had)
    awapCorrENSO_MAM = corr(awap_MAM,enso_MAM_Had)
    awapCorrENSO_Jun = corr(awap_June,enso_Jun_Had)
    awapCorrENSO_Jul = corr(awap_July,enso_Jul_Had)
    awapCorrENSO_Aug = corr(awap_August,enso_Aug_Had)
    awapCorrENSO_Sep = corr(awap_September,enso_Sep_Had)
    awapCorrENSO_Oct = corr(awap_October,enso_Oct_Had)
    awapCorrENSO_Nov = corr(awap_November,enso_Nov_Had)
    awapCorrENSO_Dec = corr(awap_December,enso_Dec_Had)
    awapCorrENSO_Jan = corr(awap_January,enso_Jan_Had)
    awapCorrENSO_Feb = corr(awap_February,enso_Feb_Had)
    awapCorrENSO_Mar = corr(awap_March,enso_Mar_Had)
    awapCorrENSO_Apr = corr(awap_April,enso_Apr_Had)
    awapCorrENSO_May = corr(awap_May,enso_May_Had)
    return awapCorrENSO_annual, awapCorrENSO_JJA, awapCorrENSO_SON, awapCorrENSO_DJF,\
           awapCorrENSO_MAM,awapCorrENSO_Jun,awapCorrENSO_Jul,awapCorrENSO_Aug,\
           awapCorrENSO_Sep,awapCorrENSO_Oct,awapCorrENSO_Nov,awapCorrENSO_Dec,\
           awapCorrENSO_Jan,awapCorrENSO_Feb,awapCorrENSO_Mar,awapCorrENSO_Apr,\
           awapCorrENSO_May

def awapCorrTPI_data():
    awapCorrTPI_annual = corr(awap_Annual,IPO_had_Annual)
    awapCorrTPI_JJA = corr(awap_JJA,IPO_had_JJA)
    awapCorrTPI_SON = corr(awap_SON,IPO_had_SON)
    awapCorrTPI_DJF = corr(awap_DJF,IPO_had_DJF)
    awapCorrTPI_MAM = corr(awap_MAM,IPO_had_MAM)
    awapCorrTPI_Jun = corr(awap_June,IPO_had_Jun)
    awapCorrTPI_Jul = corr(awap_July,IPO_had_Jul)
    awapCorrTPI_Aug = corr(awap_August,IPO_had_Aug)
    awapCorrTPI_Sep = corr(awap_September,IPO_had_Sep)
    awapCorrTPI_Oct = corr(awap_October,IPO_had_Oct)
    awapCorrTPI_Nov = corr(awap_November,IPO_had_Nov)
    awapCorrTPI_Dec = corr(awap_December,IPO_had_Dec)
    awapCorrTPI_Jan = corr(awap_January,IPO_had_Jan)
    awapCorrTPI_Feb = corr(awap_February,IPO_had_Feb)
    awapCorrTPI_Mar = corr(awap_March,IPO_had_Mar)
    awapCorrTPI_Apr = corr(awap_April,IPO_had_Apr)
    awapCorrTPI_May = corr(awap_May,IPO_had_May)
    return awapCorrTPI_annual, awapCorrTPI_JJA, awapCorrTPI_SON, awapCorrTPI_DJF,\
           awapCorrTPI_MAM,awapCorrTPI_Jun,awapCorrTPI_Jul,awapCorrTPI_Aug,\
           awapCorrTPI_Sep,awapCorrTPI_Oct,awapCorrTPI_Nov,awapCorrTPI_Dec,\
           awapCorrTPI_Jan,awapCorrTPI_Feb,awapCorrTPI_Mar,awapCorrTPI_Apr,\
           awapCorrTPI_May


"""
awapCorrENSO()
awapCorrIPO()
"""
