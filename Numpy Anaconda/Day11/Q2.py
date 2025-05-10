# Use reduce()

from functools import reduce


def myFunc(x,y):
    return x+y

a=[1,2,3,4,5,6,7,8,9,10]
b=reduce(myFunc,a)
print("Addition",b)


# Use of lambda function
b=reduce(lambda x,y: x+y,a)
print("Addition using lambda function",b)