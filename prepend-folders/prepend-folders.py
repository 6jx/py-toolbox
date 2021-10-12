import os
lsdir = os.listdir(path='.')
folders = []
print("Folder Name Prepender")
ic = input("What do you wish to prepend this folder with?")
prepend = ic
for x in lsdir:
    isDir = os.path.isdir(x)
    if isDir is True and x != __file__:
        folders.append(x)
for x in folders:
    try:
        os.replace(x, prepend + x)
        print(x + " ===> " + prepend + x)
    except:
        print("Failed to rename a folder.")
