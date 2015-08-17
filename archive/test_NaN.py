"""
Test adding NaN values to a python list and finding mean
"""
import numpy as np
import numpy.ma as ma

myList = [1,2,4,7,7,9,3,2,1,10]
myListTest = [1,2,4,7,7,9,3,2,1,10]
myListNew = [2,4,7,7,9,3,2,1,10]

myArray = np.array(myListTest)
mx_myArray = ma.masked_less_equal(myArray,3)
print np.mean(mx_myArray)


"""
print np.mean(myList)
print np.mean(myListNew)

print myListTest
myListTest = [np.nan if x < 3 else x for x in myListTest]

print myListTest
print np.mean(myListTest)

myArray = np.array(myListTest)
np.isnan(myArray)
~np.isnan(myArray)
print myArray[~np.isnan(myArray)]
print myArray[~np.isnan(myArray)].mean()
"""    
