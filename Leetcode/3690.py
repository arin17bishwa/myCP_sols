from collections import deque
from typing import List


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        start, target = tuple(nums1), tuple(nums2)
        n = len(nums1)

        if start == target:
            return 0

        seen, q = {start}, deque([(start, 0)])

        while q:
            arr, steps = q.popleft()
            for left in range(n):
                for right in range(left, n):
                    sub, rem = arr[left : right + 1], arr[:left] + arr[right + 1 :]
                    for k in range(len(rem) + 1):
                        nxt = rem[:k] + sub + rem[k:]
                        if nxt == target:
                            return steps + 1
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append((nxt, steps + 1))
        return -1


def main():
    obj = Solution()
    arr1 = [3, 1, 2]
    arr2 = [1, 2, 3]

    # arr1=[1,1,2,3,4,5]
    # arr2=[5,4,3,2,1,1]

    ans = obj.minSplitMerge(arr1, arr2)

    print(ans)


if __name__ == "__main__":
    main()
