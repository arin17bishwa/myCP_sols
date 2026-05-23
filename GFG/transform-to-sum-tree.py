class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def toSumTree(self, root: Node):

        def dfs(node: Node | None) -> int:
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            t, node.data = node.data, left + right
            return t + node.data

        dfs(root)

        return root
