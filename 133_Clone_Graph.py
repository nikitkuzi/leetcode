"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:  # already cloned
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """
#
# from typing import Optional
#
#
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return
#         q = deque([node])
#         clones = {node.val: Node(node.val, [])}
#         while q:
#             nd = q.popleft()
#             for nghb in nd.neighbors:
#                 if nghb.val not in clones:
#                     clones[nghb.val] = Node(nghb.val, [])
#                     q.append(nghb)
#                 clones[nd.val].neighbors.append(clones[nghb.val])
#         return clones[node.val]
#
#

