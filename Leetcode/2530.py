from typing import List
import heapq
from math import ceil


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        ans = 0
        for _ in range(k):
            mx = -heapq.heappop(heap)
            ans += mx
            heapq.heappush(heap, -ceil(mx / 3))
        return ans
