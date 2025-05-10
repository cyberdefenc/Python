#Use values() function

dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York",
}
print(dict1)
x = dict1.values()
print("By using values() function")
for x in dict1.values():
    print(x)