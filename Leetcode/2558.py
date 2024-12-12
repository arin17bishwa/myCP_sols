import heapq
from math import sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-i for i in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            mx = -heapq.heappop(heap)
            heapq.heappush(heap, -int(sqrt(mx)))
        return -sum(heap)
