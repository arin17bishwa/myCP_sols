from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans: list[list[int]] = []
        if not root:
            return []

        from_left: int = 1
        d = deque([root])

        while d:
            this_layer: list[int] = []
            for _ in range(len(d)):
                curr = d.popleft()
                this_layer.append(curr.val)
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            ans.append(this_layer[:] if from_left else this_layer[::-1])

            from_left ^= 1
        return ans
