class Employee:
    company="ITC"
    language="Python"
    name="Vatshal"
    salary=120000
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company="ITC Infotech"
    name="Rakesh"
    language="C"
    salary=10000
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a=Employee()

b=Programmer()
print(a.company,b.company,a.name,a.language,b.language,b.name)
# first you have to define name,language and company then you use
a.show() # here you have to first define(name,salary..) then you call function to perform
b.showLanguage()