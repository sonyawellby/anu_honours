"""
A function to call the data file to be analysed.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 4 August 2015.
"""

from cwd import *

def analyseFile():
    """
    The user specifies the file-path of the file of interest.
    """
    cwdInFunction()
    data = raw_input('Enter the file-path of the file of interest: ')
