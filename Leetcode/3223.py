from collections import defaultdict, Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        for v in freq.values():
            if v < 3:
                ans += v
            else:
                ans += 1 if v & 1 else 2
        return ans
