with open ("file.txt","r")as f:
    f.seek(10) # move to the 10th byte in file
    data=f.read(5)

    print(data)
    print(f.tell()) # it tell your current poisition where are you in file in this case 15 bytes 