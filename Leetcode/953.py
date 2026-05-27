from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map: dict[str, int] = {ch: idx for idx, ch in enumerate(order)}

        arr: list[tuple[int, ...]] = [
            tuple(order_map[ch] for ch in word) for word in words
        ]

        prev: tuple[int, ...] = (-1,)

        for i in arr:
            if i < prev:
                return False
            prev = i
        return True


def main():
    obj = Solution()

    arr = ["hello", "leetcode"]
    s = "hlabcdefgijkmnopqrstuvwxyz"

    ans = obj.isAlienSorted(arr, s)

    print(ans)


if __name__ == "__main__":
    main()
