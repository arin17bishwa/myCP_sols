class Solution:
    def countMinOperations(self, arr: list[int]) -> int:
        ans = mx = 0

        for i in arr:
            ans += bin(i).count("1")
            mx = max(mx, i)

        while mx > 1:
            ans += 1
            mx >>= 1

        return ans


def main():
    obj = Solution()

    arr = [16, 16, 16]

    arr = [2, 3]

    ans = obj.countMinOperations(arr)

    # print(ans)


if __name__ == "__main__":
    main()
