import heapq
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        arr = nums
        positive_heap: List[int] = []
        negative_heap: List[int] = []
        for i in arr:
            if i > 0:
                positive_heap.append(i)
            else:
                heapq.heappush(negative_heap, i)

        while negative_heap and k > 0:
            mn = heapq.heappop(negative_heap)
            positive_heap.append(-mn)
            k -= 1

        k %= 2
        return (
            sum(negative_heap)
            + sum(positive_heap)
            + (-1 if k else 0) * (2 * min(positive_heap))
        )
