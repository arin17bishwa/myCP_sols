from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, words: List[str]) -> int:
        freq = defaultdict(int)

        for word in words:
            first = ord(word[0])
            signature = tuple((ord(c) - first) % 26 for c in word)
            freq[signature] += 1

        ans = 0
        for k in freq.values():
            ans += k * (k - 1) // 2

        return ans
