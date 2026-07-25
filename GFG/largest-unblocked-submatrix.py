class Solution:
    def largestArea(self, n: int, m: int, arr: list[list[int]]) -> int:
        rows: list[int] = [-1]
        cols: list[int] = [-1]
        for i, j in arr:
            rows.append(i - 1)
            cols.append(j - 1)

        rows.sort()
        cols.sort()

        rows.append(n)
        cols.append(m)
        max_rows = max_cols = 0

        for i in range(1, len(rows)):
            max_rows = max(max_rows, rows[i] - rows[i - 1] - 1)

        for i in range(1, len(cols)):
            max_cols = max(max_cols, cols[i] - cols[i - 1] - 1)

        return max_rows * max_cols
