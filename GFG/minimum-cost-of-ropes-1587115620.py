import heapq


class Solution:
    def minCost(self, arr: list[int]) -> int:
        heapq.heapify(arr)
        ans: int = 0

        while len(arr) > 1:
            a, b = heapq.heappop(arr), heapq.heappop(arr)
            ans += a + b
            heapq.heappush(arr, a + b)

        return ans
