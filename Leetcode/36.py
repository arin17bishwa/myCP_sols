from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [defaultdict(int) for _ in range(n)]
        cols = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rows[i][board[i][j]] += 1
                cols[j][board[i][j]] += 1
                if board[i][j] != "." and (
                    rows[i][board[i][j]] > 1 or cols[j][board[i][j]] > 1
                ):
                    return False
        for x in range(0, n, 3):
            for y in range(0, n, 3):
                seen = set()
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        if board[i][j] in seen:
                            return False
                        if board[i][j] != ".":
                            seen.add(board[i][j])

        return True
