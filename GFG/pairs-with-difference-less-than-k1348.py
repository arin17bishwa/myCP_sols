class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        arr.sort()
        n = len(arr)

        ans = j = 0

        for i in range(n):
            while j < n and arr[j] - arr[i] < k:
                j += 1
            ans += j - i - 1

        return ans
