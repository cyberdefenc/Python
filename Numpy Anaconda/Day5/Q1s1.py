# print dimesion of the array

# Reshape array

import numpy as np
arr=np.random.randint(1,50,12)
print(arr)
print(arr.shape)

arr=arr.reshape(2,6) 
print(arr)
print(arr.ndim)
