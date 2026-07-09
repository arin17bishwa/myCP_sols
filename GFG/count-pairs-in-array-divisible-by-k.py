from collections import Counter


class Solution:
    def countKdivPairs(self, arr: list[int], k: int) -> int:
        freq = Counter((i % k for i in arr))
        ans: int = (freq[0] * (freq[0] - 1)) >> 1
        for i in range(1, 1 + k // 2):
            ans += (
                freq[i] * freq[k - i]
                if (i << 1) != k
                else (freq[i] * (freq[i] - 1)) >> 1
            )

        return ans
