from typing import List, Dict, Set
import heapq


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = nums
        heap: List[int] = []
        seen: Set[int] = set()
        for i in arr:
            if i in seen:
                continue
            heapq.heappush(heap, i)
            seen.add(i)
            if len(heap) > 3:
                seen.remove(heapq.heappop(heap))
        return heap[1] if len(heap) == 2 else heap[0]
