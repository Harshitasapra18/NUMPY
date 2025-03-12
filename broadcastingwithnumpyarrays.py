import numpy as np
var1=np.array([1,2,3,4])
var2=np.array([1,2,3,4])
print(var1+var2)
#same dimension.
#The dimensions of the arrays are equal or one of them is 1.
var3=np.array([1,2,3])
var4=np.array([[1],[2],[3]])
print(var3+var4)
var5=np.array([[1],[2]])
var6=np.array([[1,2,3],[4,5,6]])
print(var5 + var6) 