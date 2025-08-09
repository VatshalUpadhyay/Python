import os
folders= os.listdir("Data")


for folder in folders:
    print(folder)
    print(os.listdir(f"Data/{folder}"))
    # it also print Day8 file 