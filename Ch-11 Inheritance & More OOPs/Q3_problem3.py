class Employee:
    salary=100
    increament=20
    @property #We use this becz hum dot lga kar uska use karske like e.salaryAfterIncreament 
    def salaryAfterIncreament(self):
        return (self.salary+self.salary*(self.increament/100))

    @salaryAfterIncreament.setter # if i give salaryAfterIncreament it change it tell how much it change
    def salaryAfterIncreament(self,salary):
        self.increament=((salary/self.salary)-1)*100 # it help to find e.increament

e=Employee()
print(e.salaryAfterIncreament) #It print salary after increament with help of e(dot)salaryAfterIncreament
print(e.increament) # it tell us kitne ka increament hua 
e.salaryAfterIncreament=200 # it set the value of salary at @salaryAfterIncreament place then after it calculate the increament according to that set value of salary
print(e.increament)
