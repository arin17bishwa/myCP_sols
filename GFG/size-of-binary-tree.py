# Definition for Node
from typing import Optional


class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def getSize(self, root: Optional[Node]) -> int:

        def dfs(node: Optional[Node]) -> int:
            if not node:
                return 0
            return dfs(node.left) + dfs(node.right) + 1

        return dfs(root)
