from bisect import bisect_left


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        arr = citations
        arr.sort()
        lo, hi = 0, len(arr)
        ans = 0
        while lo <= hi:
            mid = (hi + lo) >> 1
            if self.check(arr, mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    @staticmethod
    def check(arr: list[int], x: int) -> bool:
        return len(arr) - bisect_left(arr, x) >= x


def main():
    obj = Solution()
    arr = [3, 0, 5, 3, 0]
    arr = [5, 1, 2, 4, 1]
    arr = [0, 0]

    ans = obj.hIndex(arr)
    print(ans)


if __name__ == "__main__":
    main()
