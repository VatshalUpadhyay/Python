m1="Makes a lot of money"
m2="Buy this"
m3="click on this"
m4="subscribe this"

comment=input("Enter your comment:")

if((m1 in comment)or (m2 in comment) or (m3 in comment) or (m4 in comment)):
    print("This comment is spam")

else:
    print("This comment is not spam")    