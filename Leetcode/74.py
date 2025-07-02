from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def get_row() -> int:
            nonlocal m, n, target, matrix
            lo, hi = 0, m - 1
            while lo <= hi:
                mid = (hi + lo) >> 1
                a, b = matrix[mid][0], matrix[mid][-1]
                if a <= target <= b:
                    return mid
                elif target < a:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        def get_col(row) -> bool:
            nonlocal m, n, target, matrix
            lo, hi = 0, n - 1
            while lo <= hi:
                mid = (lo + hi) >> 1
                x = matrix[row][mid]
                if x == target:
                    return True
                elif x < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False

        row_num = get_row()
        if row_num == -1:
            return False
        return get_col(row_num)
