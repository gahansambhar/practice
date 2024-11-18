def findBinary(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n % 2 + 10 * (findBinary(int(n // 2)))


print(findBinary(7))
