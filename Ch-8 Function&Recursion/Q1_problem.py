
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#        return c
# a=int(input("Enter the number: "))
# b=int(input("Enter the number: "))
# c=int(input("Enter the number: "))

# greater_number=greatest(a,b,c)
# print(f"The greatest number is: {greater_number}")   


# i use both the return function and normal way also


a=3
b=5
c=6
def greatest(a,b,c):
     if(a>b and a>c):
         print("this is big" )
         return a
     elif(b>a and b>c):
          print("this is big")
          return b
     elif(c>a and c>b):
         print("this is big")
         return c


print(f"the value is {greatest(a,b,c)}")