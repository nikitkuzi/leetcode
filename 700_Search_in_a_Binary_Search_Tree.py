# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None

    # def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     if not root:
    #         return
    #     if val < root.val and root.left:
    #         return self.searchBST(root.left,val)
    #     if val > root.val and root.right:
    #         return self.searchBST(root.right,val)
    #     if val == root.val:
    #         return root
