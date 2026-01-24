class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mx = nums[0]+nums[-1]
        # print(nums)
        for i in range(1, n//2):
            mx = max(mx, nums[i]+nums[n-1-i])
        return mx