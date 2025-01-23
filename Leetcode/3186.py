from collections import Counter
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        arr = power
        freq = Counter(arr)
        elements = sorted(set(arr))
        n = len(elements)
        dp = [0] * n
        dp[0] = elements[0] * freq[elements[0]]

        for i in range(1, n):
            curr_damage = elements[i]
            dp[i] = curr_damage * freq[curr_damage]
            dp[i] = dp[i - 1]

            prev_idx = i - 1
            eligible_spell_found = False
            for prev_idx in range(i - 1, max(-1, i - 4), -1):
                if elements[prev_idx] < curr_damage - 2:
                    eligible_spell_found = True
                    break
            if eligible_spell_found:
                dp[i] = max(dp[i], dp[prev_idx] + curr_damage * freq[curr_damage])
            else:
                dp[i] = max(dp[i], curr_damage * freq[curr_damage])

        return dp[-1]
