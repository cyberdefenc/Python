# Condtional Selection in array

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
ars=arr[arr%2==0]

print(arr) 
print(ars)

arr=np.array([1,2,3,4,5,6,7,8,9])
ars=arr[arr%2==0]=0

print(arr) 
print(ars)