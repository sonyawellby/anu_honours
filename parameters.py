"""
A file to define parameters which require input from the user.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 26 August 2015.
"""
from cwd import cwdInFunction
cwdInFunction()

#Base period (0 = 1900)
baseStart = 70
baseEnd = 100

#Define Chebyshev low pass filter parameters (for 'tpi_csv.py')
n = 6
rp = 13
wn = 0.1
