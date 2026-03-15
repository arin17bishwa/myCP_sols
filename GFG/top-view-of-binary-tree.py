from typing import Optional


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root: Optional[Node]):
        view: dict[int, tuple[int, int]] = dict()

        def dfs(node: Optional[Node], idx: int = 0, depth: int = 0):
            nonlocal view

            if not node:
                return

            if idx not in view:
                view[idx] = (depth, node.data)
            elif depth < view[idx][0]:
                view[idx] = (depth, node.data)

            dfs(node.left, idx - 1, depth + 1)
            dfs(node.right, idx + 1, depth + 1)

        dfs(root, idx=0, depth=0)

        return [view[i][1] for i in sorted(view.keys())]
