import numpy as np
var=np.array([[1,2,3,4],[1,2,3,4]])
print(var)
print()
print(var.shape)
var1=np.array([1,2,3,4],ndmin=4)
print(var1)
print(var1.ndim)
print()
print(var1.shape)
#reshaping to convert  the dimensions of arrays ex if we want to convert 3d array to 2d array 
#1 1d to 2d
var2=np.array([1,2,3,4,5,6])
x=var2.reshape(3,2)
print(x)
print(var2.ndim)
print(x.ndim) 
#2 1d to 3d
var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1=var3.reshape(2,3,2)
print(x1)
print(var3.ndim)
print(x1.ndim) 
#3 3d to 1d
one=x1.reshape(-1)
print(one)