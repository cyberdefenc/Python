#  Read whole file using readline()



myfile = open(r'E:\story.txt', 'r', encoding='utf-8')

line = " "

while line:
    line = myfile.readline()
    print(line, end=' ')  # Correct use of end

myfile.close()
