from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = 0
        reference = strs[0]
        m = len(reference)
        while ans < m:
            if all(ans < len(s) and reference[ans] == s[ans] for s in strs):
                ans += 1
            else:
                break
        return reference[:ans]
