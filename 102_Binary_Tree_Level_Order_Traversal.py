# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def f(root, lvl):
            if not root:
                return None
            if len(ans) == lvl:
                ans.append([])
            ans[lvl].append(root.val)
            if root.left:
                f(root.left,lvl+1)
            if root.right:
                f(root.right,lvl+1)
        f(root,0)
        return ans