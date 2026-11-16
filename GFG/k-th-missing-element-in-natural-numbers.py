class Solution:
    def findKthSmall(self, arr: list[int], k: int) -> int:
        curr = cnt = 1

        s = set(arr)

        for _ in range(10**7):
            if curr in s:
                cnt -= 1
            if cnt == k:
                return curr
            curr += 1
            cnt += 1
        return -1
