class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def findMedian(self, root: Node) -> float | int:
        arr = []

        def dfs(node: Node | None):
            nonlocal arr
            if not node:
                return
            dfs(node.left)
            arr.append(node.data)
            dfs(node.right)

        dfs(root)
        n = len(arr)
        return arr[n // 2] if n & 1 else arr[(n + 1) // 2 - 1]
