#  If read first 10 character then read next 10 charcter more

myfile = open(r'E:\story.txt', 'r', encoding='utf-8')
str = myfile.read(10)
str1= myfile.read(10)  # will read the next 10 character from last check point
print(str1)