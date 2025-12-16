from typing import List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        arr = balance
        n = len(arr)
        tot = sum(arr)

        if tot < 0:
            return -1
        ans = need = 0
        neg = -1

        for idx, i in enumerate(arr):
            if i < 0:
                neg = idx
                need = -i
                break

        if neg == -1:
            return 0

        balances = [
            (min((neg - i) % n, (i - neg) % n), ele)
            for i, ele in enumerate(arr)
            if ele > 0
        ]

        balances.sort()

        for dist, bal in balances:
            take = min(need, bal)
            ans += take * dist
            need -= take
            if need == 0:
                break

        return ans
