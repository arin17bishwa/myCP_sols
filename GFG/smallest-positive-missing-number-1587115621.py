class Solution:
    def missingNumber(self, arr: list[int]):
        arr.sort()
        ans = 1

        for i in arr:
            if i <= 0:
                continue
            if i > ans:
                return ans
            ans = i + 1
        return max(1, arr[-1] + 1)
