from euler.utils import is_palindrome


def test_is_palindrome():
    assert(is_palindrome(101))
    assert(not is_palindrome(112))
