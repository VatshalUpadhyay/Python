marks=[]
f1=int(input("Enter the marks here:"))
marks.append(f1) # we us append to if we start with empty list and then add element into it
f2=int(input("Enter the marks here:"))
marks.append(f2)
f3=int(input("Enter the marks here:"))
marks.append(f3)
f4=int(input("Enter the marks here:"))
marks.append(f4)
f5=int(input("Enter the marks here:"))
marks.append(f5)
f6=int(input("Enter the marks here:"))
marks.append(f6)
f7=int(input("Enter the marks here:"))
marks.append(f7)
marks.sort() # it method sort in ascending order thats why to perform i also use int in input to easy to sort otherwise it thing that its string
             # and it sort according to alphabet like phele 1 then 2 jo ki glat ho jata
print(marks)