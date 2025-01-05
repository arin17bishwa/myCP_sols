from typing import List
from string import ascii_lowercase


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * (n + 1)

        for start, end, direction in shifts:
            movement = -1 if direction == 0 else 1
            arr[start] += movement
            arr[end + 1] -= movement
        for i in range(1, n + 1):
            arr[i] += arr[i - 1]

        def shifted_letter(original: str, shift: int) -> str:
            return ascii_lowercase[(ascii_lowercase.index(original) + shift) % 26]

        return "".join(map(lambda idx: shifted_letter(s[idx], arr[idx]), range(n)))
