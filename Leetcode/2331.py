from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if node.left is None:
                return bool(node.val)
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            if node.val == 2:
                return left_val or right_val
            return left_val and right_val

        return dfs(root)
