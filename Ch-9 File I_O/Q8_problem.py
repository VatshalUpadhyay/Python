with open("log.txt")as f:
    content1=f.read()

with open("poem.txt")as f:
    content2=f.read()

if(content1==content2):
    print("This files are identical and same")

else:
    print("The files are different")