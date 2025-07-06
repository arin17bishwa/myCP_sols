from collections import Counter
from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.arr1 = nums1
        self.arr2 = nums2
        self.arr1_freq: Counter[int] = Counter(self.arr1)
        self.arr2_freq: Counter[int] = Counter(self.arr2)

    def add(self, index: int, val: int) -> None:
        old_val = self.arr2[index]
        self.arr2[index] += val
        self.arr2_freq[old_val] -= 1
        self.arr2_freq[self.arr2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num in self.arr1:
            if tot - num in self.arr2_freq:
                res += self.arr2_freq[tot - num]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
