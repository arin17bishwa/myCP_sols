from collections import deque
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        arr = rains
        n = len(arr)
        ans = [-1] * n
        full = set()
        queue = deque()
        for idx, ele in enumerate(arr):
            if ele:
                queue.append(idx)

        for idx, ele in enumerate(arr):
            if ele:
                if ele in full:
                    return []
                else:
                    full.add(ele)
            else:
                # find what to empty
                while queue and queue[0] <= idx:
                    queue.popleft()

                while queue and arr[queue[0]] not in full:
                    queue.popleft()

                if queue:
                    ans[idx] = arr[queue.popleft()]
                    full.remove(ans[idx])
                else:
                    ans[idx] = 1

        return ans


def main():
    obj = Solution()

    arr = [1, 2, 3, 4]
    arr = [1, 2, 0, 0, 2, 1]
    arr = [1, 2, 0, 1, 2]

    ans = obj.avoidFlood(arr)

    print(ans)


if __name__ == "__main__":
    main()
