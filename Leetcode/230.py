from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        curr_cnt = 0

        def dfs(node: TreeNode | None) -> int:
            nonlocal curr_cnt, k
            if not node:
                return -1

            left = dfs(node.left)
            if left >= 0:
                return left

            curr_cnt += 1
            if curr_cnt == k:
                return node.val

            right = dfs(node.right)
            if right >= 0:
                return right
            return -1

        return dfs(root)
