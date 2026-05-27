from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        lower = defaultdict(lambda: -1)
        upper = defaultdict(lambda: n)

        for idx, ch in enumerate(word):
            if ch.islower():
                lower[ch] = max(lower[ch], idx)
            else:
                upper[ch.lower()] = min(upper[ch.lower()], idx)

        return sum((ch.lower() in lower and ch.lower() in upper) and lower[ch.lower()] < upper[ch.lower()] for ch in lower.keys())
