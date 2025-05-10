# Reshape array but only proivde columns

import numpy as np
arr=np.random.randint(1,50,12)
print(arr)
print(arr.shape)

arr=arr.reshape(-1,2)  # 2 rows and -1 (means system can decide itself how many rows to create)

print(arr)
print(arr.ndim)
print(arr.shape)