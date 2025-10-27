class Solution:
    def totalMoney(self, n: int) -> int:
        k, mod = divmod(n, 7)
        return 28 * k + 7 * ((k * (k - 1)) // 2) + k * mod + ((mod * (mod + 1)) >> 1)
