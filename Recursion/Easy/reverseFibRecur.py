def fibo(N, a=0, b=1):
    if N == 1:
        return str(a)
    else:
        return str(fibo(N - 1, b, a + b)) + " " + str(a)


print(fibo(10))
