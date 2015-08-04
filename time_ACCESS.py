"""
A routine to reshape ACCESS data for analysis.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 4 August 2015.
"""

def timeACCESS(data):
    """
    A routine to:
        (1) find how many days separate each month of the ACCESS dataset
        (2) reshape the dataset relative to days (rather than seconds since
            01/01/0001 on the Proleptic Gregorian calendar).

    Data: The file to apply this function to.
    """
    
    time = data.variables['time']
    timeDiff = [time[i]-time[i-1] for i in range(0,len(time))]
    timeDiff.pop(0)
    timeDiff.append(30.5)
    timeDiffNP = np.array(timeDiff)
    #Reshape the data array as 156 years of 12 months
    months = np.reshape(timeDiffNP,(156,12))
