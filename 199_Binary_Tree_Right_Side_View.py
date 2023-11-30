# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def f(root, h):
            if not root:
                return None
            if h > len(ans):
                ans.append(root.val)
            if root.right:
                f(root.right, h + 1)
            if root.left:
                f(root.left, h + 1)

        f(root, 1)
        return ans
