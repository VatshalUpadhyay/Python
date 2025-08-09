class Myclass:
    def __init__(self,value):
        self.value=value

    def show(self):
        print(f"Value is {self.value}")
    @property  # getter @ lagane se property baan jata h method ye method par @ iske baad property ban gya
    def ten_value(self):
        return 10* self.value

    @ten_value.setter # it modify or set the value 
    def ten_value(self,new_value):
        self.value=new_value/10

a=Myclass(10)
a.ten_value=50
a.show()

#abstraction=impletation detail ko chupa diya user se
# or Hiding the impletation detail of class and only showing the essential feature to user
#Encapsulation=humne bhut sare kaam karne wale component ko ek particular unit(class employee h) mai pack kar diya
# or Wrapping the data and function into single unit(object) 