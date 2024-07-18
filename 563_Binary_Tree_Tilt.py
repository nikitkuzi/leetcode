# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def f(root):
            if not root:
                return 0
            l = f(root.left)
            r = f(root.right)
            self.ans+=abs(l-r)
            return l+r+root.val
        self.ans = 0
        f(root)

        return self.ans
