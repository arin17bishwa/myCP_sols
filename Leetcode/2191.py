from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(
            nums, key=lambda x: int("".join((str(mapping[int(i)]) for i in str(x))))
        )
