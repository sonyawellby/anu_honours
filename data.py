"""
A script to specify the file-paths of the eight main datasets for analysis.
Download information given here.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 21 August 2015.
"""

from cwd import *
cwdInFunction()

"""
ACCESS1.3 precipitation data
----------------------------
Data from http://cera-www.dkrz.de/WDCC/ui/EntryList.jsp?acronym=CSA3hi
(requires a free CERA account to download).
Downloaded data:
cmip5 output1 CSIRO-BOM ACCESS1-3 historical mon atmos Amon r1i1p1 v1 pr
cmip5 output1 CSIRO-BOM ACCESS1-3 historical mon atmos Amon r2i1p1 v2 pr
cmip5 output1 CSIRO-BOM ACCESS1-3 historical mon atmos Amon r3i1p1 v4 pr
"""
access_pr_r1 = 'data/pr_Amon_ACCESS1-3_historical_r1i1p1_185001-200512.nc'
access_pr_r2 = 'data/pr_Amon_ACCESS1-3_historical_r2i1p1_185001-200512.nc'
access_pr_r3 = 'data/pr_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc'

"""
ACCESS1.3 sea-surface temperature data
--------------------------------------
Data from http://cera-www.dkrz.de/WDCC/ui/EntryList.jsp?acronym=CSA3hi
(requires a free CERA account to download).
Downloaded data:
cmip5 output1 CSIRO-BOM ACCESS1-3 historical mon atmos Amon r1i1p1 v1 ts
cmip5 output1 CSIRO-BOM ACCESS1-3 historical mon atmos Amon r2i1p1 v2 ts
cmip5 output1 CSIRO-BOM ACCESS1-3 historical mon atmos Amon r3i1p1 v4 ts
"""
access_ts_r1 = 'data/ts_Amon_ACCESS1-3_historical_r1i1p1_185001-200512.nc'
access_ts_r2 = 'data/ts_Amon_ACCESS1-3_historical_r2i1p1_185001-200512.nc'
access_ts_r3 = 'data/ts_Amon_ACCESS1-3_historical_r3i1p1_185001-200512.nc'

"""
HadISST1.1 sea-surface temperature data
----------------------------------------
Data from http://www.metoffice.gov.uk/hadobs/hadisst/data/download.html
Downloaded NetCDF file (HadISST_sst.nc.gz)
"""
hadisst = 'data/HadISST_sst.nc'

"""
AWAP precipitation data
-----------------------
Run 26j.  Data from http://www.eoc.csiro.au/awap/
Accessed via FTP site (ftp.eoc.csiro.au/pub/awap/Australia_historical/Run26j/Precip)
"""
#awap = 'data/AWAP_1900-2014_monthly_precip_swACCESSgrid_v4.nc'
#awap = 'data/AWAP_1900-2014_monthly_precip_swACCESSgrid_fpm_v1.nc'
awap = 'data/AWAP_1900-2013_annual_precip_v1.nc'
