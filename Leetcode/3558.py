from collections import defaultdict
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        max_depth = 0

        def dfs(node: int, prev: int, curr_depth: int = 0):
            nonlocal max_depth

            max_depth = max(max_depth, curr_depth)

            for child in g[node]:
                if child != prev:
                    dfs(child, node, curr_depth + 1)

        dfs(1, 0, 0)

        return pow(2, max_depth - 1, 10**9 + 7)


def main():
    obj = Solution()

    arr = [[1, 2]]
    arr = [[1, 2], [1, 3], [3, 4], [3, 5]]

    ans = obj.assignEdgeWeights(arr)

    print(ans)


if __name__ == "__main__":
    main()
