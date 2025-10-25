import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap: list[list[int]] = [[i * i + j * j, i, j] for i, j in points]
        heapq.heapify(heap)
        ans: list[list[int]] = []
        for _ in range(k):
            _, i, j = heapq.heappop(heap)
            ans.append([i, j])
        return ans
