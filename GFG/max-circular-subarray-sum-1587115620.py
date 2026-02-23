class Solution:
    def maxCircularSum(self, arr: list[int]) -> int:
        n = len(arr)
        complement = tot = curr_comp = curr = kadane_ans = 0
        mx = arr[0]

        for i in range(n):
            tot += arr[i]

            curr_comp += arr[i]
            curr += arr[i]
            mx = max(mx, arr[i])

            if curr_comp >= 0:
                curr_comp = 0
            if curr < 0:
                curr = 0

            complement = min(complement, curr_comp)
            kadane_ans = max(kadane_ans, curr)

        return (
            mx
            if max(kadane_ans, tot - complement) == 0
            else max(kadane_ans, tot - complement)
        )


def main():
    obj = Solution()

    arr = [8, -8, 9, -9, 10, -11, 12]
    arr = [10, -3, -4, 7, 6, 5, -4, -1]
    arr = [5, -2, 3, 4]
    arr = list(
        map(
            int,
            "-7 32 -11 21 18 35 -26 -17 35 -12 -38 -33 32 16 44 11 -40 -21 2 27 -35 21 -37 -12 1".split(),
        )
    )

    ans = obj.maxCircularSum(arr)
    # print(ans)


if __name__ == "__main__":
    main()
