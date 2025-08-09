x=10 #global variable

def my_function():
    global x # now it defined globally outside function alsp
    x=4
    y=5 #local variable only in function
    print(y)

my_function() # it print y=5
print(x) #here it print 4 not 10 becz i use global keyword
# print(y) this will give you error becz it not defined globally it is local variable not axxess outside function