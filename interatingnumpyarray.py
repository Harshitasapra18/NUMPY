import numpy as np
var=np.array([19,6,4,3,7,1])
for i in range(len(var)):
    print(var[i])
var1=np.array([[1,2,3],[4,5,6]])
for j in range(len(var1)):
    print(var1[j])
for k in var1:
    for l in k:
        print(l)
#nditer function
var3=([[[1,2,3],[4,5,6]]])
for m in np.nditer(var3,flags=["buffered"],op_dtypes=['S']):
    print(m)
