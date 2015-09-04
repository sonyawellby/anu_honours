"""
A routine to convert CSV multi-column data into a single array.

Submitted by Sonya Wellby for ENVS4055, 2015.
Last updated 4 September 2015.
"""

from cwd import cwdInFunction
import csv
import numpy as np

cwdInFunction()

filename = raw_input('Enter the name of the file: ')
#data/Mantua_IPO.csv
#data/Parker_IPO.csv
#data/HadISST_NCEP_Nino34.csv

index = open(filename,'rU')
csvReader = csv.reader(index)

sheet = []

for row in csvReader:
    sheet.append(row)
index.close()

sheet_array = np.array(sheet)
flat = sheet_array.flatten()
flat_rm_beg = flat[5:]
flat_rm_end = flat_rm_beg[:1260]
final = flat_rm_end.astype(np.float)

filenameNew = raw_input('Enter the name of the new file: ')
np.savetxt(filenameNew,final,delimiter=",")
