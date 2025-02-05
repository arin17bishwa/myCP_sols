from typing import Tuple


class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def diameter(self, root: Node):
        ans = 0

        def dfs(node: Node) -> Tuple[int, int]:
            if not node:
                return -1, -1
            left_max_self, left_max_continued = dfs(node.left)
            right_max_self, right_max_continued = dfs(node.right)
            return (
                max(
                    left_max_self,
                    right_max_self,
                    left_max_continued + right_max_continued + 2,
                ),
                max(left_max_continued, right_max_continued) + 1,
            )

        return max(dfs(root))
