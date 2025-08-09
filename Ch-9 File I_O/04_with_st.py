# f=open("file.txt")
# print(f.read)
# f.close()
# this same can written as
with open("file.txt")as f:
    print(f.read())