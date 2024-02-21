from typing import List


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left_bin: List[str] = list(bin(left)[2:].zfill(32))
        right_bin: List[str] = list(bin(right)[2:].zfill(32))
        ans = []
        for i in range(32):
            if right_bin[i] != left_bin[i]:
                ans.extend(["0"] * (32 - len(ans)))
                break
            else:
                ans.append(right_bin[i])
        return int("".join(ans), 2)
