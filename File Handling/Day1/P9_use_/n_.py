# write() function use

f=open("tvs.txt","w")
for i in range(5):
    name=input("Enter Your Name -: ")
    f.write(name)
    f.write('\n')
f.close()