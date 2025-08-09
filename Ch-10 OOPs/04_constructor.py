class Employee:
    language="Python" #this is class attribute
    salary=10000000 


    def __init__(self,name,salary,language): # init is dunder method which called automatically when you call any function
         self.name=name
         self.salary=salary
         self.language=language
         print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language} and The salary is {self.salary}")

    @staticmethod # it use becz We do not want to use any object property just print greet function and thats why i not use self here
    def greet():
        print("Good Morning")

vatshal=Employee("Vatshal",12000000,"C") # here i pass those value so it will taken,you do when you use init
# vatshal.name="Vatshal"
vatshal.greet()
print(vatshal.name,vatshal.salary,vatshal.language)
# i passed as argument in init and during calling