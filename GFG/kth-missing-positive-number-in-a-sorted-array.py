class Solution:
    def kthMissing(self, arr: list[int], k: int) -> int:
        n = len(arr)
        for i in range(n):
            if arr[i] > i + k:
                return i + k
        return n + k


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
