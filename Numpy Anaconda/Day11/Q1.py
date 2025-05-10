# Use of map()




a=[1,2,3,4,5,6,7,8,9,10]
def myFunc(x):
    if x<18:
        return False
    else:
        return True
    
def myFunc1(x):
    return x*x

adults=filter(myFunc,a)

for x in adults:
    print(x)

squares=map(myFunc1,a)
for x in squares:
    print(x)



print("Using lambda function")
adults=filter(lambda x: x>18,a)
squares=list(map(lambda x: x*x,a))
print(squares)
