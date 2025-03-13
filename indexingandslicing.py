#indexing
import numpy as np
var=np.array([1,3,6,9,8])
print(var[3])
var1=np.array([[9,8,7,9,10],[4,5,6,15,16]])
print(var1[0,1])
#slicing [start:stop:step]
print(var[1:4])
print(var[1 : ])
print(var[ : 5])
print(var[1:4:2])
print(var1[0,1:3])
