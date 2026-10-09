fileobject=open("helloworld.txt","w+")
fileobject.write("edited from cmd")
fileobject.close()
fileptr=open("helloworld.txt","r+")
print(fileptr.read())
if(fileobject):
    print("file created")
    

