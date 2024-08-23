from typing import List
from collections import Counter


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = Counter(deliciousness)
        two_powers = [1 << i for i in range(22)]
        ans = 0
        for a in freq:
            ans += sum(
                (freq[a] * max(0, freq[a] - 1)) if i == 2 * a else freq[a] * freq[i - a]
                for i in two_powers
            )
        return (ans // 2) % (pow(10, 9) + 7)
