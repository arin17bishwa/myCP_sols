# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode | None, mx_seen: int = -(10**9)) -> int:
            if not node:
                return 0

            return (
                int(node.val >= mx_seen)
                + dfs(node.left, max(mx_seen, node.val))
                + dfs(node.right, max(mx_seen, node.val))
            )

        return dfs(root)
