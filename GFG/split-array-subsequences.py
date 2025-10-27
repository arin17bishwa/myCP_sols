import heapq


class Solution:
    def isPossible(self, arr: list[int], k: int) -> bool:
        heap: list[tuple[int, int]] = []
        n = len(arr)
        i = 0
        while i < n:
            curr = arr[i]
            if not heap:
                heapq.heappush(heap, (curr, 1))
                i += 1
            else:
                top = heap[0]
                if curr == top[0]:
                    heapq.heappush(heap, (curr, 1))
                    i += 1
                elif curr == top[0] + 1:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (curr, top[1] + 1))
                    i += 1
                else:
                    if top[1] < k:
                        return False
                    heapq.heappop(heap)

        while heap:
            if heap[0][1] < k:
                return False
            heapq.heappop(heap)
        return True
