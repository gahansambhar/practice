def printn(n):
    if n == 0:
        pass
    else:
        print("*", end=" ")
        printn(n - 1)


def printPyramid(base, i=1):
    if i > base:
        pass
    else:
        printn(i)
        print("")
        printPyramid(base, i + 1)


def printInvertedPyramid(base):
    if base > 0:
        printn(base)
        print("")
        printInvertedPyramid(base - 1)
    if base == 0:
        print("", end="")


printPyramid(5)
printInvertedPyramid(6)
