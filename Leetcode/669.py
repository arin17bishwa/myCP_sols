from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dfs(self)->None:
        ans=[]
        def _dfs(node:TreeNode)->None:
            if not node:
                return
            _dfs(node.left)
            ans.append(node.val)
            _dfs(node.right)

        _dfs(self)
        print(ans)


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


