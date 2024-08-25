from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []

        def dfs(node: Optional[TreeNode], arr: List[int]):
            if not node:
                return
            dfs(node.left, arr)
            dfs(node.right, arr)
            arr.append(node.val)

        dfs(root, ans)
        return ans
