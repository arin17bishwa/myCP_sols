from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)
        for i in range(1, n):
            a, b = s[i - 1 : i + 1]
            if a != b and int(a) == freq[a] and int(b) == freq[b]:
                return s[i - 1 : i + 1]
        return ""
