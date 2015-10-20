"""
Code which stratifies ENSO/IPO and AWAP rainfall data
for composite analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 19 October 2015.
"""
from composite import *
import indices_phase
import awap_prepare
import access_trimmed

#Change as required to "1_sd", "2_sd", "3_sd"
num = "1_sd"
sigma = '' # r' (2 $\sigma$)'  r' (3 $\sigma$)'

#AWAP: June

output(awap_prepare.awap_June,indices_phase.IPO_posHad_Jun,indices_phase.ENSO_posHad_Jun,\
       "","/composite/"+num+"/rainfall/AWAP/June/1","/composite/"+num+"/rainfall_anomalies/AWAP/June/1")
output(awap_prepare.awap_June,indices_phase.IPO_posHad_Jun,indices_phase.ENSO_neutralHad_Jun,\
       "","/composite/"+num+"/rainfall/AWAP/June/2","/composite/"+num+"/rainfall_anomalies/AWAP/June/2")
output(awap_prepare.awap_June,indices_phase.IPO_posHad_Jun,indices_phase.ENSO_negHad_Jun,\
       "","/composite/"+num+"/rainfall/AWAP/June/3","/composite/"+num+"/rainfall_anomalies/AWAP/June/3")
output(awap_prepare.awap_June,indices_phase.IPO_neutralHad_Jun,indices_phase.ENSO_posHad_Jun,\
       "","/composite/"+num+"/rainfall/AWAP/June/4","/composite/"+num+"/rainfall_anomalies/AWAP/June/4")
output(awap_prepare.awap_June,indices_phase.IPO_neutralHad_Jun,indices_phase.ENSO_neutralHad_Jun,\
       "","/composite/"+num+"/rainfall/AWAP/June/5","/composite/"+num+"/rainfall_anomalies/AWAP/June/5")
output(awap_prepare.awap_June,indices_phase.IPO_neutralHad_Jun,indices_phase.ENSO_negHad_Jun,\
       "","/composite/"+num+"/rainfall/AWAP/June/6","/composite/"+num+"/rainfall_anomalies/AWAP/June/6")
output(awap_prepare.awap_June,indices_phase.IPO_negHad_Jun,indices_phase.ENSO_posHad_Jun,\
       "","/composite/"+num+"/rainfall/AWAP/June/7","/composite/"+num+"/rainfall_anomalies/AWAP/June/7")
output(awap_prepare.awap_June,indices_phase.IPO_negHad_Jun,indices_phase.ENSO_neutralHad_Jun,\
       "","/composite/"+num+"/rainfall/AWAP/June/8","/composite/"+num+"/rainfall_anomalies/AWAP/June/8")
output(awap_prepare.awap_June,indices_phase.IPO_negHad_Jun,indices_phase.ENSO_negHad_Jun,\
       "","/composite/"+num+"/rainfall/AWAP/June/9","/composite/"+num+"/rainfall_anomalies/AWAP/June/9")

AWAP_June = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/June/*.png",3,3,title=(r'AWAP June: mean rainfall'+sigma))
AWAP_June_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/June/*.png",3,3,title=(r'AWAP June: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_June,"","composite/"+num+"_compiled/AWAP/AWAP_June")
maps_sub.saveFig(AWAP_June_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_June_Anom")


#AWAP: July

output(awap_prepare.awap_July,indices_phase.IPO_posHad_Jul,indices_phase.ENSO_posHad_Jul,\
       "","/composite/"+num+"/rainfall/AWAP/July/1","/composite/"+num+"/rainfall_anomalies/AWAP/July/1")
output(awap_prepare.awap_July,indices_phase.IPO_posHad_Jul,indices_phase.ENSO_neutralHad_Jul,\
       "","/composite/"+num+"/rainfall/AWAP/July/2","/composite/"+num+"/rainfall_anomalies/AWAP/July/2")
output(awap_prepare.awap_July,indices_phase.IPO_posHad_Jul,indices_phase.ENSO_negHad_Jul,\
       "","/composite/"+num+"/rainfall/AWAP/July/3","/composite/"+num+"/rainfall_anomalies/AWAP/July/3")
output(awap_prepare.awap_July,indices_phase.IPO_neutralHad_Jul,indices_phase.ENSO_posHad_Jul,\
       "","/composite/"+num+"/rainfall/AWAP/July/4","/composite/"+num+"/rainfall_anomalies/AWAP/July/4")
output(awap_prepare.awap_July,indices_phase.IPO_neutralHad_Jul,indices_phase.ENSO_neutralHad_Jul,\
       "","/composite/"+num+"/rainfall/AWAP/July/5","/composite/"+num+"/rainfall_anomalies/AWAP/July/5")
output(awap_prepare.awap_July,indices_phase.IPO_neutralHad_Jul,indices_phase.ENSO_negHad_Jul,\
       "","/composite/"+num+"/rainfall/AWAP/July/6","/composite/"+num+"/rainfall_anomalies/AWAP/July/6")
output(awap_prepare.awap_July,indices_phase.IPO_negHad_Jul,indices_phase.ENSO_posHad_Jul,\
       "","/composite/"+num+"/rainfall/AWAP/July/7","/composite/"+num+"/rainfall_anomalies/AWAP/July/7")
output(awap_prepare.awap_July,indices_phase.IPO_negHad_Jul,indices_phase.ENSO_neutralHad_Jul,\
       "","/composite/"+num+"/rainfall/AWAP/July/8","/composite/"+num+"/rainfall_anomalies/AWAP/July/8")
output(awap_prepare.awap_July,indices_phase.IPO_negHad_Jul,indices_phase.ENSO_negHad_Jul,\
       "","/composite/"+num+"/rainfall/AWAP/July/9","/composite/"+num+"/rainfall_anomalies/AWAP/July/9")

AWAP_July = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/July/*.png",3,3,title=(r'AWAP July: mean rainfall'+sigma))
AWAP_July_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/July/*.png",3,3,title=(r'AWAP July: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_July,"","composite/"+num+"_compiled/AWAP/AWAP_July")
maps_sub.saveFig(AWAP_July_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_July_Anom")


#AWAP: August

output(awap_prepare.awap_August,indices_phase.IPO_posHad_Aug,indices_phase.ENSO_posHad_Aug,\
       "","/composite/"+num+"/rainfall/AWAP/August/1","/composite/"+num+"/rainfall_anomalies/AWAP/August/1")
output(awap_prepare.awap_August,indices_phase.IPO_posHad_Aug,indices_phase.ENSO_neutralHad_Aug,\
       "","/composite/"+num+"/rainfall/AWAP/August/2","/composite/"+num+"/rainfall_anomalies/AWAP/August/2")
output(awap_prepare.awap_August,indices_phase.IPO_posHad_Aug,indices_phase.ENSO_negHad_Aug,\
       "","/composite/"+num+"/rainfall/AWAP/August/3","/composite/"+num+"/rainfall_anomalies/AWAP/August/3")
output(awap_prepare.awap_August,indices_phase.IPO_neutralHad_Aug,indices_phase.ENSO_posHad_Aug,\
       "","/composite/"+num+"/rainfall/AWAP/August/4","/composite/"+num+"/rainfall_anomalies/AWAP/August/4")
output(awap_prepare.awap_August,indices_phase.IPO_neutralHad_Aug,indices_phase.ENSO_neutralHad_Aug,\
       "","/composite/"+num+"/rainfall/AWAP/August/5","/composite/"+num+"/rainfall_anomalies/AWAP/August/5")
output(awap_prepare.awap_August,indices_phase.IPO_neutralHad_Aug,indices_phase.ENSO_negHad_Aug,\
       "","/composite/"+num+"/rainfall/AWAP/August/6","/composite/"+num+"/rainfall_anomalies/AWAP/August/6")
output(awap_prepare.awap_August,indices_phase.IPO_negHad_Aug,indices_phase.ENSO_posHad_Aug,\
       "","/composite/"+num+"/rainfall/AWAP/August/7","/composite/"+num+"/rainfall_anomalies/AWAP/August/7")
output(awap_prepare.awap_August,indices_phase.IPO_negHad_Aug,indices_phase.ENSO_neutralHad_Aug,\
       "","/composite/"+num+"/rainfall/AWAP/August/8","/composite/"+num+"/rainfall_anomalies/AWAP/August/8")
output(awap_prepare.awap_August,indices_phase.IPO_negHad_Aug,indices_phase.ENSO_negHad_Aug,\
       "","/composite/"+num+"/rainfall/AWAP/August/9","/composite/"+num+"/rainfall_anomalies/AWAP/August/9")

AWAP_August = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/August/*.png",3,3,title=(r'AWAP August: mean rainfall'+sigma))
AWAP_August_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/August/*.png",3,3,title=(r'AWAP August: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_August,"","composite/"+num+"_compiled/AWAP/AWAP_August")
maps_sub.saveFig(AWAP_August_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_August_Anom")


#AWAP: September

output(awap_prepare.awap_September,indices_phase.IPO_posHad_Sep,indices_phase.ENSO_posHad_Sep,\
       "","/composite/"+num+"/rainfall/AWAP/September/1","/composite/"+num+"/rainfall_anomalies/AWAP/September/1")
output(awap_prepare.awap_September,indices_phase.IPO_posHad_Sep,indices_phase.ENSO_neutralHad_Sep,\
       "","/composite/"+num+"/rainfall/AWAP/September/2","/composite/"+num+"/rainfall_anomalies/AWAP/September/2")
output(awap_prepare.awap_September,indices_phase.IPO_posHad_Sep,indices_phase.ENSO_negHad_Sep,\
       "","/composite/"+num+"/rainfall/AWAP/September/3","/composite/"+num+"/rainfall_anomalies/AWAP/September/3")
output(awap_prepare.awap_September,indices_phase.IPO_neutralHad_Sep,indices_phase.ENSO_posHad_Sep,\
       "","/composite/"+num+"/rainfall/AWAP/September/4","/composite/"+num+"/rainfall_anomalies/AWAP/September/4")
output(awap_prepare.awap_September,indices_phase.IPO_neutralHad_Sep,indices_phase.ENSO_neutralHad_Sep,\
       "","/composite/"+num+"/rainfall/AWAP/September/5","/composite/"+num+"/rainfall_anomalies/AWAP/September/5")
output(awap_prepare.awap_September,indices_phase.IPO_neutralHad_Sep,indices_phase.ENSO_negHad_Sep,\
       "","/composite/"+num+"/rainfall/AWAP/September/6","/composite/"+num+"/rainfall_anomalies/AWAP/September/6")
output(awap_prepare.awap_September,indices_phase.IPO_negHad_Sep,indices_phase.ENSO_posHad_Sep,\
       "","/composite/"+num+"/rainfall/AWAP/September/7","/composite/"+num+"/rainfall_anomalies/AWAP/September/7")
output(awap_prepare.awap_September,indices_phase.IPO_negHad_Sep,indices_phase.ENSO_neutralHad_Sep,\
       "","/composite/"+num+"/rainfall/AWAP/September/8","/composite/"+num+"/rainfall_anomalies/AWAP/September/8")
output(awap_prepare.awap_September,indices_phase.IPO_negHad_Sep,indices_phase.ENSO_negHad_Sep,\
       "","/composite/"+num+"/rainfall/AWAP/September/9","/composite/"+num+"/rainfall_anomalies/AWAP/September/9")

AWAP_September = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/September/*.png",3,3,title=(r'AWAP September: mean rainfall'+sigma))
AWAP_September_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/September/*.png",3,3,title=(r'AWAP September: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_September,"","composite/"+num+"_compiled/AWAP/AWAP_September")
maps_sub.saveFig(AWAP_September_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_September_Anom")


#AWAP: October

output(awap_prepare.awap_October,indices_phase.IPO_posHad_Oct,indices_phase.ENSO_posHad_Oct,\
       "","/composite/"+num+"/rainfall/AWAP/October/1","/composite/"+num+"/rainfall_anomalies/AWAP/October/1")
output(awap_prepare.awap_October,indices_phase.IPO_posHad_Oct,indices_phase.ENSO_neutralHad_Oct,\
       "","/composite/"+num+"/rainfall/AWAP/October/2","/composite/"+num+"/rainfall_anomalies/AWAP/October/2")
output(awap_prepare.awap_October,indices_phase.IPO_posHad_Oct,indices_phase.ENSO_negHad_Oct,\
       "","/composite/"+num+"/rainfall/AWAP/October/3","/composite/"+num+"/rainfall_anomalies/AWAP/October/3")
output(awap_prepare.awap_October,indices_phase.IPO_neutralHad_Oct,indices_phase.ENSO_posHad_Oct,\
       "","/composite/"+num+"/rainfall/AWAP/October/4","/composite/"+num+"/rainfall_anomalies/AWAP/October/4")
output(awap_prepare.awap_October,indices_phase.IPO_neutralHad_Oct,indices_phase.ENSO_neutralHad_Oct,\
       "","/composite/"+num+"/rainfall/AWAP/October/5","/composite/"+num+"/rainfall_anomalies/AWAP/October/5")
output(awap_prepare.awap_October,indices_phase.IPO_neutralHad_Oct,indices_phase.ENSO_negHad_Oct,\
       "","/composite/"+num+"/rainfall/AWAP/October/6","/composite/"+num+"/rainfall_anomalies/AWAP/October/6")
output(awap_prepare.awap_October,indices_phase.IPO_negHad_Oct,indices_phase.ENSO_posHad_Oct,\
       "","/composite/"+num+"/rainfall/AWAP/October/7","/composite/"+num+"/rainfall_anomalies/AWAP/October/7")
output(awap_prepare.awap_October,indices_phase.IPO_negHad_Oct,indices_phase.ENSO_neutralHad_Oct,\
       "","/composite/"+num+"/rainfall/AWAP/October/8","/composite/"+num+"/rainfall_anomalies/AWAP/October/8")
output(awap_prepare.awap_October,indices_phase.IPO_negHad_Oct,indices_phase.ENSO_negHad_Oct,\
       "","/composite/"+num+"/rainfall/AWAP/October/9","/composite/"+num+"/rainfall_anomalies/AWAP/October/9")

AWAP_October = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/October/*.png",3,3,title=(r'AWAP October: mean rainfall'+sigma))
AWAP_October_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/October/*.png",3,3,title=(r'AWAP October: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_October,"","composite/"+num+"_compiled/AWAP/AWAP_October")
maps_sub.saveFig(AWAP_October_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_October_Anom")


#AWAP: November

output(awap_prepare.awap_November,indices_phase.IPO_posHad_Nov,indices_phase.ENSO_posHad_Nov,\
       "","/composite/"+num+"/rainfall/AWAP/November/1","/composite/"+num+"/rainfall_anomalies/AWAP/November/1")
output(awap_prepare.awap_November,indices_phase.IPO_posHad_Nov,indices_phase.ENSO_neutralHad_Nov,\
       "","/composite/"+num+"/rainfall/AWAP/November/2","/composite/"+num+"/rainfall_anomalies/AWAP/November/2")
output(awap_prepare.awap_November,indices_phase.IPO_posHad_Nov,indices_phase.ENSO_negHad_Nov,\
       "","/composite/"+num+"/rainfall/AWAP/November/3","/composite/"+num+"/rainfall_anomalies/AWAP/November/3")
output(awap_prepare.awap_November,indices_phase.IPO_neutralHad_Nov,indices_phase.ENSO_posHad_Nov,\
       "","/composite/"+num+"/rainfall/AWAP/November/4","/composite/"+num+"/rainfall_anomalies/AWAP/November/4")
output(awap_prepare.awap_November,indices_phase.IPO_neutralHad_Nov,indices_phase.ENSO_neutralHad_Nov,\
       "","/composite/"+num+"/rainfall/AWAP/November/5","/composite/"+num+"/rainfall_anomalies/AWAP/November/5")
output(awap_prepare.awap_November,indices_phase.IPO_neutralHad_Nov,indices_phase.ENSO_negHad_Nov,\
       "","/composite/"+num+"/rainfall/AWAP/November/6","/composite/"+num+"/rainfall_anomalies/AWAP/November/6")
output(awap_prepare.awap_November,indices_phase.IPO_negHad_Nov,indices_phase.ENSO_posHad_Nov,\
       "","/composite/"+num+"/rainfall/AWAP/November/7","/composite/"+num+"/rainfall_anomalies/AWAP/November/7")
output(awap_prepare.awap_November,indices_phase.IPO_negHad_Nov,indices_phase.ENSO_neutralHad_Nov,\
       "","/composite/"+num+"/rainfall/AWAP/November/8","/composite/"+num+"/rainfall_anomalies/AWAP/November/8")
output(awap_prepare.awap_November,indices_phase.IPO_negHad_Nov,indices_phase.ENSO_negHad_Nov,\
       "","/composite/"+num+"/rainfall/AWAP/November/9","/composite/"+num+"/rainfall_anomalies/AWAP/November/9")

AWAP_November = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/November/*.png",3,3,title=(r'AWAP November: mean rainfall'+sigma))
AWAP_November_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/November/*.png",3,3,title=(r'AWAP November: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_November,"","composite/"+num+"_compiled/AWAP/AWAP_November")
maps_sub.saveFig(AWAP_November_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_November_Anom")


#AWAP: December

output(awap_prepare.awap_December,indices_phase.IPO_posHad_Dec,indices_phase.ENSO_posHad_Dec,\
       "","/composite/"+num+"/rainfall/AWAP/December/1","/composite/"+num+"/rainfall_anomalies/AWAP/December/1")
output(awap_prepare.awap_December,indices_phase.IPO_posHad_Dec,indices_phase.ENSO_neutralHad_Dec,\
       "","/composite/"+num+"/rainfall/AWAP/December/2","/composite/"+num+"/rainfall_anomalies/AWAP/December/2")
output(awap_prepare.awap_December,indices_phase.IPO_posHad_Dec,indices_phase.ENSO_negHad_Dec,\
       "","/composite/"+num+"/rainfall/AWAP/December/3","/composite/"+num+"/rainfall_anomalies/AWAP/December/3")
output(awap_prepare.awap_December,indices_phase.IPO_neutralHad_Dec,indices_phase.ENSO_posHad_Dec,\
       "","/composite/"+num+"/rainfall/AWAP/December/4","/composite/"+num+"/rainfall_anomalies/AWAP/December/4")
output(awap_prepare.awap_December,indices_phase.IPO_neutralHad_Dec,indices_phase.ENSO_neutralHad_Dec,\
       "","/composite/"+num+"/rainfall/AWAP/December/5","/composite/"+num+"/rainfall_anomalies/AWAP/December/5")
output(awap_prepare.awap_December,indices_phase.IPO_neutralHad_Dec,indices_phase.ENSO_negHad_Dec,\
       "","/composite/"+num+"/rainfall/AWAP/December/6","/composite/"+num+"/rainfall_anomalies/AWAP/December/6")
output(awap_prepare.awap_December,indices_phase.IPO_negHad_Dec,indices_phase.ENSO_posHad_Dec,\
       "","/composite/"+num+"/rainfall/AWAP/December/7","/composite/"+num+"/rainfall_anomalies/AWAP/December/7")
output(awap_prepare.awap_December,indices_phase.IPO_negHad_Dec,indices_phase.ENSO_neutralHad_Dec,\
       "","/composite/"+num+"/rainfall/AWAP/December/8","/composite/"+num+"/rainfall_anomalies/AWAP/December/8")
output(awap_prepare.awap_December,indices_phase.IPO_negHad_Dec,indices_phase.ENSO_negHad_Dec,\
       "","/composite/"+num+"/rainfall/AWAP/December/9","/composite/"+num+"/rainfall_anomalies/AWAP/December/9")

AWAP_December = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/December/*.png",3,3,title=(r'AWAP December: mean rainfall'+sigma))
AWAP_December_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/December/*.png",3,3,title=(r'AWAP December: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_December,"","composite/"+num+"_compiled/AWAP/AWAP_December")
maps_sub.saveFig(AWAP_December_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_December_Anom")


#AWAP: January

output(awap_prepare.awap_January,indices_phase.IPO_posHad_Jan,indices_phase.ENSO_posHad_Jan,\
       "","/composite/"+num+"/rainfall/AWAP/January/1","/composite/"+num+"/rainfall_anomalies/AWAP/January/1")
output(awap_prepare.awap_January,indices_phase.IPO_posHad_Jan,indices_phase.ENSO_neutralHad_Jan,\
       "","/composite/"+num+"/rainfall/AWAP/January/2","/composite/"+num+"/rainfall_anomalies/AWAP/January/2")
output(awap_prepare.awap_January,indices_phase.IPO_posHad_Jan,indices_phase.ENSO_negHad_Jan,\
       "","/composite/"+num+"/rainfall/AWAP/January/3","/composite/"+num+"/rainfall_anomalies/AWAP/January/3")
output(awap_prepare.awap_January,indices_phase.IPO_neutralHad_Jan,indices_phase.ENSO_posHad_Jan,\
       "","/composite/"+num+"/rainfall/AWAP/January/4","/composite/"+num+"/rainfall_anomalies/AWAP/January/4")
output(awap_prepare.awap_January,indices_phase.IPO_neutralHad_Jan,indices_phase.ENSO_neutralHad_Jan,\
       "","/composite/"+num+"/rainfall/AWAP/January/5","/composite/"+num+"/rainfall_anomalies/AWAP/January/5")
output(awap_prepare.awap_January,indices_phase.IPO_neutralHad_Jan,indices_phase.ENSO_negHad_Jan,\
       "","/composite/"+num+"/rainfall/AWAP/January/6","/composite/"+num+"/rainfall_anomalies/AWAP/January/6")
output(awap_prepare.awap_January,indices_phase.IPO_negHad_Jan,indices_phase.ENSO_posHad_Jan,\
       "","/composite/"+num+"/rainfall/AWAP/January/7","/composite/"+num+"/rainfall_anomalies/AWAP/January/7")
output(awap_prepare.awap_January,indices_phase.IPO_negHad_Jan,indices_phase.ENSO_neutralHad_Jan,\
       "","/composite/"+num+"/rainfall/AWAP/January/8","/composite/"+num+"/rainfall_anomalies/AWAP/January/8")
output(awap_prepare.awap_January,indices_phase.IPO_negHad_Jan,indices_phase.ENSO_negHad_Jan,\
       "","/composite/"+num+"/rainfall/AWAP/January/9","/composite/"+num+"/rainfall_anomalies/AWAP/January/9")

AWAP_January = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/January/*.png",3,3,title=(r'AWAP January: mean rainfall'+sigma))
AWAP_January_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/January/*.png",3,3,title=(r'AWAP January: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_January,"","composite/"+num+"_compiled/AWAP/AWAP_January")
maps_sub.saveFig(AWAP_January_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_January_Anom")


#AWAP: February

output(awap_prepare.awap_February,indices_phase.IPO_posHad_Feb,indices_phase.ENSO_posHad_Feb,\
       "","/composite/"+num+"/rainfall/AWAP/February/1","/composite/"+num+"/rainfall_anomalies/AWAP/February/1")
output(awap_prepare.awap_February,indices_phase.IPO_posHad_Feb,indices_phase.ENSO_neutralHad_Feb,\
       "","/composite/"+num+"/rainfall/AWAP/February/2","/composite/"+num+"/rainfall_anomalies/AWAP/February/2")
output(awap_prepare.awap_February,indices_phase.IPO_posHad_Feb,indices_phase.ENSO_negHad_Feb,\
       "","/composite/"+num+"/rainfall/AWAP/February/3","/composite/"+num+"/rainfall_anomalies/AWAP/February/3")
output(awap_prepare.awap_February,indices_phase.IPO_neutralHad_Feb,indices_phase.ENSO_posHad_Feb,\
       "","/composite/"+num+"/rainfall/AWAP/February/4","/composite/"+num+"/rainfall_anomalies/AWAP/February/4")
output(awap_prepare.awap_February,indices_phase.IPO_neutralHad_Feb,indices_phase.ENSO_neutralHad_Feb,\
       "","/composite/"+num+"/rainfall/AWAP/February/5","/composite/"+num+"/rainfall_anomalies/AWAP/February/5")
output(awap_prepare.awap_February,indices_phase.IPO_neutralHad_Feb,indices_phase.ENSO_negHad_Feb,\
       "","/composite/"+num+"/rainfall/AWAP/February/6","/composite/"+num+"/rainfall_anomalies/AWAP/February/6")
output(awap_prepare.awap_February,indices_phase.IPO_negHad_Feb,indices_phase.ENSO_posHad_Feb,\
       "","/composite/"+num+"/rainfall/AWAP/February/7","/composite/"+num+"/rainfall_anomalies/AWAP/February/7")
output(awap_prepare.awap_February,indices_phase.IPO_negHad_Feb,indices_phase.ENSO_neutralHad_Feb,\
       "","/composite/"+num+"/rainfall/AWAP/February/8","/composite/"+num+"/rainfall_anomalies/AWAP/February/8")
output(awap_prepare.awap_February,indices_phase.IPO_negHad_Feb,indices_phase.ENSO_negHad_Feb,\
       "","/composite/"+num+"/rainfall/AWAP/February/9","/composite/"+num+"/rainfall_anomalies/AWAP/February/9")

AWAP_February = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/February/*.png",3,3,title=(r'AWAP February: mean rainfall'+sigma))
AWAP_February_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/February/*.png",3,3,title=(r'AWAP February: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_February,"","composite/"+num+"_compiled/AWAP/AWAP_February")
maps_sub.saveFig(AWAP_February_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_February_Anom")

"""
#AWAP: March

output(awap_prepare.awap_March,indices_phase.IPO_posHad_Mar,indices_phase.ENSO_posHad_Mar,\
       "","/composite/"+num+"/rainfall/AWAP/March/1","/composite/"+num+"/rainfall_anomalies/AWAP/March/1")
output(awap_prepare.awap_March,indices_phase.IPO_posHad_Mar,indices_phase.ENSO_neutralHad_Mar,\
       "","/composite/"+num+"/rainfall/AWAP/March/2","/composite/"+num+"/rainfall_anomalies/AWAP/March/2")
output(awap_prepare.awap_March,indices_phase.IPO_posHad_Mar,indices_phase.ENSO_negHad_Mar,\
       "","/composite/"+num+"/rainfall/AWAP/March/3","/composite/"+num+"/rainfall_anomalies/AWAP/March/3")
output(awap_prepare.awap_March,indices_phase.IPO_neutralHad_Mar,indices_phase.ENSO_posHad_Mar,\
       "","/composite/"+num+"/rainfall/AWAP/March/4","/composite/"+num+"/rainfall_anomalies/AWAP/March/4")
output(awap_prepare.awap_March,indices_phase.IPO_neutralHad_Mar,indices_phase.ENSO_neutralHad_Mar,\
       "","/composite/"+num+"/rainfall/AWAP/March/5","/composite/"+num+"/rainfall_anomalies/AWAP/March/5")
output(awap_prepare.awap_March,indices_phase.IPO_neutralHad_Mar,indices_phase.ENSO_negHad_Mar,\
       "","/composite/"+num+"/rainfall/AWAP/March/6","/composite/"+num+"/rainfall_anomalies/AWAP/March/6")
output(awap_prepare.awap_March,indices_phase.IPO_negHad_Mar,indices_phase.ENSO_posHad_Mar,\
       "","/composite/"+num+"/rainfall/AWAP/March/7","/composite/"+num+"/rainfall_anomalies/AWAP/March/7")
output(awap_prepare.awap_March,indices_phase.IPO_negHad_Mar,indices_phase.ENSO_neutralHad_Mar,\
       "","/composite/"+num+"/rainfall/AWAP/March/8","/composite/"+num+"/rainfall_anomalies/AWAP/March/8")
output(awap_prepare.awap_March,indices_phase.IPO_negHad_Mar,indices_phase.ENSO_negHad_Mar,\
       "","/composite/"+num+"/rainfall/AWAP/March/9","/composite/"+num+"/rainfall_anomalies/AWAP/March/9")

AWAP_March = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/March/*.png",3,3,title=(r'AWAP March: mean rainfall'+sigma))
AWAP_March_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/March/*.png",3,3,title=(r'AWAP March: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_March,"","composite/"+num+"_compiled/AWAP/AWAP_March")
maps_sub.saveFig(AWAP_March_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_March_Anom")


#AWAP: April

output(awap_prepare.awap_April,indices_phase.IPO_posHad_Apr,indices_phase.ENSO_posHad_Apr,\
       "","/composite/"+num+"/rainfall/AWAP/April/1","/composite/"+num+"/rainfall_anomalies/AWAP/April/1")
output(awap_prepare.awap_April,indices_phase.IPO_posHad_Apr,indices_phase.ENSO_neutralHad_Apr,\
       "","/composite/"+num+"/rainfall/AWAP/April/2","/composite/"+num+"/rainfall_anomalies/AWAP/April/2")
output(awap_prepare.awap_April,indices_phase.IPO_posHad_Apr,indices_phase.ENSO_negHad_Apr,\
       "","/composite/"+num+"/rainfall/AWAP/April/3","/composite/"+num+"/rainfall_anomalies/AWAP/April/3")
output(awap_prepare.awap_April,indices_phase.IPO_neutralHad_Apr,indices_phase.ENSO_posHad_Apr,\
       "","/composite/"+num+"/rainfall/AWAP/April/4","/composite/"+num+"/rainfall_anomalies/AWAP/April/4")
output(awap_prepare.awap_April,indices_phase.IPO_neutralHad_Apr,indices_phase.ENSO_neutralHad_Apr,\
       "","/composite/"+num+"/rainfall/AWAP/April/5","/composite/"+num+"/rainfall_anomalies/AWAP/April/5")
output(awap_prepare.awap_April,indices_phase.IPO_neutralHad_Apr,indices_phase.ENSO_negHad_Apr,\
       "","/composite/"+num+"/rainfall/AWAP/April/6","/composite/"+num+"/rainfall_anomalies/AWAP/April/6")
output(awap_prepare.awap_April,indices_phase.IPO_negHad_Apr,indices_phase.ENSO_posHad_Apr,\
       "","/composite/"+num+"/rainfall/AWAP/April/7","/composite/"+num+"/rainfall_anomalies/AWAP/April/7")
output(awap_prepare.awap_April,indices_phase.IPO_negHad_Apr,indices_phase.ENSO_neutralHad_Apr,\
       "","/composite/"+num+"/rainfall/AWAP/April/8","/composite/"+num+"/rainfall_anomalies/AWAP/April/8")
output(awap_prepare.awap_April,indices_phase.IPO_negHad_Apr,indices_phase.ENSO_negHad_Apr,\
       "","/composite/"+num+"/rainfall/AWAP/April/9","/composite/"+num+"/rainfall_anomalies/AWAP/April/9")

AWAP_April = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/April/*.png",3,3,title=(r'AWAP April: mean rainfall'+sigma))
AWAP_April_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/April/*.png",3,3,title=(r'AWAP April: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_April,"","composite/"+num+"_compiled/AWAP/AWAP_April")
maps_sub.saveFig(AWAP_April_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_April_Anom")


#AWAP: May

output(awap_prepare.awap_May,indices_phase.IPO_posHad_May,indices_phase.ENSO_posHad_May,\
       "","/composite/"+num+"/rainfall/AWAP/May/1","/composite/"+num+"/rainfall_anomalies/AWAP/May/1")
output(awap_prepare.awap_May,indices_phase.IPO_posHad_May,indices_phase.ENSO_neutralHad_May,\
       "","/composite/"+num+"/rainfall/AWAP/May/2","/composite/"+num+"/rainfall_anomalies/AWAP/May/2")
output(awap_prepare.awap_May,indices_phase.IPO_posHad_May,indices_phase.ENSO_negHad_May,\
       "","/composite/"+num+"/rainfall/AWAP/May/3","/composite/"+num+"/rainfall_anomalies/AWAP/May/3")
output(awap_prepare.awap_May,indices_phase.IPO_neutralHad_May,indices_phase.ENSO_posHad_May,\
       "","/composite/"+num+"/rainfall/AWAP/May/4","/composite/"+num+"/rainfall_anomalies/AWAP/May/4")
output(awap_prepare.awap_May,indices_phase.IPO_neutralHad_May,indices_phase.ENSO_neutralHad_May,\
       "","/composite/"+num+"/rainfall/AWAP/May/5","/composite/"+num+"/rainfall_anomalies/AWAP/May/5")
output(awap_prepare.awap_May,indices_phase.IPO_neutralHad_May,indices_phase.ENSO_negHad_May,\
       "","/composite/"+num+"/rainfall/AWAP/May/6","/composite/"+num+"/rainfall_anomalies/AWAP/May/6")
output(awap_prepare.awap_May,indices_phase.IPO_negHad_May,indices_phase.ENSO_posHad_May,\
       "","/composite/"+num+"/rainfall/AWAP/May/7","/composite/"+num+"/rainfall_anomalies/AWAP/May/7")
output(awap_prepare.awap_May,indices_phase.IPO_negHad_May,indices_phase.ENSO_neutralHad_May,\
       "","/composite/"+num+"/rainfall/AWAP/May/8","/composite/"+num+"/rainfall_anomalies/AWAP/May/8")
output(awap_prepare.awap_May,indices_phase.IPO_negHad_May,indices_phase.ENSO_negHad_May,\
       "","/composite/"+num+"/rainfall/AWAP/May/9","/composite/"+num+"/rainfall_anomalies/AWAP/May/9")

AWAP_May = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/May/*.png",3,3,title=(r'AWAP May: mean rainfall'+sigma))
AWAP_May_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/May/*.png",3,3,title=(r'AWAP May: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_May,"","composite/"+num+"_compiled/AWAP/AWAP_May")
maps_sub.saveFig(AWAP_May_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_May_Anom")


#AWAP: JJA

output(awap_prepare.awap_JJA,indices_phase.IPO_posHad_JJA,indices_phase.ENSO_posHad_JJA,\
       "","/composite/"+num+"/rainfall/AWAP/JJA/1","/composite/"+num+"/rainfall_anomalies/AWAP/JJA/1")
output(awap_prepare.awap_JJA,indices_phase.IPO_posHad_JJA,indices_phase.ENSO_neutralHad_JJA,\
       "","/composite/"+num+"/rainfall/AWAP/JJA/2","/composite/"+num+"/rainfall_anomalies/AWAP/JJA/2")
output(awap_prepare.awap_JJA,indices_phase.IPO_posHad_JJA,indices_phase.ENSO_negHad_JJA,\
       "","/composite/"+num+"/rainfall/AWAP/JJA/3","/composite/"+num+"/rainfall_anomalies/AWAP/JJA/3")
output(awap_prepare.awap_JJA,indices_phase.IPO_neutralHad_JJA,indices_phase.ENSO_posHad_JJA,\
       "","/composite/"+num+"/rainfall/AWAP/JJA/4","/composite/"+num+"/rainfall_anomalies/AWAP/JJA/4")
output(awap_prepare.awap_JJA,indices_phase.IPO_neutralHad_JJA,indices_phase.ENSO_neutralHad_JJA,\
       "","/composite/"+num+"/rainfall/AWAP/JJA/5","/composite/"+num+"/rainfall_anomalies/AWAP/JJA/5")
output(awap_prepare.awap_JJA,indices_phase.IPO_neutralHad_JJA,indices_phase.ENSO_negHad_JJA,\
       "","/composite/"+num+"/rainfall/AWAP/JJA/6","/composite/"+num+"/rainfall_anomalies/AWAP/JJA/6")
output(awap_prepare.awap_JJA,indices_phase.IPO_negHad_JJA,indices_phase.ENSO_posHad_JJA,\
       "","/composite/"+num+"/rainfall/AWAP/JJA/7","/composite/"+num+"/rainfall_anomalies/AWAP/JJA/7")
output(awap_prepare.awap_JJA,indices_phase.IPO_negHad_JJA,indices_phase.ENSO_neutralHad_JJA,\
       "","/composite/"+num+"/rainfall/AWAP/JJA/8","/composite/"+num+"/rainfall_anomalies/AWAP/JJA/8")
output(awap_prepare.awap_JJA,indices_phase.IPO_negHad_JJA,indices_phase.ENSO_negHad_JJA,\
       "","/composite/"+num+"/rainfall/AWAP/JJA/9","/composite/"+num+"/rainfall_anomalies/AWAP/JJA/9")

AWAP_JJA = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/JJA/*.png",3,3,title=(r'AWAP JJA: mean rainfall'+sigma))
AWAP_JJA_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/JJA/*.png",3,3,title=(r'AWAP JJA: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_JJA,"","composite/"+num+"_compiled/AWAP/AWAP_JJA")
maps_sub.saveFig(AWAP_JJA_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_JJA_Anom")


#AWAP: SON

output(awap_prepare.awap_SON,indices_phase.IPO_posHad_SON,indices_phase.ENSO_posHad_SON,\
       "","/composite/"+num+"/rainfall/AWAP/SON/1","/composite/"+num+"/rainfall_anomalies/AWAP/SON/1")
output(awap_prepare.awap_SON,indices_phase.IPO_posHad_SON,indices_phase.ENSO_neutralHad_SON,\
       "","/composite/"+num+"/rainfall/AWAP/SON/2","/composite/"+num+"/rainfall_anomalies/AWAP/SON/2")
output(awap_prepare.awap_SON,indices_phase.IPO_posHad_SON,indices_phase.ENSO_negHad_SON,\
       "","/composite/"+num+"/rainfall/AWAP/SON/3","/composite/"+num+"/rainfall_anomalies/AWAP/SON/3")
output(awap_prepare.awap_SON,indices_phase.IPO_neutralHad_SON,indices_phase.ENSO_posHad_SON,\
       "","/composite/"+num+"/rainfall/AWAP/SON/4","/composite/"+num+"/rainfall_anomalies/AWAP/SON/4")
output(awap_prepare.awap_SON,indices_phase.IPO_neutralHad_SON,indices_phase.ENSO_neutralHad_SON,\
       "","/composite/"+num+"/rainfall/AWAP/SON/5","/composite/"+num+"/rainfall_anomalies/AWAP/SON/5")
output(awap_prepare.awap_SON,indices_phase.IPO_neutralHad_SON,indices_phase.ENSO_negHad_SON,\
       "","/composite/"+num+"/rainfall/AWAP/SON/6","/composite/"+num+"/rainfall_anomalies/AWAP/SON/6")
output(awap_prepare.awap_SON,indices_phase.IPO_negHad_SON,indices_phase.ENSO_posHad_SON,\
       "","/composite/"+num+"/rainfall/AWAP/SON/7","/composite/"+num+"/rainfall_anomalies/AWAP/SON/7")
output(awap_prepare.awap_SON,indices_phase.IPO_negHad_SON,indices_phase.ENSO_neutralHad_SON,\
       "","/composite/"+num+"/rainfall/AWAP/SON/8","/composite/"+num+"/rainfall_anomalies/AWAP/SON/8")
output(awap_prepare.awap_SON,indices_phase.IPO_negHad_SON,indices_phase.ENSO_negHad_SON,\
       "","/composite/"+num+"/rainfall/AWAP/SON/9","/composite/"+num+"/rainfall_anomalies/AWAP/SON/9")

AWAP_SON = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/SON/*.png",3,3,title=(r'AWAP SON: mean rainfall'+sigma))
AWAP_SON_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/SON/*.png",3,3,title=(r'AWAP SON: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_SON,"","composite/"+num+"_compiled/AWAP/AWAP_SON")
maps_sub.saveFig(AWAP_SON_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_SON_Anom")


#AWAP: DJF

output(awap_prepare.awap_DJF,indices_phase.IPO_posHad_DJF,indices_phase.ENSO_posHad_DJF,\
       "","/composite/"+num+"/rainfall/AWAP/DJF/1","/composite/"+num+"/rainfall_anomalies/AWAP/DJF/1")
output(awap_prepare.awap_DJF,indices_phase.IPO_posHad_DJF,indices_phase.ENSO_neutralHad_DJF,\
       "","/composite/"+num+"/rainfall/AWAP/DJF/2","/composite/"+num+"/rainfall_anomalies/AWAP/DJF/2")
output(awap_prepare.awap_DJF,indices_phase.IPO_posHad_DJF,indices_phase.ENSO_negHad_DJF,\
       "","/composite/"+num+"/rainfall/AWAP/DJF/3","/composite/"+num+"/rainfall_anomalies/AWAP/DJF/3")
output(awap_prepare.awap_DJF,indices_phase.IPO_neutralHad_DJF,indices_phase.ENSO_posHad_DJF,\
       "","/composite/"+num+"/rainfall/AWAP/DJF/4","/composite/"+num+"/rainfall_anomalies/AWAP/DJF/4")
output(awap_prepare.awap_DJF,indices_phase.IPO_neutralHad_DJF,indices_phase.ENSO_neutralHad_DJF,\
       "","/composite/"+num+"/rainfall/AWAP/DJF/5","/composite/"+num+"/rainfall_anomalies/AWAP/DJF/5")
output(awap_prepare.awap_DJF,indices_phase.IPO_neutralHad_DJF,indices_phase.ENSO_negHad_DJF,\
       "","/composite/"+num+"/rainfall/AWAP/DJF/6","/composite/"+num+"/rainfall_anomalies/AWAP/DJF/6")
output(awap_prepare.awap_DJF,indices_phase.IPO_negHad_DJF,indices_phase.ENSO_posHad_DJF,\
       "","/composite/"+num+"/rainfall/AWAP/DJF/7","/composite/"+num+"/rainfall_anomalies/AWAP/DJF/7")
output(awap_prepare.awap_DJF,indices_phase.IPO_negHad_DJF,indices_phase.ENSO_neutralHad_DJF,\
       "","/composite/"+num+"/rainfall/AWAP/DJF/8","/composite/"+num+"/rainfall_anomalies/AWAP/DJF/8")
output(awap_prepare.awap_DJF,indices_phase.IPO_negHad_DJF,indices_phase.ENSO_negHad_DJF,\
       "","/composite/"+num+"/rainfall/AWAP/DJF/9","/composite/"+num+"/rainfall_anomalies/AWAP/DJF/9")

AWAP_DJF = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/DJF/*.png",3,3,title=(r'AWAP DJF: mean rainfall'+sigma))
AWAP_DJF_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/DJF/*.png",3,3,title=(r'AWAP DJF: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_DJF,"","composite/"+num+"_compiled/AWAP/AWAP_DJF")
maps_sub.saveFig(AWAP_DJF_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_DJF_Anom")


#AWAP: MAM

output(awap_prepare.awap_MAM,indices_phase.IPO_posHad_MAM,indices_phase.ENSO_posHad_MAM,\
       "","/composite/"+num+"/rainfall/AWAP/MAM/1","/composite/"+num+"/rainfall_anomalies/AWAP/MAM/1")
output(awap_prepare.awap_MAM,indices_phase.IPO_posHad_MAM,indices_phase.ENSO_neutralHad_MAM,\
       "","/composite/"+num+"/rainfall/AWAP/MAM/2","/composite/"+num+"/rainfall_anomalies/AWAP/MAM/2")
output(awap_prepare.awap_MAM,indices_phase.IPO_posHad_MAM,indices_phase.ENSO_negHad_MAM,\
       "","/composite/"+num+"/rainfall/AWAP/MAM/3","/composite/"+num+"/rainfall_anomalies/AWAP/MAM/3")
output(awap_prepare.awap_MAM,indices_phase.IPO_neutralHad_MAM,indices_phase.ENSO_posHad_MAM,\
       "","/composite/"+num+"/rainfall/AWAP/MAM/4","/composite/"+num+"/rainfall_anomalies/AWAP/MAM/4")
output(awap_prepare.awap_MAM,indices_phase.IPO_neutralHad_MAM,indices_phase.ENSO_neutralHad_MAM,\
       "","/composite/"+num+"/rainfall/AWAP/MAM/5","/composite/"+num+"/rainfall_anomalies/AWAP/MAM/5")
output(awap_prepare.awap_MAM,indices_phase.IPO_neutralHad_MAM,indices_phase.ENSO_negHad_MAM,\
       "","/composite/"+num+"/rainfall/AWAP/MAM/6","/composite/"+num+"/rainfall_anomalies/AWAP/MAM/6")
output(awap_prepare.awap_MAM,indices_phase.IPO_negHad_MAM,indices_phase.ENSO_posHad_MAM,\
       "","/composite/"+num+"/rainfall/AWAP/MAM/7","/composite/"+num+"/rainfall_anomalies/AWAP/MAM/7")
output(awap_prepare.awap_MAM,indices_phase.IPO_negHad_MAM,indices_phase.ENSO_neutralHad_MAM,\
       "","/composite/"+num+"/rainfall/AWAP/MAM/8","/composite/"+num+"/rainfall_anomalies/AWAP/MAM/8")
output(awap_prepare.awap_MAM,indices_phase.IPO_negHad_MAM,indices_phase.ENSO_negHad_MAM,\
       "","/composite/"+num+"/rainfall/AWAP/MAM/9","/composite/"+num+"/rainfall_anomalies/AWAP/MAM/9")

AWAP_MAM = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/MAM/*.png",3,3,title=(r'AWAP MAM: mean rainfall'+sigma))
AWAP_MAM_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/MAM/*.png",3,3,title=(r'AWAP MAM: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_MAM,"","composite/"+num+"_compiled/AWAP/AWAP_MAM")
maps_sub.saveFig(AWAP_MAM_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_MAM_Anom")


#AWAP: annual

output(awap_prepare.awap_Annual,indices_phase.IPO_posHad_annual,indices_phase.ENSO_posHad_annual,\
       "","/composite/"+num+"/rainfall/AWAP/Annual/1","/composite/"+num+"/rainfall_anomalies/AWAP/Annual/1")
output(awap_prepare.awap_Annual,indices_phase.IPO_posHad_annual,indices_phase.ENSO_neutralHad_annual,\
       "","/composite/"+num+"/rainfall/AWAP/Annual/2","/composite/"+num+"/rainfall_anomalies/AWAP/Annual/2")
output(awap_prepare.awap_Annual,indices_phase.IPO_posHad_annual,indices_phase.ENSO_negHad_annual,\
       "","/composite/"+num+"/rainfall/AWAP/Annual/3","/composite/"+num+"/rainfall_anomalies/AWAP/Annual/3")
output(awap_prepare.awap_Annual,indices_phase.IPO_neutralHad_annual,indices_phase.ENSO_posHad_annual,\
       "","/composite/"+num+"/rainfall/AWAP/Annual/4","/composite/"+num+"/rainfall_anomalies/AWAP/Annual/4")
output(awap_prepare.awap_Annual,indices_phase.IPO_neutralHad_annual,indices_phase.ENSO_neutralHad_annual,\
       "","/composite/"+num+"/rainfall/AWAP/Annual/5","/composite/"+num+"/rainfall_anomalies/AWAP/Annual/5")
output(awap_prepare.awap_Annual,indices_phase.IPO_neutralHad_annual,indices_phase.ENSO_negHad_annual,\
       "","/composite/"+num+"/rainfall/AWAP/Annual/6","/composite/"+num+"/rainfall_anomalies/AWAP/Annual/6")
output(awap_prepare.awap_Annual,indices_phase.IPO_negHad_annual,indices_phase.ENSO_posHad_annual,\
       "","/composite/"+num+"/rainfall/AWAP/Annual/7","/composite/"+num+"/rainfall_anomalies/AWAP/Annual/7")
output(awap_prepare.awap_Annual,indices_phase.IPO_negHad_annual,indices_phase.ENSO_neutralHad_annual,\
       "","/composite/"+num+"/rainfall/AWAP/Annual/8","/composite/"+num+"/rainfall_anomalies/AWAP/Annual/8")
output(awap_prepare.awap_Annual,indices_phase.IPO_negHad_annual,indices_phase.ENSO_negHad_annual,\
       "","/composite/"+num+"/rainfall/AWAP/Annual/9","/composite/"+num+"/rainfall_anomalies/AWAP/Annual/9")

AWAP_annual = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/Annual/*.png",3,3,title=(r'AWAP annual: mean rainfall'+sigma))
AWAP_annual_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/Annual/*.png",3,3,title=(r'AWAP annual: mean rainfall anomalies'+sigma))
maps_sub.saveFig(AWAP_annual,"","composite/"+num+"_compiled/AWAP/AWAP_annual")
maps_sub.saveFig(AWAP_annual_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_annual_Anom")
"""
