from collections import Counter


class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        n = len(arr)
        freq = Counter()
        for ele in arr:
            freq[ele] += 1
            if freq[ele] == k:
                return ele
        return -1
