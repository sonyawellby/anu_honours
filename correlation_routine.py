"""
A file to correlate ENSO with rainfall and the IPO with rainfall.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 15 September 2015.
"""

from correlation import *

"""
test = corr(awap_JJA,Nino34_JJA,0)
test1 = ma.masked_invalid(test)
Dict6 = mapCorr()
myplot = plot(test1,Dict6,labels=False,grid=False,oceans=False,cbar=True)
saveFig(myplot,"test_today","test_today")
"""

plotCorr(awap_JJA,Nino34_JJA,0,"AWAP rainfall-Nino3.4 correlation - JJA",\
         "/correlation/nino_awap/JJA")
