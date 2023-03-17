"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
from functools import lru_cache


def first_uniq_char(s: str) -> int:
    @lru_cache(26)
    def find_uniq(character):
        return False if s.count(character) > 1 else True

    for ndx, char in enumerate(s):
        if find_uniq(char):
            return ndx
    return -1

