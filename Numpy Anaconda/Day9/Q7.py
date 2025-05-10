# Find even from list using filter() and then convert function to lambda function

a=[1,2,3,4,5,6,7,8,9,10]
def evenfunc(x):
    if x%2==0:
        return True
    else:
        return False
even=filter(evenfunc,a)

for x in even:
    print(x)


    #or
print("Using lambda function")
eve=filter(lambda y:y%2==0,a)
for x in eve:
    print(x)
