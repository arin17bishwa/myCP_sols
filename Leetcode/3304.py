class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = ["a"]

        while len(ans) < k:
            ans.extend([chr(((ord(ch) - 96) % 26) + 97) for ch in ans])
        return ans[k - 1]
