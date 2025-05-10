# Reshape array but only provide rows

import numpy as np
arr=np.random.randint(1,50,12)
print(arr)
print(arr.shape)

arr=arr.reshape(2,-1)  # 2 rows and -1 (means system can decide itself how many columns to create)

print(arr)
print(arr.ndim)
print(arr.shape)