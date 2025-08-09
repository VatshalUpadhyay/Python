def generatetable(n):
    table=""
    for i in range(1,11):
        table += f"{n}x{i}={n*i}\n"

    with open(f"tables/table_{n}","w") as f: 
        f.write(table) # it write table in folder(table) from  2 to 20

for i in range(2,21):
    generatetable(i)