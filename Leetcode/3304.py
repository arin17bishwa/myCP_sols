class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = ["a"]

        def next_chars(arr: list[str]) -> list[str]:
            transformed = [chr(((ord(ch) - 96) % 26) + 97) for ch in arr]
            return transformed

        while len(ans) < k:
            nxt = next_chars(ans)
            ans.extend(nxt)
        return ans[k - 1]
