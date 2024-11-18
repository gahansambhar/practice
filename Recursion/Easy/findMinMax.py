def findMinMax(A, N, minim=float("inf"), maxim=float("-inf")):
    if N == 0:
        return (minim, maxim)
    else:
        minim = min(minim, A[N - 1])
        maxim = max(maxim, A[N - 1])
        return findMinMax(A, N - 1, minim, maxim)


A = [1, 4, 45, 6, -50, 10, 2]
N = len(A)
print(findMinMax(A, N))
