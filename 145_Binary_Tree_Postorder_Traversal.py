# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def f(node):
            if not node:
                return
            f(node.left)
            f(node.right)
            if node.val:
                ans.append(node.val)

        f(root)
        return ans