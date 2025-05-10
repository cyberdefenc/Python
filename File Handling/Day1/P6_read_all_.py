#  Read whole file at once

myfile = open(r'E:\story.txt', 'r', encoding='utf-8') # r before E means raw file
str = myfile.read()

print(str)