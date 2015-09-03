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
period = 13.0
n = 6.0
rp = 0.1
fs = 12.0 #as monthly data
fc = 1/period
wn = (fc/(0.5*fs))

#How many standard deviations above the dataset mean result in IPO pos., neg., and neutral
#Make sure this is a float.
num = 1.5
