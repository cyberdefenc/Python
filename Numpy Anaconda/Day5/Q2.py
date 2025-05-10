# Convert to 3D array

# Reshape array

import numpy as np
arr=np.random.randint(1,50,12)
print(arr)
print(arr.shape)

arr=arr.reshape(2,3,2)  # 2 rows, 3 columns, and 6 depth(no. of 2D arrays)

print(arr)
print(arr.ndim)
print(arr.shape)
