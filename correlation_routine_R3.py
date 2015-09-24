"""
A file to correlate ENSO with ACCESS R3 rainfall and the IPO with ACCESS R3
rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 25 September 2015.
"""

from correlation import *
from correlation_routine_awap import awapCorrENSO_data,awapCorrTPI_data

from access_trimmed import trim_Annual, trim_JJA,trim_SON,trim_DJF,trim_MAM,\
     trim_June, trim_July, trim_August, trim_September, trim_October, trim_November,\
     trim_December,trim_January,trim_February,trim_March,trim_April,trim_May
     
from indices_time import Nino34_Jun, Nino34_Jul, Nino34_Aug, Nino34_Sep, \
     Nino34_Oct, Nino34_Nov, Nino34_Dec, Nino34_Jan, Nino34_Feb, Nino34_Mar,\
     Nino34_Apr, Nino34_May, Nino34_JJA, Nino34_SON, Nino34_DJF, Nino34_MAM,\
    Nino34_annual, TPI_Jun, TPI_Jul, TPI_Aug, TPI_Sep, TPI_Oct, TPI_Nov,\
    TPI_Dec, TPI_Jan, TPI_Feb, TPI_Mar, TPI_Apr, TPI_May, TPI_JJA, TPI_SON, \
    TPI_DJF, TPI_MAM, TPI_annual

def accessCorrENSO(num,roundNum):
    plotCorr(trim_Annual,Nino34_annual,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - annual",\
             "/correlation/nino_"+roundNum+"/annual")
    plotCorr(trim_JJA,Nino34_JJA,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - JJA",\
             "/correlation/nino_"+roundNum+"/JJA")
    plotCorr(trim_SON,Nino34_SON,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - SON",\
             "/correlation/nino_"+roundNum+"/SON")
    plotCorr(trim_DJF,Nino34_DJF,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - DJF",\
             "/correlation/nino_"+roundNum+"/DJF")
    plotCorr(trim_MAM,Nino34_MAM,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - MAM",\
             "/correlation/nino_"+roundNum+"/MAM")
    plotCorr(trim_June,Nino34_Jun,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - June",\
             "/correlation/nino_"+roundNum+"/June")
    plotCorr(trim_July,Nino34_Jul,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - July",\
             "/correlation/nino_"+roundNum+"/July")
    plotCorr(trim_August,Nino34_Aug,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - August",\
             "/correlation/nino_"+roundNum+"/August")
    plotCorr(trim_September,Nino34_Sep,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - September",\
             "/correlation/nino_"+roundNum+"/September")
    plotCorr(trim_October,Nino34_Oct,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - October",\
             "/correlation/nino_"+roundNum+"/October")
    plotCorr(trim_November,Nino34_Nov,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - November",\
             "/correlation/nino_"+roundNum+"/November")
    plotCorr(trim_December,Nino34_Dec,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - December",\
             "/correlation/nino_"+roundNum+"/December")
    plotCorr(trim_January,Nino34_Jan,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - January",\
             "/correlation/nino_"+roundNum+"/January")
    plotCorr(trim_February,Nino34_Feb,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - February",\
             "/correlation/nino_"+roundNum+"/February")
    plotCorr(trim_March,Nino34_Mar,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - March",\
             "/correlation/nino_"+roundNum+"/March")
    plotCorr(trim_April,Nino34_Apr,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - April",\
             "/correlation/nino_"+roundNum+"/April")
    plotCorr(trim_May,Nino34_May,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - May",\
             "/correlation/nino_"+roundNum+"/May")
    return

def accessCorrIPO(num,roundNum):
    plotCorr(trim_Annual,TPI_annual,num,"ACCESS "+roundNum+" rainfall-TPI correlation - annual",\
             "/correlation/tpi_"+roundNum+"/annual")
    plotCorr(trim_JJA,TPI_JJA,num,"ACCESS "+roundNum+" rainfall-TPI correlation - JJA",\
             "/correlation/tpi_"+roundNum+"/JJA")
    plotCorr(trim_SON,TPI_SON,num,"ACCESS "+roundNum+" rainfall-TPI correlation - SON",\
             "/correlation/tpi_"+roundNum+"/SON")
    plotCorr(trim_DJF,TPI_DJF,num,"ACCESS "+roundNum+" rainfall-TPI correlation - DJF",\
             "/correlation/tpi_"+roundNum+"/DJF")
    plotCorr(trim_MAM,TPI_MAM,num,"ACCESS "+roundNum+" rainfall-TPI correlation - MAM",\
             "/correlation/tpi_"+roundNum+"/MAM")
    plotCorr(trim_June,TPI_Jun,num,"ACCESS "+roundNum+" rainfall-TPI correlation - June",\
             "/correlation/tpi_"+roundNum+"/June")
    plotCorr(trim_July,TPI_Jul,num,"ACCESS "+roundNum+" rainfall-TPI correlation - July",\
             "/correlation/tpi_"+roundNum+"/July")
    plotCorr(trim_August,TPI_Aug,num,"ACCESS "+roundNum+" rainfall-TPI correlation - August",\
             "/correlation/tpi_"+roundNum+"/August")
    plotCorr(trim_September,TPI_Sep,num,"ACCESS "+roundNum+" rainfall-TPI correlation - September",\
             "/correlation/tpi_"+roundNum+"/September")
    plotCorr(trim_October,TPI_Oct,num,"ACCESS "+roundNum+" rainfall-TPI correlation - October",\
             "/correlation/tpi_"+roundNum+"/October")
    plotCorr(trim_November,TPI_Nov,num,"ACCESS "+roundNum+" rainfall-TPI correlation - November",\
             "/correlation/tpi_"+roundNum+"/November")
    plotCorr(trim_December,TPI_Dec,num,"ACCESS "+roundNum+" rainfall-TPI correlation - December",\
             "/correlation/tpi_"+roundNum+"/December")
    plotCorr(trim_January,TPI_Jan,num,"ACCESS "+roundNum+" rainfall-TPI correlation - January",\
             "/correlation/tpi_"+roundNum+"/January")
    plotCorr(trim_February,TPI_Feb,num,"ACCESS "+roundNum+" rainfall-TPI correlation - February",\
             "/correlation/tpi_"+roundNum+"/February")
    plotCorr(trim_March,TPI_Mar,num,"ACCESS "+roundNum+" rainfall-TPI correlation - March",\
             "/correlation/tpi_"+roundNum+"/March")
    plotCorr(trim_April,TPI_Apr,num,"ACCESS "+roundNum+" rainfall-TPI correlation - April",\
             "/correlation/tpi_"+roundNum+"/etcApril")
    plotCorr(trim_May,TPI_May,num,"ACCESS "+roundNum+" rainfall-TPI correlation - May",\
             "/correlation/tpi_"+roundNum+"/May")
    return

def R3CorrENSO_data():
    R3CorrENSO_annual = corr(trim_Annual,Nino34_annual,1)
    R3CorrENSO_JJA = corr(trim_JJA,Nino34_JJA,1)
    R3CorrENSO_SON = corr(trim_SON,Nino34_SON,1)
    R3CorrENSO_DJF = corr(trim_DJF,Nino34_DJF,1)
    R3CorrENSO_MAM = corr(trim_MAM,Nino34_MAM,1)
    R3CorrENSO_Jun = corr(trim_June,Nino34_Jun,1)
    R3CorrENSO_Jul = corr(trim_July,Nino34_Jul,1)
    R3CorrENSO_Aug = corr(trim_August,Nino34_Aug,1)
    R3CorrENSO_Sep = corr(trim_September,Nino34_Sep,1)
    R3CorrENSO_Oct = corr(trim_October,Nino34_Oct,1)
    R3CorrENSO_Nov = corr(trim_November,Nino34_Nov,1)
    R3CorrENSO_Dec = corr(trim_December,Nino34_Dec,1)
    R3CorrENSO_Jan = corr(trim_January,Nino34_Jan,1)
    R3CorrENSO_Feb = corr(trim_February,Nino34_Feb,1)
    R3CorrENSO_Mar = corr(trim_March,Nino34_Mar,1)
    R3CorrENSO_Apr = corr(trim_April,Nino34_Apr,1)
    R3CorrENSO_May = corr(trim_May,Nino34_May,1)
    return R3CorrENSO_annual, R3CorrENSO_JJA, R3CorrENSO_SON, R3CorrENSO_DJF,\
           R3CorrENSO_MAM,R3CorrENSO_Jun,R3CorrENSO_Jul,R3CorrENSO_Aug,\
           R3CorrENSO_Sep,R3CorrENSO_Oct,R3CorrENSO_Nov,R3CorrENSO_Dec,\
           R3CorrENSO_Jan,R3CorrENSO_Feb,R3CorrENSO_Mar,R3CorrENSO_Apr,\
           R3CorrENSO_May

def R3CorrTPI_data():
    R3CorrTPI_annual = corr(trim_Annual,TPI_annual,3)
    R3CorrTPI_JJA = corr(trim_JJA,TPI_JJA,3)
    R3CorrTPI_SON = corr(trim_SON,TPI_SON,3)
    R3CorrTPI_DJF = corr(trim_DJF,TPI_DJF,3)
    R3CorrTPI_MAM = corr(trim_MAM,TPI_MAM,3)
    R3CorrTPI_Jun = corr(trim_June,TPI_Jun,3)
    R3CorrTPI_Jul = corr(trim_July,TPI_Jul,3)
    R3CorrTPI_Aug = corr(trim_August,TPI_Aug,3)
    R3CorrTPI_Sep = corr(trim_September,TPI_Sep,3)
    R3CorrTPI_Oct = corr(trim_October,TPI_Oct,3)
    R3CorrTPI_Nov = corr(trim_November,TPI_Nov,3)
    R3CorrTPI_Dec = corr(trim_December,TPI_Dec,3)
    R3CorrTPI_Jan = corr(trim_January,TPI_Jan,3)
    R3CorrTPI_Feb = corr(trim_February,TPI_Feb,3)
    R3CorrTPI_Mar = corr(trim_March,TPI_Mar,3)
    R3CorrTPI_Apr = corr(trim_April,TPI_Apr,3)
    R3CorrTPI_May = corr(trim_May,TPI_May,3)
    return R3CorrTPI_annual, R3CorrTPI_JJA, R3CorrTPI_SON, R3CorrTPI_DJF,\
           R3CorrTPI_MAM,R3CorrTPI_Jun,R3CorrTPI_Jul,R3CorrTPI_Aug,\
           R3CorrTPI_Sep,R3CorrTPI_Oct,R3CorrTPI_Nov,R3CorrTPI_Dec,\
           R3CorrTPI_Jan,R3CorrTPI_Feb,R3CorrTPI_Mar,R3CorrTPI_Apr,\
           R3CorrTPI_May

def corrDiffENSO_R3():
    plotCorrDiff(awapCorrENSO_annual,R3CorrENSO_annual,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - annual",\
             "/correlation/diff_nino_r3/annual")
    plotCorrDiff(awapCorrENSO_JJA,R3CorrENSO_JJA,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - JJA",\
             "/correlation/diff_nino_r3/JJA")
    plotCorrDiff(awapCorrENSO_SON,R3CorrENSO_SON,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - SON",\
             "/correlation/diff_nino_r3/SON")
    plotCorrDiff(awapCorrENSO_DJF,R3CorrENSO_DJF,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - DJF",\
             "/correlation/diff_nino_r3/DJF")
    plotCorrDiff(awapCorrENSO_MAM,R3CorrENSO_MAM,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - MAM",\
             "/correlation/diff_nino_r3/MAM")
    plotCorrDiff(awapCorrENSO_June,R3CorrENSO_Jun,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - June",\
             "/correlation/diff_nino_r3/June")
    plotCorrDiff(awapCorrENSO_July,R3CorrENSO_Jul,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - July",\
             "/correlation/diff_nino_r3/July")
    plotCorrDiff(awapCorrENSO_August,R3CorrENSO_Aug,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - August",\
             "/correlation/diff_nino_r3/August")
    plotCorrDiff(awapCorrENSO_September,R3CorrENSO_Sep,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - September",\
             "/correlation/diff_nino_r3/September")
    plotCorrDiff(awapCorrENSO_October,R3CorrENSO_Oct,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - October",\
             "/correlation/diff_nino_r3/October")
    plotCorrDiff(awapCorrENSO_November,R3CorrENSO_Nov,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - November",\
             "/correlation/diff_nino_r3/November")
    plotCorrDiff(awapCorrENSO_December,R3CorrENSO_Dec,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - December",\
             "/correlation/diff_nino_r3/December")
    plotCorrDiff(awapCorrENSO_January,R3CorrENSO_Jan,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - January",\
             "/correlation/diff_nino_r3/January")
    plotCorrDiff(awapCorrENSO_February,R3CorrENSO_Feb,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - February",\
             "/correlation/diff_nino_r3/February")
    plotCorrDiff(awapCorrENSO_March,R3CorrENSO_Mar,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - March",\
             "/correlation/diff_nino_r3/March")
    plotCorrDiff(awapCorrENSO_April,R3CorrENSO_Apr,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - April",\
             "/correlation/diff_nino_r3/April")
    plotCorrDiff(awapCorrENSO_May,R3CorrENSO_May,"Difference between AWAP and ACCESS1.3 R3 correlations with ENSO - May",\
             "/correlation/diff_nino_r3/May")
    return

def corrDiffTPI_R3():
    plotCorrDiff(awapCorrTPI_annual,R3CorrTPI_annual,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - annual",\
             "/correlation/diff_tpi_r3/annual")
    plotCorrDiff(awapCorrTPI_JJA,R3CorrTPI_JJA,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - JJA",\
             "/correlation/diff_tpi_r3/JJA")
    plotCorrDiff(awapCorrTPI_SON,R3CorrTPI_SON,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - SON",\
             "/correlation/diff_tpi_r3/SON")
    plotCorrDiff(awapCorrTPI_DJF,R3CorrTPI_DJF,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - DJF",\
             "/correlation/diff_tpi_r3/DJF")
    plotCorrDiff(awapCorrTPI_MAM,R3CorrTPI_MAM,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - MAM",\
             "/correlation/diff_tpi_r3/MAM")
    plotCorrDiff(awapCorrTPI_June,R3CorrTPI_Jun,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - June",\
             "/correlation/diff_tpi_r3/June")
    plotCorrDiff(awapCorrTPI_July,R3CorrTPI_Jul,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - July",\
             "/correlation/diff_tpi_r3/July")
    plotCorrDiff(awapCorrTPI_August,R3CorrTPI_Aug,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - August",\
             "/correlation/diff_tpi_r3/August")
    plotCorrDiff(awapCorrTPI_September,R3CorrTPI_Sep,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - September",\
             "/correlation/diff_tpi_r3/September")
    plotCorrDiff(awapCorrTPI_October,R3CorrTPI_Oct,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - October",\
             "/correlation/diff_tpi_r3/October")
    plotCorrDiff(awapCorrTPI_November,R3CorrTPI_Nov,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - November",\
             "/correlation/diff_tpi_r3/November")
    plotCorrDiff(awapCorrTPI_December,R3CorrTPI_Dec,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - December",\
             "/correlation/diff_tpi_r3/December")
    plotCorrDiff(awapCorrTPI_January,R3CorrTPI_Jan,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - January",\
             "/correlation/diff_tpi_r3/January")
    plotCorrDiff(awapCorrTPI_February,R3CorrTPI_Feb,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - February",\
             "/correlation/diff_tpi_r3/February")
    plotCorrDiff(awapCorrTPI_March,R3CorrTPI_Mar,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - March",\
             "/correlation/diff_tpi_r3/March")
    plotCorrDiff(awapCorrTPI_April,R3CorrTPI_Apr,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - April",\
             "/correlation/diff_tpi_r3/April")
    plotCorrDiff(awapCorrTPI_May,R3CorrTPI_May,"Difference between AWAP and ACCESS1.3 R3 correlations with IPO - May",\
             "/correlation/diff_tpi_r3/May")
    return

awapCorrENSO = awapCorrENSO_data()
(awapCorrENSO_annual, awapCorrENSO_JJA, awapCorrENSO_SON, awapCorrENSO_DJF,\
           awapCorrENSO_MAM,awapCorrENSO_Jun,awapCorrENSO_Jul,awapCorrENSO_Aug,\
           awapCorrENSO_Sep,awapCorrENSO_Oct,awapCorrENSO_Nov,awapCorrENSO_Dec,\
           awapCorrENSO_Jan,awapCorrENSO_Feb,awapCorrENSO_Mar,awapCorrENSO_Apr,\
           awapCorrENSO_May) = awapCorrENSO

awapCorrIPO = awapCorrTPI_data()
(awapCorrTPI_annual, awapCorrTPI_JJA, awapCorrTPI_SON, awapCorrTPI_DJF,\
           awapCorrTPI_MAM,awapCorrTPI_Jun,awapCorrTPI_Jul,awapCorrTPI_Aug,\
           awapCorrTPI_Sep,awapCorrTPI_Oct,awapCorrTPI_Nov,awapCorrTPI_Dec,\
           awapCorrTPI_Jan,awapCorrTPI_Feb,awapCorrTPI_Mar,awapCorrTPI_Apr,\
           awapCorrTPI_May) = awapCorrIPO

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

"""
accessCorrENSO(3,"r3")
accessCorrIPO(7,"r3")
corrDiffENSO_R3()
corrDiffTPI_R3()
"""

