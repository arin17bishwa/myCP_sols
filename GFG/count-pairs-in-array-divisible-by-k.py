from collections import Counter


class Solution:
    def countKdivPairs(self, arr: list[int], k: int) -> int:
        freq = Counter((i % k for i in arr))
        ans: int = (freq[0] * (freq[0] - 1)) >> 1
        for i in range(1, 1 + k // 2):
            ans += (
                freq[i] * freq[k - i]
                if (i << 1) != k
                else (freq[i] * (freq[i] - 1)) >> 1
            )

        return ans


def main():
    obj = Solution()

    arr = [2, 2, 1, 7, 5, 3]
    k = 4

    arr = [5, 9, 36, 74, 52, 31, 42]
    k = 3

    ans = obj.countKdivPairs(arr, k)

    # print(ans)


if __name__ == "__main__":
    main()
