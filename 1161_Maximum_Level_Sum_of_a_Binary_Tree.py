# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        lvl = 1
        q.append(root)
        mx = float(-inf)
        ans = 1
        while q:
            curr = 0
            n = len(q)
            for i in range(n):
                node = q.popleft()
                curr+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if mx < curr:
                mx = curr
                ans = lvl
            lvl+=1
        return ans