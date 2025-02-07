from typing import Optional, List


class Node:
    def init(self, val: int):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def inOrder(self, root: Optional[Node]) -> List[int]:
        ans = []

        def dfs(node: Optional[Node]):
            nonlocal ans
            if not node:
                return
            dfs(node.left)
            ans.append(node.data)
            dfs(node.right)

        dfs(root)
        return ans
