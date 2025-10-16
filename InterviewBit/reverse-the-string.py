class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A: str) -> str:
        s = A
        arr = s.split()
        return " ".join(arr[::-1])
