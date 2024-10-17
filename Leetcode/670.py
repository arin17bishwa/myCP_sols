from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        arr: List[str] = list(str(num))
        n = len(arr)
        mx_suffix = [n - 1] * n
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[mx_suffix[i + 1]]:
                mx_suffix[i] = i
            else:
                mx_suffix[i] = mx_suffix[i + 1]

        for i in range(n - 1):
            if arr[mx_suffix[i + 1]] > arr[i]:
                arr[i], arr[mx_suffix[i + 1]] = arr[mx_suffix[i + 1]], arr[i]
                break

        return int("".join(arr))
