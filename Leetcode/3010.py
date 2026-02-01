import heapq
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        arr = nums
        heap = arr[1:]
        heapq.heapify(heap)
        return arr[0] + sum(heapq.nsmallest(2, heap))
