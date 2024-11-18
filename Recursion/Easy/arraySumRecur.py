# A is the array
# N is the number of elements


def recurSum(A, N):
    if N == 1:
        return A[N - 1]

    ans = recurSum(A[: N - 1], N - 1) + A[N - 1]
    return ans


arr = [1, 2, 3, 4, 5]
N = len(arr)

ans = recurSum(arr, N)
print(ans)
