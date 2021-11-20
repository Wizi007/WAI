import re

mapping = {
    }

def retreive_from_file():
    file = open("info.txt", "r")
    var = file.readlines()
    count = 0
    while count < len(var):
        a = var[count]
        b = var[count + 1]
        if var[count] in mapping:
            mapping[a.rstrip('\n')].append(b)
        else:
            mapping[a.rstrip('\n')] = []
            mapping[a.rstrip('\n')].append(b)
        count = count + 2
    file.close()

retreive_from_file()

