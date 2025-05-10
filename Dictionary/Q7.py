#Dictionary inbuilt functions

#length of dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}    
print("Length of dictionary:", len(dict1)) #3

#or 
dict1 = {'a': 1, 'b': 2, 'c': 3}    
x=len(dict1)
print("Length of dictionary:",x) #3

#removing item from dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}
print("Before removing item:", dict1) 
del dict1['a'] #removes key 'a' and its value
print("After removing item:", dict1) 

#removing item from dictionary using pop() method
dict1 = {'a': 1, 'b': 2, 'c': 3}
print("Before removing item:", dict1)
dict1.pop('a') #removes key 'a' and its value
print("After removing item:", dict1)

#removing all items from dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}
print("Before removing all items:", dict1)
dict1.clear() #removes all items from dictionary
print("After removing all items:", dict1) #empty dictionary

#popitem() method Automatically removes last inserted item from dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}
print("Before removing item:", dict1)
dict1.popitem() #removes last inserted item from dictionary
print("After removing item:", dict1) #removes last inserted item from dictionary

#deleting dictionary
#dict1 = {'a': 1, 'b': 2, 'c': 3}
#print("Before deleting dictionary:", dict1)
#del dict1 #deletes dictionary
#print("After deleting dictionary:", dict1) #error: name 'dict1' is not defined 

#copying dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}    
print("Before copying dictionary:", dict1)
dict2 = dict1.copy() #copies dictionary
print("After copying dictionary:", dict2) #copies dictionary

#fromkeys() method
x=('a', 'b', 'c')
y=0
dict1 = dict.fromkeys(x, y) #creates dictionary with keys from x and value from y
print("Dictionary with keys from x and value from y:", dict1) #creates dictionary with keys from x and value from y

#setdefault() method,if key already exists, it returns the value of the key, if key does not exist, it adds the key with the value
dict1 = {'a': 1, 'b': 2, 'c': 3}
print("Before using setdefault method:", dict1)
dict1.setdefault('d', 4) #adds key 'd' with value 4 if key 'd' does not exist
print("After using setdefault method:", dict1) #adds key 'd' with value 4 if key 'd' does not exist


#update() method, updates the dictionary with the key-value pairs from another dictionary

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5}
print("Before using update method:", dict1)
dict1.update(dict2) #updates the dictionary with the key-value pairs from another dictionary
print("After using update method:", dict1) #updates the dictionary with the key-value pairs from another dictionary