# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        mx = 0
        node = TreeNode()

        def f(root, depth):
            nonlocal mx
            if not root:
                return depth
            l = f(root.left, depth + 1)
            r = f(root.right, depth + 1)
            if l == r and l >= mx:
                nonlocal node
                mx = l
                node = root
            return max(l, r)

        f(root, 1)
        return node
