from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        if n == 1:
            return arr[0]

        if arr[0] != arr[1]:
            return arr[0]
        if arr[-1] != arr[-2]:
            return arr[-1]

        lo, hi = 1, n - 2
        while lo <= hi:
            mid = (lo + hi) >> 1
            x = arr[mid]

            if x != arr[mid + 1] and x != arr[mid - 1]:
                return x
            elif x == arr[mid + 1]:
                if mid & 1:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if mid & 1:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


def main():
    obj = Solution()

    arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    # arr = [3, 3, 7, 7, 10, 10, 12]
    arr = [7, 7, 10, 11, 11, 12, 12]

    ans = obj.singleNonDuplicate(arr)

    print(ans)


if __name__ == "__main__":
    main()
