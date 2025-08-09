with open("trucncate.txt","w") as f:
    f.write("this is truncate") 
    f.truncate(10) # it cut till the number or bytes you enter and write in file 

with open("trucncate.txt","r") as f:
    print(f.read())