from math import ceil


class Solution:
    def kokoEat(self, arr: list[int], k: int) -> int:
        n = len(arr)
        lo, hi = 1, max(arr)
        ans = lo

        while lo <= hi:
            mid = (lo + hi) >> 1
            if self.is_possible(arr, mid) <= k:
                hi = mid - 1
                ans = mid
            else:
                lo = mid + 1
        return ans

    @staticmethod
    def is_possible(arr: list[int], s: int) -> int:
        return sum(ceil(i / s) for i in arr)


def main():
    obj = Solution()

    arr = [5, 10, 3]
    k = 4
    arr = [5, 10, 15, 20]
    k = 7

    ans = obj.kokoEat(arr, k)

    # print(ans)


if __name__ == "__main__":
    main()
