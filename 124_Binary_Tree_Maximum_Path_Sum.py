# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = [root.val]

        def f(root):
            if not root:
                return 0

            l = f(root.left)
            r = f(root.right)
            l = max(0, l)
            r = max(0, r)
            mx[0] = max(mx[0], l + r + root.val)
            return max(l, r) + root.val

        f(root)
        return mx[0]