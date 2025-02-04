class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx = nums[0]
        sm = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                sm += nums[i]

            else:
                sm = nums[i]
            mx = max(sm, mx)
        return mx