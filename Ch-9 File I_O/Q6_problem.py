# 
with open("log.txt") as f:
    content=f.read()

if("python" in content):
    print(" Yes,Python is present in file")
else:
    print("No,It not found")
