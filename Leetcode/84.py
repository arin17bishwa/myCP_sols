from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        q: deque[int] = deque([-1])
        arr = heights
        ans = arr[0]
        arr.append(0)
        n = len(arr)

        for i in range(n):
            ans = max(ans, arr[i])
            while q and arr[i]<arr[q[-1]]:
                last_idx = q.pop()
                ans = max(ans, arr[last_idx] * (i - q[-1] - 1))
            q.append(i)
        return ans


def main():
    obj = Solution()

    arr = [2, 1, 5, 6, 2, 3]
    # arr = [2, 4]
    # arr = [1, 1]
    # arr=[2,0,2]

    ans = obj.largestRectangleArea(arr)

    print(ans)


if __name__ == "__main__":
    main()
