import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        idx = ans = curr_day = 0
        heap: list[int] = []
        while heap or (idx < n):
            if not heap:
                curr_day = events[idx][0]
            while idx < n and events[idx][0] <= curr_day:
                heapq.heappush(heap, events[idx][1])
                idx += 1
            heapq.heappop(heap)
            ans += 1
            curr_day += 1

            while heap and heap[0] < curr_day:
                heapq.heappop(heap)
        return ans
