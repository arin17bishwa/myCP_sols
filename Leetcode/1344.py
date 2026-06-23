class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        hour_angle: float = hour * 30 + minutes * 0.5
        minute_angle = minutes * 6
        return min(abs(hour_angle - minute_angle), 360 - abs(hour_angle - minute_angle))
