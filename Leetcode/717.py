from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n:
            if i == n - 1:
                return True
            if bits[i] == 1:
                i += 1
            i += 1
        return False
