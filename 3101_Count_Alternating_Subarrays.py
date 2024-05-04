# class Solution:
#     def countAlternatingSubarrays(self, nums: List[int]) -> int:
#         dp = [1]*len(nums)
#         s = 1
#         for i in range(1, len(nums)):
#             if nums[i]!=nums[i-1]:
#                 dp[i]+=dp[i-1]
#             s+=dp[i]
#         return s
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        total, running, prev = 0, 0, 1 - nums[0]
        for num in nums:
            if num == prev:
                running = 1
            else:
                running += 1
            total += running
            prev = num
        return total