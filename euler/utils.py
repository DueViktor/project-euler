def is_palindrome(x: int) -> bool:
    """ true if x is a palindrome """
    return str(x) == str(x)[::-1]
