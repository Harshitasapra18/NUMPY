# np.min(x)
# np.max(x)
# np.argmin(x)
# np.sqrt(x)
# np.sin(x)
# np.cos(x)
# np.cumsum(x)
import numpy as np
var=np.array([1,2,3,4,5,7])
print("min : " ,np.min(var))
print("max : " ,np.max(var))
print("minindex : " ,np.argmin(var))
print("maxindex : " ,np.argmax(var))
print("squareroot : ",np.sqrt(var))
print("sin value : ",np.sin(var))
print("cos value : ",np.cos(var)) 
var1=np.array([[1,2,3],[4,5,6]])
print(np.min(var1,axis=1))
print(np.min(var1,axis=0))
print(np.cumsum(var))



