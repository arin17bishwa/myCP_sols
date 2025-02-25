from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr = [i % 2 for i in arr]
        ans = odd_cnt = prefix_sum = 0
        even_cnt = 1
        for i in arr:
            prefix_sum += i
            if prefix_sum & 1:
                odd_cnt += 1
                ans += even_cnt
            else:
                even_cnt += 1
                ans += odd_cnt
            if ans >= mod:
                ans -= mod
        return ans
