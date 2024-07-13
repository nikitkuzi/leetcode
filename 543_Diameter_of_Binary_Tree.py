# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def f(node):
            # print(node)
            if not node:
                return 0
            l = f(node.left)
            r = f(node.right)
            nonlocal mx

            mx = max(mx, l+r)
            return max(l, r)+1
        f(root)
        return mx
