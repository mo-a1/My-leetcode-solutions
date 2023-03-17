"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
 magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


def can_construct(ransom_note: str, magazine: str) -> bool:
    for char in ransom_note:
        if char in magazine:
            magazine = magazine.replace(char, "", 1)
        else:
            return False
    return True
