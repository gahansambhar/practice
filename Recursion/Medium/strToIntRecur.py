def strToInt(string):
    if len(string) == 1:
        return int(string)

    else:
        return int(string[0]) * 10 ** (len(string) - 1) + strToInt(string[1:])


print(strToInt("1234"))
