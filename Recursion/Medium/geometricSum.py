def geo(n):
    if n == 0:
        return 1.0

    else:
        return (1 / 3) ** n + geo(n - 1)


print(geo(5))
