class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def process_str(s: str):
            return "".join("1" if i == "0" else "0" for i in s)[::-1]

        curr = "0"
        for _ in range(n - 1):
            curr = "".join((curr, "1", process_str(curr)))
        return curr[k - 1]
