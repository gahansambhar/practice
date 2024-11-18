def stringLen(string):
    if string == "":
        return 0
    else:
        return 1 + stringLen(string[1:])


print(stringLen("GEEKSFORGEEKS"))
