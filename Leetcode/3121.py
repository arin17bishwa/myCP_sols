from collections import defaultdict
import string


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = defaultdict(int)
        upper = defaultdict(int)
        for idx, ch in enumerate(word, start=1):
            if ch.islower():
                lower[ch] = idx
            elif upper[ch] == 0:
                upper[ch] = idx
        ans = 0
        for ch in string.ascii_lowercase:
            if lower[ch] == 0 or upper[ch.upper()] == 0:
                continue
            if lower[ch] < upper[ch.upper()]:
                ans += 1
        return ans
