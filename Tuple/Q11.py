# tuple functions

# Program to find the length of a tuple
my_tuple = (10, 20, 30, 40, 50, 'Ram', 'Shyam')
print("Length of tuple is:", len(my_tuple))

# Program to find the maximum value in a tuple
numeric_tuple = (10, 20, 30, 40, 50)
print("Maximum value in the tuple is:", max(numeric_tuple))

# Program to find the minimum value in a tuple
print("Minimum value in the tuple is:", min(numeric_tuple))

# Program to find the index of an element in a tuple
element = (30, 56, 7, 8, 3, 2)
print("Index of element in the tuple is:", element.index(56))

# Program to count the occurrence of an element in a tuple
element = (10, 20, 30, 40, 50, 10, 20, 10)
print("Occurrence/frequency of element 10 in the tuple is:", element.count(10))

# Program to convert a list to a tuple
list6 = [10, 20, 30, 40, 50]
tuple_from_list = tuple(list6)
print("Tuple from list is:", tuple_from_list)

# Another conversion from list to tuple
t = tuple([1, 2, 3, 4, 5])
print("Another tuple from list is:", t)

# Program to convert a string to a tuple
string = "Python"
tuple_from_string = tuple(string)
print("Tuple from string is:", tuple_from_string)

# Program to convert a dictionary to a tuple
dictionary = {'a': 1, 'b': 2, 'c': 3}
tuple_from_dict = tuple(dictionary.items())
print("Tuple from dictionary is:", tuple_from_dict)