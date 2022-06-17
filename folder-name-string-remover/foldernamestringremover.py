import os
ic1 = input("Input the string which you wish to remove from all folders in this directory (CaSe SeNsItIvE, and space sensitive)    ")
dirlist = os.listdir(path=".")
for i in dirlist:
    filename, file_extension = os.path.splitext(i)
    y = filename.replace(ic1,'')
    if os.path.isdir(i) == True:
        try:
            os.replace(i,y + file_extension)
            print(i, "==>", y + file_extension)
        except:
            ("Failed to rename", i)
