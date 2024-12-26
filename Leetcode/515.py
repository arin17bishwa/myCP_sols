from collections import deque
from typing import List, Optional, Deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q: Deque[TreeNode] = deque([root])
        ans: List[int] = []

        while q:
            mx = -float("inf")
            for _ in range(len(q)):
                curr = q.popleft()
                mx = max(mx, curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            ans.append(mx)

        return ans
