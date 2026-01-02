from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = nums
        n = len(arr)
        prefix = arr[:]
        suffix = arr[:]

        for i in range(1, n):
            prefix[i] *= prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] *= suffix[i + 1]

        ans = [1] * n
        ans[0] = suffix[1]
        ans[n - 1] = prefix[n - 2]

        for i in range(1, n - 1):
            ans[i] = prefix[i - 1] * suffix[i + 1]
        return ans


def main():
    obj = Solution()

    arr = [1, 2, 3, 4]

    ans = obj.productExceptSelf(arr)

    print(ans)


if __name__ == "__main__":
    main()
