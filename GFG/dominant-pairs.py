from bisect import bisect_left


class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        m = len(arr) >> 1

        first_half = sorted(arr[:m])
        ans = 0

        for i in range(m, len(arr)):
            x = bisect_left(first_half, 5 * arr[i])
            ans += m - x

        return ans


def main():
    obj = Solution()

    arr = [10, 2, 2, 1]
    arr = [10, 8, 2, 1, 1, 2]
    arr = [5, 1, 1, 1, 1, 1, 1, 1]

    ans = obj.dominantPairs(arr)

    # print(ans)


if __name__ == "__main__":
    main()
