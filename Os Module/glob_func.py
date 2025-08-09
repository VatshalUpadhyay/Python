# it give you all the txt files which you have in you current working directory

import glob
txt_files=glob.glob("*.txt") #if you usee ("**/*.txt) it give all txt file in sub-directories too
print("TEXT files are present in directory",txt_files)