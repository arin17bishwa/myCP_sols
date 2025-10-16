from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def func(node: TreeNode | None) -> int:
            nonlocal ans
            if not node:
                return 0
            left_ht = func(node.left)
            right_ht = func(node.right)
            ans = max(ans, left_ht + right_ht)
            return 1 + max(left_ht, right_ht)

        func(root)

        return ans
