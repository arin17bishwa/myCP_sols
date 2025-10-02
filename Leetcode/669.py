from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if root is None:
            return None

        def dfs(node: Optional[TreeNode]):
            if not node:
                return None
            val = node.val
            if val < low:
                return dfs(node.right)
            elif val > high:
                return dfs(node.left)
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node

        return dfs(root)
