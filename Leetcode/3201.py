from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        return max(
            sum(i & 1 == 0 for i in nums),
            sum(i & 1 != 0 for i in nums),
            self.different_parity(nums, 0),
            self.different_parity(nums, 1),
        )

    @staticmethod
    def different_parity(arr: list[int], starting_modulo: int = 0) -> int:
        ans = 0
        current_modulo = starting_modulo
        for i in arr:
            if i % 2 == current_modulo:
                ans += 1
                current_modulo ^= 1
        return ans
