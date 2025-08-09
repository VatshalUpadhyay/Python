# sum of n natural numner

def sum(n):
    if(n==1):
        return 1
        
    return sum(n-1) + n

number=int(input("Enter the number: "))

print(f"the sum is {sum(number)}")