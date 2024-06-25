class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        r = len(nums) - 1
        res = []
        for l in range(len(nums)//2 + 1):
            res.append((nums[l] + nums[r]) / 2)
            r-=1
        return min(res)
