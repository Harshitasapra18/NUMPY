#rand()-the function is used to generate random value between 0  to 1
#randn()-the function is used to generate random values close to zero. This may return positive or negative number as well
#ranf()-the function for doing random sampling in numpy . It returns an array of specified shape and fills it with random floats in half open interval [0.0,1.0)
#randint()-the function is used to generate  a random number between a given range.
import numpy as np
var=np.random.rand(4)
var1=np.random.rand(2,4)
var2=np.random.randn(4)
var3=np.random.ranf(4)
var4=np.random.randint(2,5,(2,5))#(min.max.how many value)
print(var)
print(var1)
print(var2)
print(var3)
print(var4)
