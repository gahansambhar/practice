def isPalRec(string):
    size = len(string)

    if len(string) <= 1:
        return True

    if string[0] != string[size - 1]:
        return False
    else:
        return isPalRec(string[1 : size - 1])


print(isPalRec("malayalam"))
print(isPalRec("not a plain"))
