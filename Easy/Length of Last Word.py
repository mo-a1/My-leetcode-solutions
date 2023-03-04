"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""

import re


def length_of_last_word(s: str) -> int:
    return len(re.findall(r"\w+", s)[-1])
