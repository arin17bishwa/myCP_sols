class Solution:
    def findMean(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        ans = []
        n = len(arr)
        for i in range(1, n):
            arr[i] += arr[i - 1]

        for l, r in queries:
            ans.append((arr[r] - (0 if l == 0 else arr[l - 1])) // (r - l + 1))
        return ans
