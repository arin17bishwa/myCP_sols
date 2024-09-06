from typing import List, Dict


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        mapper: Dict[int:str] = {i: f"{i}" for i in range(10)} | {
            i + 10: chr(97 + i) for i in range(6)
        }
        ans: List[str] = []
        if num < 0:
            num = (1 << 32) + num
        while num:
            ans.append(mapper[num % 16])
            num //= 16
        return "".join(ans[::-1])
