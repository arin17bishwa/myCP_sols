import sys
from typing import List, Optional


sys.setrecursionlimit(10**5)


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def find_distances(start: int) -> list[float]:
            n = len(edges)

            def dfs(
                curr: int,
                distances: list[float],
                curr_dist: int = 0,
                visited: Optional[int] = None,
            ):
                if visited is None:
                    visited = [0] * n
                if curr == -1 or visited[curr]:
                    return
                visited[curr] = 1
                distances[curr] = curr_dist
                dfs(edges[curr], distances, curr_dist + 1, visited)

            all_distances = [float("inf")] * n
            dfs(start, all_distances)
            return all_distances

        d1 = find_distances(node1)
        d2 = find_distances(node2)

        min_dist = min(max(i, j) for i, j in zip(d1, d2))

        if min_dist == float("inf"):
            return -1
        for idx, (i, j) in enumerate(zip(d1, d2)):
            if max(i, j) == min_dist:
                return idx
        return -1
