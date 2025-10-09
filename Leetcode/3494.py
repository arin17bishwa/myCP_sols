from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        curr_free = [0] * n
        for j in range(m):
            curr_time = 0
            x = mana[j]
            for i in range(n):
                curr_time = max(curr_time, curr_free[i]) + skill[i] * mana[j]
            curr_free[-1] = curr_time
            for i in range(n - 2, -1, -1):
                curr_free[i] = curr_free[i + 1] - skill[i + 1] * mana[j]
        return curr_free[-1]
