from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = [0] + [idx for idx, ch in enumerate(bin(n)[2:][::-1]) if ch == "1"]
        m = len(powers)
        for i in range(1, m):
            powers[i] += powers[i - 1]
        mod = pow(10, 9) + 7
        return [
            pow(2, powers[right + 1] - powers[left], mod) for left, right in queries
        ]
