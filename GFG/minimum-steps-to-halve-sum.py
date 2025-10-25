import heapq


class Solution:
    def minOperations(self, arr: list[int]) -> int:
        heap = [-i for i in arr]
        heapq.heapify(heap)
        initial_sum = sum(arr)
        reduced: float = 0
        steps: int = 0
        while initial_sum - reduced > initial_sum / 2:
            curr = -heapq.heappop(heap)
            if curr == 0:
                return -1
            reduced += curr / 2
            heapq.heappush(heap, -curr / 2)
            steps += 1
        return steps
