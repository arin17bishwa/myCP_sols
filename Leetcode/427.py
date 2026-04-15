from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        n = len(grid)

        true_leaf = Node(True, True, None, None, None, None)
        false_leaf = Node(False, True, None, None, None, None)

        def dfs(x0: int, y0: int, side_len: int) -> Node:
            if side_len == 1:
                return true_leaf if grid[x0][y0] == 1 else false_leaf
            else:
                new_side_len = side_len >> 1
                top_left = dfs(x0, y0, new_side_len)
                top_right = dfs(x0, y0 + new_side_len, new_side_len)
                bottom_left = dfs(x0 + new_side_len, y0, new_side_len)
                bottom_right = dfs(x0 + new_side_len, y0 + new_side_len, new_side_len)

                sub_tres: list[Node] = [top_left, top_right, bottom_left, bottom_right]

                if (
                    all(sub_tree.isLeaf for sub_tree in sub_tres)
                    and sum(sub_tree.val for sub_tree in sub_tres) % 4 == 0
                ):
                    return top_left
                else:
                    return Node(
                        False, False, top_left, top_right, bottom_left, bottom_right
                    )

        return dfs(0, 0, n)
