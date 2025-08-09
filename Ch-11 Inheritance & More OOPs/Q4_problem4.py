class Complex:
    def __init__(self,r,i):
        self.r =r # store the real part inside this object
        self.i =i # store the imaginary part inside this object
    
    def __add__(self,c2): #self refer to c1 and c2 refer c2, then it overload the operator so we add two complex number
        return Complex(self.r + c2.r, self.i + c2.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1=Complex(1,2)
print(c1)
c2=Complex(3,4)
print(f"Add of c1 and c2 is {c1 +c2}")  # it call add function
