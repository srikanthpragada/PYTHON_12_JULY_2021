import os

allfiles = os.walk(r"d:\classroom\july12\demo")

for (dirname, dirs, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)

