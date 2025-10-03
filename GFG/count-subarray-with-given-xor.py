from collections import defaultdict


class Solution:
    def subarrayXor(self, arr: list[int], k: int) -> int:
        n = len(arr)

        for i in range(1, n):
            arr[i] ^= arr[i - 1]

        seen: defaultdict[int, int] = defaultdict(int)
        seen[0] += 1
        ans = 0

        for idx, ele in enumerate(arr):
            ans += seen[ele ^ k]
            seen[ele] += 1
        return ans


def main():
    obj = Solution()

    arr = [4, 2, 2, 6, 4]
    k = 6
    arr = [5, 6, 7, 8, 9]
    k = 5
    arr = [1, 1, 1, 1]
    k = 0

    ans = obj.subarrayXor(arr, k)

    # print(ans)


if __name__ == "__main__":
    main()
