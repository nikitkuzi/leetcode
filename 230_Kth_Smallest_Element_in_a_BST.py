# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        n = 0
        temp = root

        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            n +=1
            if n == k:
                return temp.val
            temp = temp.right