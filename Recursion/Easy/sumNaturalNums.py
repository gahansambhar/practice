def recurSum(n):
    if n <= 1:
        return 1

    else:
        return n + recurSum(n - 1)


print(recurSum(4))
