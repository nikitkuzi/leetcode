class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = 0
        mx_len = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] > mx:
                mx = nums[r]
                mx_len = 1
                l = r
            elif nums[r] == mx:
                mx_len = max(mx_len, r-l+1)
            else:
                l = r
        return mx_len