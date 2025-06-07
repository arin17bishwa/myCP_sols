class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def findMaxFork(self, root: Node, k: int):
        candidate: int = -1

        def dfs(node: Node):
            nonlocal candidate
            if not node:
                return
            if node.data <= k:
                candidate = node.data
                dfs(node.right)
            else:
                dfs(node.left)

        dfs(node=root)
        return candidate
