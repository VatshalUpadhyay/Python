class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j ")

class ThreeDVetor(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")

a=TwoDVector(1,2)
a.show()
b=ThreeDVetor(2,3,4)
b.show()
