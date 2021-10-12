import json
import os
ic1 = input("Enter the full name of the file which you want to convert.")
filename, file_extension = os.path.splitext(ic1)
supported = [".txt", ".json"]
if file_extension.lower() not in supported:
    ic2 = input("Please Specify Extension.")
    if ic2[0] == '.':
        file_extension = ic2
    if ic2[0] == 'j' or 't':
        file_extension = "." + ic2
    else:
        print("Retry")
openfile = open(filename + file_extension, "r")
if file_extension == ".txt":
    list = openfile.readlines()
    cleanlist = [x.strip("\n") for x in list]
    cleanlist.remove("")
    jsonStr = json.dumps(cleanlist)
    with open(filename + ".json", "w") as f:
        f.write(jsonStr)
    print("Dumped to file, " + filename+".json")
if file_extension == ".json":
    jsonread = json.load(openfile)
    newtxt=open(filename + ".txt","w")
    newtxt.close()
    apptxt=open(filename + ".txt","a")
    for i in jsonread:
        apptxt.write(i + "\n")
    apptxt.close()
    print("Dumped to file, " + filename+".txt")
