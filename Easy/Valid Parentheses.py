"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
import queue


def is_valid(s: str) -> bool:
    q = queue.LifoQueue()
    pr = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for i in s:
        if i in ")]}":
            if q.empty() or pr[q.get_nowait()] != i:
                return False
        else:
            q.put_nowait(i)
    return q.empty()

