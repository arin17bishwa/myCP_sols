from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        idx = 0
        while q:
            last_val = -float("inf") if idx % 2 == 0 else float("inf")
            for _ in range(len(q)):
                curr = q.popleft()
                if (
                    curr.val % 2 == idx % 2
                    or (idx % 2 != 0 and last_val <= curr.val)
                    or (idx % 2 == 0 and last_val >= curr.val)
                ):
                    return False
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                last_val = curr.val
            idx += 1
        return True
