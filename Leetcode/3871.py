class Solution:
    def countCommas(self, n: int) -> int:
        ans: int = 0
        exp = 1
        while pow(10, 3 * exp) <= n:
            ans += (exp - 1) * (pow(10, 3 * exp) - pow(10, 3 * (exp - 1)))
            exp += 1
        exp -= 1
        ans += exp * (n - pow(10, 3 * exp) + 1)
        return ans


def main():
    obj = Solution()

    n = 1002
    n = 998
    n = 1002000999
    n = 1000

    ans = obj.countCommas(n)

    print(ans)


if __name__ == "__main__":
    main()
