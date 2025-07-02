from collections import Counter


class Solution:
    def countStrings(self, s: str):
        freq = Counter(s)
        ans = 0
        n = len(s)
        for ch, cnt in freq.items():
            ans += cnt * (n - cnt)
        return (ans >> 1) + (1 if any(v > 1 for v in freq.values()) else 0)
