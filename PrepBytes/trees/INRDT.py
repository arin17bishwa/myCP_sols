"""
Complete the inOrderTraversal function below
For your reference

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

Methods implemented are:
buildTreeLevelWise(ip) # ip denotes input given by the users
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data, end=' ')
    inOrderTraversal(root.right)

