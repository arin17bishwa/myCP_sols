from collections import defaultdict
from typing import List


def make_key(s: str) -> tuple[int, ...]:
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - 97] += 1
    return tuple(freq)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp: dict[tuple[int, ...], list[str]] = defaultdict(list)
        for s in strs:
            mp[make_key(s)].append(s)
        return list(mp.values())
