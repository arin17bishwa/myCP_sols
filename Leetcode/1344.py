class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        hour_angle: float = hour * 30 + minutes * 0.5
        minute_angle = minutes * 6
        angle = abs(hour_angle - minute_angle)

        return min(angle, 360 - angle)
