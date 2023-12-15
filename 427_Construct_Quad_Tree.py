"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        s = sum([sum(row) for row in grid])
        is_leaf = (s == (n ** 2)) or (s == 0)
        if is_leaf:
            return Node(grid[0][0], True, None, None, None, None)
        # top_left = [g[:n//2] for g in grid[:n//2]]
        # bot_left = [g[:n//2] for g in grid[n//2:]]
        # top_right = [g[n//2:] for g in grid[:n//2]]
        # bot_right = [g[n//2:] for g in grid[n//2:]]

        if not is_leaf:
            top_left = self.construct([g[:n // 2] for g in grid[:n // 2]])
            top_right = self.construct([g[n // 2:] for g in grid[:n // 2]])
            bot_left = self.construct([g[:n // 2] for g in grid[n // 2:]])
            bot_right = self.construct([g[n // 2:] for g in grid[n // 2:]])
            node = Node(0, False, top_left, top_right, bot_left, bot_right)
            return node