import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nums
        heap = []

        for i in arr:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
