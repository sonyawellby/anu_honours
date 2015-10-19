"""
Code which stratifies ENSO/IPO and ACCESS1.3 R2 rainfall data
for composite analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 17 September 2015.
"""
from composite import *
import indices_phase
import awap_prepare
import access_trimmed

#Change as required to "1_sd", "2_sd", "3_sd"
num = "1_sd"
sigma = '' # ' (2 $\sigma$)'  ' (3 $\sigma$)'

#ACCESS R2: June

output(access_trimmed.trim_June,indices_phase.IPO_posR2_Jun,indices_phase.ENSO_posR2_Jun,\
       "","/composite/"+num+"/rainfall/R2/June/1","/composite/"+num+"/rainfall_anomalies/R2/June/1")
output(access_trimmed.trim_June,indices_phase.IPO_posR2_Jun,indices_phase.ENSO_neutralR2_Jun,\
       "","/composite/"+num+"/rainfall/R2/June/2","/composite/"+num+"/rainfall_anomalies/R2/June/2")
output(access_trimmed.trim_June,indices_phase.IPO_posR2_Jun,indices_phase.ENSO_negR2_Jun,\
       "","/composite/"+num+"/rainfall/R2/June/3","/composite/"+num+"/rainfall_anomalies/R2/June/3")
output(access_trimmed.trim_June,indices_phase.IPO_neutralR2_Jun,indices_phase.ENSO_posR2_Jun,\
       "","/composite/"+num+"/rainfall/R2/June/4","/composite/"+num+"/rainfall_anomalies/R2/June/4")
output(access_trimmed.trim_June,indices_phase.IPO_neutralR2_Jun,indices_phase.ENSO_neutralR2_Jun,\
       "","/composite/"+num+"/rainfall/R2/June/5","/composite/"+num+"/rainfall_anomalies/R2/June/5")
output(access_trimmed.trim_June,indices_phase.IPO_neutralR2_Jun,indices_phase.ENSO_negR2_Jun,\
       "","/composite/"+num+"/rainfall/R2/June/6","/composite/"+num+"/rainfall_anomalies/R2/June/6")
output(access_trimmed.trim_June,indices_phase.IPO_negR2_Jun,indices_phase.ENSO_posR2_Jun,\
       "","/composite/"+num+"/rainfall/R2/June/7","/composite/"+num+"/rainfall_anomalies/R2/June/7")
output(access_trimmed.trim_June,indices_phase.IPO_negR2_Jun,indices_phase.ENSO_neutralR2_Jun,\
       "","/composite/"+num+"/rainfall/R2/June/8","/composite/"+num+"/rainfall_anomalies/R2/June/8")
output(access_trimmed.trim_June,indices_phase.IPO_negR2_Jun,indices_phase.ENSO_negR2_Jun,\
       "","/composite/"+num+"/rainfall/R2/June/9","/composite/"+num+"/rainfall_anomalies/R2/June/9")

ACCESS_June = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/June/*.png",3,3,title=(r'ACCESS1.3 R2 June: mean rainfall'+sigma))
ACCESS_June_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/June/*.png",3,3,title=(r'ACCESS1.3 R2 June: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_June,"","composite/"+num+"_compiled/R2/ACCESS_June")
maps_sub.saveFig(ACCESS_June_Anom,"","composite/"+num+"_compiled/R2/ACCESS_June_Anom")


#ACCESS R2: July

output(access_trimmed.trim_July,indices_phase.IPO_posR2_Jul,indices_phase.ENSO_posR2_Jul,\
       "","/composite/"+num+"/rainfall/R2/July/1","/composite/"+num+"/rainfall_anomalies/R2/July/1")
output(access_trimmed.trim_July,indices_phase.IPO_posR2_Jul,indices_phase.ENSO_neutralR2_Jul,\
       "","/composite/"+num+"/rainfall/R2/July/2","/composite/"+num+"/rainfall_anomalies/R2/July/2")
output(access_trimmed.trim_July,indices_phase.IPO_posR2_Jul,indices_phase.ENSO_negR2_Jul,\
       "","/composite/"+num+"/rainfall/R2/July/3","/composite/"+num+"/rainfall_anomalies/R2/July/3")
output(access_trimmed.trim_July,indices_phase.IPO_neutralR2_Jul,indices_phase.ENSO_posR2_Jul,\
       "","/composite/"+num+"/rainfall/R2/July/4","/composite/"+num+"/rainfall_anomalies/R2/July/4")
output(access_trimmed.trim_July,indices_phase.IPO_neutralR2_Jul,indices_phase.ENSO_neutralR2_Jul,\
       "","/composite/"+num+"/rainfall/R2/July/5","/composite/"+num+"/rainfall_anomalies/R2/July/5")
output(access_trimmed.trim_July,indices_phase.IPO_neutralR2_Jul,indices_phase.ENSO_negR2_Jul,\
       "","/composite/"+num+"/rainfall/R2/July/6","/composite/"+num+"/rainfall_anomalies/R2/July/6")
output(access_trimmed.trim_July,indices_phase.IPO_negR2_Jul,indices_phase.ENSO_posR2_Jul,\
       "","/composite/"+num+"/rainfall/R2/July/7","/composite/"+num+"/rainfall_anomalies/R2/July/7")
output(access_trimmed.trim_July,indices_phase.IPO_negR2_Jul,indices_phase.ENSO_neutralR2_Jul,\
       "","/composite/"+num+"/rainfall/R2/July/8","/composite/"+num+"/rainfall_anomalies/R2/July/8")
output(access_trimmed.trim_July,indices_phase.IPO_negR2_Jul,indices_phase.ENSO_negR2_Jul,\
       "","/composite/"+num+"/rainfall/R2/July/9","/composite/"+num+"/rainfall_anomalies/R2/July/9")

ACCESS_July = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/July/*.png",3,3,title=(r'ACCESS1.3 R2 July: mean rainfall'+sigma))
ACCESS_July_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/July/*.png",3,3,title=(r'ACCESS1.3 R2 July: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_July,"","composite/"+num+"_compiled/R2/ACCESS_July")
maps_sub.saveFig(ACCESS_July_Anom,"","composite/"+num+"_compiled/R2/ACCESS_July_Anom")


#ACCESS R2: August

output(access_trimmed.trim_August,indices_phase.IPO_posR2_Aug,indices_phase.ENSO_posR2_Aug,\
       "","/composite/"+num+"/rainfall/R2/August/1","/composite/"+num+"/rainfall_anomalies/R2/August/1")
output(access_trimmed.trim_August,indices_phase.IPO_posR2_Aug,indices_phase.ENSO_neutralR2_Aug,\
       "","/composite/"+num+"/rainfall/R2/August/2","/composite/"+num+"/rainfall_anomalies/R2/August/2")
output(access_trimmed.trim_August,indices_phase.IPO_posR2_Aug,indices_phase.ENSO_negR2_Aug,\
       "","/composite/"+num+"/rainfall/R2/August/3","/composite/"+num+"/rainfall_anomalies/R2/August/3")
output(access_trimmed.trim_August,indices_phase.IPO_neutralR2_Aug,indices_phase.ENSO_posR2_Aug,\
       "","/composite/"+num+"/rainfall/R2/August/4","/composite/"+num+"/rainfall_anomalies/R2/August/4")
output(access_trimmed.trim_August,indices_phase.IPO_neutralR2_Aug,indices_phase.ENSO_neutralR2_Aug,\
       "","/composite/"+num+"/rainfall/R2/August/5","/composite/"+num+"/rainfall_anomalies/R2/August/5")
output(access_trimmed.trim_August,indices_phase.IPO_neutralR2_Aug,indices_phase.ENSO_negR2_Aug,\
       "","/composite/"+num+"/rainfall/R2/August/6","/composite/"+num+"/rainfall_anomalies/R2/August/6")
output(access_trimmed.trim_August,indices_phase.IPO_negR2_Aug,indices_phase.ENSO_posR2_Aug,\
       "","/composite/"+num+"/rainfall/R2/August/7","/composite/"+num+"/rainfall_anomalies/R2/August/7")
output(access_trimmed.trim_August,indices_phase.IPO_negR2_Aug,indices_phase.ENSO_neutralR2_Aug,\
       "","/composite/"+num+"/rainfall/R2/August/8","/composite/"+num+"/rainfall_anomalies/R2/August/8")
output(access_trimmed.trim_August,indices_phase.IPO_negR2_Aug,indices_phase.ENSO_negR2_Aug,\
       "","/composite/"+num+"/rainfall/R2/August/9","/composite/"+num+"/rainfall_anomalies/R2/August/9")

ACCESS_August = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/August/*.png",3,3,title=(r'ACCESS1.3 R2 August: mean rainfall'+sigma))
ACCESS_August_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/August/*.png",3,3,title=(r'ACCESS1.3 R2 August: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_August,"","composite/"+num+"_compiled/R2/ACCESS_August")
maps_sub.saveFig(ACCESS_August_Anom,"","composite/"+num+"_compiled/R2/ACCESS_August_Anom")


#ACCESS R2: September

output(access_trimmed.trim_September,indices_phase.IPO_posR2_Sep,indices_phase.ENSO_posR2_Sep,\
       "","/composite/"+num+"/rainfall/R2/September/1","/composite/"+num+"/rainfall_anomalies/R2/September/1")
output(access_trimmed.trim_September,indices_phase.IPO_posR2_Sep,indices_phase.ENSO_neutralR2_Sep,\
       "","/composite/"+num+"/rainfall/R2/September/2","/composite/"+num+"/rainfall_anomalies/R2/September/2")
output(access_trimmed.trim_September,indices_phase.IPO_posR2_Sep,indices_phase.ENSO_negR2_Sep,\
       "","/composite/"+num+"/rainfall/R2/September/3","/composite/"+num+"/rainfall_anomalies/R2/September/3")
output(access_trimmed.trim_September,indices_phase.IPO_neutralR2_Sep,indices_phase.ENSO_posR2_Sep,\
       "","/composite/"+num+"/rainfall/R2/September/4","/composite/"+num+"/rainfall_anomalies/R2/September/4")
output(access_trimmed.trim_September,indices_phase.IPO_neutralR2_Sep,indices_phase.ENSO_neutralR2_Sep,\
       "","/composite/"+num+"/rainfall/R2/September/5","/composite/"+num+"/rainfall_anomalies/R2/September/5")
output(access_trimmed.trim_September,indices_phase.IPO_neutralR2_Sep,indices_phase.ENSO_negR2_Sep,\
       "","/composite/"+num+"/rainfall/R2/September/6","/composite/"+num+"/rainfall_anomalies/R2/September/6")
output(access_trimmed.trim_September,indices_phase.IPO_negR2_Sep,indices_phase.ENSO_posR2_Sep,\
       "","/composite/"+num+"/rainfall/R2/September/7","/composite/"+num+"/rainfall_anomalies/R2/September/7")
output(access_trimmed.trim_September,indices_phase.IPO_negR2_Sep,indices_phase.ENSO_neutralR2_Sep,\
       "","/composite/"+num+"/rainfall/R2/September/8","/composite/"+num+"/rainfall_anomalies/R2/September/8")
output(access_trimmed.trim_September,indices_phase.IPO_negR2_Sep,indices_phase.ENSO_negR2_Sep,\
       "","/composite/"+num+"/rainfall/R2/September/9","/composite/"+num+"/rainfall_anomalies/R2/September/9")

ACCESS_September = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/September/*.png",3,3,title=(r'ACCESS1.3 R2 September: mean rainfall'+sigma))
ACCESS_September_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/September/*.png",3,3,title=(r'ACCESS1.3 R2 September: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_September,"","composite/"+num+"_compiled/R2/ACCESS_September")
maps_sub.saveFig(ACCESS_September_Anom,"","composite/"+num+"_compiled/R2/ACCESS_September_Anom")


#ACCESS R2: October

output(access_trimmed.trim_October,indices_phase.IPO_posR2_Oct,indices_phase.ENSO_posR2_Oct,\
       "","/composite/"+num+"/rainfall/R2/October/1","/composite/"+num+"/rainfall_anomalies/R2/October/1")
output(access_trimmed.trim_October,indices_phase.IPO_posR2_Oct,indices_phase.ENSO_neutralR2_Oct,\
       "","/composite/"+num+"/rainfall/R2/October/2","/composite/"+num+"/rainfall_anomalies/R2/October/2")
output(access_trimmed.trim_October,indices_phase.IPO_posR2_Oct,indices_phase.ENSO_negR2_Oct,\
       "","/composite/"+num+"/rainfall/R2/October/3","/composite/"+num+"/rainfall_anomalies/R2/October/3")
output(access_trimmed.trim_October,indices_phase.IPO_neutralR2_Oct,indices_phase.ENSO_posR2_Oct,\
       "","/composite/"+num+"/rainfall/R2/October/4","/composite/"+num+"/rainfall_anomalies/R2/October/4")
output(access_trimmed.trim_October,indices_phase.IPO_neutralR2_Oct,indices_phase.ENSO_neutralR2_Oct,\
       "","/composite/"+num+"/rainfall/R2/October/5","/composite/"+num+"/rainfall_anomalies/R2/October/5")
output(access_trimmed.trim_October,indices_phase.IPO_neutralR2_Oct,indices_phase.ENSO_negR2_Oct,\
       "","/composite/"+num+"/rainfall/R2/October/6","/composite/"+num+"/rainfall_anomalies/R2/October/6")
output(access_trimmed.trim_October,indices_phase.IPO_negR2_Oct,indices_phase.ENSO_posR2_Oct,\
       "","/composite/"+num+"/rainfall/R2/October/7","/composite/"+num+"/rainfall_anomalies/R2/October/7")
output(access_trimmed.trim_October,indices_phase.IPO_negR2_Oct,indices_phase.ENSO_neutralR2_Oct,\
       "","/composite/"+num+"/rainfall/R2/October/8","/composite/"+num+"/rainfall_anomalies/R2/October/8")
output(access_trimmed.trim_October,indices_phase.IPO_negR2_Oct,indices_phase.ENSO_negR2_Oct,\
       "","/composite/"+num+"/rainfall/R2/October/9","/composite/"+num+"/rainfall_anomalies/R2/October/9")

ACCESS_October = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/October/*.png",3,3,title=(r'ACCESS1.3 R2 October: mean rainfall'+sigma))
ACCESS_October_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/October/*.png",3,3,title=(r'ACCESS1.3 R2 October: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_October,"","composite/"+num+"_compiled/R2/ACCESS_October")
maps_sub.saveFig(ACCESS_October_Anom,"","composite/"+num+"_compiled/R2/ACCESS_October_Anom")


#ACCESS R2: November

output(access_trimmed.trim_November,indices_phase.IPO_posR2_Nov,indices_phase.ENSO_posR2_Nov,\
       "","/composite/"+num+"/rainfall/R2/November/1","/composite/"+num+"/rainfall_anomalies/R2/November/1")
output(access_trimmed.trim_November,indices_phase.IPO_posR2_Nov,indices_phase.ENSO_neutralR2_Nov,\
       "","/composite/"+num+"/rainfall/R2/November/2","/composite/"+num+"/rainfall_anomalies/R2/November/2")
output(access_trimmed.trim_November,indices_phase.IPO_posR2_Nov,indices_phase.ENSO_negR2_Nov,\
       "","/composite/"+num+"/rainfall/R2/November/3","/composite/"+num+"/rainfall_anomalies/R2/November/3")
output(access_trimmed.trim_November,indices_phase.IPO_neutralR2_Nov,indices_phase.ENSO_posR2_Nov,\
       "","/composite/"+num+"/rainfall/R2/November/4","/composite/"+num+"/rainfall_anomalies/R2/November/4")
output(access_trimmed.trim_November,indices_phase.IPO_neutralR2_Nov,indices_phase.ENSO_neutralR2_Nov,\
       "","/composite/"+num+"/rainfall/R2/November/5","/composite/"+num+"/rainfall_anomalies/R2/November/5")
output(access_trimmed.trim_November,indices_phase.IPO_neutralR2_Nov,indices_phase.ENSO_negR2_Nov,\
       "","/composite/"+num+"/rainfall/R2/November/6","/composite/"+num+"/rainfall_anomalies/R2/November/6")
output(access_trimmed.trim_November,indices_phase.IPO_negR2_Nov,indices_phase.ENSO_posR2_Nov,\
       "","/composite/"+num+"/rainfall/R2/November/7","/composite/"+num+"/rainfall_anomalies/R2/November/7")
output(access_trimmed.trim_November,indices_phase.IPO_negR2_Nov,indices_phase.ENSO_neutralR2_Nov,\
       "","/composite/"+num+"/rainfall/R2/November/8","/composite/"+num+"/rainfall_anomalies/R2/November/8")
output(access_trimmed.trim_November,indices_phase.IPO_negR2_Nov,indices_phase.ENSO_negR2_Nov,\
       "","/composite/"+num+"/rainfall/R2/November/9","/composite/"+num+"/rainfall_anomalies/R2/November/9")

ACCESS_November = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/November/*.png",3,3,title=(r'ACCESS1.3 R2 November: mean rainfall'+sigma))
ACCESS_November_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/November/*.png",3,3,title=(r'ACCESS1.3 R2 November: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_November,"","composite/"+num+"_compiled/R2/ACCESS_November")
maps_sub.saveFig(ACCESS_November_Anom,"","composite/"+num+"_compiled/R2/ACCESS_November_Anom")


#ACCESS R2: December

output(access_trimmed.trim_December,indices_phase.IPO_posR2_Dec,indices_phase.ENSO_posR2_Dec,\
       "","/composite/"+num+"/rainfall/R2/December/1","/composite/"+num+"/rainfall_anomalies/R2/December/1")
output(access_trimmed.trim_December,indices_phase.IPO_posR2_Dec,indices_phase.ENSO_neutralR2_Dec,\
       "","/composite/"+num+"/rainfall/R2/December/2","/composite/"+num+"/rainfall_anomalies/R2/December/2")
output(access_trimmed.trim_December,indices_phase.IPO_posR2_Dec,indices_phase.ENSO_negR2_Dec,\
       "","/composite/"+num+"/rainfall/R2/December/3","/composite/"+num+"/rainfall_anomalies/R2/December/3")
output(access_trimmed.trim_December,indices_phase.IPO_neutralR2_Dec,indices_phase.ENSO_posR2_Dec,\
       "","/composite/"+num+"/rainfall/R2/December/4","/composite/"+num+"/rainfall_anomalies/R2/December/4")
output(access_trimmed.trim_December,indices_phase.IPO_neutralR2_Dec,indices_phase.ENSO_neutralR2_Dec,\
       "","/composite/"+num+"/rainfall/R2/December/5","/composite/"+num+"/rainfall_anomalies/R2/December/5")
output(access_trimmed.trim_December,indices_phase.IPO_neutralR2_Dec,indices_phase.ENSO_negR2_Dec,\
       "","/composite/"+num+"/rainfall/R2/December/6","/composite/"+num+"/rainfall_anomalies/R2/December/6")
output(access_trimmed.trim_December,indices_phase.IPO_negR2_Dec,indices_phase.ENSO_posR2_Dec,\
       "","/composite/"+num+"/rainfall/R2/December/7","/composite/"+num+"/rainfall_anomalies/R2/December/7")
output(access_trimmed.trim_December,indices_phase.IPO_negR2_Dec,indices_phase.ENSO_neutralR2_Dec,\
       "","/composite/"+num+"/rainfall/R2/December/8","/composite/"+num+"/rainfall_anomalies/R2/December/8")
output(access_trimmed.trim_December,indices_phase.IPO_negR2_Dec,indices_phase.ENSO_negR2_Dec,\
       "","/composite/"+num+"/rainfall/R2/December/9","/composite/"+num+"/rainfall_anomalies/R2/December/9")

ACCESS_December = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/December/*.png",3,3,title=(r'ACCESS1.3 R2 December: mean rainfall'+sigma))
ACCESS_December_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/December/*.png",3,3,title=(r'ACCESS1.3 R2 December: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_December,"","composite/"+num+"_compiled/R2/ACCESS_December")
maps_sub.saveFig(ACCESS_December_Anom,"","composite/"+num+"_compiled/R2/ACCESS_December_Anom")


#ACCESS R2: January

output(access_trimmed.trim_January,indices_phase.IPO_posR2_Jan,indices_phase.ENSO_posR2_Jan,\
       "","/composite/"+num+"/rainfall/R2/January/1","/composite/"+num+"/rainfall_anomalies/R2/January/1")
output(access_trimmed.trim_January,indices_phase.IPO_posR2_Jan,indices_phase.ENSO_neutralR2_Jan,\
       "","/composite/"+num+"/rainfall/R2/January/2","/composite/"+num+"/rainfall_anomalies/R2/January/2")
output(access_trimmed.trim_January,indices_phase.IPO_posR2_Jan,indices_phase.ENSO_negR2_Jan,\
       "","/composite/"+num+"/rainfall/R2/January/3","/composite/"+num+"/rainfall_anomalies/R2/January/3")
output(access_trimmed.trim_January,indices_phase.IPO_neutralR2_Jan,indices_phase.ENSO_posR2_Jan,\
       "","/composite/"+num+"/rainfall/R2/January/4","/composite/"+num+"/rainfall_anomalies/R2/January/4")
output(access_trimmed.trim_January,indices_phase.IPO_neutralR2_Jan,indices_phase.ENSO_neutralR2_Jan,\
       "","/composite/"+num+"/rainfall/R2/January/5","/composite/"+num+"/rainfall_anomalies/R2/January/5")
output(access_trimmed.trim_January,indices_phase.IPO_neutralR2_Jan,indices_phase.ENSO_negR2_Jan,\
       "","/composite/"+num+"/rainfall/R2/January/6","/composite/"+num+"/rainfall_anomalies/R2/January/6")
output(access_trimmed.trim_January,indices_phase.IPO_negR2_Jan,indices_phase.ENSO_posR2_Jan,\
       "","/composite/"+num+"/rainfall/R2/January/7","/composite/"+num+"/rainfall_anomalies/R2/January/7")
output(access_trimmed.trim_January,indices_phase.IPO_negR2_Jan,indices_phase.ENSO_neutralR2_Jan,\
       "","/composite/"+num+"/rainfall/R2/January/8","/composite/"+num+"/rainfall_anomalies/R2/January/8")
output(access_trimmed.trim_January,indices_phase.IPO_negR2_Jan,indices_phase.ENSO_negR2_Jan,\
       "","/composite/"+num+"/rainfall/R2/January/9","/composite/"+num+"/rainfall_anomalies/R2/January/9")

ACCESS_January = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/January/*.png",3,3,title=(r'ACCESS1.3 R2 January: mean rainfall'+sigma))
ACCESS_January_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/January/*.png",3,3,title=(r'ACCESS1.3 R2 January: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_January,"","composite/"+num+"_compiled/R2/ACCESS_January")
maps_sub.saveFig(ACCESS_January_Anom,"","composite/"+num+"_compiled/R2/ACCESS_January_Anom")


#ACCESS R2: February

output(access_trimmed.trim_February,indices_phase.IPO_posR2_Feb,indices_phase.ENSO_posR2_Feb,\
       "","/composite/"+num+"/rainfall/R2/February/1","/composite/"+num+"/rainfall_anomalies/R2/February/1")
output(access_trimmed.trim_February,indices_phase.IPO_posR2_Feb,indices_phase.ENSO_neutralR2_Feb,\
       "","/composite/"+num+"/rainfall/R2/February/2","/composite/"+num+"/rainfall_anomalies/R2/February/2")
output(access_trimmed.trim_February,indices_phase.IPO_posR2_Feb,indices_phase.ENSO_negR2_Feb,\
       "","/composite/"+num+"/rainfall/R2/February/3","/composite/"+num+"/rainfall_anomalies/R2/February/3")
output(access_trimmed.trim_February,indices_phase.IPO_neutralR2_Feb,indices_phase.ENSO_posR2_Feb,\
       "","/composite/"+num+"/rainfall/R2/February/4","/composite/"+num+"/rainfall_anomalies/R2/February/4")
output(access_trimmed.trim_February,indices_phase.IPO_neutralR2_Feb,indices_phase.ENSO_neutralR2_Feb,\
       "","/composite/"+num+"/rainfall/R2/February/5","/composite/"+num+"/rainfall_anomalies/R2/February/5")
output(access_trimmed.trim_February,indices_phase.IPO_neutralR2_Feb,indices_phase.ENSO_negR2_Feb,\
       "","/composite/"+num+"/rainfall/R2/February/6","/composite/"+num+"/rainfall_anomalies/R2/February/6")
output(access_trimmed.trim_February,indices_phase.IPO_negR2_Feb,indices_phase.ENSO_posR2_Feb,\
       "","/composite/"+num+"/rainfall/R2/February/7","/composite/"+num+"/rainfall_anomalies/R2/February/7")
output(access_trimmed.trim_February,indices_phase.IPO_negR2_Feb,indices_phase.ENSO_neutralR2_Feb,\
       "","/composite/"+num+"/rainfall/R2/February/8","/composite/"+num+"/rainfall_anomalies/R2/February/8")
output(access_trimmed.trim_February,indices_phase.IPO_negR2_Feb,indices_phase.ENSO_negR2_Feb,\
       "","/composite/"+num+"/rainfall/R2/February/9","/composite/"+num+"/rainfall_anomalies/R2/February/9")

ACCESS_February = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/February/*.png",3,3,title=(r'ACCESS1.3 R2 February: mean rainfall'+sigma))
ACCESS_February_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/February/*.png",3,3,title=(r'ACCESS1.3 R2 February: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_February,"","composite/"+num+"_compiled/R2/ACCESS_February")
maps_sub.saveFig(ACCESS_February_Anom,"","composite/"+num+"_compiled/R2/ACCESS_February_Anom")


#ACCESS R2: March

output(access_trimmed.trim_March,indices_phase.IPO_posR2_Mar,indices_phase.ENSO_posR2_Mar,\
       "","/composite/"+num+"/rainfall/R2/March/1","/composite/"+num+"/rainfall_anomalies/R2/March/1")
output(access_trimmed.trim_March,indices_phase.IPO_posR2_Mar,indices_phase.ENSO_neutralR2_Mar,\
       "","/composite/"+num+"/rainfall/R2/March/2","/composite/"+num+"/rainfall_anomalies/R2/March/2")
output(access_trimmed.trim_March,indices_phase.IPO_posR2_Mar,indices_phase.ENSO_negR2_Mar,\
       "","/composite/"+num+"/rainfall/R2/March/3","/composite/"+num+"/rainfall_anomalies/R2/March/3")
output(access_trimmed.trim_March,indices_phase.IPO_neutralR2_Mar,indices_phase.ENSO_posR2_Mar,\
       "","/composite/"+num+"/rainfall/R2/March/4","/composite/"+num+"/rainfall_anomalies/R2/March/4")
output(access_trimmed.trim_March,indices_phase.IPO_neutralR2_Mar,indices_phase.ENSO_neutralR2_Mar,\
       "","/composite/"+num+"/rainfall/R2/March/5","/composite/"+num+"/rainfall_anomalies/R2/March/5")
output(access_trimmed.trim_March,indices_phase.IPO_neutralR2_Mar,indices_phase.ENSO_negR2_Mar,\
       "","/composite/"+num+"/rainfall/R2/March/6","/composite/"+num+"/rainfall_anomalies/R2/March/6")
output(access_trimmed.trim_March,indices_phase.IPO_negR2_Mar,indices_phase.ENSO_posR2_Mar,\
       "","/composite/"+num+"/rainfall/R2/March/7","/composite/"+num+"/rainfall_anomalies/R2/March/7")
output(access_trimmed.trim_March,indices_phase.IPO_negR2_Mar,indices_phase.ENSO_neutralR2_Mar,\
       "","/composite/"+num+"/rainfall/R2/March/8","/composite/"+num+"/rainfall_anomalies/R2/March/8")
output(access_trimmed.trim_March,indices_phase.IPO_negR2_Mar,indices_phase.ENSO_negR2_Mar,\
       "","/composite/"+num+"/rainfall/R2/March/9","/composite/"+num+"/rainfall_anomalies/R2/March/9")

ACCESS_March = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/March/*.png",3,3,title=(r'ACCESS1.3 R2 March: mean rainfall'+sigma))
ACCESS_March_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/March/*.png",3,3,title=(r'ACCESS1.3 R2 March: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_March,"","composite/"+num+"_compiled/R2/ACCESS_March")
maps_sub.saveFig(ACCESS_March_Anom,"","composite/"+num+"_compiled/R2/ACCESS_March_Anom")


#ACCESS R2: April

output(access_trimmed.trim_April,indices_phase.IPO_posR2_Apr,indices_phase.ENSO_posR2_Apr,\
       "","/composite/"+num+"/rainfall/R2/April/1","/composite/"+num+"/rainfall_anomalies/R2/April/1")
output(access_trimmed.trim_April,indices_phase.IPO_posR2_Apr,indices_phase.ENSO_neutralR2_Apr,\
       "","/composite/"+num+"/rainfall/R2/April/2","/composite/"+num+"/rainfall_anomalies/R2/April/2")
output(access_trimmed.trim_April,indices_phase.IPO_posR2_Apr,indices_phase.ENSO_negR2_Apr,\
       "","/composite/"+num+"/rainfall/R2/April/3","/composite/"+num+"/rainfall_anomalies/R2/April/3")
output(access_trimmed.trim_April,indices_phase.IPO_neutralR2_Apr,indices_phase.ENSO_posR2_Apr,\
       "","/composite/"+num+"/rainfall/R2/April/4","/composite/"+num+"/rainfall_anomalies/R2/April/4")
output(access_trimmed.trim_April,indices_phase.IPO_neutralR2_Apr,indices_phase.ENSO_neutralR2_Apr,\
       "","/composite/"+num+"/rainfall/R2/April/5","/composite/"+num+"/rainfall_anomalies/R2/April/5")
output(access_trimmed.trim_April,indices_phase.IPO_neutralR2_Apr,indices_phase.ENSO_negR2_Apr,\
       "","/composite/"+num+"/rainfall/R2/April/6","/composite/"+num+"/rainfall_anomalies/R2/April/6")
output(access_trimmed.trim_April,indices_phase.IPO_negR2_Apr,indices_phase.ENSO_posR2_Apr,\
       "","/composite/"+num+"/rainfall/R2/April/7","/composite/"+num+"/rainfall_anomalies/R2/April/7")
output(access_trimmed.trim_April,indices_phase.IPO_negR2_Apr,indices_phase.ENSO_neutralR2_Apr,\
       "","/composite/"+num+"/rainfall/R2/April/8","/composite/"+num+"/rainfall_anomalies/R2/April/8")
output(access_trimmed.trim_April,indices_phase.IPO_negR2_Apr,indices_phase.ENSO_negR2_Apr,\
       "","/composite/"+num+"/rainfall/R2/April/9","/composite/"+num+"/rainfall_anomalies/R2/April/9")

ACCESS_April = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/April/*.png",3,3,title=(r'ACCESS1.3 R2 April: mean rainfall'+sigma))
ACCESS_April_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/April/*.png",3,3,title=(r'ACCESS1.3 R2 April: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_April,"","composite/"+num+"_compiled/R2/ACCESS_April")
maps_sub.saveFig(ACCESS_April_Anom,"","composite/"+num+"_compiled/R2/ACCESS_April_Anom")


#ACCESS R2: May

output(access_trimmed.trim_May,indices_phase.IPO_posR2_May,indices_phase.ENSO_posR2_May,\
       "","/composite/"+num+"/rainfall/R2/May/1","/composite/"+num+"/rainfall_anomalies/R2/May/1")
output(access_trimmed.trim_May,indices_phase.IPO_posR2_May,indices_phase.ENSO_neutralR2_May,\
       "","/composite/"+num+"/rainfall/R2/May/2","/composite/"+num+"/rainfall_anomalies/R2/May/2")
output(access_trimmed.trim_May,indices_phase.IPO_posR2_May,indices_phase.ENSO_negR2_May,\
       "","/composite/"+num+"/rainfall/R2/May/3","/composite/"+num+"/rainfall_anomalies/R2/May/3")
output(access_trimmed.trim_May,indices_phase.IPO_neutralR2_May,indices_phase.ENSO_posR2_May,\
       "","/composite/"+num+"/rainfall/R2/May/4","/composite/"+num+"/rainfall_anomalies/R2/May/4")
output(access_trimmed.trim_May,indices_phase.IPO_neutralR2_May,indices_phase.ENSO_neutralR2_May,\
       "","/composite/"+num+"/rainfall/R2/May/5","/composite/"+num+"/rainfall_anomalies/R2/May/5")
output(access_trimmed.trim_May,indices_phase.IPO_neutralR2_May,indices_phase.ENSO_negR2_May,\
       "","/composite/"+num+"/rainfall/R2/May/6","/composite/"+num+"/rainfall_anomalies/R2/May/6")
output(access_trimmed.trim_May,indices_phase.IPO_negR2_May,indices_phase.ENSO_posR2_May,\
       "","/composite/"+num+"/rainfall/R2/May/7","/composite/"+num+"/rainfall_anomalies/R2/May/7")
output(access_trimmed.trim_May,indices_phase.IPO_negR2_May,indices_phase.ENSO_neutralR2_May,\
       "","/composite/"+num+"/rainfall/R2/May/8","/composite/"+num+"/rainfall_anomalies/R2/May/8")
output(access_trimmed.trim_May,indices_phase.IPO_negR2_May,indices_phase.ENSO_negR2_May,\
       "","/composite/"+num+"/rainfall/R2/May/9","/composite/"+num+"/rainfall_anomalies/R2/May/9")

ACCESS_May = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/May/*.png",3,3,title=(r'ACCESS1.3 R2 May: mean rainfall'+sigma))
ACCESS_May_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/May/*.png",3,3,title=(r'ACCESS1.3 R2 May: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_May,"","composite/"+num+"_compiled/R2/ACCESS_May")
maps_sub.saveFig(ACCESS_May_Anom,"","composite/"+num+"_compiled/R2/ACCESS_May_Anom")

#ACCESS R2: JJA

output(access_trimmed.trim_JJA,indices_phase.IPO_posR2_JJA,indices_phase.ENSO_posR2_JJA,\
       "","/composite/"+num+"/rainfall/R2/JJA/1","/composite/"+num+"/rainfall_anomalies/R2/JJA/1")
output(access_trimmed.trim_JJA,indices_phase.IPO_posR2_JJA,indices_phase.ENSO_neutralR2_JJA,\
       "","/composite/"+num+"/rainfall/R2/JJA/2","/composite/"+num+"/rainfall_anomalies/R2/JJA/2")
output(access_trimmed.trim_JJA,indices_phase.IPO_posR2_JJA,indices_phase.ENSO_negR2_JJA,\
       "","/composite/"+num+"/rainfall/R2/JJA/3","/composite/"+num+"/rainfall_anomalies/R2/JJA/3")
output(access_trimmed.trim_JJA,indices_phase.IPO_neutralR2_JJA,indices_phase.ENSO_posR2_JJA,\
       "","/composite/"+num+"/rainfall/R2/JJA/4","/composite/"+num+"/rainfall_anomalies/R2/JJA/4")
output(access_trimmed.trim_JJA,indices_phase.IPO_neutralR2_JJA,indices_phase.ENSO_neutralR2_JJA,\
       "","/composite/"+num+"/rainfall/R2/JJA/5","/composite/"+num+"/rainfall_anomalies/R2/JJA/5")
output(access_trimmed.trim_JJA,indices_phase.IPO_neutralR2_JJA,indices_phase.ENSO_negR2_JJA,\
       "","/composite/"+num+"/rainfall/R2/JJA/6","/composite/"+num+"/rainfall_anomalies/R2/JJA/6")
output(access_trimmed.trim_JJA,indices_phase.IPO_negR2_JJA,indices_phase.ENSO_posR2_JJA,\
       "","/composite/"+num+"/rainfall/R2/JJA/7","/composite/"+num+"/rainfall_anomalies/R2/JJA/7")
output(access_trimmed.trim_JJA,indices_phase.IPO_negR2_JJA,indices_phase.ENSO_neutralR2_JJA,\
       "","/composite/"+num+"/rainfall/R2/JJA/8","/composite/"+num+"/rainfall_anomalies/R2/JJA/8")
output(access_trimmed.trim_JJA,indices_phase.IPO_negR2_JJA,indices_phase.ENSO_negR2_JJA,\
       "","/composite/"+num+"/rainfall/R2/JJA/9","/composite/"+num+"/rainfall_anomalies/R2/JJA/9")

ACCESS_JJA = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/JJA/*.png",3,3,title=(r'ACCESS1.3 R2 JJA: mean rainfall'+sigma))
ACCESS_JJA_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/JJA/*.png",3,3,title=(r'ACCESS1.3 R2 JJA: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_JJA,"","composite/"+num+"_compiled/R2/ACCESS_JJA")
maps_sub.saveFig(ACCESS_JJA_Anom,"","composite/"+num+"_compiled/R2/ACCESS_JJA_Anom")


#ACCESS R2: SON

output(access_trimmed.trim_SON,indices_phase.IPO_posR2_SON,indices_phase.ENSO_posR2_SON,\
       "","/composite/"+num+"/rainfall/R2/SON/1","/composite/"+num+"/rainfall_anomalies/R2/SON/1")
output(access_trimmed.trim_SON,indices_phase.IPO_posR2_SON,indices_phase.ENSO_neutralR2_SON,\
       "","/composite/"+num+"/rainfall/R2/SON/2","/composite/"+num+"/rainfall_anomalies/R2/SON/2")
output(access_trimmed.trim_SON,indices_phase.IPO_posR2_SON,indices_phase.ENSO_negR2_SON,\
       "","/composite/"+num+"/rainfall/R2/SON/3","/composite/"+num+"/rainfall_anomalies/R2/SON/3")
output(access_trimmed.trim_SON,indices_phase.IPO_neutralR2_SON,indices_phase.ENSO_posR2_SON,\
       "","/composite/"+num+"/rainfall/R2/SON/4","/composite/"+num+"/rainfall_anomalies/R2/SON/4")
output(access_trimmed.trim_SON,indices_phase.IPO_neutralR2_SON,indices_phase.ENSO_neutralR2_SON,\
       "","/composite/"+num+"/rainfall/R2/SON/5","/composite/"+num+"/rainfall_anomalies/R2/SON/5")
output(access_trimmed.trim_SON,indices_phase.IPO_neutralR2_SON,indices_phase.ENSO_negR2_SON,\
       "","/composite/"+num+"/rainfall/R2/SON/6","/composite/"+num+"/rainfall_anomalies/R2/SON/6")
output(access_trimmed.trim_SON,indices_phase.IPO_negR2_SON,indices_phase.ENSO_posR2_SON,\
       "","/composite/"+num+"/rainfall/R2/SON/7","/composite/"+num+"/rainfall_anomalies/R2/SON/7")
output(access_trimmed.trim_SON,indices_phase.IPO_negR2_SON,indices_phase.ENSO_neutralR2_SON,\
       "","/composite/"+num+"/rainfall/R2/SON/8","/composite/"+num+"/rainfall_anomalies/R2/SON/8")
output(access_trimmed.trim_SON,indices_phase.IPO_negR2_SON,indices_phase.ENSO_negR2_SON,\
       "","/composite/"+num+"/rainfall/R2/SON/9","/composite/"+num+"/rainfall_anomalies/R2/SON/9")

ACCESS_SON = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/SON/*.png",3,3,title=(r'ACCESS1.3 R2 SON: mean rainfall'+sigma))
ACCESS_SON_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/SON/*.png",3,3,title=(r'ACCESS1.3 R2 SON: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_SON,"","composite/"+num+"_compiled/R2/ACCESS_SON")
maps_sub.saveFig(ACCESS_SON_Anom,"","composite/"+num+"_compiled/R2/ACCESS_SON_Anom")


#ACCESS R2: DJF

output(access_trimmed.trim_DJF,indices_phase.IPO_posR2_DJF,indices_phase.ENSO_posR2_DJF,\
       "","/composite/"+num+"/rainfall/R2/DJF/1","/composite/"+num+"/rainfall_anomalies/R2/DJF/1")
output(access_trimmed.trim_DJF,indices_phase.IPO_posR2_DJF,indices_phase.ENSO_neutralR2_DJF,\
       "","/composite/"+num+"/rainfall/R2/DJF/2","/composite/"+num+"/rainfall_anomalies/R2/DJF/2")
output(access_trimmed.trim_DJF,indices_phase.IPO_posR2_DJF,indices_phase.ENSO_negR2_DJF,\
       "","/composite/"+num+"/rainfall/R2/DJF/3","/composite/"+num+"/rainfall_anomalies/R2/DJF/3")
output(access_trimmed.trim_DJF,indices_phase.IPO_neutralR2_DJF,indices_phase.ENSO_posR2_DJF,\
       "","/composite/"+num+"/rainfall/R2/DJF/4","/composite/"+num+"/rainfall_anomalies/R2/DJF/4")
output(access_trimmed.trim_DJF,indices_phase.IPO_neutralR2_DJF,indices_phase.ENSO_neutralR2_DJF,\
       "","/composite/"+num+"/rainfall/R2/DJF/5","/composite/"+num+"/rainfall_anomalies/R2/DJF/5")
output(access_trimmed.trim_DJF,indices_phase.IPO_neutralR2_DJF,indices_phase.ENSO_negR2_DJF,\
       "","/composite/"+num+"/rainfall/R2/DJF/6","/composite/"+num+"/rainfall_anomalies/R2/DJF/6")
output(access_trimmed.trim_DJF,indices_phase.IPO_negR2_DJF,indices_phase.ENSO_posR2_DJF,\
       "","/composite/"+num+"/rainfall/R2/DJF/7","/composite/"+num+"/rainfall_anomalies/R2/DJF/7")
output(access_trimmed.trim_DJF,indices_phase.IPO_negR2_DJF,indices_phase.ENSO_neutralR2_DJF,\
       "","/composite/"+num+"/rainfall/R2/DJF/8","/composite/"+num+"/rainfall_anomalies/R2/DJF/8")
output(access_trimmed.trim_DJF,indices_phase.IPO_negR2_DJF,indices_phase.ENSO_negR2_DJF,\
       "","/composite/"+num+"/rainfall/R2/DJF/9","/composite/"+num+"/rainfall_anomalies/R2/DJF/9")

ACCESS_DJF = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/DJF/*.png",3,3,title=(r'ACCESS1.3 R2 DJF: mean rainfall'+sigma))
ACCESS_DJF_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/DJF/*.png",3,3,title=(r'ACCESS1.3 R2 DJF: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_DJF,"","composite/"+num+"_compiled/R2/ACCESS_DJF")
maps_sub.saveFig(ACCESS_DJF_Anom,"","composite/"+num+"_compiled/R2/ACCESS_DJF_Anom")


#ACCESS R2: MAM

output(access_trimmed.trim_MAM,indices_phase.IPO_posR2_MAM,indices_phase.ENSO_posR2_MAM,\
       "","/composite/"+num+"/rainfall/R2/MAM/1","/composite/"+num+"/rainfall_anomalies/R2/MAM/1")
output(access_trimmed.trim_MAM,indices_phase.IPO_posR2_MAM,indices_phase.ENSO_neutralR2_MAM,\
       "","/composite/"+num+"/rainfall/R2/MAM/2","/composite/"+num+"/rainfall_anomalies/R2/MAM/2")
output(access_trimmed.trim_MAM,indices_phase.IPO_posR2_MAM,indices_phase.ENSO_negR2_MAM,\
       "","/composite/"+num+"/rainfall/R2/MAM/3","/composite/"+num+"/rainfall_anomalies/R2/MAM/3")
output(access_trimmed.trim_MAM,indices_phase.IPO_neutralR2_MAM,indices_phase.ENSO_posR2_MAM,\
       "","/composite/"+num+"/rainfall/R2/MAM/4","/composite/"+num+"/rainfall_anomalies/R2/MAM/4")
output(access_trimmed.trim_MAM,indices_phase.IPO_neutralR2_MAM,indices_phase.ENSO_neutralR2_MAM,\
       "","/composite/"+num+"/rainfall/R2/MAM/5","/composite/"+num+"/rainfall_anomalies/R2/MAM/5")
output(access_trimmed.trim_MAM,indices_phase.IPO_neutralR2_MAM,indices_phase.ENSO_negR2_MAM,\
       "","/composite/"+num+"/rainfall/R2/MAM/6","/composite/"+num+"/rainfall_anomalies/R2/MAM/6")
output(access_trimmed.trim_MAM,indices_phase.IPO_negR2_MAM,indices_phase.ENSO_posR2_MAM,\
       "","/composite/"+num+"/rainfall/R2/MAM/7","/composite/"+num+"/rainfall_anomalies/R2/MAM/7")
output(access_trimmed.trim_MAM,indices_phase.IPO_negR2_MAM,indices_phase.ENSO_neutralR2_MAM,\
       "","/composite/"+num+"/rainfall/R2/MAM/8","/composite/"+num+"/rainfall_anomalies/R2/MAM/8")
output(access_trimmed.trim_MAM,indices_phase.IPO_negR2_MAM,indices_phase.ENSO_negR2_MAM,\
       "","/composite/"+num+"/rainfall/R2/MAM/9","/composite/"+num+"/rainfall_anomalies/R2/MAM/9")

ACCESS_MAM = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/MAM/*.png",3,3,title=(r'ACCESS1.3 R2 MAM: mean rainfall'+sigma))
ACCESS_MAM_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/MAM/*.png",3,3,title=(r'ACCESS1.3 R2 MAM: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_MAM,"","composite/"+num+"_compiled/R2/ACCESS_MAM")
maps_sub.saveFig(ACCESS_MAM_Anom,"","composite/"+num+"_compiled/R2/ACCESS_MAM_Anom")


#ACCESS R2: annual

output(access_trimmed.trim_Annual,indices_phase.IPO_posR2_annual,indices_phase.ENSO_posR2_annual,\
       "","/composite/"+num+"/rainfall/R2/Annual/1","/composite/"+num+"/rainfall_anomalies/R2/Annual/1")
output(access_trimmed.trim_Annual,indices_phase.IPO_posR2_annual,indices_phase.ENSO_neutralR2_annual,\
       "","/composite/"+num+"/rainfall/R2/Annual/2","/composite/"+num+"/rainfall_anomalies/R2/Annual/2")
output(access_trimmed.trim_Annual,indices_phase.IPO_posR2_annual,indices_phase.ENSO_negR2_annual,\
       "","/composite/"+num+"/rainfall/R2/Annual/3","/composite/"+num+"/rainfall_anomalies/R2/Annual/3")
output(access_trimmed.trim_Annual,indices_phase.IPO_neutralR2_annual,indices_phase.ENSO_posR2_annual,\
       "","/composite/"+num+"/rainfall/R2/Annual/4","/composite/"+num+"/rainfall_anomalies/R2/Annual/4")
output(access_trimmed.trim_Annual,indices_phase.IPO_neutralR2_annual,indices_phase.ENSO_neutralR2_annual,\
       "","/composite/"+num+"/rainfall/R2/Annual/5","/composite/"+num+"/rainfall_anomalies/R2/Annual/5")
output(access_trimmed.trim_Annual,indices_phase.IPO_neutralR2_annual,indices_phase.ENSO_negR2_annual,\
       "","/composite/"+num+"/rainfall/R2/Annual/6","/composite/"+num+"/rainfall_anomalies/R2/Annual/6")
output(access_trimmed.trim_Annual,indices_phase.IPO_negR2_annual,indices_phase.ENSO_posR2_annual,\
       "","/composite/"+num+"/rainfall/R2/Annual/7","/composite/"+num+"/rainfall_anomalies/R2/Annual/7")
output(access_trimmed.trim_Annual,indices_phase.IPO_negR2_annual,indices_phase.ENSO_neutralR2_annual,\
       "","/composite/"+num+"/rainfall/R2/Annual/8","/composite/"+num+"/rainfall_anomalies/R2/Annual/8")
output(access_trimmed.trim_Annual,indices_phase.IPO_negR2_annual,indices_phase.ENSO_negR2_annual,\
       "","/composite/"+num+"/rainfall/R2/Annual/9","/composite/"+num+"/rainfall_anomalies/R2/Annual/9")

ACCESS_annual = multi("my_coding_routines/images/composite/"+num+"/rainfall/R2/Annual/*.png",3,3,title=(r'ACCESS1.3 R2 annual: mean rainfall'+sigma))
ACCESS_annual_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R2/Annual/*.png",3,3,title=(r'ACCESS1.3 R2 annual: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_annual,"","composite/"+num+"_compiled/R2/ACCESS_annual")
maps_sub.saveFig(ACCESS_annual_Anom,"","composite/"+num+"_compiled/R2/ACCESS_annual_Anom")
