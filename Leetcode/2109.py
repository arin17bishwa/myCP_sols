from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = list(s)
        for idx in spaces:
            arr[idx] = " " + s[idx]
        return "".join(arr)
