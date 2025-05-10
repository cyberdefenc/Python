#  Divison try excpet


try:
    a=int(input("Enter the Number 1."))
    b=int(input("Enter the Number 2."))
    c=a/b
    print(c)
except:
    print("Divison with zero is not allowed.")

else :
    print("No error. Program executed Successfully")

finally: # It's Neurtal ,runs always
    print("Everthing is alright.")