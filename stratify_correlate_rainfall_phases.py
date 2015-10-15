"""
A script to stratify rainfall data into three (corresponding with either the
ENSO's or IPO's three phases), and then correlate this with the index that
the rainfall data was not stratified against.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 13 October 2015.
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

from comparison_stratified_rainfall import had_ENSO_array,had_IPO_array,\
     R1_ENSO_array,R1_IPO_array,R2_ENSO_array,R2_IPO_array,R3_ENSO_array,\
     R3_IPO_array

from ENSO_IPO_corr import hadISST_ENSO,R1_ENSO,R2_ENSO,R3_ENSO,\
     hadISST_IPO,R1_IPO,R2_IPO,R3_IPO

from cwd import cwdInFunction
cwdInFunction()

#If reprinting these graphs, change maps_sub.py: saveFig - y=1.08 and
# savefig - bbox_inches = 'tight'

def stratifyCorr(rainfall,ENSO_index_strat,IPO_index_strat,ENSO_index,IPO_index,num,num2,rainfall_dataset,rainfall_data_short,time,sd,std):

    ENSO_pos = stratify(rainfall,ENSO_index_strat[0][num])
    plotCorrStratified(ENSO_pos,IPO_index[num2],rainfall_dataset+': ENSO positive '+time+' rainfall & TPI'+std,\
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/ENSO_positive")

    ENSO_neg = stratify(rainfall,ENSO_index_strat[1][num])
    plotCorrStratified(ENSO_neg,IPO_index[num2],rainfall_dataset+': ENSO negative '+time+' rainfall & TPI'+std,\
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/ENSO_negative")

    ENSO_neutral = stratify(rainfall,ENSO_index_strat[2][num])
    plotCorrStratified(ENSO_neutral,IPO_index[num2],rainfall_dataset+': ENSO neutral '+time+' rainfall & TPI'+std,\
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/ENSO_neutral")


    IPO_pos = stratify(rainfall,IPO_index_strat[0][num])
    plotCorrStratified(IPO_pos,ENSO_index[num2],rainfall_dataset+': IPO positive '+time+' rainfall & Nino 3.4'+std,\
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/IPO_positive")

    IPO_neg = stratify(rainfall,IPO_index_strat[1][num])
    plotCorrStratified(IPO_neg,ENSO_index[num2],rainfall_dataset+': IPO negative '+time+' rainfall & Nino 3.4'+std,\
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/IPO_negative")

    IPO_neutral = stratify(rainfall,IPO_index_strat[2][num])
    plotCorrStratified(IPO_neutral,ENSO_index[num2],rainfall_dataset+': IPO neutral '+time+' rainfall & Nino 3.4'+std,\
             "stratified_correlation/"+sd+"/"+rainfall_data_short+"/"+time+"/IPO_neutral")
    return

sd = "1_SD" #"1_SD" "2_SD" "3_SD"
std = '' # '' r' (2 $\sigma\$)' r' (3 $\sigma\$)' 


stratifyCorr(awap_Annual,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,0,16,"AWAP","AWAP","annual",sd=sd,std=std)
stratifyCorr(awap_JJA,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,1,12,"AWAP","AWAP","JJA",sd=sd,std=std)
stratifyCorr(awap_SON,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,2,13,"AWAP","AWAP","SON",sd=sd,std=std)
stratifyCorr(awap_DJF,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,3,14,"AWAP","AWAP","DJF",sd=sd,std=std)
stratifyCorr(awap_MAM,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,4,15,"AWAP","AWAP","MAM",sd=sd,std=std)
stratifyCorr(awap_June,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,5,0,"AWAP","AWAP","June",sd=sd,std=std)
stratifyCorr(awap_July,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,6,1,"AWAP","AWAP","July",sd=sd,std=std)
stratifyCorr(awap_August,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,7,2,"AWAP","AWAP","August",sd=sd,std=std)
stratifyCorr(awap_September,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,8,3,"AWAP","AWAP","September",sd=sd,std=std)
stratifyCorr(awap_October,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,9,4,"AWAP","AWAP","October",sd=sd,std=std)
stratifyCorr(awap_November,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,10,5,"AWAP","AWAP","November",sd=sd,std=std)
stratifyCorr(awap_December,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,11,6,"AWAP","AWAP","December",sd=sd,std=std)
stratifyCorr(awap_January,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,12,7,"AWAP","AWAP","January",sd=sd,std=std)
stratifyCorr(awap_February,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,13,8,"AWAP","AWAP","February",sd=sd,std=std)
stratifyCorr(awap_March,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,14,9,"AWAP","AWAP","March",sd=sd,std=std)
stratifyCorr(awap_April,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,15,10,"AWAP","AWAP","April",sd=sd,std=std)
stratifyCorr(awap_May,had_ENSO_array,had_IPO_array,hadISST_ENSO,hadISST_IPO,16,11,"AWAP","AWAP","May",sd=sd,std=std)

stratifyCorr(trim_Annual,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,0,16,"ACCESS R1","R1","annual",sd=sd,std=std)
stratifyCorr(trim_JJA,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,1,12,"ACCESS R1","R1","JJA",sd=sd,std=std)
stratifyCorr(trim_SON,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,2,13,"ACCESS R1","R1","SON",sd=sd,std=std)
stratifyCorr(trim_DJF,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,3,14,"ACCESS R1","R1","DJF",sd=sd,std=std)
stratifyCorr(trim_MAM,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,4,15,"ACCESS R1","R1","MAM",sd=sd,std=std)
stratifyCorr(trim_June,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,5,0,"ACCESS R1","R1","June",sd=sd,std=std)
stratifyCorr(trim_July,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,6,1,"ACCESS R1","R1","July",sd=sd,std=std)
stratifyCorr(trim_August,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,7,2,"ACCESS R1","R1","August",sd=sd,std=std)
stratifyCorr(trim_September,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,8,3,"ACCESS R1","R1","September",sd=sd,std=std)
stratifyCorr(trim_October,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,9,4,"ACCESS R1","R1","October",sd=sd,std=std)
stratifyCorr(trim_November,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,10,5,"ACCESS R1","R1","November",sd=sd,std=std)
stratifyCorr(trim_December,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,11,6,"ACCESS R1","R1","December",sd=sd,std=std)
stratifyCorr(trim_January,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,12,7,"ACCESS R1","R1","January",sd=sd,std=std)
stratifyCorr(trim_February,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,13,8,"ACCESS R1","R1","February",sd=sd,std=std)
stratifyCorr(trim_March,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,14,9,"ACCESS R1","R1","March",sd=sd,std=std)
stratifyCorr(trim_April,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,15,10,"ACCESS R1","R1","April",sd=sd,std=std)
stratifyCorr(trim_May,R1_ENSO_array,R1_IPO_array,R1_ENSO,R1_IPO,16,11,"ACCESS R1","R1","May",sd=sd,std=std)



stratifyCorr(trim_Annual,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,0,16,"ACCESS R2","R2","annual",sd=sd,std=std)
stratifyCorr(trim_JJA,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,1,12,"ACCESS R2","R2","JJA",sd=sd,std=std)
stratifyCorr(trim_SON,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,2,13,"ACCESS R2","R2","SON",sd=sd,std=std)
stratifyCorr(trim_DJF,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,3,14,"ACCESS R2","R2","DJF",sd=sd,std=std)
stratifyCorr(trim_MAM,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,4,15,"ACCESS R2","R2","MAM",sd=sd,std=std)
stratifyCorr(trim_June,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,5,0,"ACCESS R2","R2","June",sd=sd,std=std)
stratifyCorr(trim_July,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,6,1,"ACCESS R2","R2","July",sd=sd,std=std)
stratifyCorr(trim_August,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,7,2,"ACCESS R2","R2","August",sd=sd,std=std)
stratifyCorr(trim_September,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,8,3,"ACCESS R2","R2","September",sd=sd,std=std)
stratifyCorr(trim_October,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,9,4,"ACCESS R2","R2","October",sd=sd,std=std)
stratifyCorr(trim_November,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,10,5,"ACCESS R2","R2","November",sd=sd,std=std)
stratifyCorr(trim_December,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,11,6,"ACCESS R2","R2","December",sd=sd,std=std)
stratifyCorr(trim_January,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,12,7,"ACCESS R2","R2","January",sd=sd,std=std)
stratifyCorr(trim_February,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,13,8,"ACCESS R2","R2","February",sd=sd,std=std)
stratifyCorr(trim_March,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,14,9,"ACCESS R2","R2","March",sd=sd,std=std)
stratifyCorr(trim_April,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,15,10,"ACCESS R2","R2","April",sd=sd,std=std)
stratifyCorr(trim_May,R2_ENSO_array,R2_IPO_array,R2_ENSO,R2_IPO,16,11,"ACCESS R2","R2","May",sd=sd,std=std)


stratifyCorr(trim_Annual,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,0,16,"ACCESS R3","R3","annual",sd=sd,std=std)
stratifyCorr(trim_JJA,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,1,12,"ACCESS R3","R3","JJA",sd=sd,std=std)
stratifyCorr(trim_SON,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,2,13,"ACCESS R3","R3","SON",sd=sd,std=std)
stratifyCorr(trim_DJF,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,3,14,"ACCESS R3","R3","DJF",sd=sd,std=std)
stratifyCorr(trim_MAM,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,4,15,"ACCESS R3","R3","MAM",sd=sd,std=std)
stratifyCorr(trim_June,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,5,0,"ACCESS R3","R3","June",sd=sd,std=std)
stratifyCorr(trim_July,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,6,1,"ACCESS R3","R3","July",sd=sd,std=std)
stratifyCorr(trim_August,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,7,2,"ACCESS R3","R3","August",sd=sd,std=std)
stratifyCorr(trim_September,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,8,3,"ACCESS R3","R3","September",sd=sd,std=std)
stratifyCorr(trim_October,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,9,4,"ACCESS R3","R3","October",sd=sd,std=std)
stratifyCorr(trim_November,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,10,5,"ACCESS R3","R3","November",sd=sd,std=std)
stratifyCorr(trim_December,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,11,6,"ACCESS R3","R3","December",sd=sd,std=std)
stratifyCorr(trim_January,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,12,7,"ACCESS R3","R3","January",sd=sd,std=std)
stratifyCorr(trim_February,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,13,8,"ACCESS R3","R3","February",sd=sd,std=std)
stratifyCorr(trim_March,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,14,9,"ACCESS R3","R3","March",sd=sd,std=std)
stratifyCorr(trim_April,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,15,10,"ACCESS R3","R3","April",sd=sd,std=std)
stratifyCorr(trim_May,R3_ENSO_array,R3_IPO_array,R3_ENSO,R3_IPO,16,11,"ACCESS R3","R3","May",sd=sd,std=std)

