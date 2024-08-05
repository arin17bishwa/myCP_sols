from functools import cache


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        arr = [1, 1, 2]
        curr, last = 1, 2
        while last <= k:
            curr, last = last, curr + last
            arr.append(last)
        ans = 0
        for ele in arr[::-1]:
            if ele <= k:
                k -= ele
                ans += 1
            if k == 0:
                return ans
