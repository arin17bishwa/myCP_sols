class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        arr = bulbs
        n = len(arr)
        state = [0] * 101
        for i in arr:
            state[i] ^= 1

        ans = []
        for i in range(1, 101):
            if state[i]:
                ans.append(i)
        return ans
