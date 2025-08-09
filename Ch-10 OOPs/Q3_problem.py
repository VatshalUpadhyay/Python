class Demo():
    a=4

o=Demo()
print(o.a) #Print the class attribute becz instance attribute not present 
o.a=0 # Instance attribute is set
print(o.a) #Prints the instance attribute becz instance attribute is present
print(Demo.a)# print the class attribute

# so the answer of this question is no classs attribute change 