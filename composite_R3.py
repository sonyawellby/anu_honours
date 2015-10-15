"""
Code which stratifies ENSO/IPO and ACCESS1.3 R3 rainfall data
for composite analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 30 September 2015.
"""
from composite import *
import indices_phase
import awap_prepare
import access_trimmed

#Change as required to "1_sd", "2_sd", "3_sd"
num = "1_sd"
#Enter as needed: (3 $\sigma$)

#ACCESS R3: June

output(access_trimmed.trim_June,indices_phase.IPO_posR3_Jun,indices_phase.ENSO_posR3_Jun,\
       "","/composite/"+num+"/rainfall/R3/June/1","/composite/"+num+"/rainfall_anomalies/R3/June/1")
output(access_trimmed.trim_June,indices_phase.IPO_posR3_Jun,indices_phase.ENSO_neutralR3_Jun,\
       "","/composite/"+num+"/rainfall/R3/June/2","/composite/"+num+"/rainfall_anomalies/R3/June/2")
output(access_trimmed.trim_June,indices_phase.IPO_posR3_Jun,indices_phase.ENSO_negR3_Jun,\
       "","/composite/"+num+"/rainfall/R3/June/3","/composite/"+num+"/rainfall_anomalies/R3/June/3")
output(access_trimmed.trim_June,indices_phase.IPO_neutralR3_Jun,indices_phase.ENSO_posR3_Jun,\
       "","/composite/"+num+"/rainfall/R3/June/4","/composite/"+num+"/rainfall_anomalies/R3/June/4")
output(access_trimmed.trim_June,indices_phase.IPO_neutralR3_Jun,indices_phase.ENSO_neutralR3_Jun,\
       "","/composite/"+num+"/rainfall/R3/June/5","/composite/"+num+"/rainfall_anomalies/R3/June/5")
output(access_trimmed.trim_June,indices_phase.IPO_neutralR3_Jun,indices_phase.ENSO_negR3_Jun,\
       "","/composite/"+num+"/rainfall/R3/June/6","/composite/"+num+"/rainfall_anomalies/R3/June/6")
output(access_trimmed.trim_June,indices_phase.IPO_negR3_Jun,indices_phase.ENSO_posR3_Jun,\
       "","/composite/"+num+"/rainfall/R3/June/7","/composite/"+num+"/rainfall_anomalies/R3/June/7")
output(access_trimmed.trim_June,indices_phase.IPO_negR3_Jun,indices_phase.ENSO_neutralR3_Jun,\
       "","/composite/"+num+"/rainfall/R3/June/8","/composite/"+num+"/rainfall_anomalies/R3/June/8")
output(access_trimmed.trim_June,indices_phase.IPO_negR3_Jun,indices_phase.ENSO_negR3_Jun,\
       "","/composite/"+num+"/rainfall/R3/June/9","/composite/"+num+"/rainfall_anomalies/R3/June/9")

ACCESS_June = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/June/*.png",3,3,title=(r'ACCESS1.3 R3 June: mean rainfall'))
ACCESS_June_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/June/*.png",3,3,title=(r'ACCESS1.3 R3 June: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_June,"","composite/"+num+"_compiled/R3/ACCESS_June")
maps_sub.saveFig(ACCESS_June_Anom,"","composite/"+num+"_compiled/R3/ACCESS_June_Anom")


#ACCESS R3: July

output(access_trimmed.trim_July,indices_phase.IPO_posR3_Jul,indices_phase.ENSO_posR3_Jul,\
       "","/composite/"+num+"/rainfall/R3/July/1","/composite/"+num+"/rainfall_anomalies/R3/July/1")
output(access_trimmed.trim_July,indices_phase.IPO_posR3_Jul,indices_phase.ENSO_neutralR3_Jul,\
       "","/composite/"+num+"/rainfall/R3/July/2","/composite/"+num+"/rainfall_anomalies/R3/July/2")
output(access_trimmed.trim_July,indices_phase.IPO_posR3_Jul,indices_phase.ENSO_negR3_Jul,\
       "","/composite/"+num+"/rainfall/R3/July/3","/composite/"+num+"/rainfall_anomalies/R3/July/3")
output(access_trimmed.trim_July,indices_phase.IPO_neutralR3_Jul,indices_phase.ENSO_posR3_Jul,\
       "","/composite/"+num+"/rainfall/R3/July/4","/composite/"+num+"/rainfall_anomalies/R3/July/4")
output(access_trimmed.trim_July,indices_phase.IPO_neutralR3_Jul,indices_phase.ENSO_neutralR3_Jul,\
       "","/composite/"+num+"/rainfall/R3/July/5","/composite/"+num+"/rainfall_anomalies/R3/July/5")
output(access_trimmed.trim_July,indices_phase.IPO_neutralR3_Jul,indices_phase.ENSO_negR3_Jul,\
       "","/composite/"+num+"/rainfall/R3/July/6","/composite/"+num+"/rainfall_anomalies/R3/July/6")
output(access_trimmed.trim_July,indices_phase.IPO_negR3_Jul,indices_phase.ENSO_posR3_Jul,\
       "","/composite/"+num+"/rainfall/R3/July/7","/composite/"+num+"/rainfall_anomalies/R3/July/7")
output(access_trimmed.trim_July,indices_phase.IPO_negR3_Jul,indices_phase.ENSO_neutralR3_Jul,\
       "","/composite/"+num+"/rainfall/R3/July/8","/composite/"+num+"/rainfall_anomalies/R3/July/8")
output(access_trimmed.trim_July,indices_phase.IPO_negR3_Jul,indices_phase.ENSO_negR3_Jul,\
       "","/composite/"+num+"/rainfall/R3/July/9","/composite/"+num+"/rainfall_anomalies/R3/July/9")

ACCESS_July = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/July/*.png",3,3,title=(r'ACCESS1.3 R3 July: mean rainfall'))
ACCESS_July_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/July/*.png",3,3,title=(r'ACCESS1.3 R3 July: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_July,"","composite/"+num+"_compiled/R3/ACCESS_July")
maps_sub.saveFig(ACCESS_July_Anom,"","composite/"+num+"_compiled/R3/ACCESS_July_Anom")


#ACCESS R3: August

output(access_trimmed.trim_August,indices_phase.IPO_posR3_Aug,indices_phase.ENSO_posR3_Aug,\
       "","/composite/"+num+"/rainfall/R3/August/1","/composite/"+num+"/rainfall_anomalies/R3/August/1")
output(access_trimmed.trim_August,indices_phase.IPO_posR3_Aug,indices_phase.ENSO_neutralR3_Aug,\
       "","/composite/"+num+"/rainfall/R3/August/2","/composite/"+num+"/rainfall_anomalies/R3/August/2")
output(access_trimmed.trim_August,indices_phase.IPO_posR3_Aug,indices_phase.ENSO_negR3_Aug,\
       "","/composite/"+num+"/rainfall/R3/August/3","/composite/"+num+"/rainfall_anomalies/R3/August/3")
output(access_trimmed.trim_August,indices_phase.IPO_neutralR3_Aug,indices_phase.ENSO_posR3_Aug,\
       "","/composite/"+num+"/rainfall/R3/August/4","/composite/"+num+"/rainfall_anomalies/R3/August/4")
output(access_trimmed.trim_August,indices_phase.IPO_neutralR3_Aug,indices_phase.ENSO_neutralR3_Aug,\
       "","/composite/"+num+"/rainfall/R3/August/5","/composite/"+num+"/rainfall_anomalies/R3/August/5")
output(access_trimmed.trim_August,indices_phase.IPO_neutralR3_Aug,indices_phase.ENSO_negR3_Aug,\
       "","/composite/"+num+"/rainfall/R3/August/6","/composite/"+num+"/rainfall_anomalies/R3/August/6")
output(access_trimmed.trim_August,indices_phase.IPO_negR3_Aug,indices_phase.ENSO_posR3_Aug,\
       "","/composite/"+num+"/rainfall/R3/August/7","/composite/"+num+"/rainfall_anomalies/R3/August/7")
output(access_trimmed.trim_August,indices_phase.IPO_negR3_Aug,indices_phase.ENSO_neutralR3_Aug,\
       "","/composite/"+num+"/rainfall/R3/August/8","/composite/"+num+"/rainfall_anomalies/R3/August/8")
output(access_trimmed.trim_August,indices_phase.IPO_negR3_Aug,indices_phase.ENSO_negR3_Aug,\
       "","/composite/"+num+"/rainfall/R3/August/9","/composite/"+num+"/rainfall_anomalies/R3/August/9")

ACCESS_August = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/August/*.png",3,3,title=(r'ACCESS1.3 R3 August: mean rainfall'))
ACCESS_August_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/August/*.png",3,3,title=(r'ACCESS1.3 R3 August: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_August,"","composite/"+num+"_compiled/R3/ACCESS_August")
maps_sub.saveFig(ACCESS_August_Anom,"","composite/"+num+"_compiled/R3/ACCESS_August_Anom")


#ACCESS R3: September

output(access_trimmed.trim_September,indices_phase.IPO_posR3_Sep,indices_phase.ENSO_posR3_Sep,\
       "","/composite/"+num+"/rainfall/R3/September/1","/composite/"+num+"/rainfall_anomalies/R3/September/1")
output(access_trimmed.trim_September,indices_phase.IPO_posR3_Sep,indices_phase.ENSO_neutralR3_Sep,\
       "","/composite/"+num+"/rainfall/R3/September/2","/composite/"+num+"/rainfall_anomalies/R3/September/2")
output(access_trimmed.trim_September,indices_phase.IPO_posR3_Sep,indices_phase.ENSO_negR3_Sep,\
       "","/composite/"+num+"/rainfall/R3/September/3","/composite/"+num+"/rainfall_anomalies/R3/September/3")
output(access_trimmed.trim_September,indices_phase.IPO_neutralR3_Sep,indices_phase.ENSO_posR3_Sep,\
       "","/composite/"+num+"/rainfall/R3/September/4","/composite/"+num+"/rainfall_anomalies/R3/September/4")
output(access_trimmed.trim_September,indices_phase.IPO_neutralR3_Sep,indices_phase.ENSO_neutralR3_Sep,\
       "","/composite/"+num+"/rainfall/R3/September/5","/composite/"+num+"/rainfall_anomalies/R3/September/5")
output(access_trimmed.trim_September,indices_phase.IPO_neutralR3_Sep,indices_phase.ENSO_negR3_Sep,\
       "","/composite/"+num+"/rainfall/R3/September/6","/composite/"+num+"/rainfall_anomalies/R3/September/6")
output(access_trimmed.trim_September,indices_phase.IPO_negR3_Sep,indices_phase.ENSO_posR3_Sep,\
       "","/composite/"+num+"/rainfall/R3/September/7","/composite/"+num+"/rainfall_anomalies/R3/September/7")
output(access_trimmed.trim_September,indices_phase.IPO_negR3_Sep,indices_phase.ENSO_neutralR3_Sep,\
       "","/composite/"+num+"/rainfall/R3/September/8","/composite/"+num+"/rainfall_anomalies/R3/September/8")
output(access_trimmed.trim_September,indices_phase.IPO_negR3_Sep,indices_phase.ENSO_negR3_Sep,\
       "","/composite/"+num+"/rainfall/R3/September/9","/composite/"+num+"/rainfall_anomalies/R3/September/9")

ACCESS_September = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/September/*.png",3,3,title=(r'ACCESS1.3 R3 September: mean rainfall'))
ACCESS_September_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/September/*.png",3,3,title=(r'ACCESS1.3 R3 September: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_September,"","composite/"+num+"_compiled/R3/ACCESS_September")
maps_sub.saveFig(ACCESS_September_Anom,"","composite/"+num+"_compiled/R3/ACCESS_September_Anom")


#ACCESS R3: October

output(access_trimmed.trim_October,indices_phase.IPO_posR3_Oct,indices_phase.ENSO_posR3_Oct,\
       "","/composite/"+num+"/rainfall/R3/October/1","/composite/"+num+"/rainfall_anomalies/R3/October/1")
output(access_trimmed.trim_October,indices_phase.IPO_posR3_Oct,indices_phase.ENSO_neutralR3_Oct,\
       "","/composite/"+num+"/rainfall/R3/October/2","/composite/"+num+"/rainfall_anomalies/R3/October/2")
output(access_trimmed.trim_October,indices_phase.IPO_posR3_Oct,indices_phase.ENSO_negR3_Oct,\
       "","/composite/"+num+"/rainfall/R3/October/3","/composite/"+num+"/rainfall_anomalies/R3/October/3")
output(access_trimmed.trim_October,indices_phase.IPO_neutralR3_Oct,indices_phase.ENSO_posR3_Oct,\
       "","/composite/"+num+"/rainfall/R3/October/4","/composite/"+num+"/rainfall_anomalies/R3/October/4")
output(access_trimmed.trim_October,indices_phase.IPO_neutralR3_Oct,indices_phase.ENSO_neutralR3_Oct,\
       "","/composite/"+num+"/rainfall/R3/October/5","/composite/"+num+"/rainfall_anomalies/R3/October/5")
output(access_trimmed.trim_October,indices_phase.IPO_neutralR3_Oct,indices_phase.ENSO_negR3_Oct,\
       "","/composite/"+num+"/rainfall/R3/October/6","/composite/"+num+"/rainfall_anomalies/R3/October/6")
output(access_trimmed.trim_October,indices_phase.IPO_negR3_Oct,indices_phase.ENSO_posR3_Oct,\
       "","/composite/"+num+"/rainfall/R3/October/7","/composite/"+num+"/rainfall_anomalies/R3/October/7")
output(access_trimmed.trim_October,indices_phase.IPO_negR3_Oct,indices_phase.ENSO_neutralR3_Oct,\
       "","/composite/"+num+"/rainfall/R3/October/8","/composite/"+num+"/rainfall_anomalies/R3/October/8")
output(access_trimmed.trim_October,indices_phase.IPO_negR3_Oct,indices_phase.ENSO_negR3_Oct,\
       "","/composite/"+num+"/rainfall/R3/October/9","/composite/"+num+"/rainfall_anomalies/R3/October/9")

ACCESS_October = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/October/*.png",3,3,title=(r'ACCESS1.3 R3 October: mean rainfall'))
ACCESS_October_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/October/*.png",3,3,title=(r'ACCESS1.3 R3 October: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_October,"","composite/"+num+"_compiled/R3/ACCESS_October")
maps_sub.saveFig(ACCESS_October_Anom,"","composite/"+num+"_compiled/R3/ACCESS_October_Anom")


#ACCESS R3: November

output(access_trimmed.trim_November,indices_phase.IPO_posR3_Nov,indices_phase.ENSO_posR3_Nov,\
       "","/composite/"+num+"/rainfall/R3/November/1","/composite/"+num+"/rainfall_anomalies/R3/November/1")
output(access_trimmed.trim_November,indices_phase.IPO_posR3_Nov,indices_phase.ENSO_neutralR3_Nov,\
       "","/composite/"+num+"/rainfall/R3/November/2","/composite/"+num+"/rainfall_anomalies/R3/November/2")
output(access_trimmed.trim_November,indices_phase.IPO_posR3_Nov,indices_phase.ENSO_negR3_Nov,\
       "","/composite/"+num+"/rainfall/R3/November/3","/composite/"+num+"/rainfall_anomalies/R3/November/3")
output(access_trimmed.trim_November,indices_phase.IPO_neutralR3_Nov,indices_phase.ENSO_posR3_Nov,\
       "","/composite/"+num+"/rainfall/R3/November/4","/composite/"+num+"/rainfall_anomalies/R3/November/4")
output(access_trimmed.trim_November,indices_phase.IPO_neutralR3_Nov,indices_phase.ENSO_neutralR3_Nov,\
       "","/composite/"+num+"/rainfall/R3/November/5","/composite/"+num+"/rainfall_anomalies/R3/November/5")
output(access_trimmed.trim_November,indices_phase.IPO_neutralR3_Nov,indices_phase.ENSO_negR3_Nov,\
       "","/composite/"+num+"/rainfall/R3/November/6","/composite/"+num+"/rainfall_anomalies/R3/November/6")
output(access_trimmed.trim_November,indices_phase.IPO_negR3_Nov,indices_phase.ENSO_posR3_Nov,\
       "","/composite/"+num+"/rainfall/R3/November/7","/composite/"+num+"/rainfall_anomalies/R3/November/7")
output(access_trimmed.trim_November,indices_phase.IPO_negR3_Nov,indices_phase.ENSO_neutralR3_Nov,\
       "","/composite/"+num+"/rainfall/R3/November/8","/composite/"+num+"/rainfall_anomalies/R3/November/8")
output(access_trimmed.trim_November,indices_phase.IPO_negR3_Nov,indices_phase.ENSO_negR3_Nov,\
       "","/composite/"+num+"/rainfall/R3/November/9","/composite/"+num+"/rainfall_anomalies/R3/November/9")

ACCESS_November = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/November/*.png",3,3,title=(r'ACCESS1.3 R3 November: mean rainfall'))
ACCESS_November_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/November/*.png",3,3,title=(r'ACCESS1.3 R3 November: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_November,"","composite/"+num+"_compiled/R3/ACCESS_November")
maps_sub.saveFig(ACCESS_November_Anom,"","composite/"+num+"_compiled/R3/ACCESS_November_Anom")


#ACCESS R3: December

output(access_trimmed.trim_December,indices_phase.IPO_posR3_Dec,indices_phase.ENSO_posR3_Dec,\
       "","/composite/"+num+"/rainfall/R3/December/1","/composite/"+num+"/rainfall_anomalies/R3/December/1")
output(access_trimmed.trim_December,indices_phase.IPO_posR3_Dec,indices_phase.ENSO_neutralR3_Dec,\
       "","/composite/"+num+"/rainfall/R3/December/2","/composite/"+num+"/rainfall_anomalies/R3/December/2")
output(access_trimmed.trim_December,indices_phase.IPO_posR3_Dec,indices_phase.ENSO_negR3_Dec,\
       "","/composite/"+num+"/rainfall/R3/December/3","/composite/"+num+"/rainfall_anomalies/R3/December/3")
output(access_trimmed.trim_December,indices_phase.IPO_neutralR3_Dec,indices_phase.ENSO_posR3_Dec,\
       "","/composite/"+num+"/rainfall/R3/December/4","/composite/"+num+"/rainfall_anomalies/R3/December/4")
output(access_trimmed.trim_December,indices_phase.IPO_neutralR3_Dec,indices_phase.ENSO_neutralR3_Dec,\
       "","/composite/"+num+"/rainfall/R3/December/5","/composite/"+num+"/rainfall_anomalies/R3/December/5")
output(access_trimmed.trim_December,indices_phase.IPO_neutralR3_Dec,indices_phase.ENSO_negR3_Dec,\
       "","/composite/"+num+"/rainfall/R3/December/6","/composite/"+num+"/rainfall_anomalies/R3/December/6")
output(access_trimmed.trim_December,indices_phase.IPO_negR3_Dec,indices_phase.ENSO_posR3_Dec,\
       "","/composite/"+num+"/rainfall/R3/December/7","/composite/"+num+"/rainfall_anomalies/R3/December/7")
output(access_trimmed.trim_December,indices_phase.IPO_negR3_Dec,indices_phase.ENSO_neutralR3_Dec,\
       "","/composite/"+num+"/rainfall/R3/December/8","/composite/"+num+"/rainfall_anomalies/R3/December/8")
output(access_trimmed.trim_December,indices_phase.IPO_negR3_Dec,indices_phase.ENSO_negR3_Dec,\
       "","/composite/"+num+"/rainfall/R3/December/9","/composite/"+num+"/rainfall_anomalies/R3/December/9")

ACCESS_December = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/December/*.png",3,3,title=(r'ACCESS1.3 R3 December: mean rainfall'))
ACCESS_December_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/December/*.png",3,3,title=(r'ACCESS1.3 R3 December: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_December,"","composite/"+num+"_compiled/R3/ACCESS_December")
maps_sub.saveFig(ACCESS_December_Anom,"","composite/"+num+"_compiled/R3/ACCESS_December_Anom")


#ACCESS R3: January

output(access_trimmed.trim_January,indices_phase.IPO_posR3_Jan,indices_phase.ENSO_posR3_Jan,\
       "","/composite/"+num+"/rainfall/R3/January/1","/composite/"+num+"/rainfall_anomalies/R3/January/1")
output(access_trimmed.trim_January,indices_phase.IPO_posR3_Jan,indices_phase.ENSO_neutralR3_Jan,\
       "","/composite/"+num+"/rainfall/R3/January/2","/composite/"+num+"/rainfall_anomalies/R3/January/2")
output(access_trimmed.trim_January,indices_phase.IPO_posR3_Jan,indices_phase.ENSO_negR3_Jan,\
       "","/composite/"+num+"/rainfall/R3/January/3","/composite/"+num+"/rainfall_anomalies/R3/January/3")
output(access_trimmed.trim_January,indices_phase.IPO_neutralR3_Jan,indices_phase.ENSO_posR3_Jan,\
       "","/composite/"+num+"/rainfall/R3/January/4","/composite/"+num+"/rainfall_anomalies/R3/January/4")
output(access_trimmed.trim_January,indices_phase.IPO_neutralR3_Jan,indices_phase.ENSO_neutralR3_Jan,\
       "","/composite/"+num+"/rainfall/R3/January/5","/composite/"+num+"/rainfall_anomalies/R3/January/5")
output(access_trimmed.trim_January,indices_phase.IPO_neutralR3_Jan,indices_phase.ENSO_negR3_Jan,\
       "","/composite/"+num+"/rainfall/R3/January/6","/composite/"+num+"/rainfall_anomalies/R3/January/6")
output(access_trimmed.trim_January,indices_phase.IPO_negR3_Jan,indices_phase.ENSO_posR3_Jan,\
       "","/composite/"+num+"/rainfall/R3/January/7","/composite/"+num+"/rainfall_anomalies/R3/January/7")
output(access_trimmed.trim_January,indices_phase.IPO_negR3_Jan,indices_phase.ENSO_neutralR3_Jan,\
       "","/composite/"+num+"/rainfall/R3/January/8","/composite/"+num+"/rainfall_anomalies/R3/January/8")
output(access_trimmed.trim_January,indices_phase.IPO_negR3_Jan,indices_phase.ENSO_negR3_Jan,\
       "","/composite/"+num+"/rainfall/R3/January/9","/composite/"+num+"/rainfall_anomalies/R3/January/9")

ACCESS_January = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/January/*.png",3,3,title=(r'ACCESS1.3 R3 January: mean rainfall'))
ACCESS_January_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/January/*.png",3,3,title=(r'ACCESS1.3 R3 January: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_January,"","composite/"+num+"_compiled/R3/ACCESS_January")
maps_sub.saveFig(ACCESS_January_Anom,"","composite/"+num+"_compiled/R3/ACCESS_January_Anom")


#ACCESS R3: February

output(access_trimmed.trim_February,indices_phase.IPO_posR3_Feb,indices_phase.ENSO_posR3_Feb,\
       "","/composite/"+num+"/rainfall/R3/February/1","/composite/"+num+"/rainfall_anomalies/R3/February/1")
output(access_trimmed.trim_February,indices_phase.IPO_posR3_Feb,indices_phase.ENSO_neutralR3_Feb,\
       "","/composite/"+num+"/rainfall/R3/February/2","/composite/"+num+"/rainfall_anomalies/R3/February/2")
output(access_trimmed.trim_February,indices_phase.IPO_posR3_Feb,indices_phase.ENSO_negR3_Feb,\
       "","/composite/"+num+"/rainfall/R3/February/3","/composite/"+num+"/rainfall_anomalies/R3/February/3")
output(access_trimmed.trim_February,indices_phase.IPO_neutralR3_Feb,indices_phase.ENSO_posR3_Feb,\
       "","/composite/"+num+"/rainfall/R3/February/4","/composite/"+num+"/rainfall_anomalies/R3/February/4")
output(access_trimmed.trim_February,indices_phase.IPO_neutralR3_Feb,indices_phase.ENSO_neutralR3_Feb,\
       "","/composite/"+num+"/rainfall/R3/February/5","/composite/"+num+"/rainfall_anomalies/R3/February/5")
output(access_trimmed.trim_February,indices_phase.IPO_neutralR3_Feb,indices_phase.ENSO_negR3_Feb,\
       "","/composite/"+num+"/rainfall/R3/February/6","/composite/"+num+"/rainfall_anomalies/R3/February/6")
output(access_trimmed.trim_February,indices_phase.IPO_negR3_Feb,indices_phase.ENSO_posR3_Feb,\
       "","/composite/"+num+"/rainfall/R3/February/7","/composite/"+num+"/rainfall_anomalies/R3/February/7")
output(access_trimmed.trim_February,indices_phase.IPO_negR3_Feb,indices_phase.ENSO_neutralR3_Feb,\
       "","/composite/"+num+"/rainfall/R3/February/8","/composite/"+num+"/rainfall_anomalies/R3/February/8")
output(access_trimmed.trim_February,indices_phase.IPO_negR3_Feb,indices_phase.ENSO_negR3_Feb,\
       "","/composite/"+num+"/rainfall/R3/February/9","/composite/"+num+"/rainfall_anomalies/R3/February/9")

ACCESS_February = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/February/*.png",3,3,title=(r'ACCESS1.3 R3 February: mean rainfall'))
ACCESS_February_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/February/*.png",3,3,title=(r'ACCESS1.3 R3 February: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_February,"","composite/"+num+"_compiled/R3/ACCESS_February")
maps_sub.saveFig(ACCESS_February_Anom,"","composite/"+num+"_compiled/R3/ACCESS_February_Anom")


#ACCESS R3: March

output(access_trimmed.trim_March,indices_phase.IPO_posR3_Mar,indices_phase.ENSO_posR3_Mar,\
       "","/composite/"+num+"/rainfall/R3/March/1","/composite/"+num+"/rainfall_anomalies/R3/March/1")
output(access_trimmed.trim_March,indices_phase.IPO_posR3_Mar,indices_phase.ENSO_neutralR3_Mar,\
       "","/composite/"+num+"/rainfall/R3/March/2","/composite/"+num+"/rainfall_anomalies/R3/March/2")
output(access_trimmed.trim_March,indices_phase.IPO_posR3_Mar,indices_phase.ENSO_negR3_Mar,\
       "","/composite/"+num+"/rainfall/R3/March/3","/composite/"+num+"/rainfall_anomalies/R3/March/3")
output(access_trimmed.trim_March,indices_phase.IPO_neutralR3_Mar,indices_phase.ENSO_posR3_Mar,\
       "","/composite/"+num+"/rainfall/R3/March/4","/composite/"+num+"/rainfall_anomalies/R3/March/4")
output(access_trimmed.trim_March,indices_phase.IPO_neutralR3_Mar,indices_phase.ENSO_neutralR3_Mar,\
       "","/composite/"+num+"/rainfall/R3/March/5","/composite/"+num+"/rainfall_anomalies/R3/March/5")
output(access_trimmed.trim_March,indices_phase.IPO_neutralR3_Mar,indices_phase.ENSO_negR3_Mar,\
       "","/composite/"+num+"/rainfall/R3/March/6","/composite/"+num+"/rainfall_anomalies/R3/March/6")
output(access_trimmed.trim_March,indices_phase.IPO_negR3_Mar,indices_phase.ENSO_posR3_Mar,\
       "","/composite/"+num+"/rainfall/R3/March/7","/composite/"+num+"/rainfall_anomalies/R3/March/7")
output(access_trimmed.trim_March,indices_phase.IPO_negR3_Mar,indices_phase.ENSO_neutralR3_Mar,\
       "","/composite/"+num+"/rainfall/R3/March/8","/composite/"+num+"/rainfall_anomalies/R3/March/8")
output(access_trimmed.trim_March,indices_phase.IPO_negR3_Mar,indices_phase.ENSO_negR3_Mar,\
       "","/composite/"+num+"/rainfall/R3/March/9","/composite/"+num+"/rainfall_anomalies/R3/March/9")

ACCESS_March = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/March/*.png",3,3,title=(r'ACCESS1.3 R3 March: mean rainfall'))
ACCESS_March_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/March/*.png",3,3,title=(r'ACCESS1.3 R3 March: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_March,"","composite/"+num+"_compiled/R3/ACCESS_March")
maps_sub.saveFig(ACCESS_March_Anom,"","composite/"+num+"_compiled/R3/ACCESS_March_Anom")

#ACCESS R3: April

output(access_trimmed.trim_April,indices_phase.IPO_posR3_Apr,indices_phase.ENSO_posR3_Apr,\
       "","/composite/"+num+"/rainfall/R3/April/1","/composite/"+num+"/rainfall_anomalies/R3/April/1")
output(access_trimmed.trim_April,indices_phase.IPO_posR3_Apr,indices_phase.ENSO_neutralR3_Apr,\
       "","/composite/"+num+"/rainfall/R3/April/2","/composite/"+num+"/rainfall_anomalies/R3/April/2")
output(access_trimmed.trim_April,indices_phase.IPO_posR3_Apr,indices_phase.ENSO_negR3_Apr,\
       "","/composite/"+num+"/rainfall/R3/April/3","/composite/"+num+"/rainfall_anomalies/R3/April/3")
output(access_trimmed.trim_April,indices_phase.IPO_neutralR3_Apr,indices_phase.ENSO_posR3_Apr,\
       "","/composite/"+num+"/rainfall/R3/April/4","/composite/"+num+"/rainfall_anomalies/R3/April/4")
output(access_trimmed.trim_April,indices_phase.IPO_neutralR3_Apr,indices_phase.ENSO_neutralR3_Apr,\
       "","/composite/"+num+"/rainfall/R3/April/5","/composite/"+num+"/rainfall_anomalies/R3/April/5")
output(access_trimmed.trim_April,indices_phase.IPO_neutralR3_Apr,indices_phase.ENSO_negR3_Apr,\
       "","/composite/"+num+"/rainfall/R3/April/6","/composite/"+num+"/rainfall_anomalies/R3/April/6")
output(access_trimmed.trim_April,indices_phase.IPO_negR3_Apr,indices_phase.ENSO_posR3_Apr,\
       "","/composite/"+num+"/rainfall/R3/April/7","/composite/"+num+"/rainfall_anomalies/R3/April/7")
output(access_trimmed.trim_April,indices_phase.IPO_negR3_Apr,indices_phase.ENSO_neutralR3_Apr,\
       "","/composite/"+num+"/rainfall/R3/April/8","/composite/"+num+"/rainfall_anomalies/R3/April/8")
output(access_trimmed.trim_April,indices_phase.IPO_negR3_Apr,indices_phase.ENSO_negR3_Apr,\
       "","/composite/"+num+"/rainfall/R3/April/9","/composite/"+num+"/rainfall_anomalies/R3/April/9")

ACCESS_April = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/April/*.png",3,3,title=(r'ACCESS1.3 R3 April: mean rainfall'))
ACCESS_April_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/April/*.png",3,3,title=(r'ACCESS1.3 R3 April: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_April,"","composite/"+num+"_compiled/R3/ACCESS_April")
maps_sub.saveFig(ACCESS_April_Anom,"","composite/"+num+"_compiled/R3/ACCESS_April_Anom")


#ACCESS R3: May

output(access_trimmed.trim_May,indices_phase.IPO_posR3_May,indices_phase.ENSO_posR3_May,\
       "","/composite/"+num+"/rainfall/R3/May/1","/composite/"+num+"/rainfall_anomalies/R3/May/1")
output(access_trimmed.trim_May,indices_phase.IPO_posR3_May,indices_phase.ENSO_neutralR3_May,\
       "","/composite/"+num+"/rainfall/R3/May/2","/composite/"+num+"/rainfall_anomalies/R3/May/2")
output(access_trimmed.trim_May,indices_phase.IPO_posR3_May,indices_phase.ENSO_negR3_May,\
       "","/composite/"+num+"/rainfall/R3/May/3","/composite/"+num+"/rainfall_anomalies/R3/May/3")
output(access_trimmed.trim_May,indices_phase.IPO_neutralR3_May,indices_phase.ENSO_posR3_May,\
       "","/composite/"+num+"/rainfall/R3/May/4","/composite/"+num+"/rainfall_anomalies/R3/May/4")
output(access_trimmed.trim_May,indices_phase.IPO_neutralR3_May,indices_phase.ENSO_neutralR3_May,\
       "","/composite/"+num+"/rainfall/R3/May/5","/composite/"+num+"/rainfall_anomalies/R3/May/5")
output(access_trimmed.trim_May,indices_phase.IPO_neutralR3_May,indices_phase.ENSO_negR3_May,\
       "","/composite/"+num+"/rainfall/R3/May/6","/composite/"+num+"/rainfall_anomalies/R3/May/6")
output(access_trimmed.trim_May,indices_phase.IPO_negR3_May,indices_phase.ENSO_posR3_May,\
       "","/composite/"+num+"/rainfall/R3/May/7","/composite/"+num+"/rainfall_anomalies/R3/May/7")
output(access_trimmed.trim_May,indices_phase.IPO_negR3_May,indices_phase.ENSO_neutralR3_May,\
       "","/composite/"+num+"/rainfall/R3/May/8","/composite/"+num+"/rainfall_anomalies/R3/May/8")
output(access_trimmed.trim_May,indices_phase.IPO_negR3_May,indices_phase.ENSO_negR3_May,\
       "","/composite/"+num+"/rainfall/R3/May/9","/composite/"+num+"/rainfall_anomalies/R3/May/9")

ACCESS_May = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/May/*.png",3,3,title=(r'ACCESS1.3 R3 May: mean rainfall'))
ACCESS_May_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/May/*.png",3,3,title=(r'ACCESS1.3 R3 May: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_May,"","composite/"+num+"_compiled/R3/ACCESS_May")
maps_sub.saveFig(ACCESS_May_Anom,"","composite/"+num+"_compiled/R3/ACCESS_May_Anom")


#ACCESS R3: JJA

output(access_trimmed.trim_JJA,indices_phase.IPO_posR3_JJA,indices_phase.ENSO_posR3_JJA,\
       "","/composite/"+num+"/rainfall/R3/JJA/1","/composite/"+num+"/rainfall_anomalies/R3/JJA/1")
output(access_trimmed.trim_JJA,indices_phase.IPO_posR3_JJA,indices_phase.ENSO_neutralR3_JJA,\
       "","/composite/"+num+"/rainfall/R3/JJA/2","/composite/"+num+"/rainfall_anomalies/R3/JJA/2")
output(access_trimmed.trim_JJA,indices_phase.IPO_posR3_JJA,indices_phase.ENSO_negR3_JJA,\
       "","/composite/"+num+"/rainfall/R3/JJA/3","/composite/"+num+"/rainfall_anomalies/R3/JJA/3")
output(access_trimmed.trim_JJA,indices_phase.IPO_neutralR3_JJA,indices_phase.ENSO_posR3_JJA,\
       "","/composite/"+num+"/rainfall/R3/JJA/4","/composite/"+num+"/rainfall_anomalies/R3/JJA/4")
output(access_trimmed.trim_JJA,indices_phase.IPO_neutralR3_JJA,indices_phase.ENSO_neutralR3_JJA,\
       "","/composite/"+num+"/rainfall/R3/JJA/5","/composite/"+num+"/rainfall_anomalies/R3/JJA/5")
output(access_trimmed.trim_JJA,indices_phase.IPO_neutralR3_JJA,indices_phase.ENSO_negR3_JJA,\
       "","/composite/"+num+"/rainfall/R3/JJA/6","/composite/"+num+"/rainfall_anomalies/R3/JJA/6")
output(access_trimmed.trim_JJA,indices_phase.IPO_negR3_JJA,indices_phase.ENSO_posR3_JJA,\
       "","/composite/"+num+"/rainfall/R3/JJA/7","/composite/"+num+"/rainfall_anomalies/R3/JJA/7")
output(access_trimmed.trim_JJA,indices_phase.IPO_negR3_JJA,indices_phase.ENSO_neutralR3_JJA,\
       "","/composite/"+num+"/rainfall/R3/JJA/8","/composite/"+num+"/rainfall_anomalies/R3/JJA/8")
output(access_trimmed.trim_JJA,indices_phase.IPO_negR3_JJA,indices_phase.ENSO_negR3_JJA,\
       "","/composite/"+num+"/rainfall/R3/JJA/9","/composite/"+num+"/rainfall_anomalies/R3/JJA/9")

ACCESS_JJA = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/JJA/*.png",3,3,title=(r'ACCESS1.3 R3 JJA: mean rainfall'))
ACCESS_JJA_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/JJA/*.png",3,3,title=(r'ACCESS1.3 R3 JJA: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_JJA,"","composite/"+num+"_compiled/R3/ACCESS_JJA")
maps_sub.saveFig(ACCESS_JJA_Anom,"","composite/"+num+"_compiled/R3/ACCESS_JJA_Anom")


#ACCESS R3: SON

output(access_trimmed.trim_SON,indices_phase.IPO_posR3_SON,indices_phase.ENSO_posR3_SON,\
       "","/composite/"+num+"/rainfall/R3/SON/1","/composite/"+num+"/rainfall_anomalies/R3/SON/1")
output(access_trimmed.trim_SON,indices_phase.IPO_posR3_SON,indices_phase.ENSO_neutralR3_SON,\
       "","/composite/"+num+"/rainfall/R3/SON/2","/composite/"+num+"/rainfall_anomalies/R3/SON/2")
output(access_trimmed.trim_SON,indices_phase.IPO_posR3_SON,indices_phase.ENSO_negR3_SON,\
       "","/composite/"+num+"/rainfall/R3/SON/3","/composite/"+num+"/rainfall_anomalies/R3/SON/3")
output(access_trimmed.trim_SON,indices_phase.IPO_neutralR3_SON,indices_phase.ENSO_posR3_SON,\
       "","/composite/"+num+"/rainfall/R3/SON/4","/composite/"+num+"/rainfall_anomalies/R3/SON/4")
output(access_trimmed.trim_SON,indices_phase.IPO_neutralR3_SON,indices_phase.ENSO_neutralR3_SON,\
       "","/composite/"+num+"/rainfall/R3/SON/5","/composite/"+num+"/rainfall_anomalies/R3/SON/5")
output(access_trimmed.trim_SON,indices_phase.IPO_neutralR3_SON,indices_phase.ENSO_negR3_SON,\
       "","/composite/"+num+"/rainfall/R3/SON/6","/composite/"+num+"/rainfall_anomalies/R3/SON/6")
output(access_trimmed.trim_SON,indices_phase.IPO_negR3_SON,indices_phase.ENSO_posR3_SON,\
       "","/composite/"+num+"/rainfall/R3/SON/7","/composite/"+num+"/rainfall_anomalies/R3/SON/7")
output(access_trimmed.trim_SON,indices_phase.IPO_negR3_SON,indices_phase.ENSO_neutralR3_SON,\
       "","/composite/"+num+"/rainfall/R3/SON/8","/composite/"+num+"/rainfall_anomalies/R3/SON/8")
output(access_trimmed.trim_SON,indices_phase.IPO_negR3_SON,indices_phase.ENSO_negR3_SON,\
       "","/composite/"+num+"/rainfall/R3/SON/9","/composite/"+num+"/rainfall_anomalies/R3/SON/9")

ACCESS_SON = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/SON/*.png",3,3,title=(r'ACCESS1.3 R3 SON: mean rainfall'))
ACCESS_SON_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/SON/*.png",3,3,title=(r'ACCESS1.3 R3 SON: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_SON,"","composite/"+num+"_compiled/R3/ACCESS_SON")
maps_sub.saveFig(ACCESS_SON_Anom,"","composite/"+num+"_compiled/R3/ACCESS_SON_Anom")


#ACCESS R3: DJF

output(access_trimmed.trim_DJF,indices_phase.IPO_posR3_DJF,indices_phase.ENSO_posR3_DJF,\
       "","/composite/"+num+"/rainfall/R3/DJF/1","/composite/"+num+"/rainfall_anomalies/R3/DJF/1")
output(access_trimmed.trim_DJF,indices_phase.IPO_posR3_DJF,indices_phase.ENSO_neutralR3_DJF,\
       "","/composite/"+num+"/rainfall/R3/DJF/2","/composite/"+num+"/rainfall_anomalies/R3/DJF/2")
output(access_trimmed.trim_DJF,indices_phase.IPO_posR3_DJF,indices_phase.ENSO_negR3_DJF,\
       "","/composite/"+num+"/rainfall/R3/DJF/3","/composite/"+num+"/rainfall_anomalies/R3/DJF/3")
output(access_trimmed.trim_DJF,indices_phase.IPO_neutralR3_DJF,indices_phase.ENSO_posR3_DJF,\
       "","/composite/"+num+"/rainfall/R3/DJF/4","/composite/"+num+"/rainfall_anomalies/R3/DJF/4")
output(access_trimmed.trim_DJF,indices_phase.IPO_neutralR3_DJF,indices_phase.ENSO_neutralR3_DJF,\
       "","/composite/"+num+"/rainfall/R3/DJF/5","/composite/"+num+"/rainfall_anomalies/R3/DJF/5")
output(access_trimmed.trim_DJF,indices_phase.IPO_neutralR3_DJF,indices_phase.ENSO_negR3_DJF,\
       "","/composite/"+num+"/rainfall/R3/DJF/6","/composite/"+num+"/rainfall_anomalies/R3/DJF/6")
output(access_trimmed.trim_DJF,indices_phase.IPO_negR3_DJF,indices_phase.ENSO_posR3_DJF,\
       "","/composite/"+num+"/rainfall/R3/DJF/7","/composite/"+num+"/rainfall_anomalies/R3/DJF/7")
output(access_trimmed.trim_DJF,indices_phase.IPO_negR3_DJF,indices_phase.ENSO_neutralR3_DJF,\
       "","/composite/"+num+"/rainfall/R3/DJF/8","/composite/"+num+"/rainfall_anomalies/R3/DJF/8")
output(access_trimmed.trim_DJF,indices_phase.IPO_negR3_DJF,indices_phase.ENSO_negR3_DJF,\
       "","/composite/"+num+"/rainfall/R3/DJF/9","/composite/"+num+"/rainfall_anomalies/R3/DJF/9")

ACCESS_DJF = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/DJF/*.png",3,3,title=(r'ACCESS1.3 R3 DJF: mean rainfall'))
ACCESS_DJF_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/DJF/*.png",3,3,title=(r'ACCESS1.3 R3 DJF: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_DJF,"","composite/"+num+"_compiled/R3/ACCESS_DJF")
maps_sub.saveFig(ACCESS_DJF_Anom,"","composite/"+num+"_compiled/R3/ACCESS_DJF_Anom")


#ACCESS R3: MAM

output(access_trimmed.trim_MAM,indices_phase.IPO_posR3_MAM,indices_phase.ENSO_posR3_MAM,\
       "","/composite/"+num+"/rainfall/R3/MAM/1","/composite/"+num+"/rainfall_anomalies/R3/MAM/1")
output(access_trimmed.trim_MAM,indices_phase.IPO_posR3_MAM,indices_phase.ENSO_neutralR3_MAM,\
       "","/composite/"+num+"/rainfall/R3/MAM/2","/composite/"+num+"/rainfall_anomalies/R3/MAM/2")
output(access_trimmed.trim_MAM,indices_phase.IPO_posR3_MAM,indices_phase.ENSO_negR3_MAM,\
       "","/composite/"+num+"/rainfall/R3/MAM/3","/composite/"+num+"/rainfall_anomalies/R3/MAM/3")
output(access_trimmed.trim_MAM,indices_phase.IPO_neutralR3_MAM,indices_phase.ENSO_posR3_MAM,\
       "","/composite/"+num+"/rainfall/R3/MAM/4","/composite/"+num+"/rainfall_anomalies/R3/MAM/4")
output(access_trimmed.trim_MAM,indices_phase.IPO_neutralR3_MAM,indices_phase.ENSO_neutralR3_MAM,\
       "","/composite/"+num+"/rainfall/R3/MAM/5","/composite/"+num+"/rainfall_anomalies/R3/MAM/5")
output(access_trimmed.trim_MAM,indices_phase.IPO_neutralR3_MAM,indices_phase.ENSO_negR3_MAM,\
       "","/composite/"+num+"/rainfall/R3/MAM/6","/composite/"+num+"/rainfall_anomalies/R3/MAM/6")
output(access_trimmed.trim_MAM,indices_phase.IPO_negR3_MAM,indices_phase.ENSO_posR3_MAM,\
       "","/composite/"+num+"/rainfall/R3/MAM/7","/composite/"+num+"/rainfall_anomalies/R3/MAM/7")
output(access_trimmed.trim_MAM,indices_phase.IPO_negR3_MAM,indices_phase.ENSO_neutralR3_MAM,\
       "","/composite/"+num+"/rainfall/R3/MAM/8","/composite/"+num+"/rainfall_anomalies/R3/MAM/8")
output(access_trimmed.trim_MAM,indices_phase.IPO_negR3_MAM,indices_phase.ENSO_negR3_MAM,\
       "","/composite/"+num+"/rainfall/R3/MAM/9","/composite/"+num+"/rainfall_anomalies/R3/MAM/9")

ACCESS_MAM = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/MAM/*.png",3,3,title=(r'ACCESS1.3 R3 MAM: mean rainfall'))
ACCESS_MAM_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/MAM/*.png",3,3,title=(r'ACCESS1.3 R3 MAM: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_MAM,"","composite/"+num+"_compiled/R3/ACCESS_MAM")
maps_sub.saveFig(ACCESS_MAM_Anom,"","composite/"+num+"_compiled/R3/ACCESS_MAM_Anom")


#ACCESS R3: annual

output(access_trimmed.trim_Annual,indices_phase.IPO_posR3_annual,indices_phase.ENSO_posR3_annual,\
       "","/composite/"+num+"/rainfall/R3/Annual/1","/composite/"+num+"/rainfall_anomalies/R3/Annual/1")
output(access_trimmed.trim_Annual,indices_phase.IPO_posR3_annual,indices_phase.ENSO_neutralR3_annual,\
       "","/composite/"+num+"/rainfall/R3/Annual/2","/composite/"+num+"/rainfall_anomalies/R3/Annual/2")
output(access_trimmed.trim_Annual,indices_phase.IPO_posR3_annual,indices_phase.ENSO_negR3_annual,\
       "","/composite/"+num+"/rainfall/R3/Annual/3","/composite/"+num+"/rainfall_anomalies/R3/Annual/3")
output(access_trimmed.trim_Annual,indices_phase.IPO_neutralR3_annual,indices_phase.ENSO_posR3_annual,\
       "","/composite/"+num+"/rainfall/R3/Annual/4","/composite/"+num+"/rainfall_anomalies/R3/Annual/4")
output(access_trimmed.trim_Annual,indices_phase.IPO_neutralR3_annual,indices_phase.ENSO_neutralR3_annual,\
       "","/composite/"+num+"/rainfall/R3/Annual/5","/composite/"+num+"/rainfall_anomalies/R3/Annual/5")
output(access_trimmed.trim_Annual,indices_phase.IPO_neutralR3_annual,indices_phase.ENSO_negR3_annual,\
       "","/composite/"+num+"/rainfall/R3/Annual/6","/composite/"+num+"/rainfall_anomalies/R3/Annual/6")
output(access_trimmed.trim_Annual,indices_phase.IPO_negR3_annual,indices_phase.ENSO_posR3_annual,\
       "","/composite/"+num+"/rainfall/R3/Annual/7","/composite/"+num+"/rainfall_anomalies/R3/Annual/7")
output(access_trimmed.trim_Annual,indices_phase.IPO_negR3_annual,indices_phase.ENSO_neutralR3_annual,\
       "","/composite/"+num+"/rainfall/R3/Annual/8","/composite/"+num+"/rainfall_anomalies/R3/Annual/8")
output(access_trimmed.trim_Annual,indices_phase.IPO_negR3_annual,indices_phase.ENSO_negR3_annual,\
       "","/composite/"+num+"/rainfall/R3/Annual/9","/composite/"+num+"/rainfall_anomalies/R3/Annual/9")

ACCESS_annual = multi("my_coding_routines/images/composite/"+num+"/rainfall/R3/Annual/*.png",3,3,title=(r'ACCESS1.3 R3 annual: mean rainfall'))
ACCESS_annual_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/R3/Annual/*.png",3,3,title=(r'ACCESS1.3 R3 annual: mean rainfall anomalies'))
maps_sub.saveFig(ACCESS_annual,"","composite/"+num+"_compiled/R3/ACCESS_annual")
maps_sub.saveFig(ACCESS_annual_Anom,"","composite/"+num+"_compiled/R3/ACCESS_annual_Anom")

