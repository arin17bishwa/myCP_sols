class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key=lambda a: sum(map(lambda b: b * b, a)))[:k]
