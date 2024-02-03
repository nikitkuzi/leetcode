"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if not root:
#             return
#         q = deque()
#         q.append(root)
#         lvl = 0
#         while q:
#             n = len(q)
#             for i in range(n):

#                 curr = q.popleft()
#                 if curr.left:
#                     q.append(curr.left)
#                 if curr.right:
#                     q.append(curr.right)
#                 curr.next = None if i == n-1 else q[0]
#         return root
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        leftmost = root
        while leftmost.left:
            curr = leftmost
            while curr:
                curr.left.next = curr.right
                if curr.next: curr.right.next = curr.next.left
                curr = curr.next
            leftmost = leftmost.left
        return root

