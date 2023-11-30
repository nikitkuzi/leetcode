# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def h(root, s):
            if not root:
                # return int("".join(map(str, s)))
                return 0

            # print(root.val,s, int("".join(map(str, s))))
            print(root.val, s)
            s = s * 10 + root.val
            if not root.left and not root.right:
                return s

            return h(root.left, s) + h(root.right, s)

        return h(root, 0)