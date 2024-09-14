# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         mx = 0
#         mx_len = 0
#         l = 0
#         for r in range(len(nums)):
#             if nums[r] > mx:
#                 mx = nums[r]
#                 mx_len = 1
#                 l = r
#             elif nums[r] == mx:
#                 mx_len = max(mx_len, r-l+1)

#             else:
#                 l = r+1
#         return mx_len
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        ma = 0
        st = -1
        for i in range(len(nums)):
            if nums[i] == m and st == -1:
                st = i
            if st != -1 and nums[i] != m:
                ma = max(i - st, ma)
                st = -1
        if st != -1:
            return max(len(nums) - st, ma)
        return ma