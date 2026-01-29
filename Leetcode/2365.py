from collections import defaultdict
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        arr = tasks
        n = len(arr)
        last_done: defaultdict[int, int] = defaultdict(lambda: -(10**9))
        curr_day = 0

        for i in range(n):
            delta = curr_day - last_done[arr[i]] - 1
            curr_day = curr_day if delta >= space else last_done[arr[i]] + space + 1
            last_done[arr[i]] = curr_day
            curr_day += 1
        return curr_day


def main():
    obj = Solution()

    arr = [1, 2, 1, 2, 3, 1]
    k = 3

    arr = [5, 8, 8, 5]
    k = 2

    arr = [4, 10, 10, 9, 10, 4, 10, 4]
    k = 8

    ans = obj.taskSchedulerII(arr, k)

    print(ans)


if __name__ == "__main__":
    main()
