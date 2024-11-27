def isPalindrome(string):
    size = len(string)

    if len(string) <= 1:
        return True

    if string[0] != string[size - 1]:
        return False

    else:
        return isPalindrome(string[1 : size - 1])


def longestPalindrome(string):
    if len(string) == 0:
        return 0

    if isPalindrome(string):
        return len(string)
    else:
        return max(
            longestPalindrome(string[: len(string) - 1]), longestPalindrome(string[1:])
        )


print(longestPalindrome("banana"))
