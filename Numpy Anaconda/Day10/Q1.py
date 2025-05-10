# A number is given, so find the sum of each even digits of that number and product of each odd digits

x=int(input("Enter a number: "))
sum=0
product=1
while x>0:
    digit=x%10
    if digit%2==0:
        sum=sum+digit
    else:
        product=product*digit
    x=x//10
print("Sum of even digits is: ",sum)
print("Product of odd digits is: ",product)