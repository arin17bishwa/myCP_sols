from itertools import permutations


class Solution:
    def permuteDist(self, arr: list[int]) -> list[list[int]]:
        return [list(i) for i in permutations(arr, len(arr))]


def main():
    obj = Solution()

    arr = [1, 2, 3]

    ans = obj.permuteDist(arr)

    # print(ans)


if __name__ == "__main__":
    main()
