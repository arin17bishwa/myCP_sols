from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        arr = nums
        arr.sort()
        n = len(arr)

        ans = 10**9

        if k == n:
            return arr[-1] - arr[0]

        for i in range(k - 1, n):
            ans = min(ans, arr[i] - arr[i - k + 1])
        return ans


def main():
    obj = Solution()

    arr = [9, 4, 1, 7]
    k = 2

    ans = obj.minimumDifference(arr, k)

    print(ans)


if __name__ == "__main__":
    main()
