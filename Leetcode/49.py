from typing import List, Tuple, Dict
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_groups: defaultdict = defaultdict(list)

        def create_count_tuple(s: str) -> Tuple[int]:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - 97] += 1
            return tuple(freq)

        for st in strs:
            freq_groups[create_count_tuple(st)].append(st)
        return list(freq_groups.values())
