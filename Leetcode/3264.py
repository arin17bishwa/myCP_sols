import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = nums
        heap = [(ele, idx) for idx, ele in enumerate(arr)]
        n = len(heap)
        heapq.heapify(heap)
        for _ in range(k):
            ele, idx = heapq.heappop(heap)
            heapq.heappush(heap, (ele * multiplier, idx))
        for ele, idx in heap:
            arr[idx] = ele

        return arr
