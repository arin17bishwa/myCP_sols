class Solution:
    def commonElements(self, a: list[int], b: list[int], c: list[int]) -> list[int]:
        return sorted(set(a).intersection(set(b)).intersection(set(c)))
