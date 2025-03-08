from typing import List


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s = blocks
        n = len(s)
        cost: List[int] = [0] + [int(i == "W") for i in s]

        for i in range(1, n + 1):
            cost[i] += cost[i - 1]

        return min([cost[i] - cost[i - k] for i in range(k, n + 1)])


def main():
    obj = Solution()

    s = "WBBWWBBWBW"
    k = 7

    s = "WBWW"
    k = 2

    s = "WWBBBWBBBBBWWBWWWB"
    k = 16
    # print(len(s))

    ans = obj.minimumRecolors(s, k)

    print(ans)


if __name__ == "__main__":
    main()
