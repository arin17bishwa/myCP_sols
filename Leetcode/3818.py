from typing import List


class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        if n < 2:
            return 0

        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                return i + 1
        return 0


def main():
    obj = Solution()

    arr = [1, -1, 2, 3, 3, 4, 5]
    arr = [4, 3, -2, -5]
    arr = [1, 2, 3, 4]

    ans = obj.minimumPrefixLength(arr)

    # print(ans)


if __name__ == "__main__":
    main()
