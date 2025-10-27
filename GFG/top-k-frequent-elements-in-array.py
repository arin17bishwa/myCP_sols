from collections import Counter


class Solution:
    def topKFreq(self, arr: list[int], k: int) -> list[int]:
        freq = Counter(arr)
        ans = sorted(set(arr), key=lambda x: (freq[x], x), reverse=True)
        return ans[:k]
