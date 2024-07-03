class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        cur = 0
        for n in nums:
            if n:
                cur+=1
                mx = max(mx, cur)
            else:
                cur = 0
        return mx