# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def f(node, prev):
            if not node.left and not node.right and prev == 1:
                return node.val
            res = 0
            if node.left:
                res += f(node.left, 1)
            if node.right:
                res += f(node.right, 0)
            return res
        return f(root, 0)