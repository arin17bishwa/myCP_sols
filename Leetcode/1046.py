import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)

            if x == y:
                continue
            heapq.heappush(heap, -abs(x - y))

        return 0 if not heap else -heap[0]
