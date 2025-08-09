# if you want ki vo class ke anadar(class attribute le so use @classmethod)
class Employee:
    a=1
    @classmethod
    def show(cls): # yaha par class access hogi isiliye wo class atrribute hi lega
        print(f"The class attribute is {cls.a}")

e=Employee()
e.a=33 # instance attribute ke baad bhi class attribute hi print karega becz i use classmethod and cls instead of self
e.show()
# If you use cls in any function of usi ka attribute lega if i use different(attribute) in class but apply cls on show function to fhir bhi vo a=1 hi leta 
#  agar mai dusre function mai a ki value badal bhi du fhir bhi