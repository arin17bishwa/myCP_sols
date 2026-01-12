import heapq


class Solution:
    def maxOfSubarrays(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        heap: list[tuple[int, int]] = [(-arr[i], i) for i in range(k)]
        heapq.heapify(heap)
        ans: list[int] = []

        for i in range(k, n):
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
            heapq.heappush(heap, (-arr[i], i))

        while heap and heap[0][1] < n - k:
            heapq.heappop(heap)

        ans.append(-heap[0][0])

        return ans
