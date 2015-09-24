"""
A file to correlate ENSO with AWAP rainfall and the IPO with AWAP rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 24 September 2015.
"""

from correlation import *

from indices_time import Nino34_Jun, Nino34_Jul, Nino34_Aug, Nino34_Sep, \
     Nino34_Oct, Nino34_Nov, Nino34_Dec, Nino34_Jan, Nino34_Feb, Nino34_Mar,\
     Nino34_Apr, Nino34_May, Nino34_JJA, Nino34_SON, Nino34_DJF, Nino34_MAM,\
    Nino34_annual, TPI_Jun, TPI_Jul, TPI_Aug, TPI_Sep, TPI_Oct, TPI_Nov,\
    TPI_Dec, TPI_Jan, TPI_Feb, TPI_Mar, TPI_Apr, TPI_May, TPI_JJA, TPI_SON, \
    TPI_DJF, TPI_MAM, TPI_annual

from awap_prepare import awap_Annual, awap_JJA,awap_SON,awap_DJF,awap_MAM,\
     awap_June, awap_July, awap_August, awap_September, awap_October, awap_November,\
     awap_December,awap_January,awap_February,awap_March,awap_April,awap_May
     
def awapCorrENSO():
    plotCorr(awap_Annual,Nino34_annual,0,"AWAP rainfall-Nino3.4 correlation - annual",\
             "/correlation/nino_awap/annual")
    plotCorr(awap_JJA,Nino34_JJA,0,"AWAP rainfall-Nino3.4 correlation - JJA",\
             "/correlation/nino_awap/JJA")
    plotCorr(awap_SON,Nino34_SON,0,"AWAP rainfall-Nino3.4 correlation - SON",\
             "/correlation/nino_awap/SON")
    plotCorr(awap_DJF,Nino34_DJF,0,"AWAP rainfall-Nino3.4 correlation - DJF",\
             "/correlation/nino_awap/DJF")
    plotCorr(awap_MAM,Nino34_MAM,0,"AWAP rainfall-Nino3.4 correlation - MAM",\
             "/correlation/nino_awap/MAM")
    plotCorr(awap_June,Nino34_Jun,0,"AWAP rainfall-Nino3.4 correlation - June",\
             "/correlation/nino_awap/June")
    plotCorr(awap_July,Nino34_Jul,0,"AWAP rainfall-Nino3.4 correlation - July",\
             "/correlation/nino_awap/July")
    plotCorr(awap_August,Nino34_Aug,0,"AWAP rainfall-Nino3.4 correlation - August",\
             "/correlation/nino_awap/August")
    plotCorr(awap_September,Nino34_Sep,0,"AWAP rainfall-Nino3.4 correlation - September",\
             "/correlation/nino_awap/September")
    plotCorr(awap_October,Nino34_Oct,0,"AWAP rainfall-Nino3.4 correlation - October",\
             "/correlation/nino_awap/October")
    plotCorr(awap_November,Nino34_Nov,0,"AWAP rainfall-Nino3.4 correlation - November",\
             "/correlation/nino_awap/November")
    plotCorr(awap_December,Nino34_Dec,0,"AWAP rainfall-Nino3.4 correlation - December",\
             "/correlation/nino_awap/December")
    plotCorr(awap_January,Nino34_Jan,0,"AWAP rainfall-Nino3.4 correlation - January",\
             "/correlation/nino_awap/January")
    plotCorr(awap_February,Nino34_Feb,0,"AWAP rainfall-Nino3.4 correlation - February",\
             "/correlation/nino_awap/February")
    plotCorr(awap_March,Nino34_Mar,0,"AWAP rainfall-Nino3.4 correlation - March",\
             "/correlation/nino_awap/March")
    plotCorr(awap_April,Nino34_Apr,0,"AWAP rainfall-Nino3.4 correlation - April",\
             "/correlation/nino_awap/April")
    plotCorr(awap_May,Nino34_May,0,"AWAP rainfall-Nino3.4 correlation - May",\
             "/correlation/nino_awap/May")
    return

def awapCorrIPO():
    plotCorr(awap_Annual,TPI_annual,1,"AWAP rainfall-TPI correlation - annual",\
             "/correlation/tpi_awap/annual")
    plotCorr(awap_JJA,TPI_JJA,1,"AWAP rainfall-TPI correlation - JJA",\
             "/correlation/tpi_awap/JJA")
    plotCorr(awap_SON,TPI_SON,1,"AWAP rainfall-TPI correlation - SON",\
             "/correlation/tpi_awap/SON")
    plotCorr(awap_DJF,TPI_DJF,1,"AWAP rainfall-TPI correlation - DJF",\
             "/correlation/tpi_awap/DJF")
    plotCorr(awap_MAM,TPI_MAM,1,"AWAP rainfall-TPI correlation - MAM",\
             "/correlation/tpi_awap/MAM")
    plotCorr(awap_June,TPI_Jun,1,"AWAP rainfall-TPI correlation - June",\
             "/correlation/tpi_awap/June")
    plotCorr(awap_July,TPI_Jul,1,"AWAP rainfall-TPI correlation - July",\
             "/correlation/tpi_awap/July")
    plotCorr(awap_August,TPI_Aug,1,"AWAP rainfall-TPI correlation - August",\
             "/correlation/tpi_awap/August")
    plotCorr(awap_September,TPI_Sep,1,"AWAP rainfall-TPI correlation - September",\
             "/correlation/tpi_awap/September")
    plotCorr(awap_October,TPI_Oct,1,"AWAP rainfall-TPI correlation - October",\
             "/correlation/tpi_awap/October")
    plotCorr(awap_November,TPI_Nov,1,"AWAP rainfall-TPI correlation - November",\
             "/correlation/tpi_awap/November")
    plotCorr(awap_December,TPI_Dec,1,"AWAP rainfall-TPI correlation - December",\
             "/correlation/tpi_awap/December")
    plotCorr(awap_January,TPI_Jan,1,"AWAP rainfall-TPI correlation - January",\
             "/correlation/tpi_awap/January")
    plotCorr(awap_February,TPI_Feb,1,"AWAP rainfall-TPI correlation - February",\
             "/correlation/tpi_awap/February")
    plotCorr(awap_March,TPI_Mar,1,"AWAP rainfall-TPI correlation - March",\
             "/correlation/tpi_awap/March")
    plotCorr(awap_April,TPI_Apr,1,"AWAP rainfall-TPI correlation - April",\
             "/correlation/tpi_awap/April")
    plotCorr(awap_May,TPI_May,1,"AWAP rainfall-TPI correlation - May",\
             "/correlation/tpi_awap/May")
    return

def awapCorrENSO_data():
    awapCorrENSO_annual = corr(awap_Annual,Nino34_annual,0)
    awapCorrENSO_JJA = corr(awap_JJA,Nino34_JJA,0)
    awapCorrENSO_SON = corr(awap_SON,Nino34_SON,0)
    awapCorrENSO_DJF = corr(awap_DJF,Nino34_DJF,0)
    awapCorrENSO_MAM = corr(awap_MAM,Nino34_MAM,0)
    awapCorrENSO_Jun = corr(awap_June,Nino34_Jun,0)
    awapCorrENSO_Jul = corr(awap_July,Nino34_Jul,0)
    awapCorrENSO_Aug = corr(awap_August,Nino34_Aug,0)
    awapCorrENSO_Sep = corr(awap_September,Nino34_Sep,0)
    awapCorrENSO_Oct = corr(awap_October,Nino34_Oct,0)
    awapCorrENSO_Nov = corr(awap_November,Nino34_Nov,0)
    awapCorrENSO_Dec = corr(awap_December,Nino34_Dec,0)
    awapCorrENSO_Jan = corr(awap_January,Nino34_Jan,0)
    awapCorrENSO_Feb = corr(awap_February,Nino34_Feb,0)
    awapCorrENSO_Mar = corr(awap_March,Nino34_Mar,0)
    awapCorrENSO_Apr = corr(awap_April,Nino34_Apr,0)
    awapCorrENSO_May = corr(awap_May,Nino34_May,0)
    return awapCorrENSO_annual, awapCorrENSO_JJA, awapCorrENSO_SON, awapCorrENSO_DJF,\
           awapCorrENSO_MAM,awapCorrENSO_Jun,awapCorrENSO_Jul,awapCorrENSO_Aug,\
           awapCorrENSO_Sep,awapCorrENSO_Oct,awapCorrENSO_Nov,awapCorrENSO_Dec,\
           awapCorrENSO_Jan,awapCorrENSO_Feb,awapCorrENSO_Mar,awapCorrENSO_Apr,\
           awapCorrENSO_May

def awapCorrTPI_data():
    awapCorrTPI_annual = corr(awap_Annual,TPI_annual,1)
    awapCorrTPI_JJA = corr(awap_JJA,TPI_JJA,1)
    awapCorrTPI_SON = corr(awap_SON,TPI_SON,1)
    awapCorrTPI_DJF = corr(awap_DJF,TPI_DJF,1)
    awapCorrTPI_MAM = corr(awap_MAM,TPI_MAM,1)
    awapCorrTPI_Jun = corr(awap_June,TPI_Jun,1)
    awapCorrTPI_Jul = corr(awap_July,TPI_Jul,1)
    awapCorrTPI_Aug = corr(awap_August,TPI_Aug,1)
    awapCorrTPI_Sep = corr(awap_September,TPI_Sep,1)
    awapCorrTPI_Oct = corr(awap_October,TPI_Oct,1)
    awapCorrTPI_Nov = corr(awap_November,TPI_Nov,1)
    awapCorrTPI_Dec = corr(awap_December,TPI_Dec,1)
    awapCorrTPI_Jan = corr(awap_January,TPI_Jan,1)
    awapCorrTPI_Feb = corr(awap_February,TPI_Feb,1)
    awapCorrTPI_Mar = corr(awap_March,TPI_Mar,1)
    awapCorrTPI_Apr = corr(awap_April,TPI_Apr,1)
    awapCorrTPI_May = corr(awap_May,TPI_May,1)
    return awapCorrTPI_annual, awapCorrTPI_JJA, awapCorrTPI_SON, awapCorrTPI_DJF,\
           awapCorrTPI_MAM,awapCorrTPI_Jun,awapCorrTPI_Jul,awapCorrTPI_Aug,\
           awapCorrTPI_Sep,awapCorrTPI_Oct,awapCorrTPI_Nov,awapCorrTPI_Dec,\
           awapCorrTPI_Jan,awapCorrTPI_Feb,awapCorrTPI_Mar,awapCorrTPI_Apr,\
           awapCorrTPI_May

"""
awapCorrENSO()
awapCorrIPO()
"""
