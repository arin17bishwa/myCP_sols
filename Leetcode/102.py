from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q: deque[TreeNode] = deque([root])
        ans: list[list[int]] = []

        while q:
            row: list[int] = []
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue
                row.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            if row:
                ans.append(row[:])

        return ans
