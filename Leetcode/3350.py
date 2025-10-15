from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        arr = nums[:]
        arr[0] = 1
        n = len(arr)

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                arr[i] = 1
            else:
                arr[i] = 0
        for i in range(1, n):
            if arr[i]:
                arr[i] += arr[i - 1]

        lo, hi = 1, n
        ans = lo

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.is_possible(arr, mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    def is_possible(self, arr: list[int], k: int) -> bool:
        n = len(arr)
        if 2 * k > n:
            return False

        for a in range(n - 2 * k + 1):
            if (
                arr[a + k - 1] == arr[a] + k - 1
                and arr[a + k + k - 1] == arr[a + k] + k - 1
            ):
                return True
        return False


def main():
    obj = Solution()

    arr = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
    arr = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
    arr = [5, 8, -2, -1]

    ans = obj.maxIncreasingSubarrays(arr)

    print(ans)


if __name__ == "__main__":
    main()
