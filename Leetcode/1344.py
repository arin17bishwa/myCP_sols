class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(hour * 30 + minutes * 0.5 - minutes * 6)

        return min(angle, 360 - angle)
