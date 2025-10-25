class Solution:
    def totalMoney(self, n: int) -> int:
        k, mod = divmod(n, 7)
        return 28 * k + 7 * ((k * (k - 1)) // 2) + k * mod + ((mod * (mod + 1)) >> 1)


def main():
    obj = Solution()

    n = 4
    n = 10
    n = 20

    ans = obj.totalMoney(n)

    print(ans)


if __name__ == "__main__":
    main()
