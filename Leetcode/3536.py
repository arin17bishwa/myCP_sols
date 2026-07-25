class Solution:
    def maxProduct(self, n: int) -> int:
        digs = sorted(map(int, str(n)), reverse=True)
        return digs[0] * digs[1]
