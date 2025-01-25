from collections import deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted([(ele, idx) for idx, ele in enumerate(nums)])
        n = len(arr)
        groups: List[deque[tuple[int, int]]] = [deque([arr[0]])]
        group_mapping: dict[int:int] = {arr[0][1]: 0}
        curr_group_number = 0
        for i in range(1, n):
            prev_val, prev_idx = groups[-1][-1]
            if abs(arr[i][0] - prev_val) <= limit:
                groups[-1].append(arr[i])

            else:
                groups.append(deque([arr[i]]))
                curr_group_number += 1
            group_mapping[arr[i][1]] = curr_group_number

        ans = []
        for i in range(n):
            ans.append(groups[group_mapping[i]].popleft()[0])
        return ans
