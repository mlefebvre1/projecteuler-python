def is_palindrome(n):
    n = str(n)
    if len(n) > 1:
        if n == n[::-1]:
            return 1
        else:
            return 0
    else:
        return 1
