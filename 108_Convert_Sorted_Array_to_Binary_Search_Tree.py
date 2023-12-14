# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        idx = len(nums) // 2

        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = nums[idx]
        root = TreeNode(mid)
        root.left = self.sortedArrayToBST(nums[:idx])
        root.right = self.sortedArrayToBST(nums[idx + 1:])  # if len(nums)>2 else None

        return root