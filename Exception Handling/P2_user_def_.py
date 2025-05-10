# User defined exception

age=int(input("Enter you age"))

if age<0:
    print("Negative age is not allowed")
elif age>=18:
    print("Eligible for voting")
else:
    print("Not eligible")