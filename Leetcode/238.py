from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = nums
        n = len(arr)
        ans = arr[:]
        for i in range(1, n - 1):
            ans[i] *= ans[i - 1]
        ans[-1] = ans[-2]
        curr = arr[-1]
        for i in range(n - 2, 0, -1):
            ans[i] = ans[i - 1] * curr
            curr *= arr[i]
        ans[0] = curr
        return ans


def main():
    obj = Solution()

    arr = [1, 2, 3, 4]

    ans = obj.productExceptSelf(arr)

    print(ans)


if __name__ == "__main__":
    main()
