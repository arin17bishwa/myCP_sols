from typing import List
from collections import defaultdict


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        bitset = defaultdict(int)
        ans = 1
        self.change_set_count(bitset, arr[0], True)
        tail = 0
        for head in range(1, n):
            # print(arr[head],bitset)
            self.change_set_count(bitset, arr[head], True)
            # print(bitset)
            while tail <= head and not self.is_valid(bitset):
                self.change_set_count(bitset, arr[tail], False)
                tail += 1
            ans = max(ans, head - tail + 1)
        return ans

    @staticmethod
    def change_set_count(bitset: defaultdict[int, int], n: int, increase: bool) -> None:
        diff = 1 if increase else -1
        idx = 0
        while n:
            if n & 1:
                bitset[idx] += diff
            idx += 1
            n >>= 1

    @staticmethod
    def is_valid(bitset: defaultdict[int, int]):
        return not any(v > 1 for v in bitset.values())
