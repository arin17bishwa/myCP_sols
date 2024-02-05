from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for idx, ch in enumerate(s):
            if freq[ch] == 1:
                return idx
        return -1
