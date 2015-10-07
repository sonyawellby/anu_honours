"""
A file to correlate ENSO with AWAP rainfall and the IPO with AWAP rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 7 October 2015.
"""

from correlation import *

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


# Plot correlation coefficients on Australian maps.

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

#Single value correlation coefficients (Australia, East Australia, climate regions).

def awapCorrAverageENSO():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    awapCorrAvENSO_annual = corrAverage(awap_Annual,enso_Annual_Had)
    awapCorrAvENSO_JJA = corrAverage(awap_JJA,enso_JJA_Had)
    awapCorrAvENSO_SON = corrAverage(awap_SON,enso_SON_Had)
    awapCorrAvENSO_DJF = corrAverage(awap_DJF,enso_DJF_Had)
    awapCorrAvENSO_MAM = corrAverage(awap_MAM,enso_MAM_Had)
    awapCorrAvENSO_Jun = corrAverage(awap_June,enso_Jun_Had)
    awapCorrAvENSO_Jul = corrAverage(awap_July,enso_Jul_Had)
    awapCorrAvENSO_Aug = corrAverage(awap_August,enso_Aug_Had)
    awapCorrAvENSO_Sep = corrAverage(awap_September,enso_Sep_Had)
    awapCorrAvENSO_Oct = corrAverage(awap_October,enso_Oct_Had)
    awapCorrAvENSO_Nov = corrAverage(awap_November,enso_Nov_Had)
    awapCorrAvENSO_Dec = corrAverage(awap_December,enso_Dec_Had)
    awapCorrAvENSO_Jan = corrAverage(awap_January,enso_Jan_Had)
    awapCorrAvENSO_Feb = corrAverage(awap_February,enso_Feb_Had)
    awapCorrAvENSO_Mar = corrAverage(awap_March,enso_Mar_Had)
    awapCorrAvENSO_Apr = corrAverage(awap_April,enso_Apr_Had)
    awapCorrAvENSO_May = corrAverage(awap_May,enso_May_Had)
    return awapCorrAvENSO_annual, awapCorrAvENSO_JJA,awapCorrAvENSO_SON,\
           awapCorrAvENSO_DJF,awapCorrAvENSO_MAM,awapCorrAvENSO_Jun,\
           awapCorrAvENSO_Jul,awapCorrAvENSO_Aug,awapCorrAvENSO_Sep,\
           awapCorrAvENSO_Oct,awapCorrAvENSO_Nov,awapCorrAvENSO_Dec,\
           awapCorrAvENSO_Jan,awapCorrAvENSO_Feb,awapCorrAvENSO_Mar,\
           awapCorrAvENSO_Apr,awapCorrAvENSO_May

def awapCorrAverageEastENSO():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    awapCorrEastENSO_annual = corrEastAus(awap_Annual,enso_Annual_Had)
    awapCorrEastENSO_JJA = corrEastAus(awap_JJA,enso_JJA_Had)
    awapCorrEastENSO_SON = corrEastAus(awap_SON,enso_SON_Had)
    awapCorrEastENSO_DJF = corrEastAus(awap_DJF,enso_DJF_Had)
    awapCorrEastENSO_MAM = corrEastAus(awap_MAM,enso_MAM_Had)
    awapCorrEastENSO_Jun = corrEastAus(awap_June,enso_Jun_Had)
    awapCorrEastENSO_Jul = corrEastAus(awap_July,enso_Jul_Had)
    awapCorrEastENSO_Aug = corrEastAus(awap_August,enso_Aug_Had)
    awapCorrEastENSO_Sep = corrEastAus(awap_September,enso_Sep_Had)
    awapCorrEastENSO_Oct = corrEastAus(awap_October,enso_Oct_Had)
    awapCorrEastENSO_Nov = corrEastAus(awap_November,enso_Nov_Had)
    awapCorrEastENSO_Dec = corrEastAus(awap_December,enso_Dec_Had)
    awapCorrEastENSO_Jan = corrEastAus(awap_January,enso_Jan_Had)
    awapCorrEastENSO_Feb = corrEastAus(awap_February,enso_Feb_Had)
    awapCorrEastENSO_Mar = corrEastAus(awap_March,enso_Mar_Had)
    awapCorrEastENSO_Apr = corrEastAus(awap_April,enso_Apr_Had)
    awapCorrEastENSO_May = corrEastAus(awap_May,enso_May_Had)
    return awapCorrEastENSO_annual, awapCorrEastENSO_JJA,awapCorrEastENSO_SON,\
           awapCorrEastENSO_DJF,awapCorrEastENSO_MAM,awapCorrEastENSO_Jun,\
           awapCorrEastENSO_Jul,awapCorrEastENSO_Aug,awapCorrEastENSO_Sep,\
           awapCorrEastENSO_Oct,awapCorrEastENSO_Nov,awapCorrEastENSO_Dec,\
           awapCorrEastENSO_Jan,awapCorrEastENSO_Feb,awapCorrEastENSO_Mar,\
           awapCorrEastENSO_Apr,awapCorrEastENSO_May

def awapCorrAverageTPI():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    awapCorrAvTPI_annual = corrAverage(awap_Annual,IPO_had_Annual)
    awapCorrAvTPI_JJA = corrAverage(awap_JJA,IPO_had_JJA)
    awapCorrAvTPI_SON = corrAverage(awap_SON,IPO_had_SON)
    awapCorrAvTPI_DJF = corrAverage(awap_DJF,IPO_had_DJF)
    awapCorrAvTPI_MAM = corrAverage(awap_MAM,IPO_had_MAM)
    awapCorrAvTPI_Jun = corrAverage(awap_June,IPO_had_Jun)
    awapCorrAvTPI_Jul = corrAverage(awap_July,IPO_had_Jul)
    awapCorrAvTPI_Aug = corrAverage(awap_August,IPO_had_Aug)
    awapCorrAvTPI_Sep = corrAverage(awap_September,IPO_had_Sep)
    awapCorrAvTPI_Oct = corrAverage(awap_October,IPO_had_Oct)
    awapCorrAvTPI_Nov = corrAverage(awap_November,IPO_had_Nov)
    awapCorrAvTPI_Dec = corrAverage(awap_December,IPO_had_Dec)
    awapCorrAvTPI_Jan = corrAverage(awap_January,IPO_had_Jan)
    awapCorrAvTPI_Feb = corrAverage(awap_February,IPO_had_Feb)
    awapCorrAvTPI_Mar = corrAverage(awap_March,IPO_had_Mar)
    awapCorrAvTPI_Apr = corrAverage(awap_April,IPO_had_Apr)
    awapCorrAvTPI_May = corrAverage(awap_May,IPO_had_May)
    return awapCorrAvTPI_annual, awapCorrAvTPI_JJA, awapCorrAvTPI_SON, awapCorrAvTPI_DJF,\
           awapCorrAvTPI_MAM,awapCorrAvTPI_Jun,awapCorrAvTPI_Jul,awapCorrAvTPI_Aug,\
           awapCorrAvTPI_Sep,awapCorrAvTPI_Oct,awapCorrAvTPI_Nov,awapCorrAvTPI_Dec,\
           awapCorrAvTPI_Jan,awapCorrAvTPI_Feb,awapCorrAvTPI_Mar,awapCorrAvTPI_Apr,\
           awapCorrAvTPI_May

def awapCorrAverageEastTPI():
    """
    Produces a correlation coefficient for whole of Australia.
    """
    awapCorrEastTPI_annual = corrEastAus(awap_Annual,IPO_had_Annual)
    awapCorrEastTPI_JJA = corrEastAus(awap_JJA,IPO_had_JJA)
    awapCorrEastTPI_SON = corrEastAus(awap_SON,IPO_had_SON)
    awapCorrEastTPI_DJF = corrEastAus(awap_DJF,IPO_had_DJF)
    awapCorrEastTPI_MAM = corrEastAus(awap_MAM,IPO_had_MAM)
    awapCorrEastTPI_Jun = corrEastAus(awap_June,IPO_had_Jun)
    awapCorrEastTPI_Jul = corrEastAus(awap_July,IPO_had_Jul)
    awapCorrEastTPI_Aug = corrEastAus(awap_August,IPO_had_Aug)
    awapCorrEastTPI_Sep = corrEastAus(awap_September,IPO_had_Sep)
    awapCorrEastTPI_Oct = corrEastAus(awap_October,IPO_had_Oct)
    awapCorrEastTPI_Nov = corrEastAus(awap_November,IPO_had_Nov)
    awapCorrEastTPI_Dec = corrEastAus(awap_December,IPO_had_Dec)
    awapCorrEastTPI_Jan = corrEastAus(awap_January,IPO_had_Jan)
    awapCorrEastTPI_Feb = corrEastAus(awap_February,IPO_had_Feb)
    awapCorrEastTPI_Mar = corrEastAus(awap_March,IPO_had_Mar)
    awapCorrEastTPI_Apr = corrEastAus(awap_April,IPO_had_Apr)
    awapCorrEastTPI_May = corrEastAus(awap_May,IPO_had_May)
    return awapCorrEastTPI_annual, awapCorrEastTPI_JJA, awapCorrEastTPI_SON, awapCorrEastTPI_DJF,\
           awapCorrEastTPI_MAM,awapCorrEastTPI_Jun,awapCorrEastTPI_Jul,awapCorrEastTPI_Aug,\
           awapCorrEastTPI_Sep,awapCorrEastTPI_Oct,awapCorrEastTPI_Nov,awapCorrEastTPI_Dec,\
           awapCorrEastTPI_Jan,awapCorrEastTPI_Feb,awapCorrEastTPI_Mar,awapCorrEastTPI_Apr,\
           awapCorrEastTPI_May

#Makes correlation array data available for use in other files.

def awapCorrENSO_data():
    """
    Generates correlation arrays for whole of Australia.
    """
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
    """
    Generates correlation arrays for whole of Australia.
    """
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


#Generate correlation plots
awapCorrENSO()
awapCorrIPO()

#Make correlation coefficients available:
corrAverageENSO = awapCorrAverageENSO()

corrAverageEastENSO = awapCorrAverageEastENSO()
(awapCorrEastENSO_annual, awapCorrEastENSO_JJA,awapCorrEastENSO_SON,\
           awapCorrEastENSO_DJF,awapCorrEastENSO_MAM,awapCorrEastENSO_Jun,\
           awapCorrEastENSO_Jul,awapCorrEastENSO_Aug,awapCorrEastENSO_Sep,\
           awapCorrEastENSO_Oct,awapCorrEastENSO_Nov,awapCorrEastENSO_Dec,\
           awapCorrEastENSO_Jan,awapCorrEastENSO_Feb,awapCorrEastENSO_Mar,\
           awapCorrEastENSO_Apr,awapCorrEastENSO_May) = corrAverageEastENSO

corrAverageTPI = awapCorrAverageTPI()

corrAverageEastTPI = awapCorrAverageEastTPI()
(awapCorrEastTPI_annual, awapCorrEastTPI_JJA,awapCorrEastTPI_SON,\
           awapCorrEastTPI_DJF,awapCorrEastTPI_MAM,awapCorrEastTPI_Jun,\
           awapCorrEastTPI_Jul,awapCorrEastTPI_Aug,awapCorrEastTPI_Sep,\
           awapCorrEastTPI_Oct,awapCorrEastTPI_Nov,awapCorrEastTPI_Dec,\
           awapCorrEastTPI_Jan,awapCorrEastTPI_Feb,awapCorrEastTPI_Mar,\
           awapCorrEastTPI_Apr,awapCorrEastTPI_May) = corrAverageEastTPI

#Correlation coefficients to CSV:
np.savetxt('data/Correlation_coefficients/awap_corr_coef_ENSO_Aus.csv',corrAverageENSO,delimiter=',')

output2 = np.column_stack((awapCorrEastENSO_annual, awapCorrEastENSO_JJA,awapCorrEastENSO_SON,\
           awapCorrEastENSO_DJF,awapCorrEastENSO_MAM,awapCorrEastENSO_Jun,\
           awapCorrEastENSO_Jul,awapCorrEastENSO_Aug,awapCorrEastENSO_Sep,\
           awapCorrEastENSO_Oct,awapCorrEastENSO_Nov,awapCorrEastENSO_Dec,\
           awapCorrEastENSO_Jan,awapCorrEastENSO_Feb,awapCorrEastENSO_Mar,\
           awapCorrEastENSO_Apr,awapCorrEastENSO_May))
np.savetxt('data/Correlation_coefficients/awap_corr_coef_ENSO_EastAus.csv',output2,delimiter=',')

np.savetxt('data/Correlation_coefficients/awap_corr_coef_TPI_Aus.csv',corrAverageTPI,delimiter=',')

output4 = np.column_stack((awapCorrEastTPI_annual, awapCorrEastTPI_JJA,awapCorrEastTPI_SON,\
           awapCorrEastTPI_DJF,awapCorrEastTPI_MAM,awapCorrEastTPI_Jun,\
           awapCorrEastTPI_Jul,awapCorrEastTPI_Aug,awapCorrEastTPI_Sep,\
           awapCorrEastTPI_Oct,awapCorrEastTPI_Nov,awapCorrEastTPI_Dec,\
           awapCorrEastTPI_Jan,awapCorrEastTPI_Feb,awapCorrEastTPI_Mar,\
           awapCorrEastTPI_Apr,awapCorrEastTPI_May))
np.savetxt('data/Correlation_coefficients/awap_corr_coef_TPI_EastAus.csv',output4,delimiter=',')

