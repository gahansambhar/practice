def sumOfDigits(n):
    if int(n) <= 9:
        return int(n)
    else:
        return int(str(n)[0]) + sumOfDigits(str(n)[1:])


print(sumOfDigits(12345))
