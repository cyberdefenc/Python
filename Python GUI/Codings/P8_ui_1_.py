from tkinter import *

def getvalues():
    print(f"The value of usernmae is : {uservalue.get()}")
    print(f"The value of password is : {passvalue.get()}")

root = Tk()

root.geometry("300x300")
user = Label(root, text="Username: ")
password = Label(root, text="Password: ")
user.grid()
password.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvalues).grid()



root.mainloop()