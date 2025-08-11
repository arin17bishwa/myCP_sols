from math import ceil


class Solution:
    def minMaxCandy(self, prices: list[int], k: int):
        arr = prices
        arr.sort()
        n = len(arr)
        req = ceil(n / (k + 1))
        return [sum(arr[:req]), sum(arr[-req:])]
