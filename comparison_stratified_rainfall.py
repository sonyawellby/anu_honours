"""
A script to create maps which compare stratified ACCESS/AWAP rainfall data.
Deals with standardised plots.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 19 October 2015.
"""
import numpy as np
import numpy.ma as ma

from composite import *

from awap_prepare import awap_Annual,awap_JJA,awap_SON,\
     awap_DJF,awap_MAM,awap_June,awap_July,awap_August,\
     awap_September,awap_October,awap_November,awap_December,\
     awap_January,awap_February,awap_March,awap_April,awap_May

from access_trimmed import trim_Annual,trim_June, trim_July,\
     trim_August,trim_September,trim_October,trim_November,\
     trim_December,trim_January,trim_February,trim_March,\
     trim_April,trim_May,trim_JJA,trim_SON,trim_DJF,trim_MAM

from ENSO_IPO_corr_strat import ENSO_posHad, ENSO_negHad,ENSO_neutralHad,\
     IPO_posHad, IPO_negHad,IPO_neutralHad,ENSO_posR1, ENSO_negR1,ENSO_neutralR1,\
     IPO_posR1, IPO_negR1,IPO_neutralR1,ENSO_posR2, ENSO_negR2,ENSO_neutralR2,\
     IPO_posR2, IPO_negR2,IPO_neutralR2,ENSO_posR3, ENSO_negR3,ENSO_neutralR3,\
     IPO_posR3, IPO_negR3,IPO_neutralR3

from cwd import cwdInFunction
cwdInFunction()


def stratifiedRainfall(rainfall,index_IPO,index_ENSO):
    IPO_strat = stratify(rainfall,index_IPO)
    array = stratify(IPO_strat,index_ENSO)
    array_average = stratifyAverage(array)
    return array_average

def standardised(rainfall,array_index_IPO,array_index_ENSO,num_i):
    array1 = stratifiedRainfall(rainfall,array_index_IPO[0][num_i],array_index_ENSO[0][num_i])
    array2 = stratifiedRainfall(rainfall,array_index_IPO[0][num_i],array_index_ENSO[2][num_i])
    array3 = stratifiedRainfall(rainfall,array_index_IPO[0][num_i],array_index_ENSO[1][num_i])
    array4 = stratifiedRainfall(rainfall,array_index_IPO[2][num_i],array_index_ENSO[0][num_i])
    array5 = stratifiedRainfall(rainfall,array_index_IPO[2][num_i],array_index_ENSO[2][num_i])
    array6 = stratifiedRainfall(rainfall,array_index_IPO[2][num_i],array_index_ENSO[1][num_i])
    array7 = stratifiedRainfall(rainfall,array_index_IPO[1][num_i],array_index_ENSO[0][num_i])
    array8 = stratifiedRainfall(rainfall,array_index_IPO[1][num_i],array_index_ENSO[2][num_i])
    array9 = stratifiedRainfall(rainfall,array_index_IPO[1][num_i],array_index_ENSO[1][num_i])

    new_list = [array1,array2,array3,array4,array5,array6,array7,array8,array9]

    std = np.ma.std(rainfall[60:91])
    list1 = []
    for i in new_list:
        climate_mean = np.ma.mean(rainfall[60:91],axis=0)
        anomaly = np.ma.subtract(i,climate_mean)
        list1.append(np.ma.divide(anomaly,std))
    new_array = np.asarray(list1)
    return new_array

def standardisedPlots(rainfall,index_IPO,index_ENSO,num_i,num,time,rainfall_data,rainfall_data_type,std):
    output = standardised(rainfall,index_IPO,index_ENSO,num_i)
    plotStratStandardised(output[0],rainfall,'',"standardised/"+num+"/"+time+"/"+rainfall_data+"/1")
    plotStratStandardised(output[1],rainfall,'',"standardised/"+num+"/"+time+"/"+rainfall_data+"/2")
    plotStratStandardised(output[2],rainfall,'',"standardised/"+num+"/"+time+"/"+rainfall_data+"/3")
    plotStratStandardised(output[3],rainfall,'',"standardised/"+num+"/"+time+"/"+rainfall_data+"/4")
    plotStratStandardised(output[4],rainfall,'',"standardised/"+num+"/"+time+"/"+rainfall_data+"/5")
    plotStratStandardised(output[5],rainfall,'',"standardised/"+num+"/"+time+"/"+rainfall_data+"/6")
    plotStratStandardised(output[6],rainfall,'',"standardised/"+num+"/"+time+"/"+rainfall_data+"/7")
    plotStratStandardised(output[7],rainfall,'',"standardised/"+num+"/"+time+"/"+rainfall_data+"/8")
    plotStratStandardised(output[8],rainfall,'',"standardised/"+num+"/"+time+"/"+rainfall_data+"/9")

    mapStandardised = multi("my_coding_routines/images/standardised/"+num+"/"+time+"/"+rainfall_data+"/*.png",3,3,title=(r''+rainfall_data_type+' '+time+': standardised mean rainfall'+std))
    maps_sub.saveFig(mapStandardised,"","standardised/"+num+"_compiled/"+rainfall_data+"/"+time)
    return

########################################################################################
# Make index arrays available for use
########################################################################################

had_ENSO_array = [ENSO_posHad,ENSO_negHad,ENSO_neutralHad]
had_IPO_array = [IPO_posHad,IPO_negHad,IPO_neutralHad]
R1_ENSO_array = [ENSO_posR1,ENSO_negR1,ENSO_neutralR1]
R1_IPO_array = [IPO_posR1,IPO_negR1,IPO_neutralR1]
R2_ENSO_array = [ENSO_posR2,ENSO_negR2,ENSO_neutralR2]
R2_IPO_array = [IPO_posR2,IPO_negR2,IPO_neutralR2]
R3_ENSO_array = [ENSO_posR3,ENSO_negR3,ENSO_neutralR3]
R3_IPO_array = [IPO_posR3,IPO_negR3,IPO_neutralR3]

########################################################################################
# Create standardised maps
########################################################################################

def runAWAP(std,std_caption):
    standardisedPlots(awap_Annual,had_IPO_array,had_ENSO_array,0,std,'annual','AWAP','AWAP',std_caption)
    standardisedPlots(awap_JJA,had_IPO_array,had_ENSO_array,1,std,'JJA','AWAP','AWAP',std_caption)
    standardisedPlots(awap_SON,had_IPO_array,had_ENSO_array,2,std,'SON','AWAP','AWAP',std_caption)
    standardisedPlots(awap_DJF,had_IPO_array,had_ENSO_array,3,std,'DJF','AWAP','AWAP',std_caption)
    standardisedPlots(awap_MAM,had_IPO_array,had_ENSO_array,4,std,'MAM','AWAP','AWAP',std_caption)
    standardisedPlots(awap_June,had_IPO_array,had_ENSO_array,5,std,'June','AWAP','AWAP',std_caption)
    standardisedPlots(awap_July,had_IPO_array,had_ENSO_array,6,std,'July','AWAP','AWAP',std_caption)
    standardisedPlots(awap_August,had_IPO_array,had_ENSO_array,7,std,'August','AWAP','AWAP',std_caption)
    standardisedPlots(awap_September,had_IPO_array,had_ENSO_array,8,std,'September','AWAP','AWAP',std_caption)
    standardisedPlots(awap_October,had_IPO_array,had_ENSO_array,9,std,'October','AWAP','AWAP',std_caption)
    standardisedPlots(awap_November,had_IPO_array,had_ENSO_array,10,std,'November','AWAP','AWAP',std_caption)
    standardisedPlots(awap_December,had_IPO_array,had_ENSO_array,11,std,'December','AWAP','AWAP',std_caption)
    standardisedPlots(awap_January,had_IPO_array,had_ENSO_array,12,std,'January','AWAP','AWAP',std_caption)
    standardisedPlots(awap_February,had_IPO_array,had_ENSO_array,13,std,'February','AWAP','AWAP',std_caption)
    standardisedPlots(awap_March,had_IPO_array,had_ENSO_array,14,std,'March','AWAP','AWAP',std_caption)
    standardisedPlots(awap_April,had_IPO_array,had_ENSO_array,15,std,'April','AWAP','AWAP',std_caption)
    standardisedPlots(awap_May,had_IPO_array,had_ENSO_array,16,std,'May','AWAP','AWAP',std_caption)
    return

def runACCESS(std,roundNum, roundTitle,std_caption):
    standardisedPlots(trim_Annual,had_IPO_array,had_ENSO_array,0,std,'annual',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_JJA,had_IPO_array,had_ENSO_array,1,std,'JJA',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_SON,had_IPO_array,had_ENSO_array,2,std,'SON',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_DJF,had_IPO_array,had_ENSO_array,3,std,'DJF',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_MAM,had_IPO_array,had_ENSO_array,4,std,'MAM',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_June,had_IPO_array,had_ENSO_array,5,std,'June',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_July,had_IPO_array,had_ENSO_array,6,std,'July',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_August,had_IPO_array,had_ENSO_array,7,std,'August',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_September,had_IPO_array,had_ENSO_array,8,std,'September',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_October,had_IPO_array,had_ENSO_array,9,std,'October',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_November,had_IPO_array,had_ENSO_array,10,std,'November',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_December,had_IPO_array,had_ENSO_array,11,std,'December',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_January,had_IPO_array,had_ENSO_array,12,std,'January',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_February,had_IPO_array,had_ENSO_array,13,std,'February',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_March,had_IPO_array,had_ENSO_array,14,std,'March',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_April,had_IPO_array,had_ENSO_array,15,std,'April',roundNum,roundTitle,std_caption)
    standardisedPlots(trim_May,had_IPO_array,had_ENSO_array,16,std,'May',roundNum,roundTitle,std_caption)
    return

runAWAP('1_SD','')
runAWAP('2_SD',r' (2 $\sigma$)')
runAWAP('3_SD',r' (3 $\sigma$)')

runACCESS('1_SD','R1','ACCESS R1','')
runACCESS('2_SD','R1','ACCESS R1',r' (2 $\sigma$)')
runACCESS('3_SD','R1','ACCESS R1',r' (3 $\sigma$)') 

runACCESS('1_SD','R2','ACCESS R2','')
runACCESS('2_SD','R2','ACCESS R2',r'(2 $\sigma$)')
runACCESS('3_SD','R2','ACCESS R2', r' (3 $\sigma$)') 

runACCESS('1_SD','R3','ACCESS R3','')
runACCESS('2_SD','R3','ACCESS R3',r' (2 $\sigma$)')
runACCESS('3_SD','R3','ACCESS R3', r' (3 $\sigma$)') 
