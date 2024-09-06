from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans: List[str] = []
        for hour in range(12):
            for minute in range(60):
                set_bit_count = hour.bit_count() + minute.bit_count()
                if set_bit_count == turnedOn:
                    ans.append(f"{hour}:{minute:02d}")
        return ans
