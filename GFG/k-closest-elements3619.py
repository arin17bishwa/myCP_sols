class Solution:
    def printKClosest(self, arr: list[int], k: int, x: int) -> list[int]:
        return [-i[1] for i in sorted((abs(i - x), -i) for i in arr if i != x)[:k]]
