from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k >= sum(v & 1 != 0 for v in Counter(s).values())
