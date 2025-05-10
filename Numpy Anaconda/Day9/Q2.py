# Use searchsorted()

import numpy as np
arr=np.array([1, 2, 3,5, 6,8,9])
x=np.searchsorted(arr,7) #searching performed left to right
print(x)