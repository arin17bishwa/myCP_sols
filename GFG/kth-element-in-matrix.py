class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int):
        return sorted([ele for sublist in matrix for ele in sublist])[k - 1]
