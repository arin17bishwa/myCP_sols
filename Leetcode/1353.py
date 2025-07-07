import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        idx = ans = 0
        heap: list[int] = []
        curr_day = 0
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


def main():
    obj = Solution()
    arr = [[1, 2], [2, 3], [3, 4]]
    arr = [[1, 2], [2, 3], [3, 4], [1, 2]]
    arr = [[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]
    arr = [[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]]
    arr = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]

    ans = obj.maxEvents(arr)
    print(ans)


if __name__ == "__main__":
    main()
