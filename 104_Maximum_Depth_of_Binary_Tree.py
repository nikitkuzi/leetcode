# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node, l):
            if node is None:
                return l
            l += 1

            return max(depth(node.left, l), depth(node.right, l))
        return depth(root, 0)
