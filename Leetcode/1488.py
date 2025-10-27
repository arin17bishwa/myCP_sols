# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode | None, running_max: int) -> int:
            if not node:
                return 0

            return (
                (1 if node.val >= running_max else 0)
                + dfs(node.left, max(node.val, running_max))
                + dfs(node.right, max(node.val, running_max))
            )

        return dfs(root, -(10**9))
