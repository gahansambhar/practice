def nCr(n, r):
    if r == 0 or n == r:
        return 1

    if r == 1:
        return n

    else:
        return nCr(n - 1, r - 1) + nCr(n - 1, r)


print(nCr(3, 1))
