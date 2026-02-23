class Solution:
    def findUnion(self, a: list[int], b: list[int]) -> list[int]:
        return list(set(a).union(set(b)))
