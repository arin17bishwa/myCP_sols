class Solution:
    def digitSum(self, s: str, k: int) -> str:

        def func(t: str) -> str:
            nonlocal k
            n = len(t)
            temp = [str(sum(map(int, t[i : i + k]))) for i in range(0, n, k)]
            return "".join(temp)

        while len(s) > k:
            s = func(s)
        return "".join(s)


def main():
    obj = Solution()

    s = "11111222223"
    k = 3

    # s = "00000000"
    # k = 3

    # s = "1"
    # k = 2

    # s = "01234567890"
    # k = 2

    ans = obj.digitSum(s, k)

    print(ans)


if __name__ == "__main__":
    main()
