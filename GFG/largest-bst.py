from typing import Optional


class Node:
    def __init__(self, data: int, left=None, right=None):
        self.data: int = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class Solution:
    def largestBst(self, root: Optional[Node]) -> int:
        mx = 10**9
        ans = 0

        def dfs(node: Optional[Node]) -> tuple[int, int, int]:
            nonlocal ans
            if not node:
                return mx, -mx, 0
            left = dfs(node.left)
            right = dfs(node.right)

            condition = left[1] < node.data < right[0]

            if not condition:
                return mx, -mx, -mx

            this = (
                min(left[0], node.data),
                max(right[1], node.data),
                left[2] + right[2] + 1,
            )

            ans = max(ans, this[-1])
            return this

        dfs(root)

        return ans
