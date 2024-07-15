class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sm = sum([nums[i] for i in range(0, len(nums), 2)])
        return smclass Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sm = sum([nums[i] for i in range(0, len(nums), 2)])
        return sm