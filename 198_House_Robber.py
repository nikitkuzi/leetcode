class Solution:
    def rob(self, nums: List[int]) -> int:
        # @cache
        # def f(n):
        #     if n < 0:
        #         return 0
        #     elif n <= 1:
        #         return nums[n]
        #     return max(f(n-3),f(n-2)) + nums[n]
        # return max(f(len(nums)-1),f(len(nums)-2))
        # if len(nums) < 3:
        #     return max(nums)
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = nums[1]
        # dp[2] = nums[2] + nums[0]
        # for i in range(3, len(nums)):
        #     dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        # return max(dp[-1], dp[-2])

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [None] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]