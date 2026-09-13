class Solution:
    def findMax(self, n: int, a: list[int], b: list[int], k: list[int]) -> int:
        arr: list[int] = [0] * (n + 1)
        for p, q, r in zip(a, b, k):
            arr[p] += r
            arr[q + 1] -= r

        for i in range(1, n + 1):
            arr[i] += arr[i - 1]

        return max(arr)


