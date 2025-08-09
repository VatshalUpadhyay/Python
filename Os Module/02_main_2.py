# if you want folder in data directory or folder(directory and folders are same)
import os
for i in range (1,100):
    os.mkdir(f"Data/Day{i}")
    # it create 100 folder in data 

# if you want to rename the Day to tutorial then use below code->
# import os
# for i in range(1,100):
#     os.rename(f"Data/Day{i}",f"Data/Tutorial {i}")