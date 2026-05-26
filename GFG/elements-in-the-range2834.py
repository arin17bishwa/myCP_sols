class Solution:
    def checkElements(self, start: int, end: int, arr: list[int]) -> bool:
        return all(i in set(arr) for i in range(start, end + 1))
