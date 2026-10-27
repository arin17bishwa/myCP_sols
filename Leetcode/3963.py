class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." * n] + ["".join(("#" * (n - 1), "." ))]* (m - 1)
