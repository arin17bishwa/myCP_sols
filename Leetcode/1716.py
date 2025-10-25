class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7:
            return sum(list(range(1, 8))[:n])
        k, mod = divmod(n, 7)
        ans = 28 * k + 7 * ((k * (k - 1)) // 2)
        return ans + ((k - 0) * mod + self.totalMoney(mod))


def main():
    obj = Solution()

    n = 4
    n = 10
    n = 20

    ans = obj.totalMoney(n)

    print(ans)


if __name__ == "__main__":
    main()
