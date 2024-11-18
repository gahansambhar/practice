def printNos(n):

    if n == 1:
        return "1"

    else:
        return "{} {}".format(printNos(n - 1), str(n))


print(printNos(5))
