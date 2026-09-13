class Solution:
    def countMinOperations(self, arr: list[int]) -> int:
        ans = mx = 0

        for i in arr:
            ans += bin(i).count("1")
            mx = max(mx, i)

        while mx > 1:
            ans += 1
            mx >>= 1

        return ans
