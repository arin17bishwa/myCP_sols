from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        base_arr = [0] if n & 1 else []
        for i in range((n >> 1)):
            base_arr.extend([i + 1, -i - 1])
        return base_arr
