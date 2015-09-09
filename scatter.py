"""
A file to create scatterplots showing the relationship between
ENSO and the IPO.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 9 September 2015.
"""

from ENSO_IPO_corr import *
from plot import multiGeneral


def scatter():
    """
    Generate scatterplots of Nino3.4/TPI relationship
    """
    had_ann = scatPlot(Nino34_annual[0],TPI_annual[1],"HadISST1 - annual","my_coding_routines/images/scatter/Had - annual")
    had_jun = scatPlot(Nino34_Jun[0],TPI_Jun[1],"HadISST1 - June","my_coding_routines/images/scatter/Had - Jun")
    had_jul = scatPlot(Nino34_Jul[0],TPI_Jul[1],"HadISST1 - July","my_coding_routines/images/scatter/Had - Jul")
    had_aug = scatPlot(Nino34_Aug[0],TPI_Aug[1],"HadISST1 - August","my_coding_routines/images/scatter/Had - Aug")
    had_sep = scatPlot(Nino34_Sep[0],TPI_Sep[1],"HadISST1 - September","my_coding_routines/images/scatter/Had - Sep")
    had_oct = scatPlot(Nino34_Oct[0],TPI_Oct[1],"HadISST1 - October","my_coding_routines/images/scatter/Had - Oct")
    had_nov = scatPlot(Nino34_Nov[0],TPI_Nov[1],"HadISST1 - November","my_coding_routines/images/scatter/Had - Nov")
    had_dec = scatPlot(Nino34_Dec[0],TPI_Dec[1],"HadISST1 - December","my_coding_routines/images/scatter/Had - Dec")
    had_jan = scatPlot(Nino34_Jan[0],TPI_Jan[1],"HadISST1 - January","my_coding_routines/images/scatter/Had - Jan")
    had_feb = scatPlot(Nino34_Feb[0],TPI_Feb[1],"HadISST1 - February","my_coding_routines/images/scatter/Had - Feb")
    had_mar = scatPlot(Nino34_Mar[0],TPI_Mar[1],"HadISST1 - March","my_coding_routines/images/scatter/Had - Mar")
    had_apr = scatPlot(Nino34_Apr[0],TPI_Apr[1],"HadISST1 - April","my_coding_routines/images/scatter/Had - Apr")
    had_may = scatPlot(Nino34_May[0],TPI_May[1],"HadISST1 - May","my_coding_routines/images/scatter/Had - May")
    had_jja = scatPlot(Nino34_JJA[0],TPI_JJA[1],"HadISST1 - JJA","my_coding_routines/images/scatter/Had - JJA")
    had_son = scatPlot(Nino34_SON[0],TPI_SON[1],"HadISST1 - SON","my_coding_routines/images/scatter/Had - SON")
    had_djf = scatPlot(Nino34_DJF[0],TPI_DJF[1],"HadISST1 - DJF","my_coding_routines/images/scatter/Had - DJF")
    had_mam = scatPlot(Nino34_MAM[0],TPI_MAM[1],"HadISST1 - MAM","my_coding_routines/images/scatter/Had - MAM")

    r1_ann = scatPlot(Nino34_annual[1],TPI_annual[3],"ACCESS1.3 R1 - annual","my_coding_routines/images/scatter/R1 - annual")
    r1_jun = scatPlot(Nino34_Jun[1],TPI_Jun[3],"ACCESS1.3 R1 - June","my_coding_routines/images/scatter/R1 - Jun")
    r1_jul = scatPlot(Nino34_Jul[1],TPI_Jul[3],"ACCESS1.3 R1 - July","my_coding_routines/images/scatter/R1 - Jul")
    r1_aug = scatPlot(Nino34_Aug[1],TPI_Aug[3],"ACCESS1.3 R1 - August","my_coding_routines/images/scatter/R1 - Aug")
    r1_sep = scatPlot(Nino34_Sep[1],TPI_Sep[3],"ACCESS1.3 R1 - September","my_coding_routines/images/scatter/R1 - Sep")
    r1_oct = scatPlot(Nino34_Oct[1],TPI_Oct[3],"ACCESS1.3 R1 - October","my_coding_routines/images/scatter/R1 - Oct")
    r1_nov = scatPlot(Nino34_Nov[1],TPI_Nov[3],"ACCESS1.3 R1 - November","my_coding_routines/images/scatter/R1 - Nov")
    r1_dec = scatPlot(Nino34_Dec[1],TPI_Dec[3],"ACCESS1.3 R1 - December","my_coding_routines/images/scatter/R1 - Dec")
    r1_jan = scatPlot(Nino34_Jan[1],TPI_Jan[3],"ACCESS1.3 R1 - January","my_coding_routines/images/scatter/R1 - Jan")
    r1_feb = scatPlot(Nino34_Feb[1],TPI_Feb[3],"ACCESS1.3 R1 - February","my_coding_routines/images/scatter/R1 - Feb")
    r1_mar = scatPlot(Nino34_Mar[1],TPI_Mar[3],"ACCESS1.3 R1 - March","my_coding_routines/images/scatter/R1 - Mar")
    r1_apr = scatPlot(Nino34_Apr[1],TPI_Apr[3],"ACCESS1.3 R1 - April","my_coding_routines/images/scatter/R1 - Apr")
    r1_may = scatPlot(Nino34_May[1],TPI_May[3],"ACCESS1.3 R1 - May","my_coding_routines/images/scatter/R1 - May")
    r1_jja = scatPlot(Nino34_JJA[1],TPI_JJA[3],"ACCESS1.3 R1 - JJA","my_coding_routines/images/scatter/R1 - JJA")
    r1_son = scatPlot(Nino34_SON[1],TPI_SON[3],"ACCESS1.3 R1 - SON","my_coding_routines/images/scatter/R1 - SON")
    r1_djf = scatPlot(Nino34_DJF[1],TPI_DJF[3],"ACCESS1.3 R1 - DJF","my_coding_routines/images/scatter/R1 - DJF")
    r1_mam = scatPlot(Nino34_MAM[1],TPI_MAM[3],"ACCESS1.3 R1 - MAM","my_coding_routines/images/scatter/R1 - MAM")

    r2_ann = scatPlot(Nino34_annual[2],TPI_annual[5],"ACCESS1.3 R2 - annual","my_coding_routines/images/scatter/R2 - annual")
    r2_jun = scatPlot(Nino34_Jun[2],TPI_Jun[5],"ACCESS1.3 R2 - June","my_coding_routines/images/scatter/R2 - Jun")
    r2_jul = scatPlot(Nino34_Jul[2],TPI_Jul[5],"ACCESS1.3 R2 - July","my_coding_routines/images/scatter/R2 - Jul")
    r2_aug = scatPlot(Nino34_Aug[2],TPI_Aug[5],"ACCESS1.3 R2 - August","my_coding_routines/images/scatter/R2 - Aug")
    r2_sep = scatPlot(Nino34_Sep[2],TPI_Sep[5],"ACCESS1.3 R2 - September","my_coding_routines/images/scatter/R2 - Sep")
    r2_oct = scatPlot(Nino34_Oct[2],TPI_Oct[5],"ACCESS1.3 R2 - October","my_coding_routines/images/scatter/R2 - Oct")
    r2_nov = scatPlot(Nino34_Nov[2],TPI_Nov[5],"ACCESS1.3 R2 - November","my_coding_routines/images/scatter/R2 - Nov")
    r2_dec = scatPlot(Nino34_Dec[2],TPI_Dec[5],"ACCESS1.3 R2 - December","my_coding_routines/images/scatter/R2 - Dec")
    r2_jan = scatPlot(Nino34_Jan[2],TPI_Jan[5],"ACCESS1.3 R2 - January","my_coding_routines/images/scatter/R2 - Jan")
    r2_feb = scatPlot(Nino34_Feb[2],TPI_Feb[5],"ACCESS1.3 R2 - February","my_coding_routines/images/scatter/R2 - Feb")
    r2_mar = scatPlot(Nino34_Mar[2],TPI_Mar[5],"ACCESS1.3 R2 - March","my_coding_routines/images/scatter/R2 - Mar")
    r2_apr = scatPlot(Nino34_Apr[2],TPI_Apr[5],"ACCESS1.3 R2 - April","my_coding_routines/images/scatter/R2 - Apr")
    r2_may = scatPlot(Nino34_May[2],TPI_May[5],"ACCESS1.3 R2 - May","my_coding_routines/images/scatter/R2 - May")
    r2_jja = scatPlot(Nino34_JJA[2],TPI_JJA[5],"ACCESS1.3 R2 - JJA","my_coding_routines/images/scatter/R2 - JJA")
    r2_son = scatPlot(Nino34_SON[2],TPI_SON[5],"ACCESS1.3 R2 - SON","my_coding_routines/images/scatter/R2 - SON")
    r2_djf = scatPlot(Nino34_DJF[2],TPI_DJF[5],"ACCESS1.3 R2 - DJF","my_coding_routines/images/scatter/R2 - DJF")
    r2_mam = scatPlot(Nino34_MAM[2],TPI_MAM[5],"ACCESS1.3 R2 - MAM","my_coding_routines/images/scatter/R2 - MAM")

    r3_ann = scatPlot(Nino34_annual[3],TPI_annual[7],"ACCESS1.3 R3 - annual","my_coding_routines/images/scatter/R3 - annual")
    r3_jun = scatPlot(Nino34_Jun[3],TPI_Jun[7],"ACCESS1.3 R3 - June","my_coding_routines/images/scatter/R3 - Jun")
    r3_jul = scatPlot(Nino34_Jul[3],TPI_Jul[7],"ACCESS1.3 R3 - July","my_coding_routines/images/scatter/R3 - Jul")
    r3_aug = scatPlot(Nino34_Aug[3],TPI_Aug[7],"ACCESS1.3 R3 - August","my_coding_routines/images/scatter/R3 - Aug")
    r3_sep = scatPlot(Nino34_Sep[3],TPI_Sep[7],"ACCESS1.3 R3 - September","my_coding_routines/images/scatter/R3 - Sep")
    r3_oct = scatPlot(Nino34_Oct[3],TPI_Oct[7],"ACCESS1.3 R3 - October","my_coding_routines/images/scatter/R3 - Oct")
    r3_nov = scatPlot(Nino34_Nov[3],TPI_Nov[7],"ACCESS1.3 R3 - November","my_coding_routines/images/scatter/R3 - Nov")
    r3_dec = scatPlot(Nino34_Dec[3],TPI_Dec[7],"ACCESS1.3 R3 - December","my_coding_routines/images/scatter/R3 - Dec")
    r3_jan = scatPlot(Nino34_Jan[3],TPI_Jan[7],"ACCESS1.3 R3 - January","my_coding_routines/images/scatter/R3 - Jan")
    r3_feb = scatPlot(Nino34_Feb[3],TPI_Feb[7],"ACCESS1.3 R3 - February","my_coding_routines/images/scatter/R3 - Feb")
    r3_mar = scatPlot(Nino34_Mar[3],TPI_Mar[7],"ACCESS1.3 R3 - March","my_coding_routines/images/scatter/R3 - Mar")
    r3_apr = scatPlot(Nino34_Apr[3],TPI_Apr[7],"ACCESS1.3 R3 - April","my_coding_routines/images/scatter/R3 - Apr")
    r3_may = scatPlot(Nino34_May[3],TPI_May[7],"ACCESS1.3 R3 - May","my_coding_routines/images/scatter/R3 - May")
    r3_jja = scatPlot(Nino34_JJA[3],TPI_JJA[7],"ACCESS1.3 R3 - JJA","my_coding_routines/images/scatter/R3 - JJA")
    r3_son = scatPlot(Nino34_SON[3],TPI_SON[7],"ACCESS1.3 R3 - SON","my_coding_routines/images/scatter/R3 - SON")
    r3_djf = scatPlot(Nino34_DJF[3],TPI_DJF[7],"ACCESS1.3 R3 - DJF","my_coding_routines/images/scatter/R3 - DJF")
    r3_mam = scatPlot(Nino34_MAM[3],TPI_MAM[7],"ACCESS1.3 R3 - MAM","my_coding_routines/images/scatter/R3 - MAM")

    return

