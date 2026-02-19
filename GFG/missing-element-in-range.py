class Solution:
    def missingRange(self, arr: list[int], low: int, high: int) -> list[int]:
        present = set(arr)
        return [i for i in range(low, high + 1) if i not in present]
