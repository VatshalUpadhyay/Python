words=["chutiya","bad","never"]
with open("file3.txt","r")as f:
    content=f.read()

for item in words:
    content=content.replace(item,"*" * len(item))

with open("file3.txt","w")as f:
    f.write(content)
