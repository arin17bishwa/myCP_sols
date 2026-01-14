from collections import deque


class Solution:
    def catchThieves(self, arr: list[str], k: int) -> int:
        police: deque[int] = deque()
        thief: deque[int] = deque()

        for idx, ch in enumerate(arr):
            if ch == "P":
                police.append(idx)
            else:
                thief.append(idx)
        ans = 0
        while police and thief:
            diff = police[0] - thief[0]
            if abs(diff) <= k:
                police.popleft()
                thief.popleft()
                ans += 1
            elif diff < 0:
                police.popleft()
            else:
                thief.popleft()
        return ans


def main():
    obj = Solution()

    arr = ["P", "T", "T", "P", "T"]
    k = 1
    # arr = ["T", "T", "P", "P", "T", "P"]
    # k = 2
    # arr='P P P T T P P T T P'.split()
    # k=2

    ans = obj.catchThieves(arr, k)

    # print(ans)


if __name__ == "__main__":
    main()
