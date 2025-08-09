class Employee:
    company="ITC"
    language="Java"
    name="Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company} and the language is {self.language}")

class coder:
    language="python"
    def printlanguage(self):
        print(f"Out of all language here is yor language: {self.language}")


class Programmer(Employee,coder): # programmer mai vo sb h jo employee and coder mai h 
    company="ITC Infotech"
    
    name="Vatshal"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a=Employee()
b=Programmer()


b.show() #We use (b.show) so jo b(programmer) mai defined name and company h whi use hoge ye na ki jo function ke upar jo define h 
b.printlanguage()# here in b(programmer)isme maine language define ni kiya isliye jo employee or coder mai language define h whi lega first priority employee becz vo phele h(Employee,coder)
b.showLanguage() # same as uper wala case