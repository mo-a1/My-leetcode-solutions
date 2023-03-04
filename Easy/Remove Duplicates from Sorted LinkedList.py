"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
 Return the linked list sorted as well.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    cur_node = head
    while cur_node and cur_node.next:
        if cur_node.val == cur_node.next.val:
            cur_node.next = cur_node.next.next
        else:
            cur_node = cur_node.next
    return head
