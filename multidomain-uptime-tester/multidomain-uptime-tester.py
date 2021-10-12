import pathlib
import requests
print("6JX's simple domain checker!")
print("----------------------------")
print("Checking for required files...")
dtx = "domains.txt"
dt = pathlib.Path(dtx)
if dt.exists ():
    print(dtx, "found!")
else:
    open(dtx,"w+")
    print(dtx, "has been created!")
print("Running Tester...")
print("----------------------------")
with open(dtx) as f:
    c = f.readlines()
dr = [x.strip("\n") for x in c]
d = [x for x in dr if x]
oldlen = len(d)
gd = []
while d:
    for i in d:
        if i[:7] == "http://" or i[:8] == "https://":
            r = requests.get(i)
        else:
            r = requests.get("http://" + i)
        rcode = r.status_code
        if rcode == 200:
            print(i, 'is online!')
            d.remove(i)
            gd.append(i)
        else:
            print(i, 'is offline!')
            d.remove(i)
with open(dtx, 'w') as f:
    for i in gd:
        f.write("%s\n" % i)
print("done!")
print(str(len(gd)) + " domains are online out of your list of " + str(oldlen) + ".")
