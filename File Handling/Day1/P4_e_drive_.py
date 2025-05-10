# What if the file is in another drive like here in our case it's in E drive,How will you open it

myfile = open(r'E:\story.txt', 'r', encoding='utf-8')
str = myfile.read(10)
print(str)
