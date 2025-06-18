from tkinter import *

def getval():
    print("Submitted to Fostro travellers")

root = Tk()
root.geometry("644x444")
root.title("Fostro Travellers")

# Make column 2 and 3 expandable to center properly
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Welcome message centered at top
Label(root, text="Welcome to Fostro Travellers", font="Arial 13 bold").grid(row=0, column=2, columnspan=2, pady=10)

# Labels for the form
labels = ["Name", "Phone", "Email", "Gender", "Address", "Source", "Destination", "Payment Method"]
for i, label in enumerate(labels):
    Label(root, text=label).grid(row=i+1, column=2, sticky="e", padx=10, pady=2)

# Tkinter variables
namevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
gendervalue = StringVar()
addressvalue = StringVar()
sourcevalue = StringVar()
destinationvalue = StringVar()
paymentmethodvalue = StringVar()
foodservicevalue = IntVar()

# Entry fields
entries = [
    Entry(root, textvariable=namevalue),
    Entry(root, textvariable=phonevalue),
    Entry(root, textvariable=emailvalue),
    Entry(root, textvariable=gendervalue),
    Entry(root, textvariable=addressvalue),
    Entry(root, textvariable=sourcevalue),
    Entry(root, textvariable=destinationvalue),
    Entry(root, textvariable=paymentmethodvalue)
]

for i, entry in enumerate(entries):
    entry.grid(row=i+1, column=3, padx=10, pady=2)

# Checkbox (Get your meal)
Checkbutton(root, text="Get your meal", variable=foodservicevalue).grid(row=9, column=3, pady=5)

# Submit Button
Button(root, text="Submit to Fostro", command=getval).grid(row=10, column=3, pady=10)

root.mainloop()
