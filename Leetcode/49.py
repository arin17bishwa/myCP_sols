from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def calculate_freq(st: str) -> tuple[int, ...]:
            freq = [0] * 26
            for ch in st:
                freq[ord(ch) - 97] += 1
            return tuple(freq)

        ans: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)

        for s in strs:
            ans[calculate_freq(s)].append(s)
        return list(ans.values())
