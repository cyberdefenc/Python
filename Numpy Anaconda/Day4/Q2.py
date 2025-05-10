# Slicing in 1d array

import numpy as np
a=[]
size=int(input("Enter the size of the list: ")) 
for i in range(size):
    val=int(input("Enter the value: "))
    a.append(val)
print("The list is: ",a)
arr=np.array(a)
print("The array is: ",arr)
for i in range(arr.size):
    print(arr[i])
arr1=arr[2:4] # slicing from 2 to 4 which will make new array of 2 elements
print(arr1)

#syntax for slicing in 1d array is arr[start:end:step]
