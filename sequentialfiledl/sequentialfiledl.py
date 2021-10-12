import requests
import os
import sys
print("Seq File DL")
folderurl = input("Directory Of Files To Be Downloaded:   ")
extension = "." + input("File Extension (no period):   ")
dlrange = input("Number Of Files:   ")
folder = input("Output Directory (No Trailing Slash):     ")
try:
    os.mkdir(folder)
    print("created folder")
except:
    print("Cannot Create Folder")
    sys.exit()
for i in range(1,int(dlrange) + 1):
    theurl = folderurl + str(i) + extension
    print("Downloading", theurl)
    with open(folder + "/" + str(i) + extension, 'wb') as output:
        output.write(requests.get(theurl).content)
print("Done!")
