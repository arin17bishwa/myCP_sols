class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def sumOfLongRootToLeafPath(self, root: Node):
        mx_sum = 0
        mx_height = 0

        def dfs(node: Node, height: int = 0, curr_sum: int = 0):
            nonlocal mx_sum, mx_height
            if not node:
                if height > mx_height:
                    mx_sum = curr_sum
                    mx_height=height
                elif height == mx_height:
                    mx_sum = max(mx_sum, curr_sum)
                return
            curr_sum += node.data
            dfs(node.left, height + 1, curr_sum)
            dfs(node.right, height + 1, curr_sum)
            return

        dfs(root)
        return mx_sum
