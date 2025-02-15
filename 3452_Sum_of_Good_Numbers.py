class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sm = 0
        n = len(nums)
        for i in range(n):
            f = True
            if i - k >= 0:
                f = nums[i] > nums[i-k]
                if not f:
                    continue
            if i+k < n:
                f = nums[i] > nums[i+k]
                if not f:
                    continue
            if f:
                sm += nums[i]
        return sm