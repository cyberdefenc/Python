# Make empty array and take input from user

import numpy as np
a=[]
n=int(input("Enter size of array: "))
for i in range(n):
    val=int(input("Enter the element: "))
    a.append(val)
print("The array is: ",a)