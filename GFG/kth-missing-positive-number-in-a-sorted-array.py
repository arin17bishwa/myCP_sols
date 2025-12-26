class Solution:
    def kthMissing(self, arr: list[int], k: int) -> int:
        n = len(arr)
        lo, hi = 0, n - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) >> 1
            if arr[mid] > mid + k:
                ans = mid + k
                hi = mid - 1
            else:
                lo = mid + 1

        return n + k if ans == -1 else ans


def func():
    obj = Solution()

    arr = [2, 3, 4, 7, 11]
    k = 5

    arr = [1, 2, 3]
    k = 2

    arr = [3, 5, 9, 10, 11, 12]
    k = 2

    ans = obj.kthMissing(arr, k)
    # print(ans)


def main():
    func()


if __name__ == "__main__":
    main()
