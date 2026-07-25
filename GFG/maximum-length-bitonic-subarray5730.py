class Solution:
    def bitonic(self, arr: list[int]) -> int:
        n = len(arr)

        if n < 3:
            return n

        inc: list[int] = [0] * n
        dec: list[int] = [0] * n

        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                inc[i] = inc[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1] + 1

        return max(inc[i] + dec[i] + 1 for i in range(n))
