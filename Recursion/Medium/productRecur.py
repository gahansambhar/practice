def prod(x, y):
    if y > x:
        x, y = y, x
        return prod(x, y)

    else:
        if y == 0:
            return 0
        return x + prod(x, y - 1)


print(prod(5, 100))
