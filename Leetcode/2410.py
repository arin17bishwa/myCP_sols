from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        m, n = len(players), len(trainers)
        players.sort()
        trainers.sort()
        i = j = ans = 0
        while i < m and j < n:
            x, y = players[i], trainers[j]
            if x <= y:
                ans += 1
                i += 1
            j += 1
        return ans
