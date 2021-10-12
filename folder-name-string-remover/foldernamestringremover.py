import os
lsdir = os.listdir(path=".")
ic1 = input("String to remove from all files? (CaSe SeNsItIvE)    ")
files = []
for x in lsdir:
    isDir = os.path.isdir(x)
    if isDir is False and x != __file__:
        files.append(x)
for x in files:
    filename, file_extension = os.path.splitext(x)
    y = filename.replace(ic1,'')
    try:
        os.replace(x, y + file_extension)
        print(x, "===>", y + file_extension)
    except:
        print("Failed to rename a file.")
