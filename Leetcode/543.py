from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return -1, -1
            left_self, left_mixed = dfs(node.left)
            right_self, right_mixed = dfs(node.right)
            return (
                max(left_self, right_self, left_mixed + right_mixed + 2),
                max(left_mixed, right_mixed) + 1,
            )

        return max(dfs(root))
