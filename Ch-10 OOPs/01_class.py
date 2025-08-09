class Employee:
    language="Python" #this is class attribute
    salary=10000000 
    position="A"   

Vatshal=Employee() # vatshal is object
print(Vatshal.language,Vatshal.salary)

Rakesh=Employee()
print(Rakesh.salary,Rakesh.position)

Rohan=Employee() # here you also add something what you want like name also 
Rohan.name="Rohan" # this is instance attribute
print(Rohan.name,Rohan.salary)
# salary,language and position are class attribute as they directly belong to class and
# name is object or Instance  attribute.