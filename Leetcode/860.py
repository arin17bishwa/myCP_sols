from typing import List
from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = defaultdict(int)
        for bill in bills:
            if bill == 10:
                if freq[5] < 1:
                    return False
                freq[5] -= 1
            if bill == 20:
                if freq[10] > 0 and freq[5] > 0:
                    freq[5] -= 1
                    freq[10] -= 1
                elif freq[5] > 2:
                    freq[5] -= 3
                else:
                    return False
            freq[bill] += 1
        return True
