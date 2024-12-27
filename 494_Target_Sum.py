class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        target = abs(target)
        sm = sum(nums)
        if sm < target or (sm + target) % 2:
            return 0
        targ = (sm + target) // 2
        dp = [[0 for _ in range(targ + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for sm in range(targ + 1):
                dp[i][sm] = dp[i - 1][sm]
                if sm >= nums[i - 1]:
                    dp[i][sm] += dp[i - 1][sm - nums[i - 1]]
        return dp[-1][targ]

