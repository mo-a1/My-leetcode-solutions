"""
Given two binary strings a and b, return their sum as a binary string.
"""


def add_binary(a: str, b: str) -> str:
    return bin(int(a, base=2) + int(b, base=2)).replace("0b", "")

