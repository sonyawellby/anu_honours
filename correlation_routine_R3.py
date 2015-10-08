"""
A file to correlate ENSO with awap R3 rainfall and the IPO with awap R3
rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 7 October 2015.
"""

from correlation import *
from correlation_routine_awap import awapCorrENSO_data,awapCorrTPI_data

from access_trimmed import trim_Annual, trim_JJA,trim_SON,trim_DJF,trim_MAM,\
     trim_June, trim_July, trim_August, trim_September, trim_October, trim_November,\
     trim_December,trim_January,trim_February,trim_March,trim_April,trim_May

from indices_phase import enso_Jun_R3, enso_Jul_R3, enso_Aug_R3,\
     enso_Sep_R3, enso_Oct_R3, enso_Nov_R3,enso_Dec_R3,enso_Jan_R3,\
     enso_Feb_R3,enso_Mar_R3,enso_Apr_R3,enso_May_R3,IPO_R3_Jun,\
     IPO_R3_Jul,IPO_R3_Aug,IPO_R3_Sep,IPO_R3_Oct,IPO_R3_Nov,\
     IPO_R3_Dec,IPO_R3_Jan,IPO_R3_Feb,IPO_R3_Mar,IPO_R3_Apr,IPO_R3_May

from enso_csv import enso_JJA_R3, enso_SON_R3, enso_DJF_R3, enso_MAM_R3,\
     enso_Annual_R3

from tpi_csv import IPO_R3_JJA, IPO_R3_SON, IPO_R3_DJF, IPO_R3_MAM,\
     IPO_R3_Annual

# Plots correlation maps

def accessR3_awap_corrENSO(roundNum):
    plotCorr(trim_Annual,enso_Annual_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - annual",\
             "/correlation/nino_"+roundNum+"/annual")
    plotCorr(trim_JJA,enso_JJA_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - JJA",\
             "/correlation/nino_"+roundNum+"/JJA")
    plotCorr(trim_SON,enso_SON_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - SON",\
             "/correlation/nino_"+roundNum+"/SON")
    plotCorr(trim_DJF,enso_DJF_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - DJF",\
             "/correlation/nino_"+roundNum+"/DJF")
    plotCorr(trim_MAM,enso_MAM_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - MAM",\
             "/correlation/nino_"+roundNum+"/MAM")
    plotCorr(trim_June,enso_Jun_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - June",\
             "/correlation/nino_"+roundNum+"/June")
    plotCorr(trim_July,enso_Jul_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - July",\
             "/correlation/nino_"+roundNum+"/July")
    plotCorr(trim_August,enso_Aug_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - August",\
             "/correlation/nino_"+roundNum+"/August")
    plotCorr(trim_September,enso_Sep_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - September",\
             "/correlation/nino_"+roundNum+"/September")
    plotCorr(trim_October,enso_Oct_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - October",\
             "/correlation/nino_"+roundNum+"/October")
    plotCorr(trim_November,enso_Nov_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - November",\
             "/correlation/nino_"+roundNum+"/November")
    plotCorr(trim_December,enso_Dec_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - December",\
             "/correlation/nino_"+roundNum+"/December")
    plotCorr(trim_January,enso_Jan_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - January",\
             "/correlation/nino_"+roundNum+"/January")
    plotCorr(trim_February,enso_Feb_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - February",\
             "/correlation/nino_"+roundNum+"/February")
    plotCorr(trim_March,enso_Mar_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - March",\
             "/correlation/nino_"+roundNum+"/March")
    plotCorr(trim_April,enso_Apr_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - April",\
             "/correlation/nino_"+roundNum+"/April")
    plotCorr(trim_May,enso_May_R3,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - May",\
             "/correlation/nino_"+roundNum+"/May")
    return

def accessR3_awap_corrIPO(roundNum):
    plotCorr(trim_Annual,IPO_R3_Annual,"ACCESS "+roundNum+" rainfall-TPI correlation - annual",\
             "/correlation/tpi_"+roundNum+"/annual")
    plotCorr(trim_JJA,IPO_R3_JJA,"ACCESS "+roundNum+" rainfall-TPI correlation - JJA",\
             "/correlation/tpi_"+roundNum+"/JJA")
    plotCorr(trim_SON,IPO_R3_SON,"ACCESS "+roundNum+" rainfall-TPI correlation - SON",\
             "/correlation/tpi_"+roundNum+"/SON")
    plotCorr(trim_DJF,IPO_R3_DJF,"ACCESS "+roundNum+" rainfall-TPI correlation - DJF",\
             "/correlation/tpi_"+roundNum+"/DJF")
    plotCorr(trim_MAM,IPO_R3_MAM,"ACCESS "+roundNum+" rainfall-TPI correlation - MAM",\
             "/correlation/tpi_"+roundNum+"/MAM")
    plotCorr(trim_June,IPO_R3_Jun,"ACCESS "+roundNum+" rainfall-TPI correlation - June",\
             "/correlation/tpi_"+roundNum+"/June")
    plotCorr(trim_July,IPO_R3_Jul,"ACCESS "+roundNum+" rainfall-TPI correlation - July",\
             "/correlation/tpi_"+roundNum+"/July")
    plotCorr(trim_August,IPO_R3_Aug,"ACCESS "+roundNum+" rainfall-TPI correlation - August",\
             "/correlation/tpi_"+roundNum+"/August")
    plotCorr(trim_September,IPO_R3_Sep,"ACCESS "+roundNum+" rainfall-TPI correlation - September",\
             "/correlation/tpi_"+roundNum+"/September")
    plotCorr(trim_October,IPO_R3_Oct,"ACCESS "+roundNum+" rainfall-TPI correlation - October",\
             "/correlation/tpi_"+roundNum+"/October")
    plotCorr(trim_November,IPO_R3_Nov,"ACCESS "+roundNum+" rainfall-TPI correlation - November",\
             "/correlation/tpi_"+roundNum+"/November")
    plotCorr(trim_December,IPO_R3_Dec,"ACCESS "+roundNum+" rainfall-TPI correlation - December",\
             "/correlation/tpi_"+roundNum+"/December")
    plotCorr(trim_January,IPO_R3_Jan,"ACCESS "+roundNum+" rainfall-TPI correlation - January",\
             "/correlation/tpi_"+roundNum+"/January")
    plotCorr(trim_February,IPO_R3_Feb,"ACCESS "+roundNum+" rainfall-TPI correlation - February",\
             "/correlation/tpi_"+roundNum+"/February")
    plotCorr(trim_March,IPO_R3_Mar,"ACCESS "+roundNum+" rainfall-TPI correlation - March",\
             "/correlation/tpi_"+roundNum+"/March")
    plotCorr(trim_April,IPO_R3_Apr,"ACCESS "+roundNum+" rainfall-TPI correlation - April",\
             "/correlation/tpi_"+roundNum+"/April")
    plotCorr(trim_May,IPO_R3_May,"ACCESS "+roundNum+" rainfall-TPI correlation - May",\
             "/correlation/tpi_"+roundNum+"/May")
    return

#Single value correlation coefficients (Australia, East Australia, climate regions).

def corrAverageENSO():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    corrAvENSO_annual = corrAverage(trim_Annual,enso_Annual_R3)
    corrAvENSO_JJA = corrAverage(trim_JJA,enso_JJA_R3)
    corrAvENSO_SON = corrAverage(trim_SON,enso_SON_R3)
    corrAvENSO_DJF = corrAverage(trim_DJF,enso_DJF_R3)
    corrAvENSO_MAM = corrAverage(trim_MAM,enso_MAM_R3)
    corrAvENSO_Jun = corrAverage(trim_June,enso_Jun_R3)
    corrAvENSO_Jul = corrAverage(trim_July,enso_Jul_R3)
    corrAvENSO_Aug = corrAverage(trim_August,enso_Aug_R3)
    corrAvENSO_Sep = corrAverage(trim_September,enso_Sep_R3)
    corrAvENSO_Oct = corrAverage(trim_October,enso_Oct_R3)
    corrAvENSO_Nov = corrAverage(trim_November,enso_Nov_R3)
    corrAvENSO_Dec = corrAverage(trim_December,enso_Dec_R3)
    corrAvENSO_Jan = corrAverage(trim_January,enso_Jan_R3)
    corrAvENSO_Feb = corrAverage(trim_February,enso_Feb_R3)
    corrAvENSO_Mar = corrAverage(trim_March,enso_Mar_R3)
    corrAvENSO_Apr = corrAverage(trim_April,enso_Apr_R3)
    corrAvENSO_May = corrAverage(trim_May,enso_May_R3)
    return corrAvENSO_annual, corrAvENSO_JJA,corrAvENSO_SON,\
           corrAvENSO_DJF,corrAvENSO_MAM,corrAvENSO_Jun,\
           corrAvENSO_Jul,corrAvENSO_Aug,corrAvENSO_Sep,\
           corrAvENSO_Oct,corrAvENSO_Nov,corrAvENSO_Dec,\
           corrAvENSO_Jan,corrAvENSO_Feb,corrAvENSO_Mar,\
           corrAvENSO_Apr,corrAvENSO_May

def corrAverageEastENSO():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    corrEastENSO_annual = corrEastAus(trim_Annual,enso_Annual_R3)
    corrEastENSO_JJA = corrEastAus(trim_JJA,enso_JJA_R3)
    corrEastENSO_SON = corrEastAus(trim_SON,enso_SON_R3)
    corrEastENSO_DJF = corrEastAus(trim_DJF,enso_DJF_R3)
    corrEastENSO_MAM = corrEastAus(trim_MAM,enso_MAM_R3)
    corrEastENSO_Jun = corrEastAus(trim_June,enso_Jun_R3)
    corrEastENSO_Jul = corrEastAus(trim_July,enso_Jul_R3)
    corrEastENSO_Aug = corrEastAus(trim_August,enso_Aug_R3)
    corrEastENSO_Sep = corrEastAus(trim_September,enso_Sep_R3)
    corrEastENSO_Oct = corrEastAus(trim_October,enso_Oct_R3)
    corrEastENSO_Nov = corrEastAus(trim_November,enso_Nov_R3)
    corrEastENSO_Dec = corrEastAus(trim_December,enso_Dec_R3)
    corrEastENSO_Jan = corrEastAus(trim_January,enso_Jan_R3)
    corrEastENSO_Feb = corrEastAus(trim_February,enso_Feb_R3)
    corrEastENSO_Mar = corrEastAus(trim_March,enso_Mar_R3)
    corrEastENSO_Apr = corrEastAus(trim_April,enso_Apr_R3)
    corrEastENSO_May = corrEastAus(trim_May,enso_May_R3)
    return corrEastENSO_annual, corrEastENSO_JJA,corrEastENSO_SON,\
           corrEastENSO_DJF,corrEastENSO_MAM,corrEastENSO_Jun,\
           corrEastENSO_Jul,corrEastENSO_Aug,corrEastENSO_Sep,\
           corrEastENSO_Oct,corrEastENSO_Nov,corrEastENSO_Dec,\
           corrEastENSO_Jan,corrEastENSO_Feb,corrEastENSO_Mar,\
           corrEastENSO_Apr,corrEastENSO_May

def corrAverageTPI():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    corrAvTPI_annual = corrAverage(trim_Annual,IPO_R3_Annual)
    corrAvTPI_JJA = corrAverage(trim_JJA,IPO_R3_JJA)
    corrAvTPI_SON = corrAverage(trim_SON,IPO_R3_SON)
    corrAvTPI_DJF = corrAverage(trim_DJF,IPO_R3_DJF)
    corrAvTPI_MAM = corrAverage(trim_MAM,IPO_R3_MAM)
    corrAvTPI_Jun = corrAverage(trim_June,IPO_R3_Jun)
    corrAvTPI_Jul = corrAverage(trim_July,IPO_R3_Jul)
    corrAvTPI_Aug = corrAverage(trim_August,IPO_R3_Aug)
    corrAvTPI_Sep = corrAverage(trim_September,IPO_R3_Sep)
    corrAvTPI_Oct = corrAverage(trim_October,IPO_R3_Oct)
    corrAvTPI_Nov = corrAverage(trim_November,IPO_R3_Nov)
    corrAvTPI_Dec = corrAverage(trim_December,IPO_R3_Dec)
    corrAvTPI_Jan = corrAverage(trim_January,IPO_R3_Jan)
    corrAvTPI_Feb = corrAverage(trim_February,IPO_R3_Feb)
    corrAvTPI_Mar = corrAverage(trim_March,IPO_R3_Mar)
    corrAvTPI_Apr = corrAverage(trim_April,IPO_R3_Apr)
    corrAvTPI_May = corrAverage(trim_May,IPO_R3_May)
    return corrAvTPI_annual, corrAvTPI_JJA, corrAvTPI_SON, corrAvTPI_DJF,\
           corrAvTPI_MAM,corrAvTPI_Jun,corrAvTPI_Jul,corrAvTPI_Aug,\
           corrAvTPI_Sep,corrAvTPI_Oct,corrAvTPI_Nov,corrAvTPI_Dec,\
           corrAvTPI_Jan,corrAvTPI_Feb,corrAvTPI_Mar,corrAvTPI_Apr,\
           corrAvTPI_May

def corrAverageEastTPI():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    corrEastTPI_annual = corrEastAus(trim_Annual,IPO_R3_Annual)
    corrEastTPI_JJA = corrEastAus(trim_JJA,IPO_R3_JJA)
    corrEastTPI_SON = corrEastAus(trim_SON,IPO_R3_SON)
    corrEastTPI_DJF = corrEastAus(trim_DJF,IPO_R3_DJF)
    corrEastTPI_MAM = corrEastAus(trim_MAM,IPO_R3_MAM)
    corrEastTPI_Jun = corrEastAus(trim_June,IPO_R3_Jun)
    corrEastTPI_Jul = corrEastAus(trim_July,IPO_R3_Jul)
    corrEastTPI_Aug = corrEastAus(trim_August,IPO_R3_Aug)
    corrEastTPI_Sep = corrEastAus(trim_September,IPO_R3_Sep)
    corrEastTPI_Oct = corrEastAus(trim_October,IPO_R3_Oct)
    corrEastTPI_Nov = corrEastAus(trim_November,IPO_R3_Nov)
    corrEastTPI_Dec = corrEastAus(trim_December,IPO_R3_Dec)
    corrEastTPI_Jan = corrEastAus(trim_January,IPO_R3_Jan)
    corrEastTPI_Feb = corrEastAus(trim_February,IPO_R3_Feb)
    corrEastTPI_Mar = corrEastAus(trim_March,IPO_R3_Mar)
    corrEastTPI_Apr = corrEastAus(trim_April,IPO_R3_Apr)
    corrEastTPI_May = corrEastAus(trim_May,IPO_R3_May)
    return corrEastTPI_annual, corrEastTPI_JJA, corrEastTPI_SON, corrEastTPI_DJF,\
           corrEastTPI_MAM,corrEastTPI_Jun,corrEastTPI_Jul,corrEastTPI_Aug,\
           corrEastTPI_Sep,corrEastTPI_Oct,corrEastTPI_Nov,corrEastTPI_Dec,\
           corrEastTPI_Jan,corrEastTPI_Feb,corrEastTPI_Mar,corrEastTPI_Apr,\
           corrEastTPI_May

# Makes data available for plotting correlation difference maps.

def R3CorrENSO_data():
    R3CorrENSO_annual = corr(trim_Annual,enso_Annual_R3)
    R3CorrENSO_JJA = corr(trim_JJA,enso_JJA_R3)
    R3CorrENSO_SON = corr(trim_SON,enso_SON_R3)
    R3CorrENSO_DJF = corr(trim_DJF,enso_DJF_R3)
    R3CorrENSO_MAM = corr(trim_MAM,enso_MAM_R3)
    R3CorrENSO_Jun = corr(trim_June,IPO_R3_Jun)
    R3CorrENSO_Jul = corr(trim_July,IPO_R3_Jul)
    R3CorrENSO_Aug = corr(trim_August,IPO_R3_Aug)
    R3CorrENSO_Sep = corr(trim_September,IPO_R3_Sep)
    R3CorrENSO_Oct = corr(trim_October,IPO_R3_Oct)
    R3CorrENSO_Nov = corr(trim_November,IPO_R3_Nov)
    R3CorrENSO_Dec = corr(trim_December,IPO_R3_Dec)
    R3CorrENSO_Jan = corr(trim_January,IPO_R3_Jan)
    R3CorrENSO_Feb = corr(trim_February,IPO_R3_Feb)
    R3CorrENSO_Mar = corr(trim_March,IPO_R3_Mar)
    R3CorrENSO_Apr = corr(trim_April,IPO_R3_Apr)
    R3CorrENSO_May = corr(trim_May,IPO_R3_May)
    return R3CorrENSO_annual, R3CorrENSO_JJA, R3CorrENSO_SON, R3CorrENSO_DJF,\
           R3CorrENSO_MAM,R3CorrENSO_Jun,R3CorrENSO_Jul,R3CorrENSO_Aug,\
           R3CorrENSO_Sep,R3CorrENSO_Oct,R3CorrENSO_Nov,R3CorrENSO_Dec,\
           R3CorrENSO_Jan,R3CorrENSO_Feb,R3CorrENSO_Mar,R3CorrENSO_Apr,\
           R3CorrENSO_May

def R3CorrTPI_data():
    R3CorrTPI_annual = corr(trim_Annual,IPO_R3_Annual)
    R3CorrTPI_JJA = corr(trim_JJA,IPO_R3_JJA)
    R3CorrTPI_SON = corr(trim_SON,IPO_R3_SON)
    R3CorrTPI_DJF = corr(trim_DJF,IPO_R3_DJF)
    R3CorrTPI_MAM = corr(trim_MAM,IPO_R3_MAM)
    R3CorrTPI_Jun = corr(trim_June,IPO_R3_Jun)
    R3CorrTPI_Jul = corr(trim_July,IPO_R3_Jul)
    R3CorrTPI_Aug = corr(trim_August,IPO_R3_Aug)
    R3CorrTPI_Sep = corr(trim_September,IPO_R3_Sep)
    R3CorrTPI_Oct = corr(trim_October,IPO_R3_Oct)
    R3CorrTPI_Nov = corr(trim_November,IPO_R3_Nov)
    R3CorrTPI_Dec = corr(trim_December,IPO_R3_Dec)
    R3CorrTPI_Jan = corr(trim_January,IPO_R3_Jan)
    R3CorrTPI_Feb = corr(trim_February,IPO_R3_Feb)
    R3CorrTPI_Mar = corr(trim_March,IPO_R3_Mar)
    R3CorrTPI_Apr = corr(trim_April,IPO_R3_Apr)
    R3CorrTPI_May = corr(trim_May,IPO_R3_May)
    return R3CorrTPI_annual, R3CorrTPI_JJA, R3CorrTPI_SON, R3CorrTPI_DJF,\
           R3CorrTPI_MAM,R3CorrTPI_Jun,R3CorrTPI_Jul,R3CorrTPI_Aug,\
           R3CorrTPI_Sep,R3CorrTPI_Oct,R3CorrTPI_Nov,R3CorrTPI_Dec,\
           R3CorrTPI_Jan,R3CorrTPI_Feb,R3CorrTPI_Mar,R3CorrTPI_Apr,\
           R3CorrTPI_May

#Plots Difference in AWAP and ACCESS R3 correlation maps.

def corrDiffENSO_R3():
    plotCorrDiff(awapCorrENSO_annual,R3CorrENSO_annual,"Difference in AWAP and R3 correlations, ENSO - annual",\
             "/correlation/diff_nino_R3/annual")
    plotCorrDiff(awapCorrENSO_JJA,R3CorrENSO_JJA,"Difference in AWAP and R3 correlations, ENSO - JJA",\
             "/correlation/diff_nino_R3/JJA")
    plotCorrDiff(awapCorrENSO_SON,R3CorrENSO_SON,"Difference in AWAP and R3 correlations, ENSO - SON",\
             "/correlation/diff_nino_R3/SON")
    plotCorrDiff(awapCorrENSO_DJF,R3CorrENSO_DJF,"Difference in AWAP and R3 correlations, ENSO - DJF",\
             "/correlation/diff_nino_R3/DJF")
    plotCorrDiff(awapCorrENSO_MAM,R3CorrENSO_MAM,"Difference in AWAP and R3 correlations, ENSO - MAM",\
             "/correlation/diff_nino_R3/MAM")
    plotCorrDiff(awapCorrENSO_Jun,R3CorrENSO_Jun,"Difference in AWAP and R3 correlations, ENSO - June",\
             "/correlation/diff_nino_R3/June")
    plotCorrDiff(awapCorrENSO_Jul,R3CorrENSO_Jul,"Difference in AWAP and R3 correlations, ENSO - July",\
             "/correlation/diff_nino_R3/July")
    plotCorrDiff(awapCorrENSO_Aug,R3CorrENSO_Aug,"Difference in AWAP and R3 correlations, ENSO - August",\
             "/correlation/diff_nino_R3/August")
    plotCorrDiff(awapCorrENSO_Sep,R3CorrENSO_Sep,"Difference in AWAP and R3 correlations, ENSO - September",\
             "/correlation/diff_nino_R3/September")
    plotCorrDiff(awapCorrENSO_Oct,R3CorrENSO_Oct,"Difference in AWAP and R3 correlations, ENSO - October",\
             "/correlation/diff_nino_R3/October")
    plotCorrDiff(awapCorrENSO_Nov,R3CorrENSO_Nov,"Difference in AWAP and R3 correlations, ENSO - November",\
             "/correlation/diff_nino_R3/November")
    plotCorrDiff(awapCorrENSO_Dec,R3CorrENSO_Dec,"Difference in AWAP and R3 correlations, ENSO - December",\
             "/correlation/diff_nino_R3/December")
    plotCorrDiff(awapCorrENSO_Jan,R3CorrENSO_Jan,"Difference in AWAP and R3 correlations, ENSO - January",\
             "/correlation/diff_nino_R3/January")
    plotCorrDiff(awapCorrENSO_Feb,R3CorrENSO_Feb,"Difference in AWAP and R3 correlations, ENSO - February",\
             "/correlation/diff_nino_R3/February")
    plotCorrDiff(awapCorrENSO_Mar,R3CorrENSO_Mar,"Difference in AWAP and R3 correlations, ENSO - March",\
             "/correlation/diff_nino_R3/March")
    plotCorrDiff(awapCorrENSO_Apr,R3CorrENSO_Apr,"Difference in AWAP and R3 correlations, ENSO - April",\
             "/correlation/diff_nino_R3/April")
    plotCorrDiff(awapCorrENSO_May,R3CorrENSO_May,"Difference in AWAP and R3 correlations, ENSO - May",\
             "/correlation/diff_nino_R3/May")
    return

def corrDiffTPI_R3():
    plotCorrDiff(awapCorrTPI_annual,R3CorrTPI_annual,"Difference in AWAP and R3 correlations, IPO - annual",\
             "/correlation/diff_tpi_R3/annual")
    plotCorrDiff(awapCorrTPI_JJA,R3CorrTPI_JJA,"Difference in AWAP and R3 correlations, IPO - JJA",\
             "/correlation/diff_tpi_R3/JJA")
    plotCorrDiff(awapCorrTPI_SON,R3CorrTPI_SON,"Difference in AWAP and R3 correlations, IPO - SON",\
             "/correlation/diff_tpi_R3/SON")
    plotCorrDiff(awapCorrTPI_DJF,R3CorrTPI_DJF,"Difference in AWAP and R3 correlations, IPO - DJF",\
             "/correlation/diff_tpi_R3/DJF")
    plotCorrDiff(awapCorrTPI_MAM,R3CorrTPI_MAM,"Difference in AWAP and R3 correlations, IPO - MAM",\
             "/correlation/diff_tpi_R3/MAM")
    plotCorrDiff(awapCorrTPI_Jun,R3CorrTPI_Jun,"Difference in AWAP and R3 correlations, IPO - June",\
             "/correlation/diff_tpi_R3/June")
    plotCorrDiff(awapCorrTPI_Jul,R3CorrTPI_Jul,"Difference in AWAP and R3 correlations, IPO - July",\
             "/correlation/diff_tpi_R3/July")
    plotCorrDiff(awapCorrTPI_Aug,R3CorrTPI_Aug,"Difference in AWAP and R3 correlations, IPO - August",\
             "/correlation/diff_tpi_R3/August")
    plotCorrDiff(awapCorrTPI_Sep,R3CorrTPI_Sep,"Difference in AWAP and R3 correlations, IPO - September",\
             "/correlation/diff_tpi_R3/September")
    plotCorrDiff(awapCorrTPI_Oct,R3CorrTPI_Oct,"Difference in AWAP and R3 correlations, IPO - October",\
             "/correlation/diff_tpi_R3/October")
    plotCorrDiff(awapCorrTPI_Nov,R3CorrTPI_Nov,"Difference in AWAP and R3 correlations, IPO - November",\
             "/correlation/diff_tpi_R3/November")
    plotCorrDiff(awapCorrTPI_Dec,R3CorrTPI_Dec,"Difference in AWAP and R3 correlations, IPO - December",\
             "/correlation/diff_tpi_R3/December")
    plotCorrDiff(awapCorrTPI_Jan,R3CorrTPI_Jan,"Difference in AWAP and R3 correlations, IPO - January",\
             "/correlation/diff_tpi_R3/January")
    plotCorrDiff(awapCorrTPI_Feb,R3CorrTPI_Feb,"Difference in AWAP and R3 correlations, IPO - February",\
             "/correlation/diff_tpi_R3/February")
    plotCorrDiff(awapCorrTPI_Mar,R3CorrTPI_Mar,"Difference in AWAP and R3 correlations, IPO - March",\
             "/correlation/diff_tpi_R3/March")
    plotCorrDiff(awapCorrTPI_Apr,R3CorrTPI_Apr,"Difference in AWAP and R3 correlations, IPO - April",\
             "/correlation/diff_tpi_R3/April")
    plotCorrDiff(awapCorrTPI_May,R3CorrTPI_May,"Difference in AWAP and R3 correlations, IPO - May",\
             "/correlation/diff_tpi_R3/May")
    return

#Makes data available for plotting correlation plots
corrENSO = awapCorrENSO_data()
(awapCorrENSO_annual, awapCorrENSO_JJA, awapCorrENSO_SON, awapCorrENSO_DJF,\
           awapCorrENSO_MAM,awapCorrENSO_Jun,awapCorrENSO_Jul,awapCorrENSO_Aug,\
           awapCorrENSO_Sep,awapCorrENSO_Oct,awapCorrENSO_Nov,awapCorrENSO_Dec,\
           awapCorrENSO_Jan,awapCorrENSO_Feb,awapCorrENSO_Mar,awapCorrENSO_Apr,\
           awapCorrENSO_May) = corrENSO

corrIPO = awapCorrTPI_data()
(awapCorrTPI_annual, awapCorrTPI_JJA, awapCorrTPI_SON, awapCorrTPI_DJF,\
           awapCorrTPI_MAM,awapCorrTPI_Jun,awapCorrTPI_Jul,awapCorrTPI_Aug,\
           awapCorrTPI_Sep,awapCorrTPI_Oct,awapCorrTPI_Nov,awapCorrTPI_Dec,\
           awapCorrTPI_Jan,awapCorrTPI_Feb,awapCorrTPI_Mar,awapCorrTPI_Apr,\
           awapCorrTPI_May) = corrIPO

R3corrENSO = R3CorrENSO_data()
(R3CorrENSO_annual, R3CorrENSO_JJA, R3CorrENSO_SON, R3CorrENSO_DJF,\
           R3CorrENSO_MAM,R3CorrENSO_Jun,R3CorrENSO_Jul,R3CorrENSO_Aug,\
           R3CorrENSO_Sep,R3CorrENSO_Oct,R3CorrENSO_Nov,R3CorrENSO_Dec,\
           R3CorrENSO_Jan,R3CorrENSO_Feb,R3CorrENSO_Mar,R3CorrENSO_Apr,\
           R3CorrENSO_May) = R3corrENSO

R3corrIPO = R3CorrTPI_data()
(R3CorrTPI_annual, R3CorrTPI_JJA, R3CorrTPI_SON, R3CorrTPI_DJF,\
           R3CorrTPI_MAM,R3CorrTPI_Jun,R3CorrTPI_Jul,R3CorrTPI_Aug,\
           R3CorrTPI_Sep,R3CorrTPI_Oct,R3CorrTPI_Nov,R3CorrTPI_Dec,\
           R3CorrTPI_Jan,R3CorrTPI_Feb,R3CorrTPI_Mar,R3CorrTPI_Apr,\
           R3CorrTPI_May) = R3corrIPO

#Generate correlation plots
accessR3_awap_corrENSO('R3')
accessR3_awap_corrIPO('R3')
corrDiffENSO_R3()
corrDiffTPI_R3()

#Make correlation coefficients available:
corrAverageENSO = corrAverageENSO()

corrAverageEastENSO = corrAverageEastENSO()
(corrEastENSO_annual, corrEastENSO_JJA,corrEastENSO_SON,\
           corrEastENSO_DJF,corrEastENSO_MAM,corrEastENSO_Jun,\
           corrEastENSO_Jul,corrEastENSO_Aug,corrEastENSO_Sep,\
           corrEastENSO_Oct,corrEastENSO_Nov,corrEastENSO_Dec,\
           corrEastENSO_Jan,corrEastENSO_Feb,corrEastENSO_Mar,\
           corrEastENSO_Apr,corrEastENSO_May) = corrAverageEastENSO

corrAverageTPI = corrAverageTPI()

corrAverageEastTPI = corrAverageEastTPI()
(corrEastTPI_annual, corrEastTPI_JJA,corrEastTPI_SON,\
           corrEastTPI_DJF,corrEastTPI_MAM,corrEastTPI_Jun,\
           corrEastTPI_Jul,corrEastTPI_Aug,corrEastTPI_Sep,\
           corrEastTPI_Oct,corrEastTPI_Nov,corrEastTPI_Dec,\
           corrEastTPI_Jan,corrEastTPI_Feb,corrEastTPI_Mar,\
           corrEastTPI_Apr,corrEastTPI_May) = corrAverageEastTPI

#Correlation coefficients to CSV:
np.savetxt('data/Correlation_coefficients/R3_corr_coef_ENSO_Aus.csv',corrAverageENSO,delimiter=',')

output2 = np.column_stack((corrEastENSO_annual, corrEastENSO_JJA,corrEastENSO_SON,\
           corrEastENSO_DJF,corrEastENSO_MAM,corrEastENSO_Jun,\
           corrEastENSO_Jul,corrEastENSO_Aug,corrEastENSO_Sep,\
           corrEastENSO_Oct,corrEastENSO_Nov,corrEastENSO_Dec,\
           corrEastENSO_Jan,corrEastENSO_Feb,corrEastENSO_Mar,\
           corrEastENSO_Apr,corrEastENSO_May))
np.savetxt('data/Correlation_coefficients/R3_corr_coef_ENSO_EastAus.csv',output2,delimiter=',')

np.savetxt('data/Correlation_coefficients/R3_corr_coef_TPI_Aus.csv',corrAverageTPI,delimiter=',')

output4 = np.column_stack((corrEastTPI_annual, corrEastTPI_JJA,corrEastTPI_SON,\
           corrEastTPI_DJF,corrEastTPI_MAM,corrEastTPI_Jun,\
           corrEastTPI_Jul,corrEastTPI_Aug,corrEastTPI_Sep,\
           corrEastTPI_Oct,corrEastTPI_Nov,corrEastTPI_Dec,\
           corrEastTPI_Jan,corrEastTPI_Feb,corrEastTPI_Mar,\
           corrEastTPI_Apr,corrEastTPI_May))
np.savetxt('data/Correlation_coefficients/R3_corr_coef_TPI_EastAus.csv',output4,delimiter=',')

