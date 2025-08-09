'''
star printing case=3
example (for n=4 )
****
*  *
*  *
****
'''
n=int(input("Enter value of n:"))
for i in range (1, n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="") #here it print first *
        print(" "*(n-2),end="") # then it print space for time n-2
        print("*",end="") # then it print again *
    print("")