class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx = abs(z - x)
        dy = abs(z - y)
        if dx < dy:
            return 1
        if dx > dy:
            return 2
        return 0
