from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr: list[int] = []
        for row in bank:
            device_cnt = row.count("1")
            if device_cnt:
                arr.append(device_cnt)

        if len(arr) < 2:
            return 0

        ans: int = 0

        for i in range(1, len(arr)):
            ans += arr[i] * arr[i - 1]
        return ans
