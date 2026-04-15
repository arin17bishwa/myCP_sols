from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        arr = words
        n = len(arr)
        ans: int = n + 1

        for i in range(startIndex, startIndex + n):
            if arr[i % n] == target:
                ans = min(ans, i - startIndex, n - (i - startIndex))
        return -1 if ans == n + 1 else ans


def main():
    obj = Solution()

    arr = ["hello", "i", "am", "leetcode", "hello"]
    s = "hello"
    x = 1

    arr = ["a", "b", "leetcode"]
    s = "leetcode"
    x = 0

    arr = ["i", "eat", "leetcode"]
    s = "ate"
    x = 0

    ans = obj.closestTarget(arr, s, x)

    print(ans)


if __name__ == "__main__":
    main()
