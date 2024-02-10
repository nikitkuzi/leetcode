# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == key:

            if not root.right or not root.left:
                root = root.left or root.right
                return root

            left = root.left
            temp = root.right
            prev = None
            curr = temp
            while (curr):
                prev = curr
                curr = curr.left
            prev.left = left
            return temp


        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        return root


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == key:

            if not root.right or not root.left:
                root = root.left or root.right
                return root

            cur = root.left
            while cur.right:
                cur = cur.right

            root.val = cur.val
            root.left = self.deleteNode(root.left, cur.val)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        return root