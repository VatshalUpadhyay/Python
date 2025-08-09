# star printing
'''
For n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 *******
*********

'''

n = int(input("Enter the number: "))
for i in range(1, n+1):   #1 se n tak i chalega
    print(" "* (n-i), end="") # in first line or star (n-i) space print hoti h like 3 ke liye = 2 space + *(star)
    print("*"* (2*i-1), end="") # we use end="" becz new line na aajaye
    print("") # here it print new line we cant use \n becz it give extra new line
 # in line 20 for star we use odd number series