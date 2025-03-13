import numpy as np
var=np.array([1,2,3,4])
co=var.copy()
var[2]=5
print("var : ",var)
print("copy : ",co)
var1=np.array([4,5,3,4])
vi=var1.view()
var1[3]=8
print("var : ",var1)
print("view : ",vi)
# the copy owns the data . the copy of an array is a new array. the changes made in copy data does not reflect in the original array.
#the view does not owns data . a view of original data . any changes made to the view will affect the original arrray and vice versa
