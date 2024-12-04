# User function Template for python3


class Solution:

    # Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1: str, s2: str):
        return s2 in 2 * s1
