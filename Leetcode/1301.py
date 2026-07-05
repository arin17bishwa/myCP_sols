from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod: int = 10**9 + 7

        n = len(board)

        directions: list[list[int]] = [
            [-1, 0],
            [0, -1],
            [-1, -1],
        ]

        def is_valid(_x: int, _y: int) -> bool:
            return 0 <= _x < n and 0 <= _y < n and board[_x][_y] != "X"

        def find_neighbours(_x: int, _y: int):
            for dx, dy in directions:
                _i, _j = _x + dx, _y + dy
                if is_valid(_i, _j):
                    yield _i, _j

        dp: list[list[list[int]]] = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[-1][-1] = [0, 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if dp[i][j][0] < 0:
                    continue

                for nx, ny in find_neighbours(i, j):
                    curr_cell_score: int = (
                        0 if board[nx][ny] in "SE" else int(board[nx][ny])
                    )
                    _score = curr_cell_score + dp[i][j][0]

                    if dp[nx][ny][0] < _score:
                        dp[nx][ny] = [_score, dp[i][j][1]]
                    elif dp[nx][ny][0] == _score:
                        dp[nx][ny] = [
                            dp[nx][ny][0],
                            (dp[nx][ny][1] + dp[i][j][1]) % mod,
                        ]

        return dp[0][0] if dp[0][0][0] >= 0 else [0, 0]


def main():
    obj = Solution()

    arr = ["E23", "2X2", "12S"]
    arr = ["E12", "1X1", "21S"]
    arr = ["E11", "XXX", "11S"]

    ans = obj.pathsWithMaxScore(arr)

    print(ans)


if __name__ == "__main__":
    main()
