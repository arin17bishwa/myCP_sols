from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: list[int] = []

        def dfs(node: Optional[TreeNode]):
            nonlocal ans
            if not node:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans
