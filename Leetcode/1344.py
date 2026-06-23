class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        hour_angle: float = hour * 30 + minutes * 0.5
        minute_angle = minutes * 6
        return min(abs(hour_angle - minute_angle), 360 - abs(hour_angle - minute_angle))


def main():
    obj = Solution()

    h, m = 12, 30
    h, m = 3, 30
    h, m = 3, 15

    ans = obj.angleClock(h, m)

    print(ans)


if __name__ == "__main__":
    main()
