word="chutiya"
with open("file3.txt","r")as f:
    content=f.read()

contentNew=content.replace(word,"******")

with open("file3.txt","w")as f:
    f.write(contentNew)