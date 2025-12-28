from collections import deque
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        arr = prices
        n = len(arr)
        q = deque()
        ans = arr[:]
        for i in range(n - 1, -1, -1):
            while q and q[0] > arr[i]:
                q.popleft()
            if q:
                ans[i] -= q[0]
            q.appendleft(arr[i])
        return ans


def main():
    obj = Solution()

    arr = [8, 4, 6, 2, 3]
    arr = [1, 2, 3, 4, 5]
    arr = [10, 1, 1, 6]

    ans = obj.finalPrices(arr)

    print(ans)


if __name__ == "__main__":
    main()
