from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -(10**18)

        def dfs(node: TreeNode | None) -> int:
            nonlocal ans
            if not node:
                return -(10**18)

            left = dfs(node.left)
            right = dfs(node.right)
            curr = max(node.val, node.val + left, node.val + right)
            ans = max(ans, left, right, curr, left + node.val + right)
            return curr

        dfs(root)
        return ans
