class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        ans = []

        for i in arr:
            if ans and not ((i >= 0 and ans[-1] >= 0) or (i < 0 and ans[-1] < 0)):
                ans.pop()
                continue
            else:
                ans.append(i)
        return ans
