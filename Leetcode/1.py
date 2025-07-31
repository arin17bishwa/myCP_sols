from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = defaultdict(list)
        for idx, val in enumerate(nums):
            mapping[val].append(idx)

        for k in mapping:
            if target == (k << 1):
                if len(mapping[k]) > 1:
                    return mapping[k][:2]
            elif target - k in mapping:
                return [mapping[k][0], mapping[target - k][0]]
        return []
