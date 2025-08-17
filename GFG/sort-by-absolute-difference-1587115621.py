class Solution:
    def rearrange(self, arr: list[int], x: int) -> None:
        arr.sort(key=lambda k: abs(x - k))
