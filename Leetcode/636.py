from collections import deque
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans: list[int] = [0] * n
        call_stack: deque[list[int]] = deque()

        for log in logs:
            func_id, log_type, ts = log.split(":")
            func_id = int(func_id)
            ts = int(ts)

            if log_type == "start":
                if call_stack:
                    prev_func_id, prev_ts = call_stack[-1]
                    ans[prev_func_id] += ts - prev_ts
                call_stack.append([func_id, ts])
            else:
                prev_func_id, prev_ts = call_stack[-1]
                ans[func_id] += ts - prev_ts + 1

                if prev_func_id == func_id:
                    call_stack.pop()
                    if call_stack:
                        call_stack[-1][-1] = ts + 1
        return ans
