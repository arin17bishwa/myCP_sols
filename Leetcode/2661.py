from collections import defaultdict
from typing import List, Tuple, Dict


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        indices: Dict[int, Tuple[int, int]] = {
            mat[i][j]: (i, j) for i in range(m) for j in range(n)
        }
        row_freq = defaultdict(int)
        column_freq = defaultdict(int)

        for idx, x in enumerate(arr):
            i, j = indices[x]
            row_freq[i] += 1
            column_freq[j] += 1

            if row_freq[i] == n or column_freq[j] == m:
                return idx
