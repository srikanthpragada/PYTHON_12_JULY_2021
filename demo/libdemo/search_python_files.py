import os


def containsString(filename, findstring):
    try:
        with open(filename, "rt") as f:
            return findstring in f.read()
    except:
        return False


startdir = r"d:\classroom\july12\demo"
findstr = "input"

allfiles = os.walk(startdir)

for (dirname, dirs, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            filename = dirname + "\\" + f
            if containsString(filename, findstr):
                print(filename)
