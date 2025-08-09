# here i delete the word from list
def remove(l,word):
    for item in l:
        l.remove(word)
        return l

l=["vatshal","harry","Rose","Lee"]
print(remove(l,"Lee")) # here lee word is delete from l list mai l ke jagh k variable bhi le skta hu for easy reading maine dono jagh l liya
# like this ->
k=["vatshal","harry","Rose","Lee"]
print(remove(k,"Lee"))

# here i write code for i strip or cut the alphabet from name 
def cut(l,alphabet):
    n=[] # we use new list becz if we modify original list all data will removed
    for item in l: # we use for loop it go for every item in list nhi to hume manually karna padta like this result.append(l[0].strip("se")) aise
        if not(item==alphabet):

            n.append(item.strip(alphabet)) # we use append to modify empty string to add or strip the e
    return n # here you have to return ni to (none) dikhayega 

l=["vatshal","harry","Rose","Lee"]
print(cut(l,"se"))

# important point
'''in line17 agar item(vatshal,..) alphabet(se) ke equal ni h to true return hoga and for "Rose" return false so uske liye strip function use 
hoga aur strip hone ke baad append hoga mtlb (add) hoga and for vatshal ni hoga aise hi add hoga new string mai modify hone ke baad
same as for "harry" and "lee" lee ka (ee) strip hokar add hoga
''' 