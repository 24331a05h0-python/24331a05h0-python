myfile=open("demofile.txt","w+")
myfile.write("hello! this is sravya\n")
myfile.writelines("currently in btech\n department of cse\n interested in civil services\n")
myfile.close()

myfile=open("demofile.txt","r")
data=myfile.read()
print(data)
myfile.close()

myfile=open("demofile.txt","r")
data1=myfile.readline()
print(data1)
myfile.close()

myfile=open("demofile.txt","r")
data2=myfile.readlines()
print(data2)
myfile.close()





























