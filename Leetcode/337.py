from functools import cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        @cache
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if not node:
                return 0, 0

            left_mx, left_mx_root_not_taken = dfs(node.left)
            right_mx, right_mx_root_not_taken = dfs(node.right)

            return (
                node.val + left_mx_root_not_taken + right_mx_root_not_taken,
                max(left_mx, left_mx_root_not_taken)
                + max(right_mx, right_mx_root_not_taken),
            )

        return max(dfs(root))
