class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i, n in enumerate(nums):
            res[i] = nums[n]
        return res