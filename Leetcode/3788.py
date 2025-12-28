from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        suffix = arr[:]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i], suffix[i + 1])
        curr = 0
        ans = -(10**10)
        for i in range(n - 1):
            curr += arr[i]
            ans = max(ans, curr - suffix[i + 1])
        return ans


def main():
    obj = Solution()

    arr = [10, -1, 3, -4, -5]
    arr = [-7, -5, 3]
    arr = [1, 1]

    ans = obj.maximumScore(arr)

    print(ans)


if __name__ == "__main__":
    main()
