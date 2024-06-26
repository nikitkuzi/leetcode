class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[0,0] for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = nums[i] + max(dp[i-1][1], dp[i-1][0])
            dp[i][1] = dp[i-1][0] - nums[i]
        return max(dp[-1][0], dp[-1][1])