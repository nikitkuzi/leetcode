class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        mx = 0
        for i in range(len(nums)):
            mx = max(mx, abs(nums[i]-nums[(i+1)%len(nums)]))
        return mx