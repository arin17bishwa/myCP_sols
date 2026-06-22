from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        arr: list[list[int]] = [[0] * n for _ in range(m)]

        for i in range(m):
            diff = (k % n) * (1 if i & 1 else -1)
            for j in range(n):
                if mat[i][(j + diff) % n] != mat[i][j]:
                    return False
        return True


def main():
    obj = Solution()

    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 4

    arr = [[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]]
    k = 2

    arr = [[2, 2], [2, 2]]
    k = 3

    ans = obj.areSimilar(arr, k)

    print(ans)


if __name__ == "__main__":
    main()
