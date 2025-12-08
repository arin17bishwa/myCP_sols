class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high - low) >> 1) + ((low | high) & 1)


def main():
    obj = Solution()
    low, high = 3, 7
    low, high = 8, 10
    low, high = 4, 7
    low, high = 3, 8
    low, high = 11, 13

    ans = obj.countOdds(low, high)
    print(ans)


if __name__ == "__main__":
    main()
