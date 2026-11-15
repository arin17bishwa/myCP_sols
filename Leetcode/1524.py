class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        arr = [i % 2 for i in arr]
        ans = curr = odds = 0
        evens = 1

        for ele in arr:
            curr += ele
            if curr & 1:
                odds += 1
                ans += evens
            else:
                evens += 1
                ans += odds
            if ans >= mod:
                ans -= mod
        return ans
