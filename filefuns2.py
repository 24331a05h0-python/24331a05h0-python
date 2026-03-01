file=open("file.txt","w+")
file.writelines("hi!\n this is sravya\n fond of music\n")
file.flush()
print("position of cursor after writing: ",file.tell())
file.seek(5)
print("position of cursor after seek: ",file.tell())
buffer=file.read()
print("file content: ",buffer)
file.close()





























