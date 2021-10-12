import imghdr
import os
import pathlib
for root, dirs, files in os.walk('./'):
    print(root)
    dires = dirs
    filez = files
    for dor in dires:
        print(dor)
        listdir = os.listdir(dor)
        for file in listdir:
            supported = [".gif", ".jpeg", ".png", ".jpg", ".tiff"]
            nameonly = os.path.splitext("./" + dor + "/" + file)[0]
            file_extension = pathlib.Path(file).suffix
            if file_extension not in supported:
                print("Unsupported File Type")
            if file_extension.lower() in supported:
                actual = imghdr.what("./" + dor + "/" + file)
                print("hw")
                try:
                    os.rename("./" + dor + "/" + file, nameonly + "." + actual)
                    print("Renamed Successfully")
                except:
                    print("Failed on " + file + ", attempted to rename from" + nameonly)
