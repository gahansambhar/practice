def countRecur(coins, n, sum):
    if n == 0:
        return 0

    if sum == 0:
        return 1

    if sum - coins[n - 1] < 0:
        return countRecur(coins, n - 1, sum)

    else:
        return countRecur(coins, n, sum - coins[n - 1]) + countRecur(coins, n - 1, sum)


def count(coins, sum):
    return countRecur(coins, len(coins), sum)


coins = [4]
sum = 5
print(count(coins, sum))
