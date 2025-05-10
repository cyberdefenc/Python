#How to change tuple elements

x=("apple", "banana", "cherry")
print("Tuple before change = ",x)
y=list(x)
y[1]="kiwi"
x=tuple(y)
print("Tuple after change = ",x)