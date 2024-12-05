import heapq
from typing import List, Set, Tuple


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A: List[int], B: List[int], C: int):
        a, b, c = A, B, C
        a.sort(reverse=True)
        b.sort(reverse=True)
        m, n = len(a), len(b)
        heap: List[Tuple[int, int, int]] = [(-a[0] - b[0], 0, 0)]
        ans = []
        seen: Set[Tuple[int, int]] = set()
        for _ in range(c):
            x, i, j = heapq.heappop(heap)
            seen.add((i, j))
            if i < m - 1 and ((i + 1, j) not in seen):
                heapq.heappush(heap, (-a[i + 1] - b[j], i + 1, j))
                seen.add((i + 1, j))
            if j < n - 1 and ((i, j + 1) not in seen):
                heapq.heappush(heap, (-a[i] - b[j + 1], i, j + 1))
                seen.add((i, j + 1))
            ans.append(-x)
        return ans


def main():
    obj = Solution()
    a = [1, 4, 2, 3]
    b = [2, 5, 1, 6]
    c = 4

    a = [59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83]
    b = [59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83]
    c = 10

    print(obj.solve(a, b, c))


if __name__ == "__main__":
    main()
