from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            ans = node.val + dfs(node.left) + dfs(node.right)
            freq[ans] += 1
            return ans

        dfs(root)

        return [i for i, j in freq.items() if j == max(freq.values())]
