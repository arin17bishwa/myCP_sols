class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        upper_row = [1] * n
        current_row = [1] * n

        for _ in range(m - 1):
            for j in range(1, n):
                current_row[j] = current_row[j - 1] + upper_row[j]
            upper_row, current_row = current_row, [1] * n
        return upper_row[-1]
