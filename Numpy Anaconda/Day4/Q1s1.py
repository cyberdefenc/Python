# size,shape etc

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
print("The shape of the array is: ",arr.shape)
print("The size of the array is: ",arr.size)
print("The data type of the array is: ",arr.dtype)
print("The dimension of the array is: ",arr.ndim)
print("The item size of the array is: ",arr.itemsize)
print("The total bytes of the array is: ",arr.nbytes)


