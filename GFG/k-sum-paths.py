from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def sumK(self, root: Optional[Node], k: int) -> int:
        ans: int = 0
        seen: defaultdict = defaultdict(int)
        seen[0] = 1

        def dfs(node: Optional[Node], curr_sum: int = 0):
            if not node:
                return
            nonlocal seen, ans, k
            curr_sum += node.data
            ans += seen[curr_sum - k]
            seen[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            seen[curr_sum] -= 1

        dfs(root)
        return ans
