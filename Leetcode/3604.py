import heapq
from collections import defaultdict
from typing import List


class Solution:

    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))

        heap = [(0, 0)]

        vis = dict()

        while heap:
            time, node = heapq.heappop(heap)

            if node == n - 1:
                return time
            if node in vis and vis[node] <= time:
                continue
            vis[node] = time
            heapq.heappush(heap, (time + 1, node))

            for nei, start, end in graph[node]:
                if time < start:
                    heapq.heappush(heap, (start + 1, nei))
                elif start <= time <= end:
                    heapq.heappush(heap, (time + 1, nei))

        return -1


def main():
    obj = Solution()

    n = 3
    arr = [[0, 1, 0, 1], [1, 2, 2, 5]]

    # n = 4
    # arr = [[0, 1, 0, 3], [1, 3, 7, 8], [0, 2, 1, 5], [2, 3, 4, 7]]

    # n = 3
    # arr = [[1, 0, 1, 3], [1, 2, 3, 5]]

    # ans = obj.minTime(n, arr)
    # print(ans)


if __name__ == "__main__":
    main()
