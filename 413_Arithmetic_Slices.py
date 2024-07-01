class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        if n < 2:
            return 0
        dp = [0]*n
        r = 2
        while r < n:
            if (nums[r] - nums[r-1]) == (nums[r-1] - nums[r-2]):
                dp[r]+=1
                if dp[r-1]:
                    dp[r]+=dp[r-1]
                res += dp[r]
            r += 1
        return res