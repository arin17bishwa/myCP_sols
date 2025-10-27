import heapq


class Solution:
    def nearlySorted(self, arr: list[int], k: int) -> None:
        n = len(arr)
        heap = arr[: k + 1]
        heapq.heapify(heap)
        i = k + 1
        for idx in range(n):
            if i < n:
                heapq.heappush(heap, arr[i])
                i += 1

            arr[idx] = heapq.heappop(heap)
        return
