class Solution:
    def check(self, nums: List[int]) -> bool:
        mn = nums[0]
        end = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                continue
            end += 1
            if end == 2:
                return False
        if end == 0:
            return True
        if nums[-1] <= mn:
            return True
        return False

