class Animal:
    pass

class pets(Animal):
    pass

class Dog(pets):
    @staticmethod # i use this becz i dont want to use self in bark i dont need any objects property jus want to print 
    def bark():
        print("Bow Bow!")

d=Dog()
d.bark()