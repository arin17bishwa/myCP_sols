from collections import Counter
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        arr1 = A
        arr2 = B
        ans = [0] * len(arr1)
        curr = 0
        counter = Counter()
        for idx, (a, b) in enumerate(zip(arr1, arr2)):
            counter[a] += 1
            counter[b] += 1

            curr += (counter[a] == 2) + (counter[b] == 2) - (a == b)
            ans[idx] = curr
        return ans
