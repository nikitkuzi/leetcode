# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        a = []

        q = deque()

        q.append(root)
        while q:
            node = q.popleft()
            a.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        a.sort()
        mn = abs(a[0] - a[1])
        for i in range(1, len(a) - 1):
            mn = min(mn, abs(a[i] - a[i + 1]))
        return mn