from collections import defaultdict


class Solution:
    def possibleStringCount(self, word: str) -> int:
        groups = defaultdict(int)
        groups[0] = 1
        ans = last = 0
        n = len(word)
        for i in range(1, n):
            if word[i] != word[i - 1]:
                last = i
            groups[last] += 1

        for v in groups.values():
            ans += v - 1
        return ans + 1
