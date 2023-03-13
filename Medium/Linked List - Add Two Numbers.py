"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
 and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
import re
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sol1 = ""
        sol2 = ""
        crn = l1
        while crn:
            sol1 += str(crn.val)
            crn = crn.next
        crn = l2
        while crn:
            sol2 += str(crn.val)
            crn = crn.next
        try:
            sol1 = int(sol1[::-1].lstrip("0"))
        except ValueError:
            sol1 = 0
        try:
            sol2 = int(sol2[::-1].lstrip("0"))
        except ValueError:
            sol2 = 0
        temp = [int(i) for i in str(sol1 + sol2)[::-1]]
        result = ListNode(temp[0])
        crn = result
        for i in temp[1:]:
            crn.next = ListNode(i)
            crn = crn.next
        return result