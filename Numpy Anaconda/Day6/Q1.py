# Create 2D list

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