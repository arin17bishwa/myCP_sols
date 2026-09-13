class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def longestConsecutive(self, root: Node | None) -> int:
        if not root:
            return -1

        ans = -1

        def dfs(node: Node | None, parent: int, curr: int) -> int:
            nonlocal ans
            ans = max(ans, curr)

            if not node:
                return curr

            curr = curr + 1 if node.data - parent == 1 else 1
            return max(
                dfs(node.left, node.data, curr), dfs(node.right, node.data, curr)
            )

        dfs(root, 10**9, 1)

        return ans if ans > 1 else -1
