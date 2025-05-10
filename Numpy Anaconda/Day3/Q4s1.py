#Print out diagonal elements only

import numpy as np
arr=np.diag([1,2,3,4])  #here np.diag() is used to create 2D array that is matrix from the given array
# and the diagonal elements are 1,2,3,4
print(arr)
arr1=arr.diagonal() #gets the diagonal elements of the matrix
# and stores it in arr1
print(arr1)