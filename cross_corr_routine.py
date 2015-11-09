"""
A file that produces cross-correlation charts for (a) rainfall-ENSO and
rainfall-IPO data, and (b) ENSO and TPI data.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 8 October 2015.
"""
from cross_corr import *

from enso import runningSeasons

from enso_csv import enso_JJA_Had,enso_SON_Had,enso_DJF_Had,enso_MAM_Had,\
     enso_Annual_Had,cropHad,enso_JJA_R1,enso_SON_R1,enso_DJF_R1,enso_MAM_R1,\
     enso_Annual_R1,cropR1,enso_JJA_R2,enso_SON_R2,enso_DJF_R2,enso_MAM_R2,\
     enso_Annual_R2,cropR2,enso_JJA_R3,enso_SON_R3,enso_DJF_R3,enso_MAM_R3,\
     enso_Annual_R3,cropR3

from tpi_csv import Had_monthsTPI, Acc_monthsTPI_r1, Acc_monthsTPI_r2,\
     Acc_monthsTPI_r3,IPO_had_JJA,IPO_had_SON,IPO_had_DJF,IPO_had_MAM,\
     IPO_had_Annual,IPO_R1_JJA,IPO_R1_SON,IPO_R1_DJF,IPO_R1_MAM,\
     IPO_R1_Annual,IPO_R2_JJA,IPO_R2_SON,IPO_R2_DJF,IPO_R2_MAM,\
     IPO_R2_Annual,IPO_R3_JJA,IPO_R3_SON,IPO_R3_DJF,IPO_R3_MAM,\
     IPO_R3_Annual

from awap_prepare import data_flat,awap_Annual,awap_June,awap_July,awap_August,\
     awap_September,awap_October,awap_November,awap_December,awap_January,\
     awap_February,awap_March,awap_April,awap_May,awap_JJA,awap_SON,awap_DJF,\
     awap_MAM

def flatten(array):
    """
    A function to find the average rainfall value for each timestep,
    so that the data can be cross correlated with ENSO/IPO data.
    """
    list1 = []
    for i in range(0,len(array)):
        list1.append(np.ma.mean(array[i]))
    array2 = np.asarray(list1)
    return array2

def xCorr_AWAPrainfall_indices():
    """
    Generate cross-correlation plots for AWAP rainfall-ENSO and rainfall-IPO.
    """
    #ENSO
    plotXCorrel(data_flat1,cropHad,'months','AWAP-Nino 3.4 cross correlation, June 1900-May 2005',"my_coding_routines/images/xcorr_indices_rainfall/awap/All_ENSO")
    plotXCorrel(awap_Annual1,enso_Annual_Had,'years','AWAP-Nino 3.4 cross correlation, annual',"my_coding_routines/images/xcorr_indices_rainfall/awap/Annual_ENSO")
    plotXCorrel(runningSeasons(data_flat1,3,0,1),runningSeasons(cropHad,3,0,1),'seasons','AWAP-ENSO cross correlation, JJA 1900-MAM 2005',"my_coding_routines/images/xcorr_indices_rainfall/awap/Seasons_ENSO")
    plotXCorrel(awap_JJA1,enso_JJA_Had,'years','AWAP-Nino 3.4 cross correlation, JJA',"my_coding_routines/images/xcorr_indices_rainfall/awap/JJA_ENSO")
    plotXCorrel(awap_SON1,enso_SON_Had,'years','AWAP-Nino 3.4 cross correlation, SON',"my_coding_routines/images/xcorr_indices_rainfall/awap/SON_ENSO")
    plotXCorrel(awap_DJF1,enso_DJF_Had,'years','AWAP-Nino 3.4 cross correlation, DJF',"my_coding_routines/images/xcorr_indices_rainfall/awap/DJF_ENSO")
    plotXCorrel(awap_MAM1,enso_MAM_Had,'years','AWAP-Nino 3.4 cross correlation, MAM',"my_coding_routines/images/xcorr_indices_rainfall/awap/MAM_ENSO")
    #IPO
    plotXCorrel(data_flat1,Had_monthsTPI,'months','AWAP-TPI cross correlation, June 1900-May 2005',"my_coding_routines/images/xcorr_indices_rainfall/awap/All_IPO")
    plotXCorrel(awap_Annual1,IPO_had_Annual,'years','AWAP-TPI cross correlation, annual',"my_coding_routines/images/xcorr_indices_rainfall/awap/Annual_IPO")
    plotXCorrel(runningSeasons(data_flat1,3,0,1),runningSeasons(Had_monthsTPI,3,0,1),'seasons','AWAP-IPO cross correlation, JJA 1900-MAM 2005',"my_coding_routines/images/xcorr_indices_rainfall/awap/Seasons_IPO")
    plotXCorrel(awap_JJA1,IPO_had_JJA,'years','AWAP-TPI cross correlation, JJA',"my_coding_routines/images/xcorr_indices_rainfall/awap/JJA_IPO")
    plotXCorrel(awap_SON1,IPO_had_SON,'years','AWAP-TPI cross correlation, SON',"my_coding_routines/images/xcorr_indices_rainfall/awap/SON_IPO")
    plotXCorrel(awap_DJF1,IPO_had_DJF,'years','AWAP-TPI cross correlation, DJF',"my_coding_routines/images/xcorr_indices_rainfall/awap/DJF_IPO")
    plotXCorrel(awap_MAM1,IPO_had_MAM,'years','AWAP-TPI cross correlation, MAM',"my_coding_routines/images/xcorr_indices_rainfall/awap/MAM_IPO")
    return

def xCorr_ACCESSrainfall_indices(key_ENSO,key_IPO,roundNum):
    """
    Generate cross-correlation plots for ACCESS rainfall-ENSO and rainfall-IPO.

    Parameters:
    -----------
    key_ENSO : string.  The key corresponding with the ENSO values to be accessed.
    key_IPO : string.  The key corresponding with the ENSO values to be accessed. 
    roundNum : string.  'R1', 'R2' or 'R3'
    """
    Dict = {
        'R1_ENSO': [cropR1,enso_Annual_R1,enso_JJA_R1,enso_SON_R1,enso_DJF_R1,enso_MAM_R1],
        'R2_ENSO': [cropR2,enso_Annual_R2,enso_JJA_R2,enso_SON_R2,enso_DJF_R2,enso_MAM_R2],
        'R3_ENSO': [cropR3,enso_Annual_R3,enso_JJA_R3,enso_SON_R3,enso_DJF_R3,enso_MAM_R3],
        'R1_IPO': [Acc_monthsTPI_r1,IPO_R1_Annual,IPO_R1_JJA,IPO_R1_SON,IPO_R1_DJF,IPO_R1_MAM],
        'R2_IPO': [Acc_monthsTPI_r2,IPO_R2_Annual,IPO_R2_JJA,IPO_R2_SON,IPO_R2_DJF,IPO_R2_MAM],
        'R3_IPO': [Acc_monthsTPI_r3,IPO_R3_Annual,IPO_R3_JJA,IPO_R3_SON,IPO_R3_DJF,IPO_R3_MAM]
        }
    
    #ENSO
    plotXCorrel(data_flat1,Dict[key_ENSO][0],'months','ACCESS '+roundNum+'-Nino 3.4 cross correlation, June 1900-May 2005',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/All_ENSO")
    plotXCorrel(awap_Annual1,Dict[key_ENSO][1],'years','ACCESS '+roundNum+'-Nino 3.4 cross correlation, annual',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/Annual_ENSO")
    plotXCorrel(runningSeasons(data_flat1,3,0,1),runningSeasons(Dict[key_ENSO][0],3,0,1),'seasons','ACCESS '+roundNum+'-Nino 3.4 cross correlation, JJA 1900-MAM 2005',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/Seasons_ENSO")
    plotXCorrel(awap_JJA1,Dict[key_ENSO][2],'years','ACCESS '+roundNum+'-Nino 3.4 cross correlation, JJA',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/JJA_ENSO")
    plotXCorrel(awap_SON1,Dict[key_ENSO][3],'years','ACCESS '+roundNum+'-Nino 3.4 cross correlation, SON',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/SON_ENSO")
    plotXCorrel(awap_DJF1,Dict[key_ENSO][4],'years','ACCESS '+roundNum+'-Nino 3.4 cross correlation, DJF',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/DJF_ENSO")
    plotXCorrel(awap_MAM1,Dict[key_ENSO][5],'years','ACCESS '+roundNum+'-Nino 3.4 cross correlation, MAM',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/MAM_ENSO")
    #IPO
    plotXCorrel(data_flat1,Dict[key_IPO][0],'months','ACCESS '+roundNum+'-TPI cross correlation, June 1900-May 2005',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/All_IPO")
    plotXCorrel(awap_Annual1,Dict[key_IPO][1],'years','ACCESS '+roundNum+'-TPI cross correlation, annual',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/Annual_IPO")
    plotXCorrel(runningSeasons(data_flat1,3,0,1),runningSeasons(Dict[key_IPO][0],3,0,1),'seasons','ACCESS '+roundNum+'-TPI cross correlation, JJA 1900-MAM 2005',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/Seasons_IPO")
    plotXCorrel(awap_JJA1,Dict[key_IPO][2],'years','ACCESS '+roundNum+'-TPI cross correlation, JJA',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/JJA_IPO")
    plotXCorrel(awap_SON1,Dict[key_IPO][3],'years','ACCESS '+roundNum+'-TPI cross correlation, SON',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/SON_IPO")
    plotXCorrel(awap_DJF1,Dict[key_IPO][4],'years','ACCESS '+roundNum+'-TPI cross correlation, DJF',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/DJF_IPO")
    plotXCorrel(awap_MAM1,Dict[key_IPO][5],'years','ACCESS '+roundNum+'-TPI cross correlation, MAM',"my_coding_routines/images/xcorr_indices_rainfall/"+roundNum+"/MAM_IPO")
    return


def xCorrIndices_Obs():
    """
    Generate cross-correlation plots for ENSO and the IPO for
    observational data.
    """
    #ENSO-IPO
    plotXCorrel(cropHad,Had_monthsTPI,'months','Nino 3.4-TPI cross correlation, June 1900-May 2005','my_coding_routines/images/xcorr_nino_tpi/awap/All_ENSO')
    plotXCorrel(enso_Annual_Had,IPO_had_Annual,'years','Nino 3.4-TPI cross correlation, annual','my_coding_routines/images/xcorr_nino_tpi/awap/Annual_ENSO')
    plotXCorrel(runningSeasons(cropHad,3,0,1),runningSeasons(Had_monthsTPI,3,0,1),'seasons','AWAP: Nino 3.4-TPI cross correlation, JJA 1900-MAM 2005','my_coding_routines/images/xcorr_nino_tpi/awap/Seasons_ENSO')
    plotXCorrel(enso_JJA_Had,IPO_had_JJA,'years','Nino 3.4-TPI cross correlation, JJA','my_coding_routines/images/xcorr_nino_tpi/awap/JJA_ENSO')
    plotXCorrel(enso_SON_Had,IPO_had_SON,'years','Nino 3.4-TPI cross correlation, SON','my_coding_routines/images/xcorr_nino_tpi/awap/SON_ENSO')
    plotXCorrel(enso_DJF_Had,IPO_had_DJF,'years','Nino 3.4-TPI cross correlation, DJF','my_coding_routines/images/xcorr_nino_tpi/awap/DJF_ENSO')
    plotXCorrel(enso_MAM_Had,IPO_had_MAM,'years','Nino 3.4-TPI cross correlation, MAM','my_coding_routines/images/xcorr_nino_tpi/awap/MAM_ENSO')
    return

def xCorrIndices_Model(key_ENSO,key_IPO,roundNum):
    """
    Generate cross-correlation plots for ENSO and the IPO for
    modelled data.

    Parameters:
    -----------
    key_ENSO : string.  The key corresponding with the ENSO values to be accessed.
    key_IPO : string.  The key corresponding with the ENSO values to be accessed. 
    roundNum : string.  'R1', 'R2' or 'R3'
    """
    Dict = {
        'R1_ENSO': [cropR1,enso_Annual_R1,enso_JJA_R1,enso_SON_R1,enso_DJF_R1,enso_MAM_R1],
        'R2_ENSO': [cropR2,enso_Annual_R2,enso_JJA_R2,enso_SON_R2,enso_DJF_R2,enso_MAM_R2],
        'R3_ENSO': [cropR3,enso_Annual_R3,enso_JJA_R3,enso_SON_R3,enso_DJF_R3,enso_MAM_R3],
        'R1_IPO': [Acc_monthsTPI_r1,IPO_R1_Annual,IPO_R1_JJA,IPO_R1_SON,IPO_R1_DJF,IPO_R1_MAM],
        'R2_IPO': [Acc_monthsTPI_r2,IPO_R2_Annual,IPO_R2_JJA,IPO_R2_SON,IPO_R2_DJF,IPO_R2_MAM],
        'R3_IPO': [Acc_monthsTPI_r3,IPO_R3_Annual,IPO_R3_JJA,IPO_R3_SON,IPO_R3_DJF,IPO_R3_MAM]
        }
    
    #ENSO-IPO
    plotXCorrel(Dict[key_ENSO][0],Dict[key_IPO][0],'months','ACCESS '+roundNum+': Nino 3.4-TPI cross correlation, June 1900-May 2005','my_coding_routines/images/xcorr_nino_tpi/'+roundNum+'/All')
    plotXCorrel(Dict[key_ENSO][1],Dict[key_IPO][1],'years','ACCESS '+roundNum+': Nino 3.4-TPI cross correlation, annual','my_coding_routines/images/xcorr_nino_tpi/'+roundNum+'/Annual')
    plotXCorrel(runningSeasons(Dict[key_ENSO][0],3,0,1),runningSeasons(Dict[key_IPO][0],3,0,1),'seasons','ACCESS '+roundNum+': Nino 3.4-TPI cross correlation, JJA 1900-MAM 2005','my_coding_routines/images/xcorr_nino_tpi/'+roundNum+'/Seasons')
    plotXCorrel(Dict[key_ENSO][2],Dict[key_IPO][2],'years','ACCESS '+roundNum+': Nino 3.4-TPI cross correlation, JJA','my_coding_routines/images/xcorr_nino_tpi/'+roundNum+'/JJA')
    plotXCorrel(Dict[key_ENSO][3],Dict[key_IPO][3],'years','ACCESS '+roundNum+': Nino 3.4-TPI cross correlation, SON','my_coding_routines/images/xcorr_nino_tpi/'+roundNum+'/SON')
    plotXCorrel(Dict[key_ENSO][4],Dict[key_IPO][4],'years','ACCESS '+roundNum+': Nino 3.4-TPI cross correlation, DJF','my_coding_routines/images/xcorr_nino_tpi/'+roundNum+'/DJF')
    plotXCorrel(Dict[key_ENSO][5],Dict[key_IPO][5],'years','ACCESS '+roundNum+': Nino 3.4-TPI cross correlation, MAM','my_coding_routines/images/xcorr_nino_tpi/'+roundNum+'/MAM')
    return

data_flat1 = flatten(data_flat)
awap_Annual1 = flatten(awap_Annual)
awap_JJA1 = flatten(awap_JJA)
awap_SON1 = flatten(awap_SON)
awap_DJF1 = flatten(awap_DJF)
awap_MAM1 = flatten(awap_MAM)

#Generate cross correlation charts

xCorr_AWAPrainfall_indices()
xCorr_ACCESSrainfall_indices(key_ENSO='R1_ENSO',key_IPO='R1_IPO',roundNum='R1')
xCorr_ACCESSrainfall_indices(key_ENSO='R2_ENSO',key_IPO='R2_IPO',roundNum='R2')
xCorr_ACCESSrainfall_indices(key_ENSO='R3_ENSO',key_IPO='R3_IPO',roundNum='R3')

xCorrIndices_Obs()
xCorrIndices_Model(key_ENSO='R1_ENSO',key_IPO='R1_IPO',roundNum='R1')
xCorrIndices_Model(key_ENSO='R2_ENSO',key_IPO='R2_IPO',roundNum='R2')
xCorrIndices_Model(key_ENSO='R3_ENSO',key_IPO='R3_IPO',roundNum='R3')

