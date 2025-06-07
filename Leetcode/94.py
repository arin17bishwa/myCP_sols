from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], curr=None):
            if curr is None:
                curr = []
            if not node:
                return curr
            dfs(node.left, curr)
            curr.append(node.val)
            dfs(node.right, curr)

        ans = []
        _ = dfs(root, ans)
        return ans
