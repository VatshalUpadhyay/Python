def f_to_c(f): # function defination
    return 5*(f-32)/9

fahrenheit=int(input("enter temperature in F: "))
print(f"{f_to_c(fahrenheit)} degree Celsius")
# here i round this to 2 decimal place
print(f"{round(f_to_c(fahrenheit),2)} degree Celsius")
# in function call fahrenheit ke andar jo number input hoga wo (f) ke place par jayega function defination mai phir calculation hoga
