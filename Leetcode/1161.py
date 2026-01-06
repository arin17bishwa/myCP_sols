from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        tot=defaultdict(int)

        def dfs(node:Optional[TreeNode], lvl:int=1):
            nonlocal tot
            if not node:
                return

            tot[lvl]+=node.val
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)

        dfs(root,1)

        mx=-(10**9)
        ans=1
        for k,v in tot.items():
            if v>mx:
                mx=v
                ans=k
        return ans

