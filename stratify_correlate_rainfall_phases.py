"""
A script to stratify rainfall data into three (corresponding with either the
ENSO's or IPO's three phases), and then correlate this with the index that
the rainfall data was not stratified against.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 12 October 2015.
"""

import numpy as np
import numpy.ma as ma

from composite import *
from correlation import *

from awap_prepare import awap_Annual,awap_JJA,awap_SON,\
     awap_DJF,awap_MAM,awap_June,awap_July,awap_August,\
     awap_September,awap_October,awap_November,awap_December,\
     awap_January,awap_February,awap_March,awap_April,awap_May

from access_trimmed import trim_Annual,trim_June, trim_July,\
     trim_August,trim_September,trim_October,trim_November,\
     trim_December,trim_January,trim_February,trim_March,\
     trim_April,trim_May,trim_JJA,trim_SON,trim_DJF,trim_MAM

"""
from ENSO_IPO_corr_strat import ENSO_posHad, ENSO_negHad,ENSO_neutralHad,\
     IPO_posHad, IPO_negHad,IPO_neutralHad,ENSO_posR1, ENSO_negR1,ENSO_neutralR1,\
     IPO_posR1, IPO_negR1,IPO_neutralR1,ENSO_posR2, ENSO_negR2,ENSO_neutralR2,\
     IPO_posR2, IPO_negR2,IPO_neutralR2,ENSO_posR3, ENSO_negR3,ENSO_neutralR3,\
     IPO_posR3, IPO_negR3,IPO_neutralR3



        pos_all_years = stratify(awap_Annual,had_ENSO_array[0][num])
    pos = stratifyAverage(pos_all_years)
    plotCorr(pos_all_years,had_IPO_array[0][num],TITLE,FILENAME)

    neg_all_years = stratify(awap_Annual,had_ENSO_array[1][num])
    neg = stratifyAverage(neg_all_years)
    plotCorr(neg_all_years,had_IPO_array[0][num],TITLE,FILENAME)

    neutral_all_years = stratify(awap_Annual,had_ENSO_array[2][num])
    neutral = stratifyAverage(neutral_all_years)
    plotCorr(neutral_all_years,had_IPO_array[0][num],TITLE,FILENAME)
"""
from comparison_stratified_rainfall import had_ENSO_array,had_IPO_array,\
     R1_ENSO_array,R1_IPO_array,R2_ENSO_array,R2_IPO_array,R3_ENSO_array,\
     R3_IPO_array

from cwd import cwdInFunction
cwdInFunction()


def stratify(rainfall,ENSO_index,IPO_index,num,rainfall_dataset,rainfall_data_short,time,sd,std)
    ENSO_pos_all_years = stratify(rainfall,ENSO_index[0][num])
    ENSO_pos = stratifyAverage(ENSO_pos_all_years)
    plotCorr(ENSO_pos_all_years,IPO_index[0][num],rainfall_dataset+': ENSO positive '+time+' rainfall & TPI'+std,\ 
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/ENSO_positive")

    ENSO_neg_all_years = stratify(rainfall,ENSO_index[1][num])
    ENSO_neg = stratifyAverage(ENSO_neg_all_years)
    plotCorr(ENSO_neg_all_years,IPO_index[0][num],rainfall_dataset+': ENSO negative '+time+' rainfall & TPI'+std,\ 
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/ENSO_negative")

    ENSO_neutral_all_years = stratify(rainfall,ENSO_index[2][num])
    ENSO_neutral = stratifyAverage(ENSO_neutral_all_years)
    plotCorr(ENSO_neutral_all_years,IPO_index[0][num],rainfall_dataset+': ENSO neutral '+time+' rainfall & TPI'+std,\ 
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/ENSO_neutral")


    IPO_pos_all_years = stratify(rainfall,IPO_index[0][num])
    IPO_pos = stratifyAverage(IPO_pos_all_years)
    plotCorr(IPO_pos_all_years,ENSO_index[0][num],rainfall_dataset+': IPO positive '+time+' rainfall & Nino 3.4'+std,\ 
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/IPO_positive")

    IPO_neg_all_years = stratify(rainfall,IPO_index[1][num])
    IPO_neg = stratifyAverage(IPO_neg_all_years)
    plotCorr(IPO_neg_all_years,ENSO_index[0][num],rainfall_dataset+': IPO negative '+time+' rainfall & Nino 3.4'+std,\ 
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/IPO_negative")

    IPO_neutral_all_years = stratify(rainfall,IPO_index[2][num])
    IPO_neutral = stratifyAverage(IPO_neutral_all_years)
    plotCorr(IPO_neutral_all_years,ENSO_index[0][num],rainfall_dataset+': IPO neutral '+time+' rainfall & Nino 3.4'+std,\ 
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/IPO_neutral")
    return

sd = "1_SD" #"1_SD" "2_SD" "3_SD"
std = '' # '' ' (2 $\sigma\$)' ' (3 $\sigma\$)' 

stratify(awap_Annual,had_ENSO_array,had_IPO_array,0,"AWAP","AWAP","annual",sd=sd,std=std)
stratify(awap_JJA,had_ENSO_array,had_IPO_array,1,"AWAP","AWAP","JJA",sd=sd,std=std)
stratify(awap_SON,had_ENSO_array,had_IPO_array,2,"AWAP","AWAP","SON",sd=sd,std=std)
stratify(awap_DJF,had_ENSO_array,had_IPO_array,3,"AWAP","AWAP","DJF",sd=sd,std=std)
stratify(awap_MAM,had_ENSO_array,had_IPO_array,4,"AWAP","AWAP","MAM",sd=sd,std=std)
stratify(awap_June,had_ENSO_array,had_IPO_array,5,"AWAP","AWAP","June",sd=sd,std=std)
stratify(awap_July,had_ENSO_array,had_IPO_array,6,"AWAP","AWAP","July",sd=sd,std=std)
stratify(awap_August,had_ENSO_array,had_IPO_array,7,"AWAP","AWAP","August",sd=sd,std=std)
stratify(awap_September,had_ENSO_array,had_IPO_array,8,"AWAP","AWAP","September",sd=sd,std=std)
stratify(awap_October,had_ENSO_array,had_IPO_array,9,"AWAP","AWAP","October",sd=sd,std=std)
stratify(awap_November,had_ENSO_array,had_IPO_array,10,"AWAP","AWAP","November",sd=sd,std=std)
stratify(awap_December,had_ENSO_array,had_IPO_array,11,"AWAP","AWAP","December",sd=sd,std=std)
stratify(awap_January,had_ENSO_array,had_IPO_array,12,"AWAP","AWAP","January",sd=sd,std=std)
stratify(awap_February,had_ENSO_array,had_IPO_array,13,"AWAP","AWAP","February",sd=sd,std=std)
stratify(awap_March,had_ENSO_array,had_IPO_array,14,"AWAP","AWAP","March",sd=sd,std=std)
stratify(awap_April,had_ENSO_array,had_IPO_array,15,"AWAP","AWAP","April",sd=sd,std=std)
stratify(awap_May,had_ENSO_array,had_IPO_array,16,"AWAP","AWAP","May",sd=sd,std=std)

stratify(trim_Annual,had_ENSO_array,had_IPO_array,0,"ACCESS R1","R1","annual",sd=sd,std=std)
stratify(trim_JJA,had_ENSO_array,had_IPO_array,1,"ACCESS R1","R1","JJA",sd=sd,std=std)
stratify(trim_SON,had_ENSO_array,had_IPO_array,2,"ACCESS R1","R1","SON",sd=sd,std=std)
stratify(trim_DJF,had_ENSO_array,had_IPO_array,3,"ACCESS R1","R1","DJF",sd=sd,std=std)
stratify(trim_MAM,had_ENSO_array,had_IPO_array,4,"ACCESS R1","R1","MAM",sd=sd,std=std)
stratify(trim_June,had_ENSO_array,had_IPO_array,5,"ACCESS R1","R1","June",sd=sd,std=std)
stratify(trim_July,had_ENSO_array,had_IPO_array,6,"ACCESS R1","R1","July",sd=sd,std=std)
stratify(trim_August,had_ENSO_array,had_IPO_array,7,"ACCESS R1","R1","August",sd=sd,std=std)
stratify(trim_September,had_ENSO_array,had_IPO_array,8,"ACCESS R1","R1","September",sd=sd,std=std)
stratify(trim_October,had_ENSO_array,had_IPO_array,9,"ACCESS R1","R1","October",sd=sd,std=std)
stratify(trim_November,had_ENSO_array,had_IPO_array,10,"ACCESS R1","R1","November",sd=sd,std=std)
stratify(trim_December,had_ENSO_array,had_IPO_array,11,"ACCESS R1","R1","December",sd=sd,std=std)
stratify(trim_January,had_ENSO_array,had_IPO_array,12,"ACCESS R1","R1","January",sd=sd,std=std)
stratify(trim_February,had_ENSO_array,had_IPO_array,13,"ACCESS R1","R1","February",sd=sd,std=std)
stratify(trim_March,had_ENSO_array,had_IPO_array,14,"ACCESS R1","R1","March",sd=sd,std=std)
stratify(trim_April,had_ENSO_array,had_IPO_array,15,"ACCESS R1","R1","April",sd=sd,std=std)
stratify(trim_May,had_ENSO_array,had_IPO_array,16,"ACCESS R1","R1","May",sd=sd,std=std)
"""
stratify(trim_Annual,had_ENSO_array,had_IPO_array,0,"ACCESS R2","R2","annual",sd=sd,std=std)
stratify(trim_JJA,had_ENSO_array,had_IPO_array,1,"ACCESS R2","R2","JJA",sd=sd,std=std)
stratify(trim_SON,had_ENSO_array,had_IPO_array,2,"ACCESS R2","R2","SON",sd=sd,std=std)
stratify(trim_DJF,had_ENSO_array,had_IPO_array,3,"ACCESS R2","R2","DJF",sd=sd,std=std)
stratify(trim_MAM,had_ENSO_array,had_IPO_array,4,"ACCESS R2","R2","MAM",sd=sd,std=std)
stratify(trim_June,had_ENSO_array,had_IPO_array,5,"ACCESS R2","R2","June",sd=sd,std=std)
stratify(trim_July,had_ENSO_array,had_IPO_array,6,"ACCESS R2","R2","July",sd=sd,std=std)
stratify(trim_August,had_ENSO_array,had_IPO_array,7,"ACCESS R2","R2","August",sd=sd,std=std)
stratify(trim_September,had_ENSO_array,had_IPO_array,8,"ACCESS R2","R2","September",sd=sd,std=std)
stratify(trim_October,had_ENSO_array,had_IPO_array,9,"ACCESS R2","R2","October",sd=sd,std=std)
stratify(trim_November,had_ENSO_array,had_IPO_array,10,"ACCESS R2","R2","November",sd=sd,std=std)
stratify(trim_December,had_ENSO_array,had_IPO_array,11,"ACCESS R2","R2","December",sd=sd,std=std)
stratify(trim_January,had_ENSO_array,had_IPO_array,12,"ACCESS R2","R2","January",sd=sd,std=std)
stratify(trim_February,had_ENSO_array,had_IPO_array,13,"ACCESS R2","R2","February",sd=sd,std=std)
stratify(trim_March,had_ENSO_array,had_IPO_array,14,"ACCESS R2","R2","March",sd=sd,std=std)
stratify(trim_April,had_ENSO_array,had_IPO_array,15,"ACCESS R2","R2","April",sd=sd,std=std)
stratify(trim_May,had_ENSO_array,had_IPO_array,16,"ACCESS R2","R2","May",sd=sd,std=std)

stratify(trim_Annual,had_ENSO_array,had_IPO_array,0,"ACCESS R3","R3","annual",sd=sd,std=std)
stratify(trim_JJA,had_ENSO_array,had_IPO_array,1,"ACCESS R3","R3","JJA",sd=sd,std=std)
stratify(trim_SON,had_ENSO_array,had_IPO_array,2,"ACCESS R3","R3","SON",sd=sd,std=std)
stratify(trim_DJF,had_ENSO_array,had_IPO_array,3,"ACCESS R3","R3","DJF",sd=sd,std=std)
stratify(trim_MAM,had_ENSO_array,had_IPO_array,4,"ACCESS R3","R3","MAM",sd=sd,std=std)
stratify(trim_June,had_ENSO_array,had_IPO_array,5,"ACCESS R3","R3","June",sd=sd,std=std)
stratify(trim_July,had_ENSO_array,had_IPO_array,6,"ACCESS R3","R3","July",sd=sd,std=std)
stratify(trim_August,had_ENSO_array,had_IPO_array,7,"ACCESS R3","R3","August",sd=sd,std=std)
stratify(trim_September,had_ENSO_array,had_IPO_array,8,"ACCESS R3","R3","September",sd=sd,std=std)
stratify(trim_October,had_ENSO_array,had_IPO_array,9,"ACCESS R3","R3","October",sd=sd,std=std)
stratify(trim_November,had_ENSO_array,had_IPO_array,10,"ACCESS R3","R3","November",sd=sd,std=std)
stratify(trim_December,had_ENSO_array,had_IPO_array,11,"ACCESS R3","R3","December",sd=sd,std=std)
stratify(trim_January,had_ENSO_array,had_IPO_array,12,"ACCESS R3","R3","January",sd=sd,std=std)
stratify(trim_February,had_ENSO_array,had_IPO_array,13,"ACCESS R3","R3","February",sd=sd,std=std)
stratify(trim_March,had_ENSO_array,had_IPO_array,14,"ACCESS R3","R3","March",sd=sd,std=std)
stratify(trim_April,had_ENSO_array,had_IPO_array,15,"ACCESS R3","R3","April",sd=sd,std=std)
stratify(trim_May,had_ENSO_array,had_IPO_array,16,"ACCESS R3","R3","May",sd=sd,std=std)
"""
