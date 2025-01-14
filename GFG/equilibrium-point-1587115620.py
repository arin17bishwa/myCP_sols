class Solution:
    # Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        n = len(arr)
        total = sum(arr)
        curr = 0
        for idx, ele in enumerate(arr):
            if total - curr - ele == curr:
                return idx
            curr += ele
        return -1
