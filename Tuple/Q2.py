#Check size difference in List and Tuple

import sys

tuple1=(1,2,3,"Ram","Shyam")
list1=[1,2,3,"Ram","Shyam"]

print("tuple1=",tuple1)
print("list1=",list1)

print(" Size of tuple1=",sys.getsizeof(tuple1))
print(" Size of list1=",sys.getsizeof(list1))