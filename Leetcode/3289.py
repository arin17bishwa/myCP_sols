from collections import Counter
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [i for i, j in Counter(nums).items() if j > 1]
