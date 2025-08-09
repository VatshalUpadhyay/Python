marks={
    "Vatshal":98,
    "Rajesh":40,
    "Rakesh":87,
    0:"Suresh" 
}
print(marks.items()) # it give you all items in it
print(marks.keys()) # it give you which is in left side like "Vatshal","Rajesh"...
print(marks.values())# it give you which is in right side like 98,"Suresh"
marks.update({"Vatshal":100,"Lee":90}) # it update the marks then we print we also add people in it
print(marks)
print(marks["VatshalJi"]) # it give you error,      ->point 2, write in [] this bracket 
print(marks.get("VatshalJi")) # it give you none
#  the main difference in line 12 and 13 of error and none

