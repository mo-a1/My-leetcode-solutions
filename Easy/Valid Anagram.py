"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
 the original letters exactly once.
"""
import collections


def is_anagram(s: str, t: str) -> bool:
    return False if len(s) != len(t) else not collections.Counter(s) - collections.Counter(t)
