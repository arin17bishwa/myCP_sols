from typing import List


class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n = len(arr)
        zeroes = arr.count(0)

        if zeroes > 1:
            return [0] * n
        total_product = 1
        for i in arr:
            if i:
                total_product *= i
        return (
            [0 if i else total_product for i in arr]
            if zeroes == 1
            else [total_product // i for i in arr]
        )
