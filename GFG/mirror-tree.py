from typing import Optional


class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def mirror(self, root: Optional[Node]):

        def dfs(node: Optional[Node]) -> Optional[Node]:
            if not node:
                return None
            node.left, node.right = dfs(node.right), dfs(node.left)
            return node

        return dfs(root)
