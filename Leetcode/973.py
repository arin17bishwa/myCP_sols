import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: list[tuple[int, int, int]] = []

        for x, y in points:
            heapq.heappush(heap, (-(x * x + y * y), x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        return [[i, j] for _, i, j in heap]
