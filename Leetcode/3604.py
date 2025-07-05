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
