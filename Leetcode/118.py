from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_ans: List[List[int]] = [[1]]
        if numRows == 1:
            return final_ans
        for _ in range(numRows - 1):
            last_row = final_ans[-1]
            new_row = [1]
            n = len(last_row)
            for i in range(n - 1):
                new_row.append(last_row[i] + last_row[i + 1])
            new_row.append(1)
            final_ans.append(new_row[:])
        return final_ans
