"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.traverse_list = []

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.inorder_traversal(root.left)
            self.traverse_list.append(root.val)
            self.inorder_traversal(root.right)
        return self.traverse_list
