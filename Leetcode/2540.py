from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ans = -1
        i = j = 0

        while i < m and j < n:
            a, b = nums1[i], nums2[j]
            if a == b:
                return a
            elif a < b:
                i += 1
            else:
                j += 1
        return ans


def main():
    obj = Solution()

    arr1 = [1, 2, 3]
    arr2 = [2, 4]

    ans = obj.getCommon(arr1, arr2)

    print(ans)


if __name__ == "__main__":
    main()
