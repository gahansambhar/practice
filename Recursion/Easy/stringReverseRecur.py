def stringReverse(string):
    if len(string) <= 1:
        return string

    return string[-1] + stringReverse(string[: len(string) - 1])


print(stringReverse("Geeks for Geeks"))
