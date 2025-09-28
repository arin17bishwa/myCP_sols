import string
from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def freq(s: str) -> tuple[int, ...]:
            counter = Counter(s)
            return tuple(counter[i] for i in string.ascii_lowercase)

        groups: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)
        for x in strs:
            groups[freq(x)].append(x)
        return list(groups.values())
