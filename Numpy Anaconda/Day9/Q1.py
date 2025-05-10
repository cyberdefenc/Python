# Find key in array

import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6, 3, 8, 3])
x=np.where(arr==3) # makes array of that index where it founds 3
print(x)

result=np.where(arr%2==0) #makes array of that index where it founds even number
print(result) 