def printNos(n):
    if n == 1:
        print("1", end=" ")
    else:
        print(str(n), end=" ")
        printNos(n - 1)


printNos(7)
