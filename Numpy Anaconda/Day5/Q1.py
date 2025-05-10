# Reshape array

import numpy as np
arr=np.random.randint(1,50,12)
print(arr)
print(arr.shape)

arr=arr.reshape(2,6)  # 2 rows and 6 columns
print(arr)

#rememeber for reshaping the number of elements should be same