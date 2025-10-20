class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def getKClosest(self, root: Node, target: int, k: int) -> list[int]:
        arr = []

        def dfs(node: Node | None):
            nonlocal arr
            if not node:
                return
            dfs(node.left)
            arr.append(node.data)
            dfs(node.right)

        dfs(root)

        candidates = sorted(arr, key=lambda x: (abs(x - target), x))
        return candidates[:k]
