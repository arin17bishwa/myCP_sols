from collections import Counter
from typing import List, Dict


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq: List[int] = sorted(Counter(word).values(), reverse=True)
        key_mapping: Dict[int, List[int]] = {i: [] for i in range(8)}
        for idx, cnt in enumerate(freq):
            key_mapping[idx % 8].append(cnt)

        ans = 0
        for keys in key_mapping.values():
            for idx, cnt in enumerate(keys, start=1):
                ans += idx * cnt
        return ans
