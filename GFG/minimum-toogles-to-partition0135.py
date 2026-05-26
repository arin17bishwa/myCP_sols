class Solution:
    def minToggle(self, arr: list[int]) -> int:
        n = len(arr)
        ones = sum(arr)
        zeroes = n - ones
        if zeroes == 0 or zeroes == n:
            return 0

        ans = min(zeroes, ones)
        running_ones = running_zeroes = 0

        for i in arr:
            if i:
                running_ones += 1
            else:
                running_zeroes += 1

            ans = min(ans, running_ones + (zeroes - running_zeroes))

        return ans


def main():
    obj = Solution()

    arr = [1, 0, 1, 1, 0]
    arr = list(map(int, "1 1 1 1 0 1 0 1".split()))

    ans = obj.minToggle(arr)

    # print(ans)


if __name__ == "__main__":
    main()
