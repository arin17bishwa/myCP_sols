class Solution:
    def isDeadEnd(self, root) -> bool:
        if not root:
            return False

        def dfs(node, mn, mx) -> bool:
            if not node:
                return False
            if node.left is None and node.right is None:
                return mx < mn or mx == mn == node.data

            curr: int = node.data

            return dfs(node.left, mn, curr - 1) or dfs(node.right, curr + 1, mx)

        return dfs(root.left, 1, root.data - 1) or dfs(root.right, root.data + 1, 10**9)
