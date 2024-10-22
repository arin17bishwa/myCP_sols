import heapq
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        heap = []
        queue = deque([root])
        while queue:
            lvl_sum: int = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                lvl_sum += curr.val

            heapq.heappush(heap, lvl_sum)
            if len(heap) > k:
                _ = heapq.heappop(heap)
        if len(heap) < k:
            return -1
        return heap[0]
