"""
A file to correlate ENSO with rainfall and the IPO with rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 15 September 2015.
"""

from correlation import *

from awap_prepare import awap_Annual, awap_JJA,awap_SON,awap_DJF,awap_MAM,\
     awap_June, awap_July, awap_August, awap_September, awap_October, awap_November,\
     awap_December,awap_January,awap_February,awap_March,awap_May
     
import access_trimmed
     
def awapCorrENSO():
    plotCorr(awap_annual,Nino34_annual,0,"AWAP rainfall-Nino3.4 correlation - annual",\
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
    plotCorr(awap_annual,TPI_annual,1,"AWAP rainfall-TPI correlation - annual",\
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

def accessCorrENSO(num,roundNum):
    reload(access_trimmed)
    from access_trimmed import trim_Annual, trim_JJA,trim_SON,trim_DJF,trim_MAM,\
     trim_June, trim_July, trim_August, trim_September, trim_October, trim_November,\
     trim_December,trim_January,trim_February,trim_March,trim_May
    
    plotCorr(trim_Annual,Nino34_annual,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - annual",\
             "/correlation/nino_"+roundNum+"/annual")
    plotCorr(trim_JJA,Nino34_JJA,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - JJA",\
             "/correlation/nino_"+roundNum+"JJA")
    plotCorr(trim_SON,Nino34_SON,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - SON",\
             "/correlation/nino_"+roundNum+"SON")
    plotCorr(trim_DJF,Nino34_DJF,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - DJF",\
             "/correlation/nino_"+roundNum+"DJF")
    plotCorr(trim_MAM,Nino34_MAM,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - MAM",\
             "/correlation/nino_"+roundNum+"MAM")
    plotCorr(trim_June,Nino34_Jun,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - June",\
             "/correlation/nino_"+roundNum+"June")
    plotCorr(trim_July,Nino34_Jul,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - July",\
             "/correlation/nino_"+roundNum+"July")
    plotCorr(trim_August,Nino34_Aug,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - August",\
             "/correlation/nino_"+roundNum+"August")
    plotCorr(trim_September,Nino34_Sep,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - September",\
             "/correlation/nino_"+roundNum+"September")
    plotCorr(trim_October,Nino34_Oct,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - October",\
             "/correlation/nino_"+roundNum+"October")
    plotCorr(trim_November,Nino34_Nov,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - November",\
             "/correlation/nino_"+roundNum+"November")
    plotCorr(trim_December,Nino34_Dec,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - December",\
             "/correlation/nino_"+roundNum+"December")
    plotCorr(trim_January,Nino34_Jan,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - January",\
             "/correlation/nino_"+roundNum+"January")
    plotCorr(trim_February,Nino34_Feb,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - February",\
             "/correlation/nino_"+roundNum+"February")
    plotCorr(trim_March,Nino34_Mar,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - March",\
             "/correlation/nino_"+roundNum+"March")
    plotCorr(trim_April,Nino34_Apr,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - April",\
             "/correlation/nino_"+roundNum+"April")
    plotCorr(trim_May,Nino34_May,num,"ACCESS "+roundNum+" rainfall-Nino3.4 correlation - May",\
             "/correlation/nino_"+roundNum+"/May")
    return

def accessCorrIPO(num,roundNum):
    reload(access_trimmed)
    from access_trimmed import trim_Annual, trim_JJA,trim_SON,trim_DJF,trim_MAM,\
     trim_June, trim_July, trim_August, trim_September, trim_October, trim_November,\
     trim_December,trim_January,trim_February,trim_March,trim_May
    
    plotCorr(trim_Annual,TPI_annual,num,"ACCESS "+roundNum+" rainfall-TPI correlation - annual",\
             "/correlation/tpi_"+roundNum+"/annual")
    plotCorr(trim_JJA,TPI_JJA,num,"ACCESS "+roundNum+" rainfall-TPI correlation - JJA",\
             "/correlation/tpi_"+roundNum+"JJA")
    plotCorr(trim_SON,TPI_SON,num,"ACCESS "+roundNum+" rainfall-TPI correlation - SON",\
             "/correlation/tpi_"+roundNum+"SON")
    plotCorr(trim_DJF,TPI_DJF,num,"ACCESS "+roundNum+" rainfall-TPI correlation - DJF",\
             "/correlation/tpi_"+roundNum+"DJF")
    plotCorr(trim_MAM,TPI_MAM,num,"ACCESS "+roundNum+" rainfall-TPI correlation - MAM",\
             "/correlation/tpi_"+roundNum+"MAM")
    plotCorr(trim_June,TPI_Jun,num,"ACCESS "+roundNum+" rainfall-TPI correlation - June",\
             "/correlation/tpi_"+roundNum+"June")
    plotCorr(trim_July,TPI_Jul,num,"ACCESS "+roundNum+" rainfall-TPI correlation - July",\
             "/correlation/tpi_"+roundNum+"July")
    plotCorr(trim_August,TPI_Aug,num,"ACCESS "+roundNum+" rainfall-TPI correlation - August",\
             "/correlation/tpi_"+roundNum+"August")
    plotCorr(trim_September,TPI_Sep,num,"ACCESS "+roundNum+" rainfall-TPI correlation - September",\
             "/correlation/tpi_"+roundNum+"September")
    plotCorr(trim_October,TPI_Oct,num,"ACCESS "+roundNum+" rainfall-TPI correlation - October",\
             "/correlation/tpi_"+roundNum+"October")
    plotCorr(trim_November,TPI_Nov,num,"ACCESS "+roundNum+" rainfall-TPI correlation - November",\
             "/correlation/tpi_"+roundNum+"November")
    plotCorr(trim_December,TPI_Dec,num,"ACCESS "+roundNum+" rainfall-TPI correlation - December",\
             "/correlation/tpi_"+roundNum+"December")
    plotCorr(trim_January,TPI_Jan,num,"ACCESS "+roundNum+" rainfall-TPI correlation - January",\
             "/correlation/tpi_"+roundNum+"January")
    plotCorr(trim_February,TPI_Feb,num,"ACCESS "+roundNum+" rainfall-TPI correlation - February",\
             "/correlation/tpi_"+roundNum+"February")
    plotCorr(trim_March,TPI_Mar,num,"ACCESS "+roundNum+" rainfall-TPI correlation - March",\
             "/correlation/tpi_"+roundNum+"March")
    plotCorr(trim_April,TPI_Apr,num,"ACCESS "+roundNum+" rainfall-TPI correlation - April",\
             "/correlation/tpi_"+roundNum+"April")
    plotCorr(trim_May,TPI_May,num,"ACCESS "+roundNum+" rainfall-TPI correlation - May",\
             "/correlation/tpi_"+roundNum+"/May")
    return

awapCorrENSO()
awapCorrIPO()
accessCorrENSO(3,"r1")
accessCorrENSO(5,"r2")
accessCorrENSO(7,"r3")
accessCorrIPO(3,"r1")
accessCorrIPO(5,"r2")
accessCorrIPO(7,"r3")
