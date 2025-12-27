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
            # print(call_stack, ans)

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
                else:
                    ans[func_id] -= 1
        return ans


def main():
    obj = Solution()

    arr = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    n = 2

    arr = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
    n = 1

    arr = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    n = 2

    ans = obj.exclusiveTime(n, arr)

    print(ans)


if __name__ == "__main__":
    main()
