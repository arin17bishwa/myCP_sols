import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap)
        ans: int = 0
        while len(heap) > 1 and heap[0] < k:
            ans += 1
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, min(a, b) * 2 + max(a, b))
        return ans
