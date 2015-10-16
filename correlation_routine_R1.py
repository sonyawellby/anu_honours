"""
A file to correlate ENSO with ACCESS R1 rainfall and the IPO with ACCESS R1
rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 7 October 2015.
"""

from correlation import *
from correlation_routine_awap import awapCorrENSO_data,awapCorrTPI_data

from access_trimmed import trim_Annual, trim_JJA,trim_SON,trim_DJF,trim_MAM,\
     trim_June, trim_July, trim_August, trim_September, trim_October, trim_November,\
     trim_December,trim_January,trim_February,trim_March,trim_April,trim_May

from indices_phase import enso_Jun_R1, enso_Jul_R1, enso_Aug_R1,\
     enso_Sep_R1, enso_Oct_R1, enso_Nov_R1,enso_Dec_R1,enso_Jan_R1,\
     enso_Feb_R1,enso_Mar_R1,enso_Apr_R1,enso_May_R1,IPO_R1_Jun,\
     IPO_R1_Jul,IPO_R1_Aug,IPO_R1_Sep,IPO_R1_Oct,IPO_R1_Nov,\
     IPO_R1_Dec,IPO_R1_Jan,IPO_R1_Feb,IPO_R1_Mar,IPO_R1_Apr,IPO_R1_May

from enso_csv import enso_JJA_R1, enso_SON_R1, enso_DJF_R1, enso_MAM_R1,\
     enso_Annual_R1

from tpi_csv import IPO_R1_JJA, IPO_R1_SON, IPO_R1_DJF, IPO_R1_MAM,\
     IPO_R1_Annual


# Plots correlation maps

def accessR1_awap_corrENSO(roundNum):
    plotCorr(trim_Annual,enso_Annual_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - annual",\
             "/correlation/nino_"+roundNum+"/annual")
    plotCorr(trim_JJA,enso_JJA_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - JJA",\
             "/correlation/nino_"+roundNum+"/JJA")
    plotCorr(trim_SON,enso_SON_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - SON",\
             "/correlation/nino_"+roundNum+"/SON")
    plotCorr(trim_DJF,enso_DJF_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - DJF",\
             "/correlation/nino_"+roundNum+"/DJF")
    plotCorr(trim_MAM,enso_MAM_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - MAM",\
             "/correlation/nino_"+roundNum+"/MAM")
    plotCorr(trim_June,enso_Jun_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - June",\
             "/correlation/nino_"+roundNum+"/June")
    plotCorr(trim_July,enso_Jul_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - July",\
             "/correlation/nino_"+roundNum+"/July")
    plotCorr(trim_August,enso_Aug_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - August",\
             "/correlation/nino_"+roundNum+"/August")
    plotCorr(trim_September,enso_Sep_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - September",\
             "/correlation/nino_"+roundNum+"/September")
    plotCorr(trim_October,enso_Oct_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - October",\
             "/correlation/nino_"+roundNum+"/October")
    plotCorr(trim_November,enso_Nov_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - November",\
             "/correlation/nino_"+roundNum+"/November")
    plotCorr(trim_December,enso_Dec_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - December",\
             "/correlation/nino_"+roundNum+"/December")
    plotCorr(trim_January,enso_Jan_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - January",\
             "/correlation/nino_"+roundNum+"/January")
    plotCorr(trim_February,enso_Feb_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - February",\
             "/correlation/nino_"+roundNum+"/February")
    plotCorr(trim_March,enso_Mar_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - March",\
             "/correlation/nino_"+roundNum+"/March")
    plotCorr(trim_April,enso_Apr_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - April",\
             "/correlation/nino_"+roundNum+"/April")
    plotCorr(trim_May,enso_May_R1,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - May",\
             "/correlation/nino_"+roundNum+"/May")
    return

def accessR1_awap_corrIPO(roundNum):
    plotCorr(trim_Annual,IPO_R1_Annual,"ACCESS "+roundNum+" rainfall-TPI correlation - annual",\
             "/correlation/tpi_"+roundNum+"/annual")
    plotCorr(trim_JJA,IPO_R1_JJA,"ACCESS "+roundNum+" rainfall-TPI correlation - JJA",\
             "/correlation/tpi_"+roundNum+"/JJA")
    plotCorr(trim_SON,IPO_R1_SON,"ACCESS "+roundNum+" rainfall-TPI correlation - SON",\
             "/correlation/tpi_"+roundNum+"/SON")
    plotCorr(trim_DJF,IPO_R1_DJF,"ACCESS "+roundNum+" rainfall-TPI correlation - DJF",\
             "/correlation/tpi_"+roundNum+"/DJF")
    plotCorr(trim_MAM,IPO_R1_MAM,"ACCESS "+roundNum+" rainfall-TPI correlation - MAM",\
             "/correlation/tpi_"+roundNum+"/MAM")
    plotCorr(trim_June,IPO_R1_Jun,"ACCESS "+roundNum+" rainfall-TPI correlation - June",\
             "/correlation/tpi_"+roundNum+"/June")
    plotCorr(trim_July,IPO_R1_Jul,"ACCESS "+roundNum+" rainfall-TPI correlation - July",\
             "/correlation/tpi_"+roundNum+"/July")
    plotCorr(trim_August,IPO_R1_Aug,"ACCESS "+roundNum+" rainfall-TPI correlation - August",\
             "/correlation/tpi_"+roundNum+"/August")
    plotCorr(trim_September,IPO_R1_Sep,"ACCESS "+roundNum+" rainfall-TPI correlation - September",\
             "/correlation/tpi_"+roundNum+"/September")
    plotCorr(trim_October,IPO_R1_Oct,"ACCESS "+roundNum+" rainfall-TPI correlation - October",\
             "/correlation/tpi_"+roundNum+"/October")
    plotCorr(trim_November,IPO_R1_Nov,"ACCESS "+roundNum+" rainfall-TPI correlation - November",\
             "/correlation/tpi_"+roundNum+"/November")
    plotCorr(trim_December,IPO_R1_Dec,"ACCESS "+roundNum+" rainfall-TPI correlation - December",\
             "/correlation/tpi_"+roundNum+"/December")
    plotCorr(trim_January,IPO_R1_Jan,"ACCESS "+roundNum+" rainfall-TPI correlation - January",\
             "/correlation/tpi_"+roundNum+"/January")
    plotCorr(trim_February,IPO_R1_Feb,"ACCESS "+roundNum+" rainfall-TPI correlation - February",\
             "/correlation/tpi_"+roundNum+"/February")
    plotCorr(trim_March,IPO_R1_Mar,"ACCESS "+roundNum+" rainfall-TPI correlation - March",\
             "/correlation/tpi_"+roundNum+"/March")
    plotCorr(trim_April,IPO_R1_Apr,"ACCESS "+roundNum+" rainfall-TPI correlation - April",\
             "/correlation/tpi_"+roundNum+"/April")
    plotCorr(trim_May,IPO_R1_May,"ACCESS "+roundNum+" rainfall-TPI correlation - May",\
             "/correlation/tpi_"+roundNum+"/May")
    return

#Single value correlation coefficients (Australia, East Australia, climate regions).

def corrAverageENSO():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    corrAvENSO_annual = corrAverage(trim_Annual,enso_Annual_R1)
    corrAvENSO_JJA = corrAverage(trim_JJA,enso_JJA_R1)
    corrAvENSO_SON = corrAverage(trim_SON,enso_SON_R1)
    corrAvENSO_DJF = corrAverage(trim_DJF,enso_DJF_R1)
    corrAvENSO_MAM = corrAverage(trim_MAM,enso_MAM_R1)
    corrAvENSO_Jun = corrAverage(trim_June,enso_Jun_R1)
    corrAvENSO_Jul = corrAverage(trim_July,enso_Jul_R1)
    corrAvENSO_Aug = corrAverage(trim_August,enso_Aug_R1)
    corrAvENSO_Sep = corrAverage(trim_September,enso_Sep_R1)
    corrAvENSO_Oct = corrAverage(trim_October,enso_Oct_R1)
    corrAvENSO_Nov = corrAverage(trim_November,enso_Nov_R1)
    corrAvENSO_Dec = corrAverage(trim_December,enso_Dec_R1)
    corrAvENSO_Jan = corrAverage(trim_January,enso_Jan_R1)
    corrAvENSO_Feb = corrAverage(trim_February,enso_Feb_R1)
    corrAvENSO_Mar = corrAverage(trim_March,enso_Mar_R1)
    corrAvENSO_Apr = corrAverage(trim_April,enso_Apr_R1)
    corrAvENSO_May = corrAverage(trim_May,enso_May_R1)
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
    corrEastENSO_annual = corrEastAus(trim_Annual,enso_Annual_R1)
    corrEastENSO_JJA = corrEastAus(trim_JJA,enso_JJA_R1)
    corrEastENSO_SON = corrEastAus(trim_SON,enso_SON_R1)
    corrEastENSO_DJF = corrEastAus(trim_DJF,enso_DJF_R1)
    corrEastENSO_MAM = corrEastAus(trim_MAM,enso_MAM_R1)
    corrEastENSO_Jun = corrEastAus(trim_June,enso_Jun_R1)
    corrEastENSO_Jul = corrEastAus(trim_July,enso_Jul_R1)
    corrEastENSO_Aug = corrEastAus(trim_August,enso_Aug_R1)
    corrEastENSO_Sep = corrEastAus(trim_September,enso_Sep_R1)
    corrEastENSO_Oct = corrEastAus(trim_October,enso_Oct_R1)
    corrEastENSO_Nov = corrEastAus(trim_November,enso_Nov_R1)
    corrEastENSO_Dec = corrEastAus(trim_December,enso_Dec_R1)
    corrEastENSO_Jan = corrEastAus(trim_January,enso_Jan_R1)
    corrEastENSO_Feb = corrEastAus(trim_February,enso_Feb_R1)
    corrEastENSO_Mar = corrEastAus(trim_March,enso_Mar_R1)
    corrEastENSO_Apr = corrEastAus(trim_April,enso_Apr_R1)
    corrEastENSO_May = corrEastAus(trim_May,enso_May_R1)
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
    corrAvTPI_annual = corrAverage(trim_Annual,IPO_R1_Annual)
    corrAvTPI_JJA = corrAverage(trim_JJA,IPO_R1_JJA)
    corrAvTPI_SON = corrAverage(trim_SON,IPO_R1_SON)
    corrAvTPI_DJF = corrAverage(trim_DJF,IPO_R1_DJF)
    corrAvTPI_MAM = corrAverage(trim_MAM,IPO_R1_MAM)
    corrAvTPI_Jun = corrAverage(trim_June,IPO_R1_Jun)
    corrAvTPI_Jul = corrAverage(trim_July,IPO_R1_Jul)
    corrAvTPI_Aug = corrAverage(trim_August,IPO_R1_Aug)
    corrAvTPI_Sep = corrAverage(trim_September,IPO_R1_Sep)
    corrAvTPI_Oct = corrAverage(trim_October,IPO_R1_Oct)
    corrAvTPI_Nov = corrAverage(trim_November,IPO_R1_Nov)
    corrAvTPI_Dec = corrAverage(trim_December,IPO_R1_Dec)
    corrAvTPI_Jan = corrAverage(trim_January,IPO_R1_Jan)
    corrAvTPI_Feb = corrAverage(trim_February,IPO_R1_Feb)
    corrAvTPI_Mar = corrAverage(trim_March,IPO_R1_Mar)
    corrAvTPI_Apr = corrAverage(trim_April,IPO_R1_Apr)
    corrAvTPI_May = corrAverage(trim_May,IPO_R1_May)
    return corrAvTPI_annual, corrAvTPI_JJA, corrAvTPI_SON, corrAvTPI_DJF,\
           corrAvTPI_MAM,corrAvTPI_Jun,corrAvTPI_Jul,corrAvTPI_Aug,\
           corrAvTPI_Sep,corrAvTPI_Oct,corrAvTPI_Nov,corrAvTPI_Dec,\
           corrAvTPI_Jan,corrAvTPI_Feb,corrAvTPI_Mar,corrAvTPI_Apr,\
           corrAvTPI_May

def corrAverageEastTPI():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    corrEastTPI_annual = corrEastAus(trim_Annual,IPO_R1_Annual)
    corrEastTPI_JJA = corrEastAus(trim_JJA,IPO_R1_JJA)
    corrEastTPI_SON = corrEastAus(trim_SON,IPO_R1_SON)
    corrEastTPI_DJF = corrEastAus(trim_DJF,IPO_R1_DJF)
    corrEastTPI_MAM = corrEastAus(trim_MAM,IPO_R1_MAM)
    corrEastTPI_Jun = corrEastAus(trim_June,IPO_R1_Jun)
    corrEastTPI_Jul = corrEastAus(trim_July,IPO_R1_Jul)
    corrEastTPI_Aug = corrEastAus(trim_August,IPO_R1_Aug)
    corrEastTPI_Sep = corrEastAus(trim_September,IPO_R1_Sep)
    corrEastTPI_Oct = corrEastAus(trim_October,IPO_R1_Oct)
    corrEastTPI_Nov = corrEastAus(trim_November,IPO_R1_Nov)
    corrEastTPI_Dec = corrEastAus(trim_December,IPO_R1_Dec)
    corrEastTPI_Jan = corrEastAus(trim_January,IPO_R1_Jan)
    corrEastTPI_Feb = corrEastAus(trim_February,IPO_R1_Feb)
    corrEastTPI_Mar = corrEastAus(trim_March,IPO_R1_Mar)
    corrEastTPI_Apr = corrEastAus(trim_April,IPO_R1_Apr)
    corrEastTPI_May = corrEastAus(trim_May,IPO_R1_May)
    return corrEastTPI_annual, corrEastTPI_JJA, corrEastTPI_SON, corrEastTPI_DJF,\
           corrEastTPI_MAM,corrEastTPI_Jun,corrEastTPI_Jul,corrEastTPI_Aug,\
           corrEastTPI_Sep,corrEastTPI_Oct,corrEastTPI_Nov,corrEastTPI_Dec,\
           corrEastTPI_Jan,corrEastTPI_Feb,corrEastTPI_Mar,corrEastTPI_Apr,\
           corrEastTPI_May

# Makes data available for plotting correlation difference maps.

def R1CorrENSO_data():
    R1CorrENSO_annual = corr(trim_Annual,enso_Annual_R1)
    R1CorrENSO_JJA = corr(trim_JJA,enso_JJA_R1)
    R1CorrENSO_SON = corr(trim_SON,enso_SON_R1)
    R1CorrENSO_DJF = corr(trim_DJF,enso_DJF_R1)
    R1CorrENSO_MAM = corr(trim_MAM,enso_MAM_R1)
    R1CorrENSO_Jun = corr(trim_June,IPO_R1_Jun)
    R1CorrENSO_Jul = corr(trim_July,IPO_R1_Jul)
    R1CorrENSO_Aug = corr(trim_August,IPO_R1_Aug)
    R1CorrENSO_Sep = corr(trim_September,IPO_R1_Sep)
    R1CorrENSO_Oct = corr(trim_October,IPO_R1_Oct)
    R1CorrENSO_Nov = corr(trim_November,IPO_R1_Nov)
    R1CorrENSO_Dec = corr(trim_December,IPO_R1_Dec)
    R1CorrENSO_Jan = corr(trim_January,IPO_R1_Jan)
    R1CorrENSO_Feb = corr(trim_February,IPO_R1_Feb)
    R1CorrENSO_Mar = corr(trim_March,IPO_R1_Mar)
    R1CorrENSO_Apr = corr(trim_April,IPO_R1_Apr)
    R1CorrENSO_May = corr(trim_May,IPO_R1_May)
    return R1CorrENSO_annual, R1CorrENSO_JJA, R1CorrENSO_SON, R1CorrENSO_DJF,\
           R1CorrENSO_MAM,R1CorrENSO_Jun,R1CorrENSO_Jul,R1CorrENSO_Aug,\
           R1CorrENSO_Sep,R1CorrENSO_Oct,R1CorrENSO_Nov,R1CorrENSO_Dec,\
           R1CorrENSO_Jan,R1CorrENSO_Feb,R1CorrENSO_Mar,R1CorrENSO_Apr,\
           R1CorrENSO_May

def R1CorrTPI_data():
    R1CorrTPI_annual = corr(trim_Annual,IPO_R1_Annual)
    R1CorrTPI_JJA = corr(trim_JJA,IPO_R1_JJA)
    R1CorrTPI_SON = corr(trim_SON,IPO_R1_SON)
    R1CorrTPI_DJF = corr(trim_DJF,IPO_R1_DJF)
    R1CorrTPI_MAM = corr(trim_MAM,IPO_R1_MAM)
    R1CorrTPI_Jun = corr(trim_June,IPO_R1_Jun)
    R1CorrTPI_Jul = corr(trim_July,IPO_R1_Jul)
    R1CorrTPI_Aug = corr(trim_August,IPO_R1_Aug)
    R1CorrTPI_Sep = corr(trim_September,IPO_R1_Sep)
    R1CorrTPI_Oct = corr(trim_October,IPO_R1_Oct)
    R1CorrTPI_Nov = corr(trim_November,IPO_R1_Nov)
    R1CorrTPI_Dec = corr(trim_December,IPO_R1_Dec)
    R1CorrTPI_Jan = corr(trim_January,IPO_R1_Jan)
    R1CorrTPI_Feb = corr(trim_February,IPO_R1_Feb)
    R1CorrTPI_Mar = corr(trim_March,IPO_R1_Mar)
    R1CorrTPI_Apr = corr(trim_April,IPO_R1_Apr)
    R1CorrTPI_May = corr(trim_May,IPO_R1_May)
    return R1CorrTPI_annual, R1CorrTPI_JJA, R1CorrTPI_SON, R1CorrTPI_DJF,\
           R1CorrTPI_MAM,R1CorrTPI_Jun,R1CorrTPI_Jul,R1CorrTPI_Aug,\
           R1CorrTPI_Sep,R1CorrTPI_Oct,R1CorrTPI_Nov,R1CorrTPI_Dec,\
           R1CorrTPI_Jan,R1CorrTPI_Feb,R1CorrTPI_Mar,R1CorrTPI_Apr,\
           R1CorrTPI_May

#Plots Difference in AWAP and ACCESS R1 correlation maps.

def corrDiffENSO_R1():
    plotCorrDiff(awapCorrENSO_annual,R1CorrENSO_annual,"Difference in AWAP and R1 correlations, ENSO - annual",\
             "/correlation/diff_nino_R1/annual")
    plotCorrDiff(awapCorrENSO_JJA,R1CorrENSO_JJA,"Difference in AWAP and R1 correlations, ENSO - JJA",\
             "/correlation/diff_nino_R1/JJA")
    plotCorrDiff(awapCorrENSO_SON,R1CorrENSO_SON,"Difference in AWAP and R1 correlations, ENSO - SON",\
             "/correlation/diff_nino_R1/SON")
    plotCorrDiff(awapCorrENSO_DJF,R1CorrENSO_DJF,"Difference in AWAP and R1 correlations, ENSO - DJF",\
             "/correlation/diff_nino_R1/DJF")
    plotCorrDiff(awapCorrENSO_MAM,R1CorrENSO_MAM,"Difference in AWAP and R1 correlations, ENSO - MAM",\
             "/correlation/diff_nino_R1/MAM")
    plotCorrDiff(awapCorrENSO_Jun,R1CorrENSO_Jun,"Difference in AWAP and R1 correlations, ENSO - June",\
             "/correlation/diff_nino_R1/June")
    plotCorrDiff(awapCorrENSO_Jul,R1CorrENSO_Jul,"Difference in AWAP and R1 correlations, ENSO - July",\
             "/correlation/diff_nino_R1/July")
    plotCorrDiff(awapCorrENSO_Aug,R1CorrENSO_Aug,"Difference in AWAP and R1 correlations, ENSO - August",\
             "/correlation/diff_nino_R1/August")
    plotCorrDiff(awapCorrENSO_Sep,R1CorrENSO_Sep,"Difference in AWAP and R1 correlations, ENSO - September",\
             "/correlation/diff_nino_R1/September")
    plotCorrDiff(awapCorrENSO_Oct,R1CorrENSO_Oct,"Difference in AWAP and R1 correlations, ENSO - October",\
             "/correlation/diff_nino_R1/October")
    plotCorrDiff(awapCorrENSO_Nov,R1CorrENSO_Nov,"Difference in AWAP and R1 correlations, ENSO - November",\
             "/correlation/diff_nino_R1/November")
    plotCorrDiff(awapCorrENSO_Dec,R1CorrENSO_Dec,"Difference in AWAP and R1 correlations, ENSO - December",\
             "/correlation/diff_nino_R1/December")
    plotCorrDiff(awapCorrENSO_Jan,R1CorrENSO_Jan,"Difference in AWAP and R1 correlations, ENSO - January",\
             "/correlation/diff_nino_R1/January")
    plotCorrDiff(awapCorrENSO_Feb,R1CorrENSO_Feb,"Difference in AWAP and R1 correlations, ENSO - February",\
             "/correlation/diff_nino_R1/February")
    plotCorrDiff(awapCorrENSO_Mar,R1CorrENSO_Mar,"Difference in AWAP and R1 correlations, ENSO - March",\
             "/correlation/diff_nino_R1/March")
    plotCorrDiff(awapCorrENSO_Apr,R1CorrENSO_Apr,"Difference in AWAP and R1 correlations, ENSO - April",\
             "/correlation/diff_nino_R1/April")
    plotCorrDiff(awapCorrENSO_May,R1CorrENSO_May,"Difference in AWAP and R1 correlations, ENSO - May",\
             "/correlation/diff_nino_R1/May")
    return

def corrDiffTPI_R1():
    plotCorrDiff(awapCorrTPI_annual,R1CorrTPI_annual,"Difference in AWAP and R1 correlations, IPO - annual",\
             "/correlation/diff_tpi_R1/annual")
    plotCorrDiff(awapCorrTPI_JJA,R1CorrTPI_JJA,"Difference in AWAP and R1 correlations, IPO - JJA",\
             "/correlation/diff_tpi_R1/JJA")
    plotCorrDiff(awapCorrTPI_SON,R1CorrTPI_SON,"Difference in AWAP and R1 correlations, IPO - SON",\
             "/correlation/diff_tpi_R1/SON")
    plotCorrDiff(awapCorrTPI_DJF,R1CorrTPI_DJF,"Difference in AWAP and R1 correlations, IPO - DJF",\
             "/correlation/diff_tpi_R1/DJF")
    plotCorrDiff(awapCorrTPI_MAM,R1CorrTPI_MAM,"Difference in AWAP and R1 correlations, IPO - MAM",\
             "/correlation/diff_tpi_R1/MAM")
    plotCorrDiff(awapCorrTPI_Jun,R1CorrTPI_Jun,"Difference in AWAP and R1 correlations, IPO - June",\
             "/correlation/diff_tpi_R1/June")
    plotCorrDiff(awapCorrTPI_Jul,R1CorrTPI_Jul,"Difference in AWAP and R1 correlations, IPO - July",\
             "/correlation/diff_tpi_R1/July")
    plotCorrDiff(awapCorrTPI_Aug,R1CorrTPI_Aug,"Difference in AWAP and R1 correlations, IPO - August",\
             "/correlation/diff_tpi_R1/August")
    plotCorrDiff(awapCorrTPI_Sep,R1CorrTPI_Sep,"Difference in AWAP and R1 correlations, IPO - September",\
             "/correlation/diff_tpi_R1/September")
    plotCorrDiff(awapCorrTPI_Oct,R1CorrTPI_Oct,"Difference in AWAP and R1 correlations, IPO - October",\
             "/correlation/diff_tpi_R1/October")
    plotCorrDiff(awapCorrTPI_Nov,R1CorrTPI_Nov,"Difference in AWAP and R1 correlations, IPO - November",\
             "/correlation/diff_tpi_R1/November")
    plotCorrDiff(awapCorrTPI_Dec,R1CorrTPI_Dec,"Difference in AWAP and R1 correlations, IPO - December",\
             "/correlation/diff_tpi_R1/December")
    plotCorrDiff(awapCorrTPI_Jan,R1CorrTPI_Jan,"Difference in AWAP and R1 correlations, IPO - January",\
             "/correlation/diff_tpi_R1/January")
    plotCorrDiff(awapCorrTPI_Feb,R1CorrTPI_Feb,"Difference in AWAP and R1 correlations, IPO - February",\
             "/correlation/diff_tpi_R1/February")
    plotCorrDiff(awapCorrTPI_Mar,R1CorrTPI_Mar,"Difference in AWAP and R1 correlations, IPO - March",\
             "/correlation/diff_tpi_R1/March")
    plotCorrDiff(awapCorrTPI_Apr,R1CorrTPI_Apr,"Difference in AWAP and R1 correlations, IPO - April",\
             "/correlation/diff_tpi_R1/April")
    plotCorrDiff(awapCorrTPI_May,R1CorrTPI_May,"Difference in AWAP and R1 correlations, IPO - May",\
             "/correlation/diff_tpi_R1/May")
    return

#Make ACCESS R1 data available as a list; creates an array of rainfall averages
rainfall_R1 = [trim_June, trim_July, trim_August, trim_September, trim_October, trim_November,\
      trim_December,trim_January,trim_February,trim_March,trim_April,trim_May,\
      trim_JJA,trim_SON,trim_DJF,trim_MAM,trim_Annual]

rainfall_R1_average = averageArray(rainfall_R1)

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

R1corrENSO = R1CorrENSO_data()
(R1CorrENSO_annual, R1CorrENSO_JJA, R1CorrENSO_SON, R1CorrENSO_DJF,\
           R1CorrENSO_MAM,R1CorrENSO_Jun,R1CorrENSO_Jul,R1CorrENSO_Aug,\
           R1CorrENSO_Sep,R1CorrENSO_Oct,R1CorrENSO_Nov,R1CorrENSO_Dec,\
           R1CorrENSO_Jan,R1CorrENSO_Feb,R1CorrENSO_Mar,R1CorrENSO_Apr,\
           R1CorrENSO_May) = R1corrENSO

R1corrIPO = R1CorrTPI_data()
(R1CorrTPI_annual, R1CorrTPI_JJA, R1CorrTPI_SON, R1CorrTPI_DJF,\
           R1CorrTPI_MAM,R1CorrTPI_Jun,R1CorrTPI_Jul,R1CorrTPI_Aug,\
           R1CorrTPI_Sep,R1CorrTPI_Oct,R1CorrTPI_Nov,R1CorrTPI_Dec,\
           R1CorrTPI_Jan,R1CorrTPI_Feb,R1CorrTPI_Mar,R1CorrTPI_Apr,\
           R1CorrTPI_May) = R1corrIPO

#Generate correlation plots
accessR1_awap_corrENSO('R1')
accessR1_awap_corrIPO('R1')
corrDiffENSO_R1()
corrDiffTPI_R1()

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
np.savetxt('data/Correlation_coefficients/R1_corr_coef_ENSO_Aus.csv',corrAverageENSO,delimiter=',')

output2 = np.column_stack((corrEastENSO_annual, corrEastENSO_JJA,corrEastENSO_SON,\
           corrEastENSO_DJF,corrEastENSO_MAM,corrEastENSO_Jun,\
           corrEastENSO_Jul,corrEastENSO_Aug,corrEastENSO_Sep,\
           corrEastENSO_Oct,corrEastENSO_Nov,corrEastENSO_Dec,\
           corrEastENSO_Jan,corrEastENSO_Feb,corrEastENSO_Mar,\
           corrEastENSO_Apr,corrEastENSO_May))
np.savetxt('data/Correlation_coefficients/R1_corr_coef_ENSO_EastAus.csv',output2,delimiter=',')

np.savetxt('data/Correlation_coefficients/R1_corr_coef_TPI_Aus.csv',corrAverageTPI,delimiter=',')

output4 = np.column_stack((corrEastTPI_annual, corrEastTPI_JJA,corrEastTPI_SON,\
           corrEastTPI_DJF,corrEastTPI_MAM,corrEastTPI_Jun,\
           corrEastTPI_Jul,corrEastTPI_Aug,corrEastTPI_Sep,\
           corrEastTPI_Oct,corrEastTPI_Nov,corrEastTPI_Dec,\
           corrEastTPI_Jan,corrEastTPI_Feb,corrEastTPI_Mar,\
           corrEastTPI_Apr,corrEastTPI_May))
np.savetxt('data/Correlation_coefficients/R1_corr_coef_TPI_EastAus.csv',output4,delimiter=',')

