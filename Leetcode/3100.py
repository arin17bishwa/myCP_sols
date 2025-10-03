class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans: int = numBottles
        empty_bottles = numBottles
        k = numExchange
        while empty_bottles >= k:
            empty_bottles -= k
            k += 1
            empty_bottles += 1
            ans += 1
        return ans
