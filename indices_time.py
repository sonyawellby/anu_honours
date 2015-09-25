"""
A file to divide Nino 3.4 and TPI index data into years, seasons and months. 

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 10 September 2015.
"""
#25 September: I don't think I need this  file still.  But check.

import netCDF4 as n
import numpy as np
from indices_array import Nino34, TPI
from cwd import cwdInFunction

cwdInFunction()

def indexTime(index):
    """
    A function to break indices into annual, seasonal and monthly resolution.
    Parameters:
    -----------
    The index (as an array) of interest (either Nino34 or TPI).  Length will vary
    between 4 and 8.
    """
    Jun = []
    Jul = []
    Aug = []
    Sep = []
    Oct = []
    Nov = []
    Dec = []
    Jan = []
    Feb = []
    Mar = []
    Apr = []
    May = []
    JJA = []
    SON = []
    DJF = []
    MAM = []
    annual = []

    count = 0

    while count < len(index):
        jun = index[count][0::12]
        jul = index[count][1::12]
        aug = index[count][2::12]
        sep = index[count][3::12]
        octo = index[count][4::12]
        nov = index[count][5::12]
        dec = index[count][6::12]
        jan = index[count][7::12]
        feb = index[count][8::12]
        mar = index[count][9::12]
        apr = index[count][10::12]
        may = index[count][11::12]
        jja = (index[count][0::12] + index[count][1::12] + index[count][2::12])/3.0
        son = (index[count][3::12] + index[count][4::12] + index[count][5::12])/3.0
        djf = (index[count][6::12] + index[count][7::12] + index[count][8::12])/3.0
        mam = (index[count][9::12] + index[count][10::12] + index[count][11::12])/3.0
        Annual = (jja + son + djf + mam)/4.0

        Jun.append(jun)
        Jul.append(jul)
        Aug.append(aug)
        Sep.append(sep)
        Oct.append(octo)
        Nov.append(nov)
        Dec.append(dec)
        Jan.append(jan)
        Feb.append(feb)
        Mar.append(mar)
        Apr.append(apr)
        May.append(may)
        JJA.append(jja)
        SON.append(son)
        DJF.append(djf)
        MAM.append(mam)
        annual.append(Annual)
        
        count += 1

    Jun = np.asarray(Jun)
    Jul = np.asarray(Jul)
    Aug = np.asarray(Aug)
    Sep = np.asarray(Sep)
    Oct = np.asarray(Oct)
    Nov = np.asarray(Nov)
    Dec = np.asarray(Dec)
    Jan = np.asarray(Jan)
    Feb = np.asarray(Feb)
    Mar = np.asarray(Mar)
    Apr = np.asarray(Apr)
    May = np.asarray(May)
    JJA = np.asarray(JJA)
    SON = np.asarray(SON)
    DJF = np.asarray(DJF)
    MAM = np.asarray(MAM)
    annual = np.asarray(annual)
    return Jun, Jul, Aug, Sep, Oct, Nov, Dec, Jan, Feb, Mar, Apr, May,\
           JJA, SON, DJF, MAM, annual

def arrayShape(time,num):
    """
    Create an array with same dimensions as AWAP (27 by 22) populated with
    the one value for each time-step. 

    Parameters:
    -----------
    time : the 1x105 time array to be expanded to a 105x22x27 array.
    num : the index corresponding with the Nino34/TPI array to be
        computed (e.g. HadISST, ACCESS1.3 r1). 
    """
    #Create an array with AWAP dimensions
    count = 0
    new = []
    while count < 105:
        a = np.zeros((27,22))
        a.fill(time[num][count])
        new.append(a)
        count += 1
    new1 = np.asarray(new)
    return new1

def nino34Time(index,num):
    enso = indexTime(index)
    (Jun, Jul, Aug, Sep, Oct, Nov, Dec, \
     Jan, Feb, Mar, Apr, May,\
     JJA, SON, DJF, MAM, annual) = enso

    Nino34_Jun = arrayShape(Jun,num)
    Nino34_Jul = arrayShape(Jul,num)
    Nino34_Aug = arrayShape(Aug,num)
    Nino34_Sep = arrayShape(Sep,num)
    Nino34_Oct = arrayShape(Oct,num)
    Nino34_Nov = arrayShape(Nov,num)
    Nino34_Dec = arrayShape(Dec,num)
    Nino34_Jan = arrayShape(Jan,num)
    Nino34_Feb = arrayShape(Feb,num)
    Nino34_Mar = arrayShape(Mar,num)
    Nino34_Apr = arrayShape(Apr,num)
    Nino34_May = arrayShape(May,num)
    Nino34_JJA = arrayShape(JJA,num)
    Nino34_SON = arrayShape(SON,num)
    Nino34_DJF = arrayShape(DJF,num)
    Nino34_MAM = arrayShape(MAM,num)
    Nino34_annual = arrayShape(annual,num)
    return Nino34_Jun,Nino34_Jul,Nino34_Aug,Nino34_Sep,Nino34_Oct,Nino34_Nov,\
           Nino34_Dec,Nino34_Jan,Nino34_Feb,Nino34_Mar,Nino34_Apr,Nino34_May,\
           Nino34_JJA,Nino34_SON,Nino34_DJF,Nino34_MAM,Nino34_annual

def tpiTime(index,num):
    tpi = indexTime(index)
    (Jun, Jul, Aug, Sep, Oct, Nov, Dec, \
     Jan, Feb, Mar, Apr, May,\
     JJA, SON, DJF, MAM, annual) = tpi

    TPI_Jun = arrayShape(Jun,num)
    TPI_Jul = arrayShape(Jul,num)
    TPI_Aug = arrayShape(Aug,num)
    TPI_Sep = arrayShape(Sep,num)
    TPI_Oct = arrayShape(Oct,num)
    TPI_Nov = arrayShape(Nov,num)
    TPI_Dec = arrayShape(Dec,num)
    TPI_Jan = arrayShape(Jan,num)
    TPI_Feb = arrayShape(Feb,num)
    TPI_Mar = arrayShape(Mar,num)
    TPI_Apr = arrayShape(Apr,num)
    TPI_May = arrayShape(May,num)
    TPI_JJA = arrayShape(JJA,num)
    TPI_SON = arrayShape(SON,num)
    TPI_DJF = arrayShape(DJF,num)
    TPI_MAM = arrayShape(MAM,num)
    TPI_annual = arrayShape(annual,num)
    return TPI_Jun,TPI_Jul,TPI_Aug,TPI_Sep,TPI_Oct,TPI_Nov,TPI_Dec,TPI_Jan,\
           TPI_Feb,TPI_Mar,TPI_Apr,TPI_May,TPI_JJA,TPI_SON,TPI_DJF,TPI_MAM,\
           TPI_annual
"""
#Observational data
enso = nino34Time(Nino34,0)
(Nino34_Jun, Nino34_Jul, Nino34_Aug, Nino34_Sep, Nino34_Oct, Nino34_Nov, \
 Nino34_Dec, Nino34_Jan, Nino34_Feb, Nino34_Mar, Nino34_Apr, Nino34_May,\
 Nino34_JJA, Nino34_SON, Nino34_DJF, Nino34_MAM, Nino34_annual) = enso

ipo = tpiTime(TPI,1)
(TPI_Jun, TPI_Jul, TPI_Aug, TPI_Sep, TPI_Oct, TPI_Nov, TPI_Dec, \
 TPI_Jan, TPI_Feb, TPI_Mar, TPI_Apr, TPI_May,\
 TPI_JJA, TPI_SON, TPI_DJF, TPI_MAM, TPI_annual) = ipo
"""

enso = indexTime(Nino34)
(Jun, Jul, Aug, Sep, Oct, Nov, Dec, Jan, Feb, Mar, Apr, May,\
           JJA, SON, DJF, MAM, annual) = enso

Nino34_Jun = Jun
Nino34_Jul = Jul
Nino34_Aug = Aug
Nino34_Sep = Sep
Nino34_Oct = Oct
Nino34_Nov = Nov
Nino34_Dec = Dec
Nino34_Jan = Jan
Nino34_Feb = Feb
Nino34_Mar = Mar
Nino34_Apr = Apr
Nino34_May = May
Nino34_JJA = JJA
Nino34_SON = SON
Nino34_DJF = DJF
Nino34_MAM = MAM
Nino34_annual = annual

ipo = indexTime(TPI)
(Jun, Jul, Aug, Sep, Oct, Nov, Dec, Jan, Feb, Mar, Apr, May,\
           JJA, SON, DJF, MAM, annual) = ipo

TPI_Jun = Jun
TPI_Jul = Jul
TPI_Aug = Aug
TPI_Sep = Sep
TPI_Oct = Oct
TPI_Nov = Nov
TPI_Dec = Dec
TPI_Jan = Jan
TPI_Feb = Feb
TPI_Mar = Mar
TPI_Apr = Apr
TPI_May = May
TPI_JJA = JJA
TPI_SON = SON
TPI_DJF = DJF
TPI_MAM = MAM
TPI_annual = annual
