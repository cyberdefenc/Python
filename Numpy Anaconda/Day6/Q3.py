# View and copy use

import numpy as np
a=np.array([1,2,4,5,6,66,55,34,23,78,45,99,12,14])
print(a)
slicing=a[3:6]
slicing[:]=0
print(a)
print("view method has replaced original values")

#copy 
k=np.array([1,2,4,5,6,66,55,34,23,78,45,99,12,14])
print(k)
slicing=k[3:6].copy() #updated part of array stored here
slicing[:]=0
print(k)
print("copy method any changes made not effect original once")