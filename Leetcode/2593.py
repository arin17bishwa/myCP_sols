import heapq
from typing import List, Tuple, Set


class Solution:
    def findScore(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        heap: List[Tuple[int, int]] = [(ele, idx) for idx, ele in enumerate(arr)]
        heapq.heapify(heap)
        ans = 0
        marked: Set[int] = set()
        while heap:
            ele, idx = heapq.heappop(heap)
            if idx in marked:
                continue
            ans += ele
            marked.add(idx)
            marked.add(idx + 1)
            marked.add(idx - 1)
        return ans
