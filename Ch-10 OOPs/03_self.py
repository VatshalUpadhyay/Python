class Employee:
    language="Python" #this is class attribute
    salary=10000000 
    def getinfo(self):
        print(f"The language is {self.language} and The salary is {self.salary}")
    #you have to use self ni to jb function call hoga to chalega ni->
    @staticmethod # it use becz We do not want to use any object like(salary,language) we use(greet function) to print goodmorning nothing object required
    def greet(): # thats why i not use self here becz i use staticmethod we only print we dont use an object property like(salray,..)
        print("Good Morning")



Vatshal=Employee() # vatshal is object
Vatshal.greet()
Vatshal.getinfo()

# aur vo Employee.getinfo(Vatshal) aise ho jata fhir argment mai vatshal pass hota aur vo leta ni error aata thats why i use self