class Solution:
    def isBitSet(self, n: int) -> bool:
        return bin(n).count("0") == 1
