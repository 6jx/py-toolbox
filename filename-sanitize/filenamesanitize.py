import os
lsdir = os.listdir(path='.')
files = []
allowedchars = "abcdefghijklmnopqrstuvwxyz.- _=+"
print("Folder File Name Sanitizer")
for x in lsdir:
    isDir = os.path.isdir(x)
    if isDir is False and x != __file__:
        files.append(x)
for x in files:
    filename, file_extension = os.path.splitext(x)
    charlist = list(filename)
    goodname = []
    for char in charlist:
        if char.lower() in allowedchars:
            goodname.append(char)
    y = ''.join(map(str, goodname))
    try:
        os.replace(x, y + file_extension)
        print(x + " ===> " + y + file_extension)

    except:
        print("Failed to rename a file.")
