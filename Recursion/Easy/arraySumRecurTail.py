def recurSumTail(A, N, Sum=0):
    if N == 1:
        return Sum + A[N - 1]
    else:
        return recurSumTail(A, N - 1, A[N - 1] + Sum)


A = [2, 55, 1, 7]
N = len(A)
print(recurSumTail(A, N))
