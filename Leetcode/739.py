from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = temperatures
        n = len(arr)
        q: deque[int] = deque()
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while q and arr[i] >= arr[q[0]]:
                q.popleft()
            if q:
                ans[i] = q[0] - i
            q.appendleft(i)
        return ans


def main():
    obj = Solution()

    arr = [73, 74, 75, 71, 69, 72, 76, 73]
    arr = [30, 40, 50, 60]
    arr = [30, 60, 90]
    arr = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]

    ans = obj.dailyTemperatures(arr)

    print(ans)


if __name__ == "__main__":
    main()
