"""
A file to define parameters which require input from the user.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 26 August 2015.
"""
from cwd import cwdInFunction
cwdInFunction()

"""
BASE PERIOD
------------
Choose numbers which match years interested in, between 0-104.
NB: 0 = 1900-1901, 104 = 2004-2005
NB: if want 1970 as end period, choose '70' (code in tpi.py accounts for
    python slicing).
"""
#Base period for whole study (1961-1990)
baseStart = 61
baseEnd = 90

"""
#Base period TPI/Nino3.4 for this analysis:
baseStart =
baseEnd =

#Base period TPI (Henley) - 1971-2000
baseStart = 71 #June 1971-May 1972
baseEnd = 100 #June 2000-May 2001

#Base period IPO (Mantua) - 1947-1995
baseStart = 47
baseEnd = 95

#Base period IPO (Parker) - 1961-1990
baseStart = 61
baseEnd = 90

#Base period Nino3.4 (NCAR - Trenberth) - 1950-1979
baseStart = 50
baseEnd = 79

#Base period Nino3.4 (CPC - OISSTv2, ERSSTv4) - 1981-2010
baseStart = 81
baseEnd = 104
"""

"""
CHEBYSHEV LOW PASS FILTER
"""

#Define Chebyshev low pass filter parameters (for 'tpi_csv.py')
period = 13.0
n = 6.0
rp = 0.1
fs = 12.0 #as monthly data
fc = 1/period
wn = (fc/(0.5*fs))

"""
IPO PHASES
"""
#How many standard deviations above the dataset mean result in IPO pos., neg., and neutral
#Make sure this is a float.
num = 1.5
