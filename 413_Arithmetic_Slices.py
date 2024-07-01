class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [[0 for i in range(len(nums))] for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)-2):
            for j in range(i+2, len(nums)):
                # if j == i+2:
                #     if ((nums[j+1] - nums[j]) == (nums[j+2] - nums[j+1])):
                #         dp[i][j] = 1
                #         res += 1
                # else:
                if (nums[j] - nums[j-1]) == (nums[j-1] - nums[j-2]):
                    dp[i][j] = 1
                    res += 1
                if not dp[i][j]:
                    break
        return res