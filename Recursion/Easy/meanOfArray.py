# N is the number of items in the array
# A is the array itself


def findMean(A, N):
    if N == 1:
        return A[N - 1]

    else:
        meanCalc = ((findMean(A[: N - 1], N - 1) * (N - 1)) + A[N - 1]) / N

        return meanCalc


A = [1, 2, 3, 4, 5]
N = len(A)
print(findMean(A, N))
