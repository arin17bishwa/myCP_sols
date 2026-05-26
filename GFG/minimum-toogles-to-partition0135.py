class Solution:
    def minToggle(self, arr: list[int]) -> int:
        n = len(arr)
        ones = sum(arr)
        if ones == 0 or ones == n:
            return 0

        ans = min(ones, n - ones)
        running_ones = running_zeroes = 0

        for i in arr:
            if i:
                running_ones += 1
            else:
                running_zeroes += 1

            ans = min(ans, running_ones + (n - ones - running_zeroes))

        return ans


def main():
    obj = Solution()

    arr = [1, 0, 1, 1, 0]
    arr = list(map(int, "1 1 1 1 0 1 0 1".split()))

    ans = obj.minToggle(arr)

    # print(ans)


if __name__ == "__main__":
    main()
