"""
A file to correlate ENSO with ACCESS R2 rainfall and the IPO with ACCESS R2
rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 7 October 2015.
"""

from correlation import *
from correlation_routine_awap import awapCorrENSO_data,awapCorrTPI_data

from access_trimmed import trim_Annual, trim_JJA,trim_SON,trim_DJF,trim_MAM,\
     trim_June, trim_July, trim_August, trim_September, trim_October, trim_November,\
     trim_December,trim_January,trim_February,trim_March,trim_April,trim_May

from indices_phase import enso_Jun_R2, enso_Jul_R2, enso_Aug_R2,\
     enso_Sep_R2, enso_Oct_R2, enso_Nov_R2,enso_Dec_R2,enso_Jan_R2,\
     enso_Feb_R2,enso_Mar_R2,enso_Apr_R2,enso_May_R2,IPO_R2_Jun,\
     IPO_R2_Jul,IPO_R2_Aug,IPO_R2_Sep,IPO_R2_Oct,IPO_R2_Nov,\
     IPO_R2_Dec,IPO_R2_Jan,IPO_R2_Feb,IPO_R2_Mar,IPO_R2_Apr,IPO_R2_May

from enso_csv import enso_JJA_R2, enso_SON_R2, enso_DJF_R2, enso_MAM_R2,\
     enso_Annual_R2

from tpi_csv import IPO_R2_JJA, IPO_R2_SON, IPO_R2_DJF, IPO_R2_MAM,\
     IPO_R2_Annual

# Plots correlation maps

def accessR2_awap_corrENSO(roundNum):
    plotCorr(trim_Annual,enso_Annual_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - annual",\
             "/correlation/nino_"+roundNum+"/annual")
    plotCorr(trim_JJA,enso_JJA_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - JJA",\
             "/correlation/nino_"+roundNum+"/JJA")
    plotCorr(trim_SON,enso_SON_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - SON",\
             "/correlation/nino_"+roundNum+"/SON")
    plotCorr(trim_DJF,enso_DJF_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - DJF",\
             "/correlation/nino_"+roundNum+"/DJF")
    plotCorr(trim_MAM,enso_MAM_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - MAM",\
             "/correlation/nino_"+roundNum+"/MAM")
    plotCorr(trim_June,enso_Jun_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - June",\
             "/correlation/nino_"+roundNum+"/June")
    plotCorr(trim_July,enso_Jul_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - July",\
             "/correlation/nino_"+roundNum+"/July")
    plotCorr(trim_August,enso_Aug_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - August",\
             "/correlation/nino_"+roundNum+"/August")
    plotCorr(trim_September,enso_Sep_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - September",\
             "/correlation/nino_"+roundNum+"/September")
    plotCorr(trim_October,enso_Oct_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - October",\
             "/correlation/nino_"+roundNum+"/October")
    plotCorr(trim_November,enso_Nov_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - November",\
             "/correlation/nino_"+roundNum+"/November")
    plotCorr(trim_December,enso_Dec_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - December",\
             "/correlation/nino_"+roundNum+"/December")
    plotCorr(trim_January,enso_Jan_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - January",\
             "/correlation/nino_"+roundNum+"/January")
    plotCorr(trim_February,enso_Feb_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - February",\
             "/correlation/nino_"+roundNum+"/February")
    plotCorr(trim_March,enso_Mar_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - March",\
             "/correlation/nino_"+roundNum+"/March")
    plotCorr(trim_April,enso_Apr_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - April",\
             "/correlation/nino_"+roundNum+"/April")
    plotCorr(trim_May,enso_May_R2,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - May",\
             "/correlation/nino_"+roundNum+"/May")
    return

def accessR2_awap_corrIPO(roundNum):
    plotCorr(trim_Annual,IPO_R2_Annual,"ACCESS "+roundNum+" rainfall-TPI correlation - annual",\
             "/correlation/tpi_"+roundNum+"/annual")
    plotCorr(trim_JJA,IPO_R2_JJA,"ACCESS "+roundNum+" rainfall-TPI correlation - JJA",\
             "/correlation/tpi_"+roundNum+"/JJA")
    plotCorr(trim_SON,IPO_R2_SON,"ACCESS "+roundNum+" rainfall-TPI correlation - SON",\
             "/correlation/tpi_"+roundNum+"/SON")
    plotCorr(trim_DJF,IPO_R2_DJF,"ACCESS "+roundNum+" rainfall-TPI correlation - DJF",\
             "/correlation/tpi_"+roundNum+"/DJF")
    plotCorr(trim_MAM,IPO_R2_MAM,"ACCESS "+roundNum+" rainfall-TPI correlation - MAM",\
             "/correlation/tpi_"+roundNum+"/MAM")
    plotCorr(trim_June,IPO_R2_Jun,"ACCESS "+roundNum+" rainfall-TPI correlation - June",\
             "/correlation/tpi_"+roundNum+"/June")
    plotCorr(trim_July,IPO_R2_Jul,"ACCESS "+roundNum+" rainfall-TPI correlation - July",\
             "/correlation/tpi_"+roundNum+"/July")
    plotCorr(trim_August,IPO_R2_Aug,"ACCESS "+roundNum+" rainfall-TPI correlation - August",\
             "/correlation/tpi_"+roundNum+"/August")
    plotCorr(trim_September,IPO_R2_Sep,"ACCESS "+roundNum+" rainfall-TPI correlation - September",\
             "/correlation/tpi_"+roundNum+"/September")
    plotCorr(trim_October,IPO_R2_Oct,"ACCESS "+roundNum+" rainfall-TPI correlation - October",\
             "/correlation/tpi_"+roundNum+"/October")
    plotCorr(trim_November,IPO_R2_Nov,"ACCESS "+roundNum+" rainfall-TPI correlation - November",\
             "/correlation/tpi_"+roundNum+"/November")
    plotCorr(trim_December,IPO_R2_Dec,"ACCESS "+roundNum+" rainfall-TPI correlation - December",\
             "/correlation/tpi_"+roundNum+"/December")
    plotCorr(trim_January,IPO_R2_Jan,"ACCESS "+roundNum+" rainfall-TPI correlation - January",\
             "/correlation/tpi_"+roundNum+"/January")
    plotCorr(trim_February,IPO_R2_Feb,"ACCESS "+roundNum+" rainfall-TPI correlation - February",\
             "/correlation/tpi_"+roundNum+"/February")
    plotCorr(trim_March,IPO_R2_Mar,"ACCESS "+roundNum+" rainfall-TPI correlation - March",\
             "/correlation/tpi_"+roundNum+"/March")
    plotCorr(trim_April,IPO_R2_Apr,"ACCESS "+roundNum+" rainfall-TPI correlation - April",\
             "/correlation/tpi_"+roundNum+"/April")
    plotCorr(trim_May,IPO_R2_May,"ACCESS "+roundNum+" rainfall-TPI correlation - May",\
             "/correlation/tpi_"+roundNum+"/May")
    return

#Single value correlation coefficients (Australia, East Australia, climate regions).

def corrAverageENSO():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    corrAvENSO_annual = corrAverage(trim_Annual,enso_Annual_R2)
    corrAvENSO_JJA = corrAverage(trim_JJA,enso_JJA_R2)
    corrAvENSO_SON = corrAverage(trim_SON,enso_SON_R2)
    corrAvENSO_DJF = corrAverage(trim_DJF,enso_DJF_R2)
    corrAvENSO_MAM = corrAverage(trim_MAM,enso_MAM_R2)
    corrAvENSO_Jun = corrAverage(trim_June,enso_Jun_R2)
    corrAvENSO_Jul = corrAverage(trim_July,enso_Jul_R2)
    corrAvENSO_Aug = corrAverage(trim_August,enso_Aug_R2)
    corrAvENSO_Sep = corrAverage(trim_September,enso_Sep_R2)
    corrAvENSO_Oct = corrAverage(trim_October,enso_Oct_R2)
    corrAvENSO_Nov = corrAverage(trim_November,enso_Nov_R2)
    corrAvENSO_Dec = corrAverage(trim_December,enso_Dec_R2)
    corrAvENSO_Jan = corrAverage(trim_January,enso_Jan_R2)
    corrAvENSO_Feb = corrAverage(trim_February,enso_Feb_R2)
    corrAvENSO_Mar = corrAverage(trim_March,enso_Mar_R2)
    corrAvENSO_Apr = corrAverage(trim_April,enso_Apr_R2)
    corrAvENSO_May = corrAverage(trim_May,enso_May_R2)
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
    corrEastENSO_annual = corrEastAus(trim_Annual,enso_Annual_R2)
    corrEastENSO_JJA = corrEastAus(trim_JJA,enso_JJA_R2)
    corrEastENSO_SON = corrEastAus(trim_SON,enso_SON_R2)
    corrEastENSO_DJF = corrEastAus(trim_DJF,enso_DJF_R2)
    corrEastENSO_MAM = corrEastAus(trim_MAM,enso_MAM_R2)
    corrEastENSO_Jun = corrEastAus(trim_June,enso_Jun_R2)
    corrEastENSO_Jul = corrEastAus(trim_July,enso_Jul_R2)
    corrEastENSO_Aug = corrEastAus(trim_August,enso_Aug_R2)
    corrEastENSO_Sep = corrEastAus(trim_September,enso_Sep_R2)
    corrEastENSO_Oct = corrEastAus(trim_October,enso_Oct_R2)
    corrEastENSO_Nov = corrEastAus(trim_November,enso_Nov_R2)
    corrEastENSO_Dec = corrEastAus(trim_December,enso_Dec_R2)
    corrEastENSO_Jan = corrEastAus(trim_January,enso_Jan_R2)
    corrEastENSO_Feb = corrEastAus(trim_February,enso_Feb_R2)
    corrEastENSO_Mar = corrEastAus(trim_March,enso_Mar_R2)
    corrEastENSO_Apr = corrEastAus(trim_April,enso_Apr_R2)
    corrEastENSO_May = corrEastAus(trim_May,enso_May_R2)
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
    corrAvTPI_annual = corrAverage(trim_Annual,IPO_R2_Annual)
    corrAvTPI_JJA = corrAverage(trim_JJA,IPO_R2_JJA)
    corrAvTPI_SON = corrAverage(trim_SON,IPO_R2_SON)
    corrAvTPI_DJF = corrAverage(trim_DJF,IPO_R2_DJF)
    corrAvTPI_MAM = corrAverage(trim_MAM,IPO_R2_MAM)
    corrAvTPI_Jun = corrAverage(trim_June,IPO_R2_Jun)
    corrAvTPI_Jul = corrAverage(trim_July,IPO_R2_Jul)
    corrAvTPI_Aug = corrAverage(trim_August,IPO_R2_Aug)
    corrAvTPI_Sep = corrAverage(trim_September,IPO_R2_Sep)
    corrAvTPI_Oct = corrAverage(trim_October,IPO_R2_Oct)
    corrAvTPI_Nov = corrAverage(trim_November,IPO_R2_Nov)
    corrAvTPI_Dec = corrAverage(trim_December,IPO_R2_Dec)
    corrAvTPI_Jan = corrAverage(trim_January,IPO_R2_Jan)
    corrAvTPI_Feb = corrAverage(trim_February,IPO_R2_Feb)
    corrAvTPI_Mar = corrAverage(trim_March,IPO_R2_Mar)
    corrAvTPI_Apr = corrAverage(trim_April,IPO_R2_Apr)
    corrAvTPI_May = corrAverage(trim_May,IPO_R2_May)
    return corrAvTPI_annual, corrAvTPI_JJA, corrAvTPI_SON, corrAvTPI_DJF,\
           corrAvTPI_MAM,corrAvTPI_Jun,corrAvTPI_Jul,corrAvTPI_Aug,\
           corrAvTPI_Sep,corrAvTPI_Oct,corrAvTPI_Nov,corrAvTPI_Dec,\
           corrAvTPI_Jan,corrAvTPI_Feb,corrAvTPI_Mar,corrAvTPI_Apr,\
           corrAvTPI_May

def corrAverageEastTPI():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    corrEastTPI_annual = corrEastAus(trim_Annual,IPO_R2_Annual)
    corrEastTPI_JJA = corrEastAus(trim_JJA,IPO_R2_JJA)
    corrEastTPI_SON = corrEastAus(trim_SON,IPO_R2_SON)
    corrEastTPI_DJF = corrEastAus(trim_DJF,IPO_R2_DJF)
    corrEastTPI_MAM = corrEastAus(trim_MAM,IPO_R2_MAM)
    corrEastTPI_Jun = corrEastAus(trim_June,IPO_R2_Jun)
    corrEastTPI_Jul = corrEastAus(trim_July,IPO_R2_Jul)
    corrEastTPI_Aug = corrEastAus(trim_August,IPO_R2_Aug)
    corrEastTPI_Sep = corrEastAus(trim_September,IPO_R2_Sep)
    corrEastTPI_Oct = corrEastAus(trim_October,IPO_R2_Oct)
    corrEastTPI_Nov = corrEastAus(trim_November,IPO_R2_Nov)
    corrEastTPI_Dec = corrEastAus(trim_December,IPO_R2_Dec)
    corrEastTPI_Jan = corrEastAus(trim_January,IPO_R2_Jan)
    corrEastTPI_Feb = corrEastAus(trim_February,IPO_R2_Feb)
    corrEastTPI_Mar = corrEastAus(trim_March,IPO_R2_Mar)
    corrEastTPI_Apr = corrEastAus(trim_April,IPO_R2_Apr)
    corrEastTPI_May = corrEastAus(trim_May,IPO_R2_May)
    return corrEastTPI_annual, corrEastTPI_JJA, corrEastTPI_SON, corrEastTPI_DJF,\
           corrEastTPI_MAM,corrEastTPI_Jun,corrEastTPI_Jul,corrEastTPI_Aug,\
           corrEastTPI_Sep,corrEastTPI_Oct,corrEastTPI_Nov,corrEastTPI_Dec,\
           corrEastTPI_Jan,corrEastTPI_Feb,corrEastTPI_Mar,corrEastTPI_Apr,\
           corrEastTPI_May

# Makes data available for plotting correlation difference maps.

def R2CorrENSO_data():
    R2CorrENSO_annual = corr(trim_Annual,enso_Annual_R2)
    R2CorrENSO_JJA = corr(trim_JJA,enso_JJA_R2)
    R2CorrENSO_SON = corr(trim_SON,enso_SON_R2)
    R2CorrENSO_DJF = corr(trim_DJF,enso_DJF_R2)
    R2CorrENSO_MAM = corr(trim_MAM,enso_MAM_R2)
    R2CorrENSO_Jun = corr(trim_June,IPO_R2_Jun)
    R2CorrENSO_Jul = corr(trim_July,IPO_R2_Jul)
    R2CorrENSO_Aug = corr(trim_August,IPO_R2_Aug)
    R2CorrENSO_Sep = corr(trim_September,IPO_R2_Sep)
    R2CorrENSO_Oct = corr(trim_October,IPO_R2_Oct)
    R2CorrENSO_Nov = corr(trim_November,IPO_R2_Nov)
    R2CorrENSO_Dec = corr(trim_December,IPO_R2_Dec)
    R2CorrENSO_Jan = corr(trim_January,IPO_R2_Jan)
    R2CorrENSO_Feb = corr(trim_February,IPO_R2_Feb)
    R2CorrENSO_Mar = corr(trim_March,IPO_R2_Mar)
    R2CorrENSO_Apr = corr(trim_April,IPO_R2_Apr)
    R2CorrENSO_May = corr(trim_May,IPO_R2_May)
    return R2CorrENSO_annual, R2CorrENSO_JJA, R2CorrENSO_SON, R2CorrENSO_DJF,\
           R2CorrENSO_MAM,R2CorrENSO_Jun,R2CorrENSO_Jul,R2CorrENSO_Aug,\
           R2CorrENSO_Sep,R2CorrENSO_Oct,R2CorrENSO_Nov,R2CorrENSO_Dec,\
           R2CorrENSO_Jan,R2CorrENSO_Feb,R2CorrENSO_Mar,R2CorrENSO_Apr,\
           R2CorrENSO_May

def R2CorrTPI_data():
    R2CorrTPI_annual = corr(trim_Annual,IPO_R2_Annual)
    R2CorrTPI_JJA = corr(trim_JJA,IPO_R2_JJA)
    R2CorrTPI_SON = corr(trim_SON,IPO_R2_SON)
    R2CorrTPI_DJF = corr(trim_DJF,IPO_R2_DJF)
    R2CorrTPI_MAM = corr(trim_MAM,IPO_R2_MAM)
    R2CorrTPI_Jun = corr(trim_June,IPO_R2_Jun)
    R2CorrTPI_Jul = corr(trim_July,IPO_R2_Jul)
    R2CorrTPI_Aug = corr(trim_August,IPO_R2_Aug)
    R2CorrTPI_Sep = corr(trim_September,IPO_R2_Sep)
    R2CorrTPI_Oct = corr(trim_October,IPO_R2_Oct)
    R2CorrTPI_Nov = corr(trim_November,IPO_R2_Nov)
    R2CorrTPI_Dec = corr(trim_December,IPO_R2_Dec)
    R2CorrTPI_Jan = corr(trim_January,IPO_R2_Jan)
    R2CorrTPI_Feb = corr(trim_February,IPO_R2_Feb)
    R2CorrTPI_Mar = corr(trim_March,IPO_R2_Mar)
    R2CorrTPI_Apr = corr(trim_April,IPO_R2_Apr)
    R2CorrTPI_May = corr(trim_May,IPO_R2_May)
    return R2CorrTPI_annual, R2CorrTPI_JJA, R2CorrTPI_SON, R2CorrTPI_DJF,\
           R2CorrTPI_MAM,R2CorrTPI_Jun,R2CorrTPI_Jul,R2CorrTPI_Aug,\
           R2CorrTPI_Sep,R2CorrTPI_Oct,R2CorrTPI_Nov,R2CorrTPI_Dec,\
           R2CorrTPI_Jan,R2CorrTPI_Feb,R2CorrTPI_Mar,R2CorrTPI_Apr,\
           R2CorrTPI_May

#Plots Difference in AWAP and ACCESS R2 correlation maps.

def corrDiffENSO_R2():
    plotCorrDiff(awapCorrENSO_annual,R2CorrENSO_annual,"Difference in AWAP and R2 correlations, ENSO - annual",\
             "/correlation/diff_nino_R2/annual")
    plotCorrDiff(awapCorrENSO_JJA,R2CorrENSO_JJA,"Difference in AWAP and R2 correlations, ENSO - JJA",\
             "/correlation/diff_nino_R2/JJA")
    plotCorrDiff(awapCorrENSO_SON,R2CorrENSO_SON,"Difference in AWAP and R2 correlations, ENSO - SON",\
             "/correlation/diff_nino_R2/SON")
    plotCorrDiff(awapCorrENSO_DJF,R2CorrENSO_DJF,"Difference in AWAP and R2 correlations, ENSO - DJF",\
             "/correlation/diff_nino_R2/DJF")
    plotCorrDiff(awapCorrENSO_MAM,R2CorrENSO_MAM,"Difference in AWAP and R2 correlations, ENSO - MAM",\
             "/correlation/diff_nino_R2/MAM")
    plotCorrDiff(awapCorrENSO_Jun,R2CorrENSO_Jun,"Difference in AWAP and R2 correlations, ENSO - June",\
             "/correlation/diff_nino_R2/June")
    plotCorrDiff(awapCorrENSO_Jul,R2CorrENSO_Jul,"Difference in AWAP and R2 correlations, ENSO - July",\
             "/correlation/diff_nino_R2/July")
    plotCorrDiff(awapCorrENSO_Aug,R2CorrENSO_Aug,"Difference in AWAP and R2 correlations, ENSO - August",\
             "/correlation/diff_nino_R2/August")
    plotCorrDiff(awapCorrENSO_Sep,R2CorrENSO_Sep,"Difference in AWAP and R2 correlations, ENSO - September",\
             "/correlation/diff_nino_R2/September")
    plotCorrDiff(awapCorrENSO_Oct,R2CorrENSO_Oct,"Difference in AWAP and R2 correlations, ENSO - October",\
             "/correlation/diff_nino_R2/October")
    plotCorrDiff(awapCorrENSO_Nov,R2CorrENSO_Nov,"Difference in AWAP and R2 correlations, ENSO - November",\
             "/correlation/diff_nino_R2/November")
    plotCorrDiff(awapCorrENSO_Dec,R2CorrENSO_Dec,"Difference in AWAP and R2 correlations, ENSO - December",\
             "/correlation/diff_nino_R2/December")
    plotCorrDiff(awapCorrENSO_Jan,R2CorrENSO_Jan,"Difference in AWAP and R2 correlations, ENSO - January",\
             "/correlation/diff_nino_R2/January")
    plotCorrDiff(awapCorrENSO_Feb,R2CorrENSO_Feb,"Difference in AWAP and R2 correlations, ENSO - February",\
             "/correlation/diff_nino_R2/February")
    plotCorrDiff(awapCorrENSO_Mar,R2CorrENSO_Mar,"Difference in AWAP and R2 correlations, ENSO - March",\
             "/correlation/diff_nino_R2/March")
    plotCorrDiff(awapCorrENSO_Apr,R2CorrENSO_Apr,"Difference in AWAP and R2 correlations, ENSO - April",\
             "/correlation/diff_nino_R2/April")
    plotCorrDiff(awapCorrENSO_May,R2CorrENSO_May,"Difference in AWAP and R2 correlations, ENSO - May",\
             "/correlation/diff_nino_R2/May")
    return

def corrDiffTPI_R2():
    plotCorrDiff(awapCorrTPI_annual,R2CorrTPI_annual,"Difference in AWAP and R2 correlations, IPO - annual",\
             "/correlation/diff_tpi_R2/annual")
    plotCorrDiff(awapCorrTPI_JJA,R2CorrTPI_JJA,"Difference in AWAP and R2 correlations, IPO - JJA",\
             "/correlation/diff_tpi_R2/JJA")
    plotCorrDiff(awapCorrTPI_SON,R2CorrTPI_SON,"Difference in AWAP and R2 correlations, IPO - SON",\
             "/correlation/diff_tpi_R2/SON")
    plotCorrDiff(awapCorrTPI_DJF,R2CorrTPI_DJF,"Difference in AWAP and R2 correlations, IPO - DJF",\
             "/correlation/diff_tpi_R2/DJF")
    plotCorrDiff(awapCorrTPI_MAM,R2CorrTPI_MAM,"Difference in AWAP and R2 correlations, IPO - MAM",\
             "/correlation/diff_tpi_R2/MAM")
    plotCorrDiff(awapCorrTPI_Jun,R2CorrTPI_Jun,"Difference in AWAP and R2 correlations, IPO - June",\
             "/correlation/diff_tpi_R2/June")
    plotCorrDiff(awapCorrTPI_Jul,R2CorrTPI_Jul,"Difference in AWAP and R2 correlations, IPO - July",\
             "/correlation/diff_tpi_R2/July")
    plotCorrDiff(awapCorrTPI_Aug,R2CorrTPI_Aug,"Difference in AWAP and R2 correlations, IPO - August",\
             "/correlation/diff_tpi_R2/August")
    plotCorrDiff(awapCorrTPI_Sep,R2CorrTPI_Sep,"Difference in AWAP and R2 correlations, IPO - September",\
             "/correlation/diff_tpi_R2/September")
    plotCorrDiff(awapCorrTPI_Oct,R2CorrTPI_Oct,"Difference in AWAP and R2 correlations, IPO - October",\
             "/correlation/diff_tpi_R2/October")
    plotCorrDiff(awapCorrTPI_Nov,R2CorrTPI_Nov,"Difference in AWAP and R2 correlations, IPO - November",\
             "/correlation/diff_tpi_R2/November")
    plotCorrDiff(awapCorrTPI_Dec,R2CorrTPI_Dec,"Difference in AWAP and R2 correlations, IPO - December",\
             "/correlation/diff_tpi_R2/December")
    plotCorrDiff(awapCorrTPI_Jan,R2CorrTPI_Jan,"Difference in AWAP and R2 correlations, IPO - January",\
             "/correlation/diff_tpi_R2/January")
    plotCorrDiff(awapCorrTPI_Feb,R2CorrTPI_Feb,"Difference in AWAP and R2 correlations, IPO - February",\
             "/correlation/diff_tpi_R2/February")
    plotCorrDiff(awapCorrTPI_Mar,R2CorrTPI_Mar,"Difference in AWAP and R2 correlations, IPO - March",\
             "/correlation/diff_tpi_R2/March")
    plotCorrDiff(awapCorrTPI_Apr,R2CorrTPI_Apr,"Difference in AWAP and R2 correlations, IPO - April",\
             "/correlation/diff_tpi_R2/April")
    plotCorrDiff(awapCorrTPI_May,R2CorrTPI_May,"Difference in AWAP and R2 correlations, IPO - May",\
             "/correlation/diff_tpi_R2/May")
    return

#Make ACCESS R2 data available as a list; creates an array of rainfall averages
rainfall_R2 = [trim_June, trim_July, trim_August, trim_September, trim_October, trim_November,\
      trim_December,trim_January,trim_February,trim_March,trim_April,trim_May,\
      trim_JJA,trim_SON,trim_DJF,trim_MAM,trim_Annual]

rainfall_R2_average = averageArray(rainfall_R2)

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

R2corrENSO = R2CorrENSO_data()
(R2CorrENSO_annual, R2CorrENSO_JJA, R2CorrENSO_SON, R2CorrENSO_DJF,\
           R2CorrENSO_MAM,R2CorrENSO_Jun,R2CorrENSO_Jul,R2CorrENSO_Aug,\
           R2CorrENSO_Sep,R2CorrENSO_Oct,R2CorrENSO_Nov,R2CorrENSO_Dec,\
           R2CorrENSO_Jan,R2CorrENSO_Feb,R2CorrENSO_Mar,R2CorrENSO_Apr,\
           R2CorrENSO_May) = R2corrENSO

R2corrIPO = R2CorrTPI_data()
(R2CorrTPI_annual, R2CorrTPI_JJA, R2CorrTPI_SON, R2CorrTPI_DJF,\
           R2CorrTPI_MAM,R2CorrTPI_Jun,R2CorrTPI_Jul,R2CorrTPI_Aug,\
           R2CorrTPI_Sep,R2CorrTPI_Oct,R2CorrTPI_Nov,R2CorrTPI_Dec,\
           R2CorrTPI_Jan,R2CorrTPI_Feb,R2CorrTPI_Mar,R2CorrTPI_Apr,\
           R2CorrTPI_May) = R2corrIPO

#Generate correlation plots
accessR2_awap_corrENSO('R2')
accessR2_awap_corrIPO('R2')
corrDiffENSO_R2()
corrDiffTPI_R2()

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
np.savetxt('data/Correlation_coefficients/R2_corr_coef_ENSO_Aus.csv',corrAverageENSO,delimiter=',')

output2 = np.column_stack((corrEastENSO_annual, corrEastENSO_JJA,corrEastENSO_SON,\
           corrEastENSO_DJF,corrEastENSO_MAM,corrEastENSO_Jun,\
           corrEastENSO_Jul,corrEastENSO_Aug,corrEastENSO_Sep,\
           corrEastENSO_Oct,corrEastENSO_Nov,corrEastENSO_Dec,\
           corrEastENSO_Jan,corrEastENSO_Feb,corrEastENSO_Mar,\
           corrEastENSO_Apr,corrEastENSO_May))
np.savetxt('data/Correlation_coefficients/R2_corr_coef_ENSO_EastAus.csv',output2,delimiter=',')

np.savetxt('data/Correlation_coefficients/R2_corr_coef_TPI_Aus.csv',corrAverageTPI,delimiter=',')

output4 = np.column_stack((corrEastTPI_annual, corrEastTPI_JJA,corrEastTPI_SON,\
           corrEastTPI_DJF,corrEastTPI_MAM,corrEastTPI_Jun,\
           corrEastTPI_Jul,corrEastTPI_Aug,corrEastTPI_Sep,\
           corrEastTPI_Oct,corrEastTPI_Nov,corrEastTPI_Dec,\
           corrEastTPI_Jan,corrEastTPI_Feb,corrEastTPI_Mar,\
           corrEastTPI_Apr,corrEastTPI_May))
np.savetxt('data/Correlation_coefficients/R2_corr_coef_TPI_EastAus.csv',output4,delimiter=',')

