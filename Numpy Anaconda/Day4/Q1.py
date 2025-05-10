# Make user defined list and convert to 1D array
import numpy as np
a=[]
size=int(input("Enter the size of the list: "))
for i in range(size):
    val=int(input("Enter the value: "))
    a.append(val)
print("The list is: ",a)
arr=np.array(a)
for i in range(size):
    print(arr[i])

