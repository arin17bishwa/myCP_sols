from collections import Counter
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones_1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones_2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        if not ones_1 or not ones_2:
            return 0

        diffs: Counter[tuple[int, int]] = Counter()

        for x1, y1 in ones_1:
            for x2, y2 in ones_2:
                diffs[(x2 - x1, y2 - y1)] += 1

        return diffs.most_common(1)[0][1]
