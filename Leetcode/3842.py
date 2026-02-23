class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        arr = bulbs
        state = [0] * 101

        for i in arr:
            state[i] ^= 1

        return [i for i in range(1, 101) if state[i]]
