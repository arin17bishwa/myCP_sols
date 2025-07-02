from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        arr = nums
        n = len(arr)
        arr.sort()
        mod = 10**9 + 7
        ans = 0
        tail = n - 1
        for head in range(n):
            while head <= tail and arr[head] + arr[tail] > target:
                tail -= 1
            if head > tail:
                break
            ans += pow(2, tail - head, mod)
            if ans > mod:
                ans -= mod
        return ans
