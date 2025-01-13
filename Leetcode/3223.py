from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if v & 1 else 2 for v in Counter(s).values())
