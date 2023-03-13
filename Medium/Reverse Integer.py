"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


def reverse(x: int) -> int:
    rs = str(x)[::-1].strip("-0")
    if x == 0 or rs.zfill(10) > "2147483647":
        return 0
    else:
        return int(rs) if x > 0 else -int(rs)


# solution on leetcode.com
# https://leetcode.com/problems/reverse-integer/solutions/3270178/easy-python-solution/
