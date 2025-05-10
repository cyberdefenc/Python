# Convert 2D list to 2D array

import numpy as np

matrix =[]
row=int(input("Enter number of rows: "))
column=int(input("Enter number of columns: "))
for i in range(row):
    a=[]
    for j in range(column):
        val=int(input("Enter element: "))
        a.append(val)
    matrix.append(a)
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()

arr=np.array(matrix)
for i in range(row):
    for j in range(column):
        print(arr[i][j], end=" ")
    print()

print("That was 2D array")
print(type(arr))