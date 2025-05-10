# Opening a file

f=open("tvs.txt","r")

# x=f.read(5)  #Here 5 means 5 bytes (a character takes 1 byte) and store in x ,x is string variable

# print(x)


 #or

x=f.read() #Here bracket is empty so it will read everything in file,not specified how much to read
print(x)

