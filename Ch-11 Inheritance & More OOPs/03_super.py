class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmerr")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=3

# o=Employee()
# print(o.a) # it print the constructor of employee and 1
o=Manager()
print(o.a,o.b,o.c) # here i use super keyword which print the both constructor programmer and manager mean dono ke init chalenge ni 
# to phele bus 1 2 3 print hota aur consructor of manager chlta
# we use super ki manager apne parent yani programmer ka constructor bhi chla de
