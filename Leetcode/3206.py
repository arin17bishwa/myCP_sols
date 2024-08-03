from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i in range(n):
            a, b, c = i % n, (i + 1) % n, (i + 2) % n
            if colors[a] == colors[c] != colors[b]:
                ans += 1
        return ans
