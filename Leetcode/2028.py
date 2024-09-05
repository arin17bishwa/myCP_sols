from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        known_sum = sum(rolls)
        required_sum = mean * (m + n)
        rem_sum = required_sum - known_sum
        if not n <= rem_sum <= 6 * n:
            return []
        ans = [rem_sum // n] * n
        curr_sum = known_sum + n * (rem_sum // n)
        for i in range(n):
            if curr_sum >= required_sum:
                break
            ans[i] += 1
            curr_sum += 1
        return ans
