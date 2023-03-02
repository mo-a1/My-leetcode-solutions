"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x < 10:
        return True
    return str(x) == str(x)[::-1]
