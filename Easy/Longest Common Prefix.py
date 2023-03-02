"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    res = ""
    for a in zip(*strs):
        if len(set(a)) == 1:
            res += a[0]
        else:
            return res
    return res
