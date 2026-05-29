from collections import defaultdict


# Structure of binary tree node
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class Solution:
    def verticalSum(self, root: Node | None) -> list[int]:
        if not root:
            return []

        d = defaultdict(int)

        def dfs(node: Node | None, pos: int) -> None:
            nonlocal d
            if not node:
                return

            d[pos] += node.data
            dfs(node.left, pos - 1)
            dfs(node.right, pos + 1)

        dfs(root, 0)

        return [d[k] for k in sorted(d.keys())]
