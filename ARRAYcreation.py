"""import numpy as np
x=np.array([1,2,3,4])
print(x)
print(type(x)) 
print (x.ndim)"""

"""import numpy as np
l=[]
for i in range(1,5):
    int_1=int(input("enter : "))
    l.append(int_1)
print(np.array(l))"""

# 1d array=[1 2 3 4]
# 2d array=[[1 2 3 4]]
# 3d array=[[[1 2 3 4]]]
# ndim for finding dimension of array 

"""import numpy as np
ar2=np.array([[1,2,3,4],[1,2,3,4]])
print(ar2)
print(ar2.ndim)"""

"""import numpy as np
ar3=np.array([[[1,2,3,4],[1,2,3,4]]])
print(ar3)
print(ar3.ndim) """

#ndmin for n dimension array
import numpy as np
arn=np.array([1,2,3,4] , ndmin=10)
print(arn)
print(arn.ndim)