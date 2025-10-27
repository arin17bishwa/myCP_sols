from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode | None, left: int, right: int):
            if not node:
                return True
            return (
                left < node.val < right
                and dfs(node.left, left, node.val)
                and dfs(node.right, node.val, right)
            )

        return dfs(root, -(1 << 32), 1 << 32)
