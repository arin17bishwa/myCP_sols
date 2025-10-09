class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def postOrder(self, root: Node):
        ans: list[int] = []

        def dfs(node: Node | None):
            nonlocal ans
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.data)

        dfs(root)
        return ans
