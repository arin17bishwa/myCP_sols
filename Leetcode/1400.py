from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = Counter(s)
        odds = sum(v % 2 for v in freq.values())
        return len(s) >= k >= odds
