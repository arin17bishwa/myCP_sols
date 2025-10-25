class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key=lambda a: pow(a[0], 2) + pow(a[1], 2))[:k]
