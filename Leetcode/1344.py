class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(hour * 30 - minutes * 5.5)

        return min(angle, 360 - angle)
