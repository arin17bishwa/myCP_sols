import heapq
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        ans = 0
        while k and heap[0] < 0:
            x = -heapq.heappop(heap)
            ans += x
            k -= 1
            heapq.heappush(heap, -ceil(x / 3))
        return ans
