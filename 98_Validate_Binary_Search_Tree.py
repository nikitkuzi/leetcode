# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        q,temp = [], root
        while q or temp:
            while temp:
                q.append(temp)
                temp = temp.left
            node = q.pop()
            ans.append(node.val)
            temp = node.right
        print(ans)
        for i in range(len(ans)-1):
            if ans[i] >= ans[i+1]:
                return False
        return True