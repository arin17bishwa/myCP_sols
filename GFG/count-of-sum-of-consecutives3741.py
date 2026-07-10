class Solution:
    def getCount(self, n: int) -> int:
        ans: int = 0
        k: int = 2
        while True:
            x = (k * (k - 1)) >> 1
            if x >= n:
                break
            ans += (n - x) % k == 0
            k += 1
        return ans


def main():
    obj = Solution()

    n = 15

    ans = obj.getCount(n)

    # print(ans)


if __name__ == "__main__":
    main()
