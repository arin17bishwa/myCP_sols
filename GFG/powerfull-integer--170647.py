from collections import defaultdict


class Solution:
    def powerfulInteger(self, intervals: list[list[int]], k: int):
        suffix = defaultdict(int)
        for i, j in intervals:
            suffix[j] += 1
            suffix[i - 1] -= 1

        curr = 0
        for key in sorted(suffix.keys(), reverse=True):
            curr += suffix[key]
            if curr >= k:
                return key
        return -1
