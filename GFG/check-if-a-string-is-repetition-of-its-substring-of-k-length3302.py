from collections import defaultdict


class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        freq = defaultdict(int)
        n = len(s)
        if n % k != 0:
            return False

        for i in range(0, n, k):
            freq[s[i : i + k]] += 1

        if len(freq) > 2:
            return False
        if len(freq) == 1:
            return True
        return 1 in freq.values()
