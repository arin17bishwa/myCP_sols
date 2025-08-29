from itertools import groupby
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        return sum(
            map(
                lambda x: (x * (x + 1)) >> 1,
                map(
                    lambda x: len(tuple(x[1])),
                    filter(lambda x: x[0] == 0, groupby(nums)),
                ),
            )
        )
