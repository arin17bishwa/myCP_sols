class Solution:
    def printKClosest(self, arr: list[int], k: int, x: int) -> list[int]:
        _ans = sorted((abs(i - x), -i) for i in arr if i != x)
        return [-i[1] for i in _ans[:k]]
