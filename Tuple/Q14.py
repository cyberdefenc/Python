#Add items in tuple by converting it in list then again in tuple

tuple1 = (1, 2, 3, 4, 5)
print("Tuple before adding item = ", tuple1)
list1 = list(tuple1) 
list1.append(6)
tuple1 = tuple(list1)
print("Tuple after adding item = ", tuple1)