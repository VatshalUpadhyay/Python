with open("this_q7.txt") as f:
    content=f.read()

with open ("this_copy.txt", "w")as f:
    f.write(content)