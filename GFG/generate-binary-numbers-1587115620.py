class Solution:
    def generateBinary(self, n: int) -> list[str]:
        return [bin(i + 1)[2:] for i in range(n)]
