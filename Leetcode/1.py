from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = nums
        indices = defaultdict(list)
        for idx, ele in enumerate(arr):
            indices[ele].append(idx)
        for ele in indices:
            comp = target - ele

            if comp in indices:
                if comp == ele:
                    if len(indices[ele]) > 1:
                        return indices[ele][:2]
                else:
                    return sorted([indices[ele][0], indices[comp][0]])
        return [-1, -1]
