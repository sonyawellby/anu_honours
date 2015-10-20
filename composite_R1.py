"""
Code which stratifies ENSO/IPO and ACCESS1.3 R1 rainfall data
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
sigma = ''# r' (2 $\sigma$)'  r' (3 $\sigma$)'sigma = '' # ' (2 $\sigma$)'  ' (3 $\sigma$)'

#ACCESS R1: June
"""
output(access_trimmed.trim_June,indices_phase.IPO_posR1_Jun,indices_phase.ENSO_posR1_Jun,\
       "","/composite/"+num+"/rainfall/R1/June/1","/composite/"+num+"/rainfall_anomalies/R1/June/1")
output(access_trimmed.trim_June,indices_phase.IPO_posR1_Jun,indices_phase.ENSO_neutralR1_Jun,\
       "","/composite/"+num+"/rainfall/R1/June/2","/composite/"+num+"/rainfall_anomalies/R1/June/2")
output(access_trimmed.trim_June,indices_phase.IPO_posR1_Jun,indices_phase.ENSO_negR1_Jun,\
       "","/composite/"+num+"/rainfall/R1/June/3","/composite/"+num+"/rainfall_anomalies/R1/June/3")
output(access_trimmed.trim_June,indices_phase.IPO_neutralR1_Jun,indices_phase.ENSO_posR1_Jun,\
       "","/composite/"+num+"/rainfall/R1/June/4","/composite/"+num+"/rainfall_anomalies/R1/June/4")
output(access_trimmed.trim_June,indices_phase.IPO_neutralR1_Jun,indices_phase.ENSO_neutralR1_Jun,\
       "","/composite/"+num+"/rainfall/R1/June/5","/composite/"+num+"/rainfall_anomalies/R1/June/5")
output(access_trimmed.trim_June,indices_phase.IPO_neutralR1_Jun,indices_phase.ENSO_negR1_Jun,\
       "","/composite/"+num+"/rainfall/R1/June/6","/composite/"+num+"/rainfall_anomalies/R1/June/6")
output(access_trimmed.trim_June,indices_phase.IPO_negR1_Jun,indices_phase.ENSO_posR1_Jun,\
       "","/composite/"+num+"/rainfall/R1/June/7","/composite/"+num+"/rainfall_anomalies/R1/June/7")
output(access_trimmed.trim_June,indices_phase.IPO_negR1_Jun,indices_phase.ENSO_neutralR1_Jun,\
       "","/composite/"+num+"/rainfall/R1/June/8","/composite/"+num+"/rainfall_anomalies/R1/June/8")
output(access_trimmed.trim_June,indices_phase.IPO_negR1_Jun,indices_phase.ENSO_negR1_Jun,\
       "","/composite/"+num+"/rainfall/R1/June/9","/composite/"+num+"/rainfall_anomalies/R1/June/9")

ACCESS_June = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/June/*.png",3,3,title=(r'ACCESS1.3 R1 June: mean rainfall'+sigma))
ACCESS_June_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/June/*.png",3,3,title=(r'ACCESS1.3 R1 June: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_June,"","composite/"+num+"_compiled/R1/ACCESS_June")
maps_sub.saveFig(ACCESS_June_Anom,"","composite/"+num+"_compiled/R1/ACCESS_June_Anom")


#ACCESS R1: July

output(access_trimmed.trim_July,indices_phase.IPO_posR1_Jul,indices_phase.ENSO_posR1_Jul,\
       "","/composite/"+num+"/rainfall/R1/July/1","/composite/"+num+"/rainfall_anomalies/R1/July/1")
output(access_trimmed.trim_July,indices_phase.IPO_posR1_Jul,indices_phase.ENSO_neutralR1_Jul,\
       "","/composite/"+num+"/rainfall/R1/July/2","/composite/"+num+"/rainfall_anomalies/R1/July/2")
output(access_trimmed.trim_July,indices_phase.IPO_posR1_Jul,indices_phase.ENSO_negR1_Jul,\
       "","/composite/"+num+"/rainfall/R1/July/3","/composite/"+num+"/rainfall_anomalies/R1/July/3")
output(access_trimmed.trim_July,indices_phase.IPO_neutralR1_Jul,indices_phase.ENSO_posR1_Jul,\
       "","/composite/"+num+"/rainfall/R1/July/4","/composite/"+num+"/rainfall_anomalies/R1/July/4")
output(access_trimmed.trim_July,indices_phase.IPO_neutralR1_Jul,indices_phase.ENSO_neutralR1_Jul,\
       "","/composite/"+num+"/rainfall/R1/July/5","/composite/"+num+"/rainfall_anomalies/R1/July/5")
output(access_trimmed.trim_July,indices_phase.IPO_neutralR1_Jul,indices_phase.ENSO_negR1_Jul,\
       "","/composite/"+num+"/rainfall/R1/July/6","/composite/"+num+"/rainfall_anomalies/R1/July/6")
output(access_trimmed.trim_July,indices_phase.IPO_negR1_Jul,indices_phase.ENSO_posR1_Jul,\
       "","/composite/"+num+"/rainfall/R1/July/7","/composite/"+num+"/rainfall_anomalies/R1/July/7")
output(access_trimmed.trim_July,indices_phase.IPO_negR1_Jul,indices_phase.ENSO_neutralR1_Jul,\
       "","/composite/"+num+"/rainfall/R1/July/8","/composite/"+num+"/rainfall_anomalies/R1/July/8")
output(access_trimmed.trim_July,indices_phase.IPO_negR1_Jul,indices_phase.ENSO_negR1_Jul,\
       "","/composite/"+num+"/rainfall/R1/July/9","/composite/"+num+"/rainfall_anomalies/R1/July/9")

ACCESS_July = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/July/*.png",3,3,title=(r'ACCESS1.3 R1 July: mean rainfall'+sigma))
ACCESS_July_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/July/*.png",3,3,title=(r'ACCESS1.3 R1 July: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_July,"","composite/"+num+"_compiled/R1/ACCESS_July")
maps_sub.saveFig(ACCESS_July_Anom,"","composite/"+num+"_compiled/R1/ACCESS_July_Anom")


#ACCESS R1: August

output(access_trimmed.trim_August,indices_phase.IPO_posR1_Aug,indices_phase.ENSO_posR1_Aug,\
       "","/composite/"+num+"/rainfall/R1/August/1","/composite/"+num+"/rainfall_anomalies/R1/August/1")
output(access_trimmed.trim_August,indices_phase.IPO_posR1_Aug,indices_phase.ENSO_neutralR1_Aug,\
       "","/composite/"+num+"/rainfall/R1/August/2","/composite/"+num+"/rainfall_anomalies/R1/August/2")
output(access_trimmed.trim_August,indices_phase.IPO_posR1_Aug,indices_phase.ENSO_negR1_Aug,\
       "","/composite/"+num+"/rainfall/R1/August/3","/composite/"+num+"/rainfall_anomalies/R1/August/3")
output(access_trimmed.trim_August,indices_phase.IPO_neutralR1_Aug,indices_phase.ENSO_posR1_Aug,\
       "","/composite/"+num+"/rainfall/R1/August/4","/composite/"+num+"/rainfall_anomalies/R1/August/4")
output(access_trimmed.trim_August,indices_phase.IPO_neutralR1_Aug,indices_phase.ENSO_neutralR1_Aug,\
       "","/composite/"+num+"/rainfall/R1/August/5","/composite/"+num+"/rainfall_anomalies/R1/August/5")
output(access_trimmed.trim_August,indices_phase.IPO_neutralR1_Aug,indices_phase.ENSO_negR1_Aug,\
       "","/composite/"+num+"/rainfall/R1/August/6","/composite/"+num+"/rainfall_anomalies/R1/August/6")
output(access_trimmed.trim_August,indices_phase.IPO_negR1_Aug,indices_phase.ENSO_posR1_Aug,\
       "","/composite/"+num+"/rainfall/R1/August/7","/composite/"+num+"/rainfall_anomalies/R1/August/7")
output(access_trimmed.trim_August,indices_phase.IPO_negR1_Aug,indices_phase.ENSO_neutralR1_Aug,\
       "","/composite/"+num+"/rainfall/R1/August/8","/composite/"+num+"/rainfall_anomalies/R1/August/8")
output(access_trimmed.trim_August,indices_phase.IPO_negR1_Aug,indices_phase.ENSO_negR1_Aug,\
       "","/composite/"+num+"/rainfall/R1/August/9","/composite/"+num+"/rainfall_anomalies/R1/August/9")

ACCESS_August = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/August/*.png",3,3,title=(r'ACCESS1.3 R1 August: mean rainfall'+sigma))
ACCESS_August_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/August/*.png",3,3,title=(r'ACCESS1.3 R1 August: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_August,"","composite/"+num+"_compiled/R1/ACCESS_August")
maps_sub.saveFig(ACCESS_August_Anom,"","composite/"+num+"_compiled/R1/ACCESS_August_Anom")


#ACCESS R1: September

output(access_trimmed.trim_September,indices_phase.IPO_posR1_Sep,indices_phase.ENSO_posR1_Sep,\
       "","/composite/"+num+"/rainfall/R1/September/1","/composite/"+num+"/rainfall_anomalies/R1/September/1")
output(access_trimmed.trim_September,indices_phase.IPO_posR1_Sep,indices_phase.ENSO_neutralR1_Sep,\
       "","/composite/"+num+"/rainfall/R1/September/2","/composite/"+num+"/rainfall_anomalies/R1/September/2")
output(access_trimmed.trim_September,indices_phase.IPO_posR1_Sep,indices_phase.ENSO_negR1_Sep,\
       "","/composite/"+num+"/rainfall/R1/September/3","/composite/"+num+"/rainfall_anomalies/R1/September/3")
output(access_trimmed.trim_September,indices_phase.IPO_neutralR1_Sep,indices_phase.ENSO_posR1_Sep,\
       "","/composite/"+num+"/rainfall/R1/September/4","/composite/"+num+"/rainfall_anomalies/R1/September/4")
output(access_trimmed.trim_September,indices_phase.IPO_neutralR1_Sep,indices_phase.ENSO_neutralR1_Sep,\
       "","/composite/"+num+"/rainfall/R1/September/5","/composite/"+num+"/rainfall_anomalies/R1/September/5")
output(access_trimmed.trim_September,indices_phase.IPO_neutralR1_Sep,indices_phase.ENSO_negR1_Sep,\
       "","/composite/"+num+"/rainfall/R1/September/6","/composite/"+num+"/rainfall_anomalies/R1/September/6")
output(access_trimmed.trim_September,indices_phase.IPO_negR1_Sep,indices_phase.ENSO_posR1_Sep,\
       "","/composite/"+num+"/rainfall/R1/September/7","/composite/"+num+"/rainfall_anomalies/R1/September/7")
output(access_trimmed.trim_September,indices_phase.IPO_negR1_Sep,indices_phase.ENSO_neutralR1_Sep,\
       "","/composite/"+num+"/rainfall/R1/September/8","/composite/"+num+"/rainfall_anomalies/R1/September/8")
output(access_trimmed.trim_September,indices_phase.IPO_negR1_Sep,indices_phase.ENSO_negR1_Sep,\
       "","/composite/"+num+"/rainfall/R1/September/9","/composite/"+num+"/rainfall_anomalies/R1/September/9")

ACCESS_September = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/September/*.png",3,3,title=(r'ACCESS1.3 R1 September: mean rainfall'+sigma))
ACCESS_September_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/September/*.png",3,3,title=(r'ACCESS1.3 R1 September: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_September,"","composite/"+num+"_compiled/R1/ACCESS_September")
maps_sub.saveFig(ACCESS_September_Anom,"","composite/"+num+"_compiled/R1/ACCESS_September_Anom")


#ACCESS R1: October

output(access_trimmed.trim_October,indices_phase.IPO_posR1_Oct,indices_phase.ENSO_posR1_Oct,\
       "","/composite/"+num+"/rainfall/R1/October/1","/composite/"+num+"/rainfall_anomalies/R1/October/1")
output(access_trimmed.trim_October,indices_phase.IPO_posR1_Oct,indices_phase.ENSO_neutralR1_Oct,\
       "","/composite/"+num+"/rainfall/R1/October/2","/composite/"+num+"/rainfall_anomalies/R1/October/2")
output(access_trimmed.trim_October,indices_phase.IPO_posR1_Oct,indices_phase.ENSO_negR1_Oct,\
       "","/composite/"+num+"/rainfall/R1/October/3","/composite/"+num+"/rainfall_anomalies/R1/October/3")
output(access_trimmed.trim_October,indices_phase.IPO_neutralR1_Oct,indices_phase.ENSO_posR1_Oct,\
       "","/composite/"+num+"/rainfall/R1/October/4","/composite/"+num+"/rainfall_anomalies/R1/October/4")
output(access_trimmed.trim_October,indices_phase.IPO_neutralR1_Oct,indices_phase.ENSO_neutralR1_Oct,\
       "","/composite/"+num+"/rainfall/R1/October/5","/composite/"+num+"/rainfall_anomalies/R1/October/5")
output(access_trimmed.trim_October,indices_phase.IPO_neutralR1_Oct,indices_phase.ENSO_negR1_Oct,\
       "","/composite/"+num+"/rainfall/R1/October/6","/composite/"+num+"/rainfall_anomalies/R1/October/6")
output(access_trimmed.trim_October,indices_phase.IPO_negR1_Oct,indices_phase.ENSO_posR1_Oct,\
       "","/composite/"+num+"/rainfall/R1/October/7","/composite/"+num+"/rainfall_anomalies/R1/October/7")
output(access_trimmed.trim_October,indices_phase.IPO_negR1_Oct,indices_phase.ENSO_neutralR1_Oct,\
       "","/composite/"+num+"/rainfall/R1/October/8","/composite/"+num+"/rainfall_anomalies/R1/October/8")
output(access_trimmed.trim_October,indices_phase.IPO_negR1_Oct,indices_phase.ENSO_negR1_Oct,\
       "","/composite/"+num+"/rainfall/R1/October/9","/composite/"+num+"/rainfall_anomalies/R1/October/9")

ACCESS_October = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/October/*.png",3,3,title=(r'ACCESS1.3 R1 October: mean rainfall'+sigma))
ACCESS_October_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/October/*.png",3,3,title=(r'ACCESS1.3 R1 October: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_October,"","composite/"+num+"_compiled/R1/ACCESS_October")
maps_sub.saveFig(ACCESS_October_Anom,"","composite/"+num+"_compiled/R1/ACCESS_October_Anom")


#ACCESS R1: November

output(access_trimmed.trim_November,indices_phase.IPO_posR1_Nov,indices_phase.ENSO_posR1_Nov,\
       "","/composite/"+num+"/rainfall/R1/November/1","/composite/"+num+"/rainfall_anomalies/R1/November/1")
output(access_trimmed.trim_November,indices_phase.IPO_posR1_Nov,indices_phase.ENSO_neutralR1_Nov,\
       "","/composite/"+num+"/rainfall/R1/November/2","/composite/"+num+"/rainfall_anomalies/R1/November/2")
output(access_trimmed.trim_November,indices_phase.IPO_posR1_Nov,indices_phase.ENSO_negR1_Nov,\
       "","/composite/"+num+"/rainfall/R1/November/3","/composite/"+num+"/rainfall_anomalies/R1/November/3")
output(access_trimmed.trim_November,indices_phase.IPO_neutralR1_Nov,indices_phase.ENSO_posR1_Nov,\
       "","/composite/"+num+"/rainfall/R1/November/4","/composite/"+num+"/rainfall_anomalies/R1/November/4")
output(access_trimmed.trim_November,indices_phase.IPO_neutralR1_Nov,indices_phase.ENSO_neutralR1_Nov,\
       "","/composite/"+num+"/rainfall/R1/November/5","/composite/"+num+"/rainfall_anomalies/R1/November/5")
output(access_trimmed.trim_November,indices_phase.IPO_neutralR1_Nov,indices_phase.ENSO_negR1_Nov,\
       "","/composite/"+num+"/rainfall/R1/November/6","/composite/"+num+"/rainfall_anomalies/R1/November/6")
output(access_trimmed.trim_November,indices_phase.IPO_negR1_Nov,indices_phase.ENSO_posR1_Nov,\
       "","/composite/"+num+"/rainfall/R1/November/7","/composite/"+num+"/rainfall_anomalies/R1/November/7")
output(access_trimmed.trim_November,indices_phase.IPO_negR1_Nov,indices_phase.ENSO_neutralR1_Nov,\
       "","/composite/"+num+"/rainfall/R1/November/8","/composite/"+num+"/rainfall_anomalies/R1/November/8")
output(access_trimmed.trim_November,indices_phase.IPO_negR1_Nov,indices_phase.ENSO_negR1_Nov,\
       "","/composite/"+num+"/rainfall/R1/November/9","/composite/"+num+"/rainfall_anomalies/R1/November/9")

ACCESS_November = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/November/*.png",3,3,title=(r'ACCESS1.3 R1 November: mean rainfall'+sigma))
ACCESS_November_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/November/*.png",3,3,title=(r'ACCESS1.3 R1 November: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_November,"","composite/"+num+"_compiled/R1/ACCESS_November")
maps_sub.saveFig(ACCESS_November_Anom,"","composite/"+num+"_compiled/R1/ACCESS_November_Anom")


#ACCESS R1: December

output(access_trimmed.trim_December,indices_phase.IPO_posR1_Dec,indices_phase.ENSO_posR1_Dec,\
       "","/composite/"+num+"/rainfall/R1/December/1","/composite/"+num+"/rainfall_anomalies/R1/December/1")
output(access_trimmed.trim_December,indices_phase.IPO_posR1_Dec,indices_phase.ENSO_neutralR1_Dec,\
       "","/composite/"+num+"/rainfall/R1/December/2","/composite/"+num+"/rainfall_anomalies/R1/December/2")
output(access_trimmed.trim_December,indices_phase.IPO_posR1_Dec,indices_phase.ENSO_negR1_Dec,\
       "","/composite/"+num+"/rainfall/R1/December/3","/composite/"+num+"/rainfall_anomalies/R1/December/3")
output(access_trimmed.trim_December,indices_phase.IPO_neutralR1_Dec,indices_phase.ENSO_posR1_Dec,\
       "","/composite/"+num+"/rainfall/R1/December/4","/composite/"+num+"/rainfall_anomalies/R1/December/4")
output(access_trimmed.trim_December,indices_phase.IPO_neutralR1_Dec,indices_phase.ENSO_neutralR1_Dec,\
       "","/composite/"+num+"/rainfall/R1/December/5","/composite/"+num+"/rainfall_anomalies/R1/December/5")
output(access_trimmed.trim_December,indices_phase.IPO_neutralR1_Dec,indices_phase.ENSO_negR1_Dec,\
       "","/composite/"+num+"/rainfall/R1/December/6","/composite/"+num+"/rainfall_anomalies/R1/December/6")
output(access_trimmed.trim_December,indices_phase.IPO_negR1_Dec,indices_phase.ENSO_posR1_Dec,\
       "","/composite/"+num+"/rainfall/R1/December/7","/composite/"+num+"/rainfall_anomalies/R1/December/7")
output(access_trimmed.trim_December,indices_phase.IPO_negR1_Dec,indices_phase.ENSO_neutralR1_Dec,\
       "","/composite/"+num+"/rainfall/R1/December/8","/composite/"+num+"/rainfall_anomalies/R1/December/8")
output(access_trimmed.trim_December,indices_phase.IPO_negR1_Dec,indices_phase.ENSO_negR1_Dec,\
       "","/composite/"+num+"/rainfall/R1/December/9","/composite/"+num+"/rainfall_anomalies/R1/December/9")

ACCESS_December = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/December/*.png",3,3,title=(r'ACCESS1.3 R1 December: mean rainfall'+sigma))
ACCESS_December_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/December/*.png",3,3,title=(r'ACCESS1.3 R1 December: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_December,"","composite/"+num+"_compiled/R1/ACCESS_December")
maps_sub.saveFig(ACCESS_December_Anom,"","composite/"+num+"_compiled/R1/ACCESS_December_Anom")


#ACCESS R1: January

output(access_trimmed.trim_January,indices_phase.IPO_posR1_Jan,indices_phase.ENSO_posR1_Jan,\
       "","/composite/"+num+"/rainfall/R1/January/1","/composite/"+num+"/rainfall_anomalies/R1/January/1")
output(access_trimmed.trim_January,indices_phase.IPO_posR1_Jan,indices_phase.ENSO_neutralR1_Jan,\
       "","/composite/"+num+"/rainfall/R1/January/2","/composite/"+num+"/rainfall_anomalies/R1/January/2")
output(access_trimmed.trim_January,indices_phase.IPO_posR1_Jan,indices_phase.ENSO_negR1_Jan,\
       "","/composite/"+num+"/rainfall/R1/January/3","/composite/"+num+"/rainfall_anomalies/R1/January/3")
output(access_trimmed.trim_January,indices_phase.IPO_neutralR1_Jan,indices_phase.ENSO_posR1_Jan,\
       "","/composite/"+num+"/rainfall/R1/January/4","/composite/"+num+"/rainfall_anomalies/R1/January/4")
output(access_trimmed.trim_January,indices_phase.IPO_neutralR1_Jan,indices_phase.ENSO_neutralR1_Jan,\
       "","/composite/"+num+"/rainfall/R1/January/5","/composite/"+num+"/rainfall_anomalies/R1/January/5")
output(access_trimmed.trim_January,indices_phase.IPO_neutralR1_Jan,indices_phase.ENSO_negR1_Jan,\
       "","/composite/"+num+"/rainfall/R1/January/6","/composite/"+num+"/rainfall_anomalies/R1/January/6")
output(access_trimmed.trim_January,indices_phase.IPO_negR1_Jan,indices_phase.ENSO_posR1_Jan,\
       "","/composite/"+num+"/rainfall/R1/January/7","/composite/"+num+"/rainfall_anomalies/R1/January/7")
output(access_trimmed.trim_January,indices_phase.IPO_negR1_Jan,indices_phase.ENSO_neutralR1_Jan,\
       "","/composite/"+num+"/rainfall/R1/January/8","/composite/"+num+"/rainfall_anomalies/R1/January/8")
output(access_trimmed.trim_January,indices_phase.IPO_negR1_Jan,indices_phase.ENSO_negR1_Jan,\
       "","/composite/"+num+"/rainfall/R1/January/9","/composite/"+num+"/rainfall_anomalies/R1/January/9")

ACCESS_January = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/January/*.png",3,3,title=(r'ACCESS1.3 R1 January: mean rainfall'+sigma))
ACCESS_January_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/January/*.png",3,3,title=(r'ACCESS1.3 R1 January: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_January,"","composite/"+num+"_compiled/R1/ACCESS_January")
maps_sub.saveFig(ACCESS_January_Anom,"","composite/"+num+"_compiled/R1/ACCESS_January_Anom")


#ACCESS R1: February

output(access_trimmed.trim_February,indices_phase.IPO_posR1_Feb,indices_phase.ENSO_posR1_Feb,\
       "","/composite/"+num+"/rainfall/R1/February/1","/composite/"+num+"/rainfall_anomalies/R1/February/1")
output(access_trimmed.trim_February,indices_phase.IPO_posR1_Feb,indices_phase.ENSO_neutralR1_Feb,\
       "","/composite/"+num+"/rainfall/R1/February/2","/composite/"+num+"/rainfall_anomalies/R1/February/2")
output(access_trimmed.trim_February,indices_phase.IPO_posR1_Feb,indices_phase.ENSO_negR1_Feb,\
       "","/composite/"+num+"/rainfall/R1/February/3","/composite/"+num+"/rainfall_anomalies/R1/February/3")
output(access_trimmed.trim_February,indices_phase.IPO_neutralR1_Feb,indices_phase.ENSO_posR1_Feb,\
       "","/composite/"+num+"/rainfall/R1/February/4","/composite/"+num+"/rainfall_anomalies/R1/February/4")
output(access_trimmed.trim_February,indices_phase.IPO_neutralR1_Feb,indices_phase.ENSO_neutralR1_Feb,\
       "","/composite/"+num+"/rainfall/R1/February/5","/composite/"+num+"/rainfall_anomalies/R1/February/5")
output(access_trimmed.trim_February,indices_phase.IPO_neutralR1_Feb,indices_phase.ENSO_negR1_Feb,\
       "","/composite/"+num+"/rainfall/R1/February/6","/composite/"+num+"/rainfall_anomalies/R1/February/6")
output(access_trimmed.trim_February,indices_phase.IPO_negR1_Feb,indices_phase.ENSO_posR1_Feb,\
       "","/composite/"+num+"/rainfall/R1/February/7","/composite/"+num+"/rainfall_anomalies/R1/February/7")
output(access_trimmed.trim_February,indices_phase.IPO_negR1_Feb,indices_phase.ENSO_neutralR1_Feb,\
       "","/composite/"+num+"/rainfall/R1/February/8","/composite/"+num+"/rainfall_anomalies/R1/February/8")
output(access_trimmed.trim_February,indices_phase.IPO_negR1_Feb,indices_phase.ENSO_negR1_Feb,\
       "","/composite/"+num+"/rainfall/R1/February/9","/composite/"+num+"/rainfall_anomalies/R1/February/9")

ACCESS_February = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/February/*.png",3,3,title=(r'ACCESS1.3 R1 February: mean rainfall'+sigma))
ACCESS_February_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/February/*.png",3,3,title=(r'ACCESS1.3 R1 February: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_February,"","composite/"+num+"_compiled/R1/ACCESS_February")
maps_sub.saveFig(ACCESS_February_Anom,"","composite/"+num+"_compiled/R1/ACCESS_February_Anom")


#ACCESS R1: March

output(access_trimmed.trim_March,indices_phase.IPO_posR1_Mar,indices_phase.ENSO_posR1_Mar,\
       "","/composite/"+num+"/rainfall/R1/March/1","/composite/"+num+"/rainfall_anomalies/R1/March/1")
output(access_trimmed.trim_March,indices_phase.IPO_posR1_Mar,indices_phase.ENSO_neutralR1_Mar,\
       "","/composite/"+num+"/rainfall/R1/March/2","/composite/"+num+"/rainfall_anomalies/R1/March/2")
output(access_trimmed.trim_March,indices_phase.IPO_posR1_Mar,indices_phase.ENSO_negR1_Mar,\
       "","/composite/"+num+"/rainfall/R1/March/3","/composite/"+num+"/rainfall_anomalies/R1/March/3")
output(access_trimmed.trim_March,indices_phase.IPO_neutralR1_Mar,indices_phase.ENSO_posR1_Mar,\
       "","/composite/"+num+"/rainfall/R1/March/4","/composite/"+num+"/rainfall_anomalies/R1/March/4")
output(access_trimmed.trim_March,indices_phase.IPO_neutralR1_Mar,indices_phase.ENSO_neutralR1_Mar,\
       "","/composite/"+num+"/rainfall/R1/March/5","/composite/"+num+"/rainfall_anomalies/R1/March/5")
output(access_trimmed.trim_March,indices_phase.IPO_neutralR1_Mar,indices_phase.ENSO_negR1_Mar,\
       "","/composite/"+num+"/rainfall/R1/March/6","/composite/"+num+"/rainfall_anomalies/R1/March/6")
output(access_trimmed.trim_March,indices_phase.IPO_negR1_Mar,indices_phase.ENSO_posR1_Mar,\
       "","/composite/"+num+"/rainfall/R1/March/7","/composite/"+num+"/rainfall_anomalies/R1/March/7")
output(access_trimmed.trim_March,indices_phase.IPO_negR1_Mar,indices_phase.ENSO_neutralR1_Mar,\
       "","/composite/"+num+"/rainfall/R1/March/8","/composite/"+num+"/rainfall_anomalies/R1/March/8")
output(access_trimmed.trim_March,indices_phase.IPO_negR1_Mar,indices_phase.ENSO_negR1_Mar,\
       "","/composite/"+num+"/rainfall/R1/March/9","/composite/"+num+"/rainfall_anomalies/R1/March/9")

ACCESS_March = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/March/*.png",3,3,title=(r'ACCESS1.3 R1 March: mean rainfall'+sigma))
ACCESS_March_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/March/*.png",3,3,title=(r'ACCESS1.3 R1 March: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_March,"","composite/"+num+"_compiled/R1/ACCESS_March")
maps_sub.saveFig(ACCESS_March_Anom,"","composite/"+num+"_compiled/R1/ACCESS_March_Anom")


"""
#ACCESS R1: April

output(access_trimmed.trim_April,indices_phase.IPO_posR1_Apr,indices_phase.ENSO_posR1_Apr,\
       "","/composite/"+num+"/rainfall/R1/April/1","/composite/"+num+"/rainfall_anomalies/R1/April/1")
output(access_trimmed.trim_April,indices_phase.IPO_posR1_Apr,indices_phase.ENSO_neutralR1_Apr,\
       "","/composite/"+num+"/rainfall/R1/April/2","/composite/"+num+"/rainfall_anomalies/R1/April/2")
output(access_trimmed.trim_April,indices_phase.IPO_posR1_Apr,indices_phase.ENSO_negR1_Apr,\
       "","/composite/"+num+"/rainfall/R1/April/3","/composite/"+num+"/rainfall_anomalies/R1/April/3")
output(access_trimmed.trim_April,indices_phase.IPO_neutralR1_Apr,indices_phase.ENSO_posR1_Apr,\
       "","/composite/"+num+"/rainfall/R1/April/4","/composite/"+num+"/rainfall_anomalies/R1/April/4")
output(access_trimmed.trim_April,indices_phase.IPO_neutralR1_Apr,indices_phase.ENSO_neutralR1_Apr,\
       "","/composite/"+num+"/rainfall/R1/April/5","/composite/"+num+"/rainfall_anomalies/R1/April/5")
output(access_trimmed.trim_April,indices_phase.IPO_neutralR1_Apr,indices_phase.ENSO_negR1_Apr,\
       "","/composite/"+num+"/rainfall/R1/April/6","/composite/"+num+"/rainfall_anomalies/R1/April/6")
output(access_trimmed.trim_April,indices_phase.IPO_negR1_Apr,indices_phase.ENSO_posR1_Apr,\
       "","/composite/"+num+"/rainfall/R1/April/7","/composite/"+num+"/rainfall_anomalies/R1/April/7")
output(access_trimmed.trim_April,indices_phase.IPO_negR1_Apr,indices_phase.ENSO_neutralR1_Apr,\
       "","/composite/"+num+"/rainfall/R1/April/8","/composite/"+num+"/rainfall_anomalies/R1/April/8")
output(access_trimmed.trim_April,indices_phase.IPO_negR1_Apr,indices_phase.ENSO_negR1_Apr,\
       "","/composite/"+num+"/rainfall/R1/April/9","/composite/"+num+"/rainfall_anomalies/R1/April/9")

ACCESS_April = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/April/*.png",3,3,title=(r'ACCESS1.3 R1 April: mean rainfall'+sigma))
ACCESS_April_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/April/*.png",3,3,title=(r'ACCESS1.3 R1 April: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_April,"","composite/"+num+"_compiled/R1/ACCESS_April")
maps_sub.saveFig(ACCESS_April_Anom,"","composite/"+num+"_compiled/R1/ACCESS_April_Anom")


#ACCESS R1: May

output(access_trimmed.trim_May,indices_phase.IPO_posR1_May,indices_phase.ENSO_posR1_May,\
       "","/composite/"+num+"/rainfall/R1/May/1","/composite/"+num+"/rainfall_anomalies/R1/May/1")
output(access_trimmed.trim_May,indices_phase.IPO_posR1_May,indices_phase.ENSO_neutralR1_May,\
       "","/composite/"+num+"/rainfall/R1/May/2","/composite/"+num+"/rainfall_anomalies/R1/May/2")
output(access_trimmed.trim_May,indices_phase.IPO_posR1_May,indices_phase.ENSO_negR1_May,\
       "","/composite/"+num+"/rainfall/R1/May/3","/composite/"+num+"/rainfall_anomalies/R1/May/3")
output(access_trimmed.trim_May,indices_phase.IPO_neutralR1_May,indices_phase.ENSO_posR1_May,\
       "","/composite/"+num+"/rainfall/R1/May/4","/composite/"+num+"/rainfall_anomalies/R1/May/4")
output(access_trimmed.trim_May,indices_phase.IPO_neutralR1_May,indices_phase.ENSO_neutralR1_May,\
       "","/composite/"+num+"/rainfall/R1/May/5","/composite/"+num+"/rainfall_anomalies/R1/May/5")
output(access_trimmed.trim_May,indices_phase.IPO_neutralR1_May,indices_phase.ENSO_negR1_May,\
       "","/composite/"+num+"/rainfall/R1/May/6","/composite/"+num+"/rainfall_anomalies/R1/May/6")
output(access_trimmed.trim_May,indices_phase.IPO_negR1_May,indices_phase.ENSO_posR1_May,\
       "","/composite/"+num+"/rainfall/R1/May/7","/composite/"+num+"/rainfall_anomalies/R1/May/7")
output(access_trimmed.trim_May,indices_phase.IPO_negR1_May,indices_phase.ENSO_neutralR1_May,\
       "","/composite/"+num+"/rainfall/R1/May/8","/composite/"+num+"/rainfall_anomalies/R1/May/8")
output(access_trimmed.trim_May,indices_phase.IPO_negR1_May,indices_phase.ENSO_negR1_May,\
       "","/composite/"+num+"/rainfall/R1/May/9","/composite/"+num+"/rainfall_anomalies/R1/May/9")

ACCESS_May = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/May/*.png",3,3,title=(r'ACCESS1.3 R1 May: mean rainfall'+sigma))
ACCESS_May_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/May/*.png",3,3,title=(r'ACCESS1.3 R1 May: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_May,"","composite/"+num+"_compiled/R1/ACCESS_May")
maps_sub.saveFig(ACCESS_May_Anom,"","composite/"+num+"_compiled/R1/ACCESS_May_Anom")


#ACCESS R1: JJA

output(access_trimmed.trim_JJA,indices_phase.IPO_posR1_JJA,indices_phase.ENSO_posR1_JJA,\
       "","/composite/"+num+"/rainfall/R1/JJA/1","/composite/"+num+"/rainfall_anomalies/R1/JJA/1")
output(access_trimmed.trim_JJA,indices_phase.IPO_posR1_JJA,indices_phase.ENSO_neutralR1_JJA,\
       "","/composite/"+num+"/rainfall/R1/JJA/2","/composite/"+num+"/rainfall_anomalies/R1/JJA/2")
output(access_trimmed.trim_JJA,indices_phase.IPO_posR1_JJA,indices_phase.ENSO_negR1_JJA,\
       "","/composite/"+num+"/rainfall/R1/JJA/3","/composite/"+num+"/rainfall_anomalies/R1/JJA/3")
output(access_trimmed.trim_JJA,indices_phase.IPO_neutralR1_JJA,indices_phase.ENSO_posR1_JJA,\
       "","/composite/"+num+"/rainfall/R1/JJA/4","/composite/"+num+"/rainfall_anomalies/R1/JJA/4")
output(access_trimmed.trim_JJA,indices_phase.IPO_neutralR1_JJA,indices_phase.ENSO_neutralR1_JJA,\
       "","/composite/"+num+"/rainfall/R1/JJA/5","/composite/"+num+"/rainfall_anomalies/R1/JJA/5")
output(access_trimmed.trim_JJA,indices_phase.IPO_neutralR1_JJA,indices_phase.ENSO_negR1_JJA,\
       "","/composite/"+num+"/rainfall/R1/JJA/6","/composite/"+num+"/rainfall_anomalies/R1/JJA/6")
output(access_trimmed.trim_JJA,indices_phase.IPO_negR1_JJA,indices_phase.ENSO_posR1_JJA,\
       "","/composite/"+num+"/rainfall/R1/JJA/7","/composite/"+num+"/rainfall_anomalies/R1/JJA/7")
output(access_trimmed.trim_JJA,indices_phase.IPO_negR1_JJA,indices_phase.ENSO_neutralR1_JJA,\
       "","/composite/"+num+"/rainfall/R1/JJA/8","/composite/"+num+"/rainfall_anomalies/R1/JJA/8")
output(access_trimmed.trim_JJA,indices_phase.IPO_negR1_JJA,indices_phase.ENSO_negR1_JJA,\
       "","/composite/"+num+"/rainfall/R1/JJA/9","/composite/"+num+"/rainfall_anomalies/R1/JJA/9")

ACCESS_JJA = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/JJA/*.png",3,3,title=(r'ACCESS1.3 R1 JJA: mean rainfall'+sigma))
ACCESS_JJA_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/JJA/*.png",3,3,title=(r'ACCESS1.3 R1 JJA: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_JJA,"","composite/"+num+"_compiled/R1/ACCESS_JJA")
maps_sub.saveFig(ACCESS_JJA_Anom,"","composite/"+num+"_compiled/R1/ACCESS_JJA_Anom")


#ACCESS R1: SON

output(access_trimmed.trim_SON,indices_phase.IPO_posR1_SON,indices_phase.ENSO_posR1_SON,\
       "","/composite/"+num+"/rainfall/R1/SON/1","/composite/"+num+"/rainfall_anomalies/R1/SON/1")
output(access_trimmed.trim_SON,indices_phase.IPO_posR1_SON,indices_phase.ENSO_neutralR1_SON,\
       "","/composite/"+num+"/rainfall/R1/SON/2","/composite/"+num+"/rainfall_anomalies/R1/SON/2")
output(access_trimmed.trim_SON,indices_phase.IPO_posR1_SON,indices_phase.ENSO_negR1_SON,\
       "","/composite/"+num+"/rainfall/R1/SON/3","/composite/"+num+"/rainfall_anomalies/R1/SON/3")
output(access_trimmed.trim_SON,indices_phase.IPO_neutralR1_SON,indices_phase.ENSO_posR1_SON,\
       "","/composite/"+num+"/rainfall/R1/SON/4","/composite/"+num+"/rainfall_anomalies/R1/SON/4")
output(access_trimmed.trim_SON,indices_phase.IPO_neutralR1_SON,indices_phase.ENSO_neutralR1_SON,\
       "","/composite/"+num+"/rainfall/R1/SON/5","/composite/"+num+"/rainfall_anomalies/R1/SON/5")
output(access_trimmed.trim_SON,indices_phase.IPO_neutralR1_SON,indices_phase.ENSO_negR1_SON,\
       "","/composite/"+num+"/rainfall/R1/SON/6","/composite/"+num+"/rainfall_anomalies/R1/SON/6")
output(access_trimmed.trim_SON,indices_phase.IPO_negR1_SON,indices_phase.ENSO_posR1_SON,\
       "","/composite/"+num+"/rainfall/R1/SON/7","/composite/"+num+"/rainfall_anomalies/R1/SON/7")
output(access_trimmed.trim_SON,indices_phase.IPO_negR1_SON,indices_phase.ENSO_neutralR1_SON,\
       "","/composite/"+num+"/rainfall/R1/SON/8","/composite/"+num+"/rainfall_anomalies/R1/SON/8")
output(access_trimmed.trim_SON,indices_phase.IPO_negR1_SON,indices_phase.ENSO_negR1_SON,\
       "","/composite/"+num+"/rainfall/R1/SON/9","/composite/"+num+"/rainfall_anomalies/R1/SON/9")

ACCESS_SON = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/SON/*.png",3,3,title=(r'ACCESS1.3 R1 SON: mean rainfall'+sigma))
ACCESS_SON_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/SON/*.png",3,3,title=(r'ACCESS1.3 R1 SON: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_SON,"","composite/"+num+"_compiled/R1/ACCESS_SON")
maps_sub.saveFig(ACCESS_SON_Anom,"","composite/"+num+"_compiled/R1/ACCESS_SON_Anom")


#ACCESS R1: DJF

output(access_trimmed.trim_DJF,indices_phase.IPO_posR1_DJF,indices_phase.ENSO_posR1_DJF,\
       "","/composite/"+num+"/rainfall/R1/DJF/1","/composite/"+num+"/rainfall_anomalies/R1/DJF/1")
output(access_trimmed.trim_DJF,indices_phase.IPO_posR1_DJF,indices_phase.ENSO_neutralR1_DJF,\
       "","/composite/"+num+"/rainfall/R1/DJF/2","/composite/"+num+"/rainfall_anomalies/R1/DJF/2")
output(access_trimmed.trim_DJF,indices_phase.IPO_posR1_DJF,indices_phase.ENSO_negR1_DJF,\
       "","/composite/"+num+"/rainfall/R1/DJF/3","/composite/"+num+"/rainfall_anomalies/R1/DJF/3")
output(access_trimmed.trim_DJF,indices_phase.IPO_neutralR1_DJF,indices_phase.ENSO_posR1_DJF,\
       "","/composite/"+num+"/rainfall/R1/DJF/4","/composite/"+num+"/rainfall_anomalies/R1/DJF/4")
output(access_trimmed.trim_DJF,indices_phase.IPO_neutralR1_DJF,indices_phase.ENSO_neutralR1_DJF,\
       "","/composite/"+num+"/rainfall/R1/DJF/5","/composite/"+num+"/rainfall_anomalies/R1/DJF/5")
output(access_trimmed.trim_DJF,indices_phase.IPO_neutralR1_DJF,indices_phase.ENSO_negR1_DJF,\
       "","/composite/"+num+"/rainfall/R1/DJF/6","/composite/"+num+"/rainfall_anomalies/R1/DJF/6")
output(access_trimmed.trim_DJF,indices_phase.IPO_negR1_DJF,indices_phase.ENSO_posR1_DJF,\
       "","/composite/"+num+"/rainfall/R1/DJF/7","/composite/"+num+"/rainfall_anomalies/R1/DJF/7")
output(access_trimmed.trim_DJF,indices_phase.IPO_negR1_DJF,indices_phase.ENSO_neutralR1_DJF,\
       "","/composite/"+num+"/rainfall/R1/DJF/8","/composite/"+num+"/rainfall_anomalies/R1/DJF/8")
output(access_trimmed.trim_DJF,indices_phase.IPO_negR1_DJF,indices_phase.ENSO_negR1_DJF,\
       "","/composite/"+num+"/rainfall/R1/DJF/9","/composite/"+num+"/rainfall_anomalies/R1/DJF/9")

ACCESS_DJF = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/DJF/*.png",3,3,title=(r'ACCESS1.3 R1 DJF: mean rainfall'+sigma))
ACCESS_DJF_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/DJF/*.png",3,3,title=(r'ACCESS1.3 R1 DJF: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_DJF,"","composite/"+num+"_compiled/R1/ACCESS_DJF")
maps_sub.saveFig(ACCESS_DJF_Anom,"","composite/"+num+"_compiled/R1/ACCESS_DJF_Anom")


#ACCESS R1: MAM

output(access_trimmed.trim_MAM,indices_phase.IPO_posR1_MAM,indices_phase.ENSO_posR1_MAM,\
       "","/composite/"+num+"/rainfall/R1/MAM/1","/composite/"+num+"/rainfall_anomalies/R1/MAM/1")
output(access_trimmed.trim_MAM,indices_phase.IPO_posR1_MAM,indices_phase.ENSO_neutralR1_MAM,\
       "","/composite/"+num+"/rainfall/R1/MAM/2","/composite/"+num+"/rainfall_anomalies/R1/MAM/2")
output(access_trimmed.trim_MAM,indices_phase.IPO_posR1_MAM,indices_phase.ENSO_negR1_MAM,\
       "","/composite/"+num+"/rainfall/R1/MAM/3","/composite/"+num+"/rainfall_anomalies/R1/MAM/3")
output(access_trimmed.trim_MAM,indices_phase.IPO_neutralR1_MAM,indices_phase.ENSO_posR1_MAM,\
       "","/composite/"+num+"/rainfall/R1/MAM/4","/composite/"+num+"/rainfall_anomalies/R1/MAM/4")
output(access_trimmed.trim_MAM,indices_phase.IPO_neutralR1_MAM,indices_phase.ENSO_neutralR1_MAM,\
       "","/composite/"+num+"/rainfall/R1/MAM/5","/composite/"+num+"/rainfall_anomalies/R1/MAM/5")
output(access_trimmed.trim_MAM,indices_phase.IPO_neutralR1_MAM,indices_phase.ENSO_negR1_MAM,\
       "","/composite/"+num+"/rainfall/R1/MAM/6","/composite/"+num+"/rainfall_anomalies/R1/MAM/6")
output(access_trimmed.trim_MAM,indices_phase.IPO_negR1_MAM,indices_phase.ENSO_posR1_MAM,\
       "","/composite/"+num+"/rainfall/R1/MAM/7","/composite/"+num+"/rainfall_anomalies/R1/MAM/7")
output(access_trimmed.trim_MAM,indices_phase.IPO_negR1_MAM,indices_phase.ENSO_neutralR1_MAM,\
       "","/composite/"+num+"/rainfall/R1/MAM/8","/composite/"+num+"/rainfall_anomalies/R1/MAM/8")
output(access_trimmed.trim_MAM,indices_phase.IPO_negR1_MAM,indices_phase.ENSO_negR1_MAM,\
       "","/composite/"+num+"/rainfall/R1/MAM/9","/composite/"+num+"/rainfall_anomalies/R1/MAM/9")

ACCESS_MAM = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/MAM/*.png",3,3,title=(r'ACCESS1.3 R1 MAM: mean rainfall'+sigma))
ACCESS_MAM_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/MAM/*.png",3,3,title=(r'ACCESS1.3 R1 MAM: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_MAM,"","composite/"+num+"_compiled/R1/ACCESS_MAM")
maps_sub.saveFig(ACCESS_MAM_Anom,"","composite/"+num+"_compiled/R1/ACCESS_MAM_Anom")


#ACCESS R1: annual

output(access_trimmed.trim_Annual,indices_phase.IPO_posR1_annual,indices_phase.ENSO_posR1_annual,\
       "","/composite/"+num+"/rainfall/R1/Annual/1","/composite/"+num+"/rainfall_anomalies/R1/Annual/1")
output(access_trimmed.trim_Annual,indices_phase.IPO_posR1_annual,indices_phase.ENSO_neutralR1_annual,\
       "","/composite/"+num+"/rainfall/R1/Annual/2","/composite/"+num+"/rainfall_anomalies/R1/Annual/2")
output(access_trimmed.trim_Annual,indices_phase.IPO_posR1_annual,indices_phase.ENSO_negR1_annual,\
       "","/composite/"+num+"/rainfall/R1/Annual/3","/composite/"+num+"/rainfall_anomalies/R1/Annual/3")
output(access_trimmed.trim_Annual,indices_phase.IPO_neutralR1_annual,indices_phase.ENSO_posR1_annual,\
       "","/composite/"+num+"/rainfall/R1/Annual/4","/composite/"+num+"/rainfall_anomalies/R1/Annual/4")
output(access_trimmed.trim_Annual,indices_phase.IPO_neutralR1_annual,indices_phase.ENSO_neutralR1_annual,\
       "","/composite/"+num+"/rainfall/R1/Annual/5","/composite/"+num+"/rainfall_anomalies/R1/Annual/5")
output(access_trimmed.trim_Annual,indices_phase.IPO_neutralR1_annual,indices_phase.ENSO_negR1_annual,\
       "","/composite/"+num+"/rainfall/R1/Annual/6","/composite/"+num+"/rainfall_anomalies/R1/Annual/6")
output(access_trimmed.trim_Annual,indices_phase.IPO_negR1_annual,indices_phase.ENSO_posR1_annual,\
       "","/composite/"+num+"/rainfall/R1/Annual/7","/composite/"+num+"/rainfall_anomalies/R1/Annual/7")
output(access_trimmed.trim_Annual,indices_phase.IPO_negR1_annual,indices_phase.ENSO_neutralR1_annual,\
       "","/composite/"+num+"/rainfall/R1/Annual/8","/composite/"+num+"/rainfall_anomalies/R1/Annual/8")
output(access_trimmed.trim_Annual,indices_phase.IPO_negR1_annual,indices_phase.ENSO_negR1_annual,\
       "","/composite/"+num+"/rainfall/R1/Annual/9","/composite/"+num+"/rainfall_anomalies/R1/Annual/9")

ACCESS_annual = multi("my_coding_routines/images/composite/"+num+"/rainfall/R1/Annual/*.png",3,3,title=(r'ACCESS1.3 R1 annual: mean rainfall'+sigma))
ACCESS_annual_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R1/Annual/*.png",3,3,title=(r'ACCESS1.3 R1 annual: mean rainfall anomalies'+sigma))
maps_sub.saveFig(ACCESS_annual,"","composite/"+num+"_compiled/R1/ACCESS_annual")
maps_sub.saveFig(ACCESS_annual_Anom,"","composite/"+num+"_compiled/R1/ACCESS_annual_Anom")

