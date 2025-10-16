from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def func(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return (
                n1.val == n2.val and func(n1.left, n2.left) and func(n1.right, n2.right)
            )

        return func(p, q)
