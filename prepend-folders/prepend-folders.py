import os
lsdir = os.listdir(path=".")
print("Folder Name Prepender")
ic = input("Input String To Prepend      ")
for i in lsdir:
    if os.path.isdir(i) == True:
        try:
            os.replace(i, ic + i)
            print(i, "=>", ic + i)
        except:
            print("Failed to rename", i)
