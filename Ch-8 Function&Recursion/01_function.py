# function defination
def avg():
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    c=int(input("Enter the number: "))
    average=(a+b+c)/3
    print(average)
    return(average) # it return average in variable a so when you print it give you the value

a=avg() # Function call
 # Function call
print("value of a is",a) 
avg() # second time function call