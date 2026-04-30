class Solution:
    def visibleBuildings(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 1
        mx = arr[0]
        for i in range(1, n):
            if arr[i] >= mx:
                ans += 1
                mx = arr[i]
        return ans
