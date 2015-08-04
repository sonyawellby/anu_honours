"""
Routine to set the current working directory.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 4 August 2015.
"""

def cwd():
    """A function to set and check the current working directory."""
    import os
    os.chdir("/home/sonya/Documents/")
    print os.getcwd()
    #If working directory set up correctly, this file should load
    f = open("my_coding_routines/foo.py","r")
    print f

def cwdInFunction():
    """Function to set the current working directory within a function."""
    import os
    os.chdir("/home/sonya/Documents/")
