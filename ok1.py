import re

mapping = {
    }

def retreive_from_file():
    file = open("info.txt", "r")
    var = file.readlines()
    count = 0
    while count < len(var):
        a = var[count]
        a = a.rstrip("\n")
        b = var[count + 1]
        b = b.rstrip("\n")
        if a in mapping:
            mapping[a].append(b)
        else:
            mapping[a] = []
            mapping[a].append(b)
        count = count + 2
    file.close()

retreive_from_file()

