import numpy as np

def chunks(l,n):
    n = max(1,n)
    return [l[i:i+n] for i in range(0,len(l),n)]

mylist = range(0,144)

new = chunks(mylist,3)

newlist = []
"""
count = 0
while count < (len(new)+1):
    if count/3.0 == 0:
        newlist.append(new[count])
    count +=1
"""
list1 = range(0,len(new),4)
for i in list1:
    newlist.append(new[i])
newarray = np.asarray(newlist)

newNewlist = []
for i in newarray:
    newNewlist.append(np.average(i))
newNewarray = np.asarray(newNewlist)
