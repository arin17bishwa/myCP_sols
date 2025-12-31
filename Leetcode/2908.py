from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        int_max = (1 << 32) - 1
        prefix_min = [int_max] * n
        suffix_min = [int_max] * n

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], arr[i - 1])

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i + 1])

        # print(arr)
        # print(prefix_min)
        # print(suffix_min)

        ans = int_max
        for i in range(1, n - 1):
            if prefix_min[i] < arr[i] and suffix_min[i] < arr[i]:
                ans = min(ans, prefix_min[i] + arr[i] + suffix_min[i])
        return ans if not ans >= int_max else -1


def main():
    obj = Solution()

    arr = [5, 4, 8, 7, 10, 2]

    ans = obj.minimumSum(arr)

    print(ans)


if __name__ == "__main__":
    main()
