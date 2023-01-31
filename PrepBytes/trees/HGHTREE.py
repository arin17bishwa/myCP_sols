"""
Complete the calculateHeight function below
For your reference

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

Methods implemented are:
buildTreeLevelWise(ip) # ip denotes input given by the users
"""


def calculateHeight(root):
    if not root:
        return 0
    return max(calculateHeight(root.left), calculateHeight(root.right)) + 1
