class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        p = [nums[0]]
        for i in range(1, len(nums)):
            p.append(p[-1]+nums[i])
        res = 0
        for i in range(len(nums)-1):
            if abs((p[-1]-p[i]) - p[i]) % 2 == 0:
                res+=1
        return res