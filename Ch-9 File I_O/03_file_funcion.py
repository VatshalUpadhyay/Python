f=open("file.txt")
lines=f.readlines()
# here if you use line it only read first line
print(lines)
print(type(lines))

f.close()