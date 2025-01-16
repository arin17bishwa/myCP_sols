from collections import defaultdict
from typing import List


class Solution:
    def maxLen(self, arr: List[int]):
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                arr[i] = -1

        for i in range(1, n):
            arr[i] += arr[i - 1]
        ans = 0
        indices = defaultdict(list)

        for i, j in enumerate(arr):
            indices[j].append(i)

        # print(arr)
        # print(indices)
        return max(
            max(
                (val[-1] - val[0] for val in indices.values() if len(val) > 1),
                default=0,
            ),
            indices.get(0, [-1])[-1] + 1,
        )


def main():
    obj = Solution()

    arr = [0]
    arr = list(map(int, "1 0 1 1 1 0 0".split()))

    ans = obj.maxLen(arr)

    print(ans)


if __name__ == "__main__":
    main()
