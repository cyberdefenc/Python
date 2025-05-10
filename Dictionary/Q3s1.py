#Use for x in dict1

dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York",
}
print(dict1)
print("By not using values() function,it will only print keys not values")
for x in dict1:
    print(x)