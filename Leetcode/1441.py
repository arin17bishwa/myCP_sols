from collections import deque
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = deque(target)
        ans: list[str] = []
        for i in range(1, 1 + n):
            if t:
                ans.append("Push")

                if t[0] != i:
                    ans.append("Pop")
                else:
                    t.popleft()
            else:
                break
        return ans


def main():
    obj = Solution()

    arr = [1, 3]
    n = 3

    arr = [1, 2, 3]
    n = 3

    ans = obj.buildArray(arr, n)

    print(ans)


if __name__ == "__main__":
    main()
