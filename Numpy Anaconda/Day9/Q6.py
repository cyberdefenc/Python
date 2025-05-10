# Use filter

import numpy as np

ag=[5,11,45,78,12,3,4,2,3,4,89,76]
def myfunc(x):
    if x<18:
        return False
    else:
        return True
    
adults=filter(myfunc,ag)
for x in adults:
    print(x)

    #or

print("Using lambda function")
adults=filter(lambda x: x>18,ag) # filter captures that element on the basis of condition and then stores it in adults as list
for x in adults:
    print(x)


#above you can see the difference between  lambda and normal function ,lambda converted the function into a single line and made it more readable.