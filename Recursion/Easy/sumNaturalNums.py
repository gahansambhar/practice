def recurSum(n):
    # Ensuring that the program does not fail for 0 or negative input
    if n <= 1:
        return 1

    else:
        return n + recurSum(n - 1)


print(recurSum(4))
